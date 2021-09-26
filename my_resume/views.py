from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.views import PasswordChangeView
from django.views import View

# import pdfkit
from django.http import HttpResponse
from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa


from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView
from .models import Person, Awards, Education, Experience, Skills, Project, Volunteer
from .forms import  PersonForm, AwardForm, ExperienceForm, EducationForm, SkillsForm, ProjectForm, SignUpForm, EditAccountForm, PasswordChangingForm, VolunteerForm

# @login_required(login_url='login')
# def MyPerson(request):
#     context = {}
#     form = PersonForm
#     context['form'] = form

#     def form_valid(self, form):
#         person = form.save(commit=False)
#         person.user = self.request.user  
#         person.save()
#         return redirect('resume_done')

#     return render(request, 'create_user.html', context)

class MyPerson(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Person
    form_class= PersonForm
    template_name= 'create_user.html'
    success_url= reverse_lazy('resume_done')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        return Person.objects.filter(user=self.request.user)

@login_required(login_url='login')
def EditPerson(request, pk):
        person = get_object_or_404(Person, pk=pk)
        form = PersonForm(instance=person)
        if request.method == 'POST':
            form = PersonForm(request.POST, instance=person)
            if form.is_valid():
                form.save()
                return redirect('resume_done')
        context = {'form':form}
        return render(request, 'create_user.html', context)


class MySkills(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Skills
    form_class =SkillsForm
    template_name = 'create_skills.html'
    success_url = reverse_lazy('resume')

    def form_valid(self, form):
        experience = form.save(commit=False)
        experience.user = self.request.user  
        experience.save()
        return redirect('resume')

@login_required(login_url='login')
def EditSkills(request, pk):
        skills = get_object_or_404(Skills, pk=pk)
        form = SkillsForm(instance=skills)
        if request.method == 'POST':
            form = SkillsForm(request.POST, instance=skills)
            if form.is_valid():
                form.save()
                return redirect('resume_done')
        context = {'form':form}
        return render(request, 'create_skills.html', context)


class MyAward(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Awards
    form_class = AwardForm
    template_name = 'create_award.html'

    def form_valid(self, form):
        experience = form.save(commit=False)
        experience.user = self.request.user  
        experience.save()
        return redirect('resume')

@login_required(login_url='login')
def EditAward(request, pk):
        award = get_object_or_404(Awards, pk=pk)
        form = AwardForm(instance=award)
        if request.method == 'POST':
            form = AwardForm(request.POST, instance=award)
            if form.is_valid():
                form.save()
                return redirect('resume_done')
        context = {'form':form}
        return render(request, 'create_award.html', context)


class MyExperience(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Experience
    form_class = ExperienceForm
    template_name = 'create_experience.html'

    def form_valid(self, form):
        experience = form.save(commit=False)
        experience.user = self.request.user  
        experience.save()
        return redirect('resume')

@login_required(login_url='login')
def EditExperience(request, pk):
        experience = get_object_or_404(Experience, pk=pk)
        form = ExperienceForm(instance=experience)
        if request.method == 'POST':
            form = ExperienceForm(request.POST, instance=experience)
            if form.is_valid():
                form.save()
                return redirect('resume_done')
        context = {'form':form}
        return render(request, 'create_experience.html', context)


class MyEducation(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Education
    form_class = EducationForm
    template_name = 'create_education.html'

    def form_valid(self, form):
        experience = form.save(commit=False)
        experience.user = self.request.user  
        experience.save()
        return redirect('resume')

@login_required(login_url='login')
def EditEducation(request, pk):
        education = get_object_or_404(Education, pk=pk)
        form = EducationForm(instance=education)
        if request.method == 'POST':
            form = EducationForm(request.POST, instance=education)
            if form.is_valid():
                form.save()
                return redirect('resume_done')
        context = {'form':form}
        return render(request, 'create_education.html', context)


class MyProject(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Project
    form_class = ProjectForm
    template_name = 'create_project.html'
    success_url = reverse_lazy('resume')

    def form_valid(self, form):
        experience = form.save(commit=False)
        experience.user = self.request.user  
        experience.save()
        return redirect('resume')

@login_required(login_url='login')
def EditProject(request, pk):
        project = get_object_or_404(Project, pk=pk)
        form = ProjectForm(instance=project)
        if request.method == 'POST':
            form = ProjectForm(request.POST, instance=project)
            if form.is_valid():
                form.save()
                return redirect('resume_done')
        context = {'form':form}
        return render(request, 'create_project.html', context)


@login_required(login_url='login')
def Resume(request):
    education = Education.objects.filter(user = request.user)[:3]
    experience = Experience.objects.filter(user = request.user)[:5]
    person = Person.objects.filter(user = request.user)[:1]
    skills = Skills.objects.filter(user = request.user)[:7]
    awards = Awards.objects.filter(user = request.user)[:5]
    projects = Project.objects.filter(user = request.user)[:5]
    volunteer = Volunteer.objects.filter(user = request.user)[:5]
    return render(request, 'add_resume.html', {'education':education, 'experience':
        experience, 'person': person, 'skills':skills, 'awards': awards, 'projects': projects, 'volunteer':volunteer})



class CreateAccount(CreateView):
    form_class= SignUpForm
    template_name='registration/register.html'
    success_url= reverse_lazy('resume')

class UpdateAccount(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = User
    form_class= EditAccountForm
    template_name='registration/edit_profile.html'
    success_url= reverse_lazy('blog_list')

    def get_object(self):
        return self.request.user

@login_required(login_url='login')
def UserDelete(request):
     user = request.user
     if request.method == 'POST':
                user.delete()
                return redirect('login')


class PasswordsChangeView(LoginRequiredMixin, PasswordChangeView):
    login_url = 'login'
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')

@login_required(login_url='login')
def DeletePerson(request, pk):
	person  = Person .objects.get(id=pk)
	person.delete()
	return redirect('resume')

@login_required(login_url='login')
def DeleteSkills(request, pk):
	skills =Skills.objects.get(id=pk)
	skills.delete()
	return redirect('resume')

@login_required(login_url='login')
def DeleteExperience(request, pk):
	experience = Experience.objects.get(id=pk)
	experience.delete()
	return redirect('resume')

@login_required(login_url='login')
def DeleteEducation(request, pk):
	education = Education.objects.get(id=pk)
	education.delete()
	return redirect('resume')

@login_required(login_url='login')
def DeleteAwards(request, pk):
	queryset = Awards.objects.get(id=pk)
	queryset.delete()
	return redirect('resume')

@login_required(login_url='login')
def DeleteProject(request, pk):
	project = Project.objects.get(id=pk)
	project.delete()
	return redirect('resume')

class Volunteers(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Volunteer
    form_class = VolunteerForm
    template_name = 'create_volunteer.html'
    success_url = reverse_lazy('resume')

    def form_valid(self, form):
        volunteer = form.save(commit=False)
        volunteer.user = self.request.user  
        volunteer.save()
        return redirect('resume')


@login_required(login_url='login')
def EditVolunteers(request, pk):
        volunteer = get_object_or_404(Volunteer, pk=pk)
        form = VolunteerForm(instance=volunteer)
        if request.method == 'POST':
            form = VolunteerForm(request.POST, instance=volunteer)
            if form.is_valid():
                form.save()
                return redirect('resume_done')
        context = {'form':form}
        return render(request, 'create_volunteer.html', context)

@login_required(login_url='login')
def DeleteVolunteers(request, pk):
	volunteer = Volunteer.objects.get(id=pk)
	volunteer.delete()
	return redirect('resume')

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

class ViewPDF(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        education = Education.objects.filter(user = request.user)[:3]
        experience = Experience.objects.filter(user = request.user)[:5]
        person = Person.objects.filter(user = request.user)[:1]
        skills = Skills.objects.filter(user = request.user)[:7]
        awards = Awards.objects.filter(user = request.user)[:5]
        projects = Project.objects.filter(user = request.user)[:5]
        volunteer = Volunteer.objects.filter(user = request.user)[:5]
        data = {'education':education, 'experience':
        experience, 'person': person, 'skills':skills, 'awards': awards, 'projects': projects, 'volunteer':volunteer, 'user':user}

        pdf = render_to_pdf('pdf_template.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class DownloadPDF(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        education = Education.objects.filter(user = request.user)[:3]
        experience = Experience.objects.filter(user = request.user)[:5]
        person = Person.objects.filter(user = request.user)[:1]
        skills = Skills.objects.filter(user = request.user)[:7]
        awards = Awards.objects.filter(user = request.user)[:5]
        projects = Project.objects.filter(user = request.user)[:5]
        volunteer = Volunteer.objects.filter(user = request.user)[:5]
        data = {'education':education, 'experience':
        experience, 'person': person, 'skills':skills, 'awards': awards, 'projects': projects, 'volunteer':volunteer, 'user':user}
        pdf = render_to_pdf('pdf_template.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'my_resume.pdf'
        content = "attachment; filename='%s'" %(filename)
        response['Content-Disposition'] = content
        return response

def ResumeDone(request):
    return render(request, 'resume_done.html', {})



def Portfolio(request, username):
    context = {}
    emma = request.user
    username = get_object_or_404(User, username=username)
    person = Person.objects.filter(user=username.id)
    education = Education.objects.filter(user=username.id)
    skills = Skills.objects.filter(user=username.id)
    experience = Experience.objects.filter(user=username.id)
    projects = Project.objects.filter(user=username.id)
    awards = Awards.objects.filter(user=username.id)
    volunteer = Volunteer.objects.filter(user=username.id)
    context['username'] = username
    context['person'] = person
    context['education'] = education
    context['skills'] = skills
    context['experience'] = experience
    context['projects'] = projects
    context['awards'] = awards
    return render(request, "portfolio.html", context)

