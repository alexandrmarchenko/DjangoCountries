from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.main, name="home"),
    path('countries_list/', views.countries_list, name="countries_list"),
    path('languages_list/', views.languages_list, name="languages_list"),
    path('country-by-letter/<str:letter>/', views.countries_by_letter, name="countries_by_letter"),
    path('country/<int:country>/', views.country, name="country_detail"),
    path('language/<int:lang>/', views.lang, name="language_detail"),
]
