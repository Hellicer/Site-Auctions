from contextlib import redirect_stdout
from email import message
import re
from venv import create
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.db import models
from django.forms.forms import Form
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User, Card, Category, Comment, Rate, Watchlist
from .forms import CardForm, CategoryForm, CommentForm, RateForm, StatusForm
from django.utils import timezone


# 1.сделать проверки указания цены, чтобы вводное значение не было больше предыдущего.+
# 2. если лот закрыт, то он не должен отображаться в графе "Активные лоты".+
# 2.1. Если лот закрыт, его нельзя будет открыть заново, написать комментарий, или же добовать(изменить) цену.+
# 5.сделать отображение только последних пяти ставок в графе layout_page > "сделано Х ставок".+

# !!! отображение уведомление о выиграше лота у победителя возле вкладки "личный кабинет"

# 3. сделать карточки.
# 4. сделать(по-возможности) адаптивное время.
# 6. возможно, Изменить логику отображения категорий.
# 7. переделать layout, вынести графу "личный кабинет" в одну сторону, мб сделать popup c "создать лот" и "список наблюдения".
# 9. ДОбавить таймер.
# 10. ставку не может делать владелц лоn


def index(request):
    cards = Card.objects.order_by('-pub_date').all().exclude(status_lot=False)

    return render(request, "auctions/index.html", {
        "cards": cards,
        "watchlists": Watchlist.objects.all(),

    })


def listing(request, item_title, id_card):
    comment = CommentForm(request.POST)
    price = RateForm(request.POST)
    status = StatusForm(request.POST)
    lot = Card.objects.get(pk=id_card)
    rate = Rate.objects.filter(card=lot.id)
    card = Card.objects.get(pk=lot.id)
    
    # user = User.objects.get(username=request.user)
    message = ""

    if rate:
        rate_last = rate.filter(card=id_card).latest('pub_date')
        rate_last_user = rate_last.user

        rate_last = rate_last.price
    else:
        rate_last = lot.price
    if request.POST.get("button") == "Bid":
        now_price = card.now_price
        user = User.objects.get(username=request.user)
        nprice = price.save()
        f_price = nprice.price
        user_price = nprice.user
        card_author = card.author
        if f_price > rate_last and user != card_author:        
            nprice_lot = Rate.objects.get(pk=nprice.id)
            nprice_lot.user = user
            nprice_lot.save(update_fields=['user'])
            nprice_lot.card = lot
            nprice_lot.save(update_fields=['card'])
            message = ""
            now_price = nprice_lot.price
            card.now_price = now_price
            card.save(update_fields=['now_price'])
            return HttpResponseRedirect(reverse("listing", args=(item_title, id_card)))
            
        else:
            if f_price < rate_last:
                message = " <li>Ставка не может быть меньше нынешней </li>"
            elif f_price > rate_last:
                if user_price == card_author:
                    message = " <li> Вы не можете сделать ставку на свой лот </li>"
                else:
                    message = " <li> Ошибка ввода </li>"
            else:
                message = " <li> Ошибка ввода </li>"
            nprice.delete()

    if request.POST.get("button") == "Watchlist":
        user = User.objects.get(username=request.user)
        try:
            Watchlist.objects.get(user=user, title=lot).delete()
        except:
            Watchlist.objects.create(user=user, title=lot)
        return HttpResponseRedirect(reverse("listing", args=(item_title, id_card)))

    if request.POST.get("button") == "Check":
        card = Card.objects.get(winner=request.user, title=item_title)
        card.checked = True
        card.save(update_fields=['checked'])
        return HttpResponseRedirect(reverse("listing", args=(item_title, id_card)))

    if request.POST.get("button") == "Send_comment":
        user = User.objects.get(username=request.user)
        new_comment = comment.save()
        comment_lot = Comment.objects.get(pk=new_comment.id)
        comment_lot.card = lot
        comment_lot.save(update_fields=['card'])
        comment_lot.user = User.objects.get(username=request.user)
        comment_lot.save(update_fields=['user'])
        return HttpResponseRedirect(reverse("listing", args=(item_title, id_card)))

    if request.POST.get("button") == "Close":
        card.status_lot = False
        card.winner = rate_last_user
        now = timezone.now()
        card.close_date = now
        card.save(update_fields=['status_lot', 'winner', 'close_date'])

        return HttpResponseRedirect(reverse("listing", args=(item_title, id_card)))

    return render(request, "auctions/listing.html", {
        "card": card,
        "categorys": lot.category.all(),
        "comments": Comment.objects.filter(card=lot.id),
        "comment": comment,
        "price": price,
        "allrate": rate,
        "rate": Rate.objects.filter(card=lot.id).order_by('-price')[:5],
        "rate_last": rate_last,
        "status": status,
        "error_price": message,
        "card_user": str(card.author)
        # "winner": winner
    })


def add(request):
    form = CardForm(request.POST, request.FILES)
    form_category = CategoryForm(request.POST)
    card_author = User.objects.get(username=request.user)

    if request.method == "POST":
        new_lot = form.save()
        title = new_lot.id
        card = Card.objects.get(pk=title)
        card.author = card_author
        card.save(update_fields=['author'])
        card.status_lot = True
        card.save(update_fields=['status_lot'])
        return HttpResponseRedirect(reverse("listing", args=(card, title)))
    else:
        return render(request, "auctions/add.html", {
            "form": form,
            "form_category": form_category,
            # "categorys": categorys,
        })


def watchlists(request):
    return render(request, "auctions/watchlist.html", {
        "cards": Watchlist.objects.filter(user=request.user.id)
    })


def listlots(request, category):
    category = Category.objects.get(categorys=category)
    cards = Card.objects.filter(category=category)
    category = category
    return render(request, "auctions/listlots.html", {
        "cards": cards,
        "category": category,
        "watchlist": Watchlist.objects.all()
    })


def category(request):
    categorys = Category.objects.all()
    return render(request, "auctions/category.html", {
        "categorys": categorys
    })


@login_required
def account(request, user):
    user = User.objects.get(username=request.user)
    status = StatusForm(request.POST)
    cards = Card.objects.filter(author=user.id)
    card_author = Card.objects.filter(author=user.id)
    card_archive = Card.objects.filter(author=user.id, status_lot=False)
    card_open = Card.objects.filter(author=user.id, status_lot=True)
    checked = Card.objects.filter(checked=1, winner=request.user)
    winner_card = Card.objects.filter(winner=user)
    check_card_author = 0
    check_card_archive = 0
    check_card_open = 0
    check_checked = 0
    if request.POST.get("button") == "winner_lot":
        cards = winner_card
        check_checked = 1

    if request.POST.get("button") == "card_author":
        cards = card_author.order_by('pub_date')
        check_card_author = 1
    if request.POST.get("button") == "card_archive":
        cards = card_archive.order_by('pub_date')
        check_card_archive = 1
    if request.POST.get("button") == "card_open":
        cards = card_open.order_by('pub_date')
        check_card_open = 1

    return render(request, "auctions/userpage.html", {
        "cards": cards,
        "status": status,
        "winner_card": winner_card,
        "card_author": card_author,
        "card_archive": card_archive,
        "card_open": card_open,
        "checked": checked,

        "check_card_author": check_card_author,
        "check_card_archive": check_card_archive,
        "check_card_open": check_card_open,
        "check_checked": check_checked
    })


def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
