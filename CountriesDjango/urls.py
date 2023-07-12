
from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.main),
    path('countries_list/', views.countries_list),
    path('languages_list/', views.languages_list),
    path('country-by-letter/<str:letter>/', views.countries_by_letter),
    path('country/<str:country>/', views.country),
    path('language/<str:lang>/', views.lang),
]
