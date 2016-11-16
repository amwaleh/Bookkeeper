from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^$',views.HomeView.as_view(), name='index'),
    url(r'search/$',views.SearchView.as_view(),name='search'),
    url(r'books/$',views.Addbooks.as_view(),name='book')
]