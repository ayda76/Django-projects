from django.shortcuts import render

from .models import Profile
# Create your views here.
def profiles(request):
    profiles=Profile.objects.all()
    context={'profiles':profiles}
    return render(request,'users/profiles.html', context)

def userProfiles(request,pk):
    profile=Profile.objects.get(id=pk)

    topSkills=profile.skills_set.exclude(description__exact="")
    otherSkills=profile.skills_set.filter(description="")
    
    context={'profile':profile, 'topskills':topSkills,'otherskills':otherSkills}
    return render(request, 'users/user-profile.html',context)