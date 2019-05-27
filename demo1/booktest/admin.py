from django.contrib import admin
from .models import Bookinfo,Heroinfo,ManageExt

# Register your models here.

class HeroinfoInLine(admin.StackedInline):
    model = Heroinfo
    extra = 1

class BookinfoAdmin(admin.ModelAdmin):
    list_display = ["title","pub_date"]
    list_filter = ["title"]
    search_fields = ["title","pub_date"]
    list_per_page = 1
    inlines = [HeroinfoInLine]

class HeroinfoAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_filter = ["name"]
    list_display = ["name","gendle","skill","book"]
    search_fields=["name","gendle","skill","book"]

admin.site.register(Bookinfo,BookinfoAdmin)
admin.site.register(Heroinfo,HeroinfoAdmin)


