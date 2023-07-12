from string import ascii_uppercase

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
import json
from MainApp.models import Language, Country


def main(request):
    return render(request, 'main.html')


def countries_list(request):
    countries = Country.objects.all()
    paginator = Paginator(countries, 20)
    page_number = request.GET.get("page")
    countries = paginator.get_page(page_number)
    context = {'countries': countries, 'alphabet': ascii_uppercase}
    return render(request, 'countries-list.html', context)


def countries_by_letter(request, letter):
    countries = Country.objects.filter(name__startswith=letter)
    paginator = Paginator(countries, 20)
    page_number = request.GET.get("page")
    countries = paginator.get_page(page_number)
    context = {'countries': countries, 'alphabet': ascii_uppercase}
    return render(request, 'countries-list.html', context)


def languages_list(request):
    languages = Language.objects.all()
    paginator = Paginator(languages, 20)
    page_number = request.GET.get("page")
    languages = paginator.get_page(page_number)
    context = {'languages': languages}
    return render(request, 'languages-list.html', context)


def country(request, country):
    country = Country.objects.get(id=country)
    languages = country.languages.all()
    context = {'country': country, 'languages': languages}
    return render(request, 'country.html', context)


def lang(request, lang):
    language = Language.objects.get(id=lang)
    countries = Country.objects.filter(languages__id=lang)
    context = {'lang': language, 'countries': countries}
    return render(request, 'lang.html', context)
