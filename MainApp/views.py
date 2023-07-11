from string import ascii_uppercase

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
import json


def main(request):
    return render(request, 'main.html')


def countries_list(request):
    with open('country-by-languages.json') as json_file:
        countries = json.load(json_file)
    paginator = Paginator(countries, 20)
    page_number = request.GET.get("page")
    countries = paginator.get_page(page_number)
    context = {'countries': countries, 'alphabet': ascii_uppercase}
    print(countries.paginator)
    return render(request, 'countries-list.html', context)


def countries_by_letter(request, letter):
    with open('country-by-languages.json') as json_file:
        countries = json.load(json_file)
    countries = [c for c in countries if c["country"].upper().startswith(letter.upper())]
    paginator = Paginator(countries, 20)
    page_number = request.GET.get("page")
    countries = paginator.get_page(page_number)
    context = {'countries': countries, 'alphabet': ascii_uppercase}
    return render(request, 'countries-list.html', context)


def languages_list(request):
    languages = []
    with open('country-by-languages.json') as json_file:
        countries = json.load(json_file)
    for country in countries:
        languages += country["languages"]
    languages = sorted(set(languages))
    paginator = Paginator(languages, 20)
    page_number = request.GET.get("page")
    languages = paginator.get_page(page_number)
    context = {'languages': languages}
    return render(request, 'languages-list.html', context)


def country(request, country):
    with open('country-by-languages.json') as json_file:
        countries = json.load(json_file)
    c = next((c for c in countries if c["country"] == country), None)
    context = {'country': c}
    return render(request, 'country.html', context)


def lang(request, lang):
    with open('country-by-languages.json') as json_file:
        countries = json.load(json_file)
    countries = (c["country"] for c in countries if lang in c["languages"])
    context = {'lang': lang, 'countries': countries}
    return render(request, 'lang.html', context)
