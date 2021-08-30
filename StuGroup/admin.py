from django.contrib import admin
from .models import User, message


admin.site.site_header = "تبادل اطلاعات با دانشجویان  "


class User_admin(admin.ModelAdmin):
    list_display = ('username', 'password', 'firstname', 'lastname', 'slug', 'mobil', 'email')
    # list_filter = ('publish', 'status', 'title')
    search_fields = ('username', 'lastname')
    prepopulated_fields = {'slug': ('username',)}


admin.site.register(User, User_admin)


class message_admin(admin.ModelAdmin):
    list_display = ('stu_no', 'title', 'namefile', 'upload', 'slug', 'contentmsg')
    # list_filter = ('publish', 'status', 'title')
    search_fields = ('title', 'namefile')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(message, message_admin)
