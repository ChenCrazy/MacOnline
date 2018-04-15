# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
# from DjangoUeditor.models import UEditorField

# 我这里不需要展示城市所以注释此外键的定义
# class CityDict(models.Model):
#     name = models.CharField(max_length=20, verbose_name=u"城市")
#     desc = models.CharField(max_length=200, verbose_name=u"描述")
#     add_time = models.DateTimeField(default=datetime.now)
#
#     class Meta:
#         verbose_name = u"城市"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.name


class DramaOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"团队组织")
    desc = models.TextField(verbose_name=u"组织描述")
    # desc = UEditorField(verbose_name=u"机构描述",width=900, height=300, imagePath="org/ueditor/",
    #                                      filePath="org/ueditor/", default='')
    # tag = models.CharField(default="全国知名", max_length=10, verbose_name=u"机构标签")
    # category = models.CharField(default="pxjg", verbose_name=u"机构类别", max_length=20,
    #                   choices=(("pxjg","培训机构"),("gr","个人"),("gx","高校")))
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏数")
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name=u"logo", max_length=100)
    region = models.CharField(max_length=150, verbose_name=u"地区")
    # city = models.ForeignKey(CityDict, verbose_name=u"所在城市")
    appreciator = models.IntegerField(default=0, verbose_name=u"观看人数")
    drama_nums = models.IntegerField(default=0, verbose_name=u"投稿数")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"团队组织"
        verbose_name_plural = verbose_name

    def get_author_nums(self):
        # 获取课程机构的作者数量
        return self.author_set.all().count()

    def __unicode__(self):
        return self.name


class Author(models.Model):
    org = models.ForeignKey(DramaOrg, verbose_name=u"团队组织")
    name = models.CharField(max_length=50, verbose_name=u"作者名")
    work_years = models.IntegerField(default=0, verbose_name=u"投稿年限")
    # work_company = models.CharField(max_length=50, verbose_name=u"就职公司")
    # work_position = models.CharField(max_length=50, verbose_name=u"公司职位")
    # points = models.CharField(max_length=50, verbose_name=u"教学特点")
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏数")
    # age = models.IntegerField(default=18, verbose_name=u"年龄")
    image = models.ImageField(default='', upload_to="teacher/%Y/%m", verbose_name=u"头像", max_length=100)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"作者"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def get_drama_nums(self):
        return self.drama_set.all().count()
