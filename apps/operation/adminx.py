# -*- coding: utf-8 -*-
__author__ = 'macbeth'
__date__ = '2018/04/16 14:43'

import xadmin

from .models import UserAsk, UserDrama, UserMessage, DramaComments, UserFavorite


class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'drama_name', 'add_time']
    search_fields = ['name', 'mobile', 'drama_name']
    list_filter = ['name', 'mobile', 'drama_name', 'add_time']
    model_icon = 'fa fa-question-circle'


class UserDramaAdmin(object):
    list_display = ['user', 'drama', 'add_time']
    search_fields = ['user', 'drama']
    list_filter = ['user', 'drama', 'add_time']
    # model_icon = 'fa fa-address-book'


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']
    model_icon = 'fa fa-envelope-o'


class DramaCommentsAdmin(object):
    list_display = ['user', 'drama', 'comments', 'add_time']
    search_fields = ['user', 'drama', 'comments']
    list_filter = ['user', 'drama', 'comments', 'add_time']
    model_icon = 'fa fa-comment'


class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']
    model_icon = 'fa fa-heart'


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserDrama, UserDramaAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(DramaComments, DramaCommentsAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)

