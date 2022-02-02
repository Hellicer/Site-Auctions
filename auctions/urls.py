from django.urls import path

from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing/@<str:item_title>'<int:id_card>", views.listing, name="listing"),
    path("category", views.category, name="category"),
    path("category/<str:category>", views.listlots, name="listlots"),
    path("listing/addpage", views.add, name="add"),
    path("@/<str:user>/", views.account, name="account"),
    path("watchlist/", views.watchlists, name="watchlists"),
    path(r'^favicon\.ico$', RedirectView.as_view(
        url='/media/images/favicon.ico'), name='favicon'),

]
