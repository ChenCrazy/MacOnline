# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

# from DjangoUeditor.models import UEditorField

from django.db import models
from organization.models import DramaOrg, Author


class Drama(models.Model):
    drama_org = models.ForeignKey(DramaOrg, verbose_name=u"团队组织", null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name=u"番剧名")
    desc = models.CharField(max_length=300, verbose_name=u"番剧描述")
    detail = models.TextField(verbose_name=u"番剧详情")
    # detail = UEditorField(verbose_name=u"番剧详情",width=600, height=300, imagePath="dramas/ueditor/",
    #                                      filePath="dramas/ueditor/", default='')
    is_banner = models.BooleanField(default=False, verbose_name=u"是否轮播")
    # author = models.ForeignKey(Author, verbose_name=u"讲师", null=True, blank=True)
    degree = models.CharField(verbose_name=u"级别", choices=(("cj", "初级"), ("zj", "中级"), ("gj", "高级")), max_length=2)
    watch_times = models.IntegerField(default=0, verbose_name=u"欣赏时长(分钟数)")
    appreciator = models.IntegerField(default=0, verbose_name=u'观看人数')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏人数')
    image = models.ImageField(upload_to="dramas/%Y/%m", verbose_name=u"封面图", max_length=100)
    click_nums = models.IntegerField(default=0, verbose_name=u"点击量")
    # category = models.CharField(default=u"后端开发", max_length=20, verbose_name=u"类别")
    # tag = models.CharField(default="", verbose_name=u"标签", max_length=10)
    # youneed_know = models.CharField(default="", max_length=300, verbose_name=u"须知")
    # author_tell = models.CharField(default="", max_length=300, verbose_name=u"作者有话说")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"番剧"
        verbose_name_plural = verbose_name

    def get_jj_nums(self):
        # 获取视频集数
        return self.serial_set.all().count()
    get_jj_nums.short_description = "剧集数"

    def go_to(self):
        from django.utils.safestring import mark_safe
        return mark_safe("<a href='http://www.projectsedu.com'>跳转</>")
    go_to.short_description = "跳转"

    def get_watch_users(self):
        return self.userdrama_set.all()[:5]

    def get_drama_serial(self):
        # 获取番剧所有剧集
        return self.serial_set.all()

    def __unicode__(self):
        return self.name


class BannerDrama(Drama):
    class Meta:
        verbose_name = "轮播"
        verbose_name_plural = verbose_name
        proxy = True


class Serial(models.Model):
    drama = models.ForeignKey(Drama, verbose_name=u"番剧")
    name = models.CharField(max_length=100, verbose_name=u"剧集名")
    watch_times = models.IntegerField(default=0, verbose_name=u"欣赏时长(分钟数)")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"剧集"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def get_serial_video(self):
        # 获取视频剧集
        return self.video_set.all()


class Video(models.Model):
    serial = models.ForeignKey(Serial, verbose_name=u"剧集")
    name = models.CharField(max_length=100, verbose_name=u"番剧名")
    watch_times = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")
    url = models.CharField(max_length=200, default="", verbose_name=u"访问地址")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class DramaResource(models.Model):
    drama = models.ForeignKey(Drama, verbose_name=u"番剧")
    name = models.CharField(max_length=100, verbose_name=u"名称")
    download = models.FileField(upload_to="dramas/resource/%Y/%m", verbose_name=u"资源文件", max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"资源"
        verbose_name_plural = verbose_name
