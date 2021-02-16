from django.urls import path

from . import views

app_name = 'needsbox'

urlpatterns = [
    path('', views.index, name="index"),
    path('search/', views.search, name="search"),
    # path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('create/', views.ServiceCreate.as_view(), name="service_form"),
    path('create_ad/', views.AdvertisementCreate.as_view(), name="advertisement_form"),
]
