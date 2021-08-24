from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required

from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView
from .models import Person, Languages, Awards, Education, Experience, Skills, Project
from .forms import  PersonForm, LanguageForm, AwardForm, ExperienceForm, EducationForm, SkillsForm, ProjectForm, SignUpForm


class MyPerson(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Person
    form_class = PersonForm
    template_name = 'create_user.html'
    success_url = reverse_lazy('resume')

@login_required(login_url='login')
def EditPerson(request, pk):
        person = get_object_or_404(Person, pk=pk)
        form = PersonForm(instance=person)
        if request.method == 'POST':
            form = PersonForm(request.POST, instance=person)
            if form.is_valid():
                form.save()
                return redirect('resume')
        context = {'form':form}
        return render(request, 'create_user.html', context)


class MySkills(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Skills
    form_class =SkillsForm
    template_name = 'create_skills.html'
    success_url = reverse_lazy('resume')

@login_required(login_url='login')
def EditSkills(request, pk):
        skills = get_object_or_404(Skills, pk=pk)
        form = SkillsForm(instance=skills)
        if request.method == 'POST':
            form = PersonForm(request.POST, instance=skills)
            if form.is_valid():
                form.save()
                return redirect('resume')
        context = {'form':form}
        return render(request, 'create_skills.html', context)

 
class MyLanguage(LoginRequiredMixin ,CreateView):
    login_url = 'login'
    model = Languages
    form_class = LanguageForm
    template_name = 'create_language.html'

@login_required(login_url='login')
def EditLanguage(request, pk):
        language = get_object_or_404(Languages, pk=pk)
        form = LanguageForm(instance=language)
        if request.method == 'POST':
            form = LanguageForm(request.POST, instance=language)
            if form.is_valid():
                form.save()
                return redirect('resume')
        context = {'form':form}
        return render(request, 'create_language.html', context)


class MyAward(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Awards
    form_class = AwardForm
    template_name = 'create_award.html'

@login_required(login_url='login')
def EditAward(request, pk):
        award = get_object_or_404(Awards, pk=pk)
        form = AwardForm(instance=award)
        if request.method == 'POST':
            form = AwardForm(request.POST, instance=award)
            if form.is_valid():
                form.save()
                return redirect('resume')
        context = {'form':form}
        return render(request, 'create_award.html', context)


class MyExperience(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Experience
    form_class = ExperienceForm
    template_name = 'create_experience.html'

@login_required(login_url='login')
def EditExperience(request, pk):
        experience = get_object_or_404(Experience, pk=pk)
        form = ExperienceForm(instance=experience)
        if request.method == 'POST':
            form = ExperienceForm(request.POST, instance=experience)
            if form.is_valid():
                form.save()
                return redirect('resume')
        context = {'form':form}
        return render(request, 'create_experience.html', context)


class MyEducation(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Education
    form_class = EducationForm
    template_name = 'create_education.html'

@login_required(login_url='login')
def EditEducation(request, pk):
        education = get_object_or_404(Education, pk=pk)
        form = EducationForm(instance=education)
        if request.method == 'POST':
            form = EducationForm(request.POST, instance=education)
            if form.is_valid():
                form.save()
                return redirect('resume')
        context = {'form':form}
        return render(request, 'create_education.html', context)


class MyProject(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Project
    form_class = ProjectForm
    template_name = 'create_project.html'
    success_url = reverse_lazy('resume')

@login_required(login_url='login')
def EditProject(request, pk):
        project = get_object_or_404(Project, pk=pk)
        form = ProjectForm(instance=project)
        if request.method == 'POST':
            form = ProjectForm(request.POST, instance=project)
            if form.is_valid():
                form.save()
                return redirect('resume')
        context = {'form':form}
        return render(request, 'create_project.html', context)

def Resume(request):
    language  = Languages.objects.all()[:5]
    education = Education.objects.all()[:3]
    experience = Experience.objects.all()[:4]
    person = Person.objects.all()[:1]
    skills = Skills.objects.all()[:5]
    awards = Awards.objects.all()[:5]
    projects = Project.objects.all()
    return render(request, 'resume.html', {'language':language, 'education':education, 'experience':
        experience, 'person': person, 'skills':skills, 'awards': awards, 'projects': projects})


class CreateAccount(CreateView):
    form_class= SignUpForm
    template_name='registration/register.html'
    success_url= reverse_lazy('resume')