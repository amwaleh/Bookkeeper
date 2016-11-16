from django.contrib import admin
from django.contrib import admin
# Register your models here.
from .models import Books, Categories
admin.site.register(Books)
admin.site.register(Categories)