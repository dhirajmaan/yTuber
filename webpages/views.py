from django.shortcuts import render
from .models import Slider, Team
from youtubers.models import Youtubers


# Create your views here.


def home(request):
    sliders = Slider.objects.all()
    teams = Team.objects.all()
    featured_youtubers = Youtubers.objects.order_by(
        '-created_date').filter(is_featured=True)
    all_tubers = Youtubers.objects.order_by('-created_date')
    data = {
        'sliders': sliders,
        'teams': teams,
        'featured_youtubers': featured_youtubers,
        'all_tubers': all_tubers,
    }

    return render(request, 'webpages/home.html', data)


def contacts(request):
    return render(request, 'webpages/contact.html')


def about(request):
    return render(request, 'webpages/about.html')


def services(request):
    return render(request, 'webpages/services.html')
