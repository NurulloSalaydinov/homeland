from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import DetailView, CreateView
from django.utils.translation import gettext as _
from .models import Tour, Gallery
from .forms import ContactForm


class TourDetail(DetailView):
    template_name = 'property-details.html'
    model = Tour
    context_object_name = 'obj'


def home_view(request):
    top_tour = Tour.objects.all().order_by('-id')[:3]
    tours = Tour.objects.all()
    galleries = Gallery.objects.all().order_by('-id')
    context = {
        'top_tours': top_tour,
        'tours': tours,
        'galleries': galleries,
    }
    return render(request, 'index.html', context)


def create_contact(request):
    messages.add_message(request, messages.INFO, 'Submitted successfully !')
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/#contact')
    return redirect('/#contact')
