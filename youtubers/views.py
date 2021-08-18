from django.shortcuts import render, get_object_or_404
from .models import Youtubers
# to search with multiple query
#from django.db.models import Q
#value=ModelName.objects.filter(Q(column_name_one__icontains=serach_query) |Q(column_name_two__icontains=serach_query ))  ###

# Create your views here.


def youtubers(request):
    tubers = Youtubers.objects.order_by('-created_date')
    data = {
        'tubers': tubers,
    }
    return render(request, 'youtubers/youtubers.html', data)


def youtubers_detail(request, id):
    tuber = get_object_or_404(Youtubers, pk=id)
    data = {
        'tuber': tuber,
    }
    return render(request, 'youtubers/youtuber_detail.html', data)


def search(request):
    tubers = Youtubers.objects.order_by('-created_date')
    camera_search = Youtubers.objects.values_list(
        'camera_type', flat=True).distinct()
    city_search = Youtubers.objects.values_list('city', flat=True).distinct()
    category_search = Youtubers.objects.values_list(
        'category', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            tubers = tubers.filter(description__icontains=keyword)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            tubers = tubers.filter(city__iexact=city)

    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            tubers = tubers.filter(category__iexact=category)

    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            tubers = tubers.filter(camera_type__iexact=camera_type)

    data = {
        'tubers': tubers,
        'camera_search': camera_search,
        'city_search': city_search,
        'category_search': category_search
    }
    return render(request, 'youtubers/search.html', data)
