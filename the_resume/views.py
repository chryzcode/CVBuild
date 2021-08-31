from django.shortcuts import render
from .models import Profile
from .forms import ProfileForm
# from django.shortcuts import render, get_object_or_404, redirect
# from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView
# from django.urls import reverse_lazy, reverse

def resume(request):
    model = Profile
    form = ProfileForm
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        summary = request.POST.get('summary', '')
        education = request.POST.get('education', '')
        skills = request.POST.get('skills', '')
        experience = request.POST.get('experience', '')

        profile = Profile(name=name, email=email, summary=summary, education=education, skills=skills, experience=experience)
        profile.save()
    return render(request, 'index.html', {'form':form})