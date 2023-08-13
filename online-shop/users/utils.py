from django.shortcuts import render, redirect
from .models import Profile
from .forms import updateProfileForm
from django.contrib import messages

def getProfilesPage(request):
    profiles=Profile.objects.all()

    return profiles
def deleteProfilePage(request,pk):
    profile=Profile.objects.get(id=pk)
    if profile is not None:
        profile.delete()

        return redirect('admin-page')

def editProfilePage(request,pk):
    profile=Profile.objects.get(id=pk)
    form=updateProfileForm(instance=profile)

    if request.method == 'POST':
        form=updateProfileForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('admin-page')
        else:
            messages.error(request,'no user found! please login')

    return form




    


