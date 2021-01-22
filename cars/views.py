from django.http import HttpResponse
from django.shortcuts import render
from cars.models import Car
from django.template import loader
from django.views.generic.detail import DetailView
from cars.forms import CarFilterForm, CarFullFilter
from django.db.models import Q

# Create your views here.
def index(request):
    template = loader.get_template('base.html')
    cars = Car.objects.select_related("manufacturer").all()
    form = CarFilterForm(request.GET)
    full_form = CarFullFilter(request.GET)

    if form.is_valid():
        if form.cleaned_data["min_year"]:
            cars = cars.filter(year__gte=form.cleaned_data["min_year"])
        if form.cleaned_data["max_year"]:
            cars = cars.filter(year__lte=form.cleaned_data["max_year"])
        if form.cleaned_data["model"]:
            cars = cars.filter(
                Q(model__icontains=form.cleaned_data["model"])|
                Q(manufacturer__title=form.cleaned_data["model"])|
                Q(manufacturer__title__icontains=form.cleaned_data["model"]))
        if form.cleaned_data["gear"] != "":
            cars = cars.filter(Q(gear=form.cleaned_data["gear"]))

        if full_form.is_valid():
            if full_form.cleaned_data["search"]:
                cars = cars.filter(Q(model=full_form.cleaned_data["search"])|
                                           Q(manufacturer__title=full_form.cleaned_data["search"])|
                                           Q(manufacturer__title__icontains=full_form.cleaned_data["search"])|
                                           # Q(year=int(full_form.cleaned_data["search"]))|
                                           Q(gear=full_form.cleaned_data["search"])|
                                           Q(gear__icontains=full_form.cleaned_data["search"]))
    return HttpResponse(template.render({ "cars": cars, "form": form, "full_form": full_form }))

class CarDetailView(DetailView):
    model = Car
