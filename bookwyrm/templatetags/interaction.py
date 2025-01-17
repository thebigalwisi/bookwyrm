""" template filters for status interaction buttons """
from django import template
from bookwyrm import models


register = template.Library()


@register.filter(name="liked")
def get_user_liked(user, status):
    """did the given user fav a status?"""
    return models.Favorite.objects.filter(user=user, status=status).exists()


@register.filter(name="boosted")
def get_user_boosted(user, status):
    """did the given user fav a status?"""
    return status.boosters.filter(user=user).exists()


@register.filter(name="saved")
def get_user_saved_lists(user, book_list):
    """did the user save a list"""
    return user.saved_lists.filter(id=book_list.id).exists()
