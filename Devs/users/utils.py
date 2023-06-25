from .models import Profile,skills
from django.db.models import Q

def searchProfiles(request):
    search_query=''
    if request.GET.get('search_query'):
        search_query= request.GET.get('search_query')

    s=skills.objects.filter(name__icontains=search_query)

    profiles=Profile.objects.distinct().filter(Q(name__icontains=search_query)|
    Q(short_intro__icontains=search_query)|
    Q(skills__in=s))

    return profiles, search_query



