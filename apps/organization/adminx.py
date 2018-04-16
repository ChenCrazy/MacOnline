# -*- coding: utf-8 -*-
__author__ = 'macbeth'
__date__ = '2018/04/16 14:40'

import xadmin
# from .models import CityDict
from .models import DramaOrg, Author


# class CityDictAdmin(object):
#     list_display = ['name', 'desc', 'add_time']
#     search_fields = ['name', 'desc']
#     list_filter = ['name', 'desc', 'add_time']
#     model_icon = 'fa fa-university'


class DramaOrgAdmin(object):
    list_display = ['name', 'desc', 'click_nums', 'fav_nums']
    search_fields = ['name', 'desc', 'click_nums', 'fav_nums']
    list_filter = ['name', 'desc', 'click_nums', 'fav_nums']
    relfield_style = 'fk-ajax'
    style_fields = {"desc":"ueditor"}
    # model_icon = 'fa fa-university'


class AuthorAdmin(object):
    list_display = ['org', 'name', 'work_years']
    search_fields = ['org', 'name', 'work_years']
    list_filter = ['org', 'name', 'work_years']
    model_icon = 'fa fa-user-md'


# xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(DramaOrg, DramaOrgAdmin)
xadmin.site.register(Author, AuthorAdmin)