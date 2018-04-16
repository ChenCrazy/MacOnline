# -*- coding: utf-8 -*-
__author__ = 'macbeth'
__date__ = '2018/04/16 14:46'

import xadmin

from .models import Drama, Serial, Video, DramaResource, BannerDrama
from organization.models import DramaOrg


class SerialInline(object):
    model = Serial
    extra = 0


class DramaResourceInline(object):
    model = DramaResource
    extra = 0


class DramaAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'watch_times', 'appreciator', 'get_jj_nums', 'go_to']
    search_fields = ['name', 'desc', 'detail', 'degree', 'appreciator']
    list_filter = ['name', 'desc', 'detail', 'degree', 'watch_times', 'appreciator']
    ordering = ['-click_nums']
    readonly_fields = ['click_nums']
    list_editable = ['degree', 'desc']
    exclude = ['fav_nums']
    inlines = [SerialInline, DramaResourceInline]
    style_fields = {"detail":"ueditor"}
    import_excel = True

    def queryset(self):
        qs = super(DramaAdmin, self).queryset()
        qs = qs.filter(is_banner=False)
        return qs

    def save_models(self):
        # 在保存课程的时候统计课程机构的课程数
        obj = self.new_obj
        obj.save()
        if obj.drama_org is not None:
            drama_org = obj.drama_org
            drama_org.drama_nums = Drama.objects.filter(drama_org=drama_org).count()
            drama_org.save()

    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:
            pass
        return super(DramaAdmin, self).post(request, args, kwargs)


class BannerDramaAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'watch_times', 'appreciator']
    search_fields = ['name', 'desc', 'detail', 'degree', 'appreciator']
    list_filter = ['name', 'desc', 'detail', 'degree', 'watch_times', 'appreciator']
    ordering = ['-click_nums']
    readonly_fields = ['click_nums']
    exclude = ['fav_nums']
    inlines = [SerialInline, DramaResourceInline]

    def queryset(self):
        qs = super(BannerDramaAdmin, self).queryset()
        qs = qs.filter(is_banner=True)
        return qs


class SerialAdmin(object):
    list_display = ['drama', 'name', 'add_time']
    search_fields = ['drama', 'name']
    list_filter = ['drama__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['serial', 'name', 'add_time']
    search_fields = ['serial', 'name']
    list_filter = ['serial', 'name', 'add_time']
    model_icon = 'fa fa-film'


class DramaResourceAdmin(object):
    list_display = ['drama', 'name', 'download', 'add_time']
    search_fields = ['drama', 'name', 'download']
    list_filter = ['drama', 'name', 'download', 'add_time']


xadmin.site.register(Drama, DramaAdmin)
xadmin.site.register(BannerDrama, BannerDramaAdmin)
xadmin.site.register(Serial, SerialAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(DramaResource, DramaResourceAdmin)