from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import SignUpForm

def frontpage(request):
    return render(request, 'core/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    else:
        form = SignUpForm()
    
    return render(request, 'core/signup.html', {'form': form})


# Видео
from django.shortcuts import render
from.models import Video

def video_view(request, video_id):
    video = Video.objects.get(id=video_id)
    return render(request, 'video.html', {'video': video})