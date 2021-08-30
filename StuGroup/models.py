from django.utils import timezone
from extensions.utils import jalali_converter
from django.db import models
# from django.urls import reverse


class User(models.Model):
    username = models.IntegerField(unique=True, null=False, primary_key=True, verbose_name="کدکاربری")
    password = models.CharField(max_length=100, null=False, verbose_name="رمز ورود")
    firstname = models.CharField(max_length=70, null=True, verbose_name="نام")
    lastname = models.CharField(max_length=70, null=True, verbose_name="نام خانوادگی")
    mobil = models.CharField(max_length=50, null=True, verbose_name='شماره تلفن همراه')
    email = models.EmailField(verbose_name="ایمیل")

    class Meta:
        verbose_name = "دانشجو"
        verbose_name_plural = "دانشجویان"
        ordering = ['lastname', 'firstname']

    def __str__(self):
        return self.lastname


class message(models.Model):
    stu_no = models.IntegerField(null=True, verbose_name='شماره دانشجویی')
    title = models.CharField(max_length=250, blank=True, verbose_name="عنوان پیام")
    upload = models.FileField(upload_to="media", blank=True, verbose_name='ارسال فایل')
    slug = models.SlugField(max_length=200, unique=True, verbose_name="آدرس پیام")
    contentmsg = models.TextField(verbose_name="متن پیام")
    publish = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "پیام"
        verbose_name_plural = "پیام ها"
        ordering = ['created']

    def __str__(self):
        return self.stu_no

    def jpublish(self):
        return jalali_converter(self.publish)

    jpublish.short_description = "زمان انتشار"

    # def get_absolute_url(self):
    #     return reverse("account:news")


class uploadfile(models.Model):
    stu_no = models.IntegerField(null=True, verbose_name='شماره دانشجویی')
    title = models.CharField(max_length=250, blank=True, verbose_name="عنوان فایل")
    upload = models.FileField(upload_to="media", blank=True, verbose_name='ارسال فایل')
    slug = models.SlugField(max_length=200, unique=True, verbose_name="آدرس فایل")
    publish = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "فایل"
        verbose_name_plural = "فایل ها"
        # ordering = ['stu_no']

    def __str__(self):
        return self.stu_no
