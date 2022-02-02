from django.contrib import admin

from .models import Card, Category, User, Comment, Rate, Watchlist

# Register your models here.


class CardAdmin(admin.ModelAdmin):
    list_display = ("title", "pub_date", "price", "author", "status_lot", "winner", "close_date", "checked")
    search_fields = ("title", "pub_date", "price", "author", "status_lot", "winner", "close_date"  )
    list_filter = ("title", "pub_date", "author", "status_lot", "winner", "close_date", "checked" )

class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "date_joined", "last_login")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("categorys",)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "card", "text", "pub_date", )
    search_fields = ('user', 'pub_date', 'card')
    list_filter = ('user', 'pub_date', 'card')

    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

class WatchlistAdmin(admin.ModelAdmin):
        list_display = ("user", "title")
        list_filter = ("user",  "title")

class RateAdmin(admin.ModelAdmin):
    list_display = ("price",  "card", "pub_date", "user",)
    search_fields = ("price", "card", "user")
    list_filter = ("price", "card",  "pub_date", "user")




class LotAdmin(admin.ModelAdmin):

    filter_horizontal = ("tag", )

admin.site.register(Rate, RateAdmin)
admin.site.register(Watchlist, WatchlistAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(User, UserAdmin)
