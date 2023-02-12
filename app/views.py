import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.core.mail import send_mail
from django.conf import settings
from .forms import *
from .tokens import account_activation_token
from django.http import JsonResponse
from django.views import View

# import pdfkit
from django.http import HttpResponse
from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa

# Create your views here.

def portfolio(request, feedback_id, slugified_full_name):
    if Personal_Details.objects.filter(feedback_id=feedback_id).exists():
        personal_detail = Personal_Details.objects.get(feedback_id=feedback_id)
        if slugified_full_name == slugify(personal_detail.full_name):
            if Profile.objects.filter(personal_detail=personal_detail).exists:
                profile = Profile.objects.filter(personal_detail=personal_detail).last()
            context = {'personal_detail':personal_detail, 'profile':profile}
            return render(request, 'pages/portfolio.html', context)
        else:
            error = 'Portfolio Does Not Exist'
            return render(request, 'pages/portfolio.html', {"error":error})
    else:
        error = 'Portfolio Does Not Exist'
        return render(request, 'pages/portfolio.html', {"error":error})


def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

class ViewPdf(View):
    def get(self, request, *args, **kwargs):
        personal_detail = Personal_Details.objects.get(pk= self.kwargs['pk'])
        profile = Profile.objects.filter(personal_detail=personal_detail).last()
        skills = Skills.objects.filter(personal_detail=personal_detail)
        experiences = Experience.objects.filter(personal_detail=personal_detail)
        projects = Project.objects.filter(personal_detail=personal_detail)
        educations = Education.objects.filter(personal_detail=personal_detail)
        languages = Language.objects.filter(personal_detail=personal_detail)
        references = Reference.objects.filter(personal_detail=personal_detail)
        awards = Award.objects.filter(personal_detail=personal_detail)
        organisations = Organisation.objects.filter(personal_detail=personal_detail)
        certificates = Certificate.objects.filter(personal_detail=personal_detail)
        interests = Interest.objects.filter(personal_detail=personal_detail)
        publications = Publication.objects.filter(personal_detail=personal_detail)
        data = {'personal_detail':personal_detail, 'skills':skills, 'profile':profile, 'experiences':experiences, 'projects':projects, 'educations':educations, 'languages':languages,  'references':references, 'awards':awards, 'organisations':organisations, 'certificates':certificates,  'interests':interests, 'publications':publications}
        pdf = render_to_pdf('pages/pdf-resume-template.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class DownloadPdf(View):
    def get(self, request, *args, **kwargs):
        personal_detail = Personal_Details.objects.get(pk= self.kwargs['pk'])
        profile = Profile.objects.filter(personal_detail=personal_detail).last()
        skills = Skills.objects.filter(personal_detail=personal_detail)
        experiences = Experience.objects.filter(personal_detail=personal_detail)
        projects = Project.objects.filter(personal_detail=personal_detail)
        educations = Education.objects.filter(personal_detail=personal_detail)
        languages = Language.objects.filter(personal_detail=personal_detail)
        references = Reference.objects.filter(personal_detail=personal_detail)
        awards = Award.objects.filter(personal_detail=personal_detail)
        organisations = Organisation.objects.filter(personal_detail=personal_detail)
        certificates = Certificate.objects.filter(personal_detail=personal_detail)
        interests = Interest.objects.filter(personal_detail=personal_detail)
        publications = Publication.objects.filter(personal_detail=personal_detail)
        data = {'personal_detail':personal_detail, 'skills':skills, 'profile':profile, 'experiences':experiences, 'projects':projects, 'educations':educations, 'languages':languages,  'references':references, 'awards':awards, 'organisations':organisations, 'certificates':certificates,  'interests':interests, 'publications':publications}
        pdf = render_to_pdf('pages/pdf-resume-template.html', data)
        filename = f'{personal_detail.resume_name}.pdf'
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="' + filename + '"'
        return response

def pdfview(request, feedback_id):
    if Personal_Details.objects.filter(feedback_id=feedback_id, user=request.user).exists():
        personal_detail = Personal_Details.objects.get(feedback_id=feedback_id, user=request.user)
        feedbacks = Feedback.objects.filter(personal_detail=personal_detail)
        profile = Profile.objects.filter(personal_detail=personal_detail).last()
        profile_form = ProfileForm(instance=profile)
        personal_detail_form = PersonalDetailsForm(instance=personal_detail)
        skill_form = SkillForm()
        link_form = LinkForm(instance=personal_detail)
        skill_levels = Skill_Level.objects.all()
        skills = Skills.objects.filter(personal_detail=personal_detail)
        experiences = Experience.objects.filter(personal_detail=personal_detail)
        experience_form = ExperienceForm()
        projects = Project.objects.filter(personal_detail=personal_detail)
        project_form = ProjectForm()
        educations = Education.objects.filter(personal_detail=personal_detail)
        education_form = EducationForm()
        language_levels = Language_Level.objects.all()
        languages = Language.objects.filter(personal_detail=personal_detail)
        language_form = LanguageForm()
        references = Reference.objects.filter(personal_detail=personal_detail)
        reference_form = ReferenceForm()
        awards = Award.objects.filter(personal_detail=personal_detail)
        award_form = AwardForm()
        organisations = Organisation.objects.filter(personal_detail=personal_detail)
        organisation_form = OrganisationForm
        certificates = Certificate.objects.filter(personal_detail=personal_detail)
        certificate_form = CertificateForm()
        interests = Interest.objects.filter(personal_detail=personal_detail)
        interest_form = InterestForm()
        publications = Publication.objects.filter(personal_detail=personal_detail)
        publication_form = PublicationForm()
        context = {'personal_detail':personal_detail, 'profile_form':profile_form, 'personal_detail_form':personal_detail_form, 'skill_form':skill_form, 'skill_levels':skill_levels, 'link_form':link_form, 'skills':skills, 'experiences':experiences, 'experience_form':experience_form, 'projects':projects, 'project_form':project_form, 'educations':educations, 'education_form':education_form, 'language_levels':language_levels, 'languages':languages, 'language_form':language_form, 'references':references, 'reference_form':reference_form, 'awards':awards, 'award_form':award_form, 'organisations':organisations, 'organisation_form':organisation_form, 'certificates':certificates, 'certificate_form':certificate_form, 'interests':interests, 'interest_form':interest_form, 'publications':publications, 'publication_form':publication_form, 'feedbacks':feedbacks, 'profile':profile}
        return render(request, "pages/pdf-template.html", context)

# def downloadpdf(request, feedback_id):
#     apiKey = 
#     resume = Personal_Details.objects.get(feedback_id=feedback_id)
#     response = requests.post(
#     'https://api.restpdf.io/v1/pdf',
#     headers = {
#         'X-API-KEY'   : apiKey,
#         'content-type': 'application/json'
#     },
#     json = {
#         "output": "data",
#         "url": "https://github.com/chryzcode"
#     }   
#     )
                                    
#     if response.status_code == 200:
#         with open(f'{resume.resume_name}.pdf', 'wb') as file:
#             file.write(response.content)

    
#             # file_path = 'Resume 2.pdf'
#             # filename = f'{resume.resume_name}.pdf'
#             # response = HttpResponse(pdf, content_type='application/pdf')
#             # response['Content-Disposition'] = 'attachment; filename="' + filename + '"'
#             # return response
#             # return redirect('Resume', feedback_id=feedback_id)

#     else:
#         print("There was an error converting the PDF")
                                    


def custom_error_404(request, exception):
    return render(request, "error-pages/404-page.html")


def custom_error_500(request):
    return render(request, "error-pages/500-page.html")
    
def account_login(request):
    context = {}
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            try:
                user = authenticate(request, email=email, password=password)
                if user:
                    login(request, user)
                    return redirect("/") 
                else:
                    messages.error(request, "Password is incorrect")  
            except:
                messages.error(request, "Authentication error")
        else:
            messages.error(request, "Account does not exist")
        

    return render(request, "account/registration/login.html", context)



@login_required(login_url="login")
def account_logout(request):
    logout(request)
    return redirect("/")

@login_required(login_url="login")
def account_delete(request):
    user = User.objects.get(email=request.user.email)
    subject = f"Request for Your CVBuild Account to be Deleted"
    message = render_to_string(
    "account/user/account-delete-email.html",
    {"user": user,
    "domain": settings.DEFAULT_DOMAIN,
    }
)
    user.is_active = False
    user.save()
    send_mail(subject, message, settings.EMAIL_HOST_USER, user.email, html_message=message)
    logout(request)
    return redirect("/")


def account_register(request):
    if request.user.is_authenticated:
        return redirect("/")
    registerform = RegistrationForm
    if request.method == "POST":
        email = request.POST.get("email")
        registerform = RegistrationForm(request.POST)
        if registerform.is_valid():
            user = registerform.save(commit=False)
            user.email = registerform.cleaned_data["email"]
            user.first_name = registerform.cleaned_data["first_name"]
            user.last_name = registerform.cleaned_data["last_name"]
            user.set_password(registerform.cleaned_data["password"])
            user.is_active = False
            user.save()
            subject = "Activate your CV Build Account"
            message = render_to_string(
                "account/registration/account_activation_email.html",
                {
                    "user": user,
                    "domain": settings.DEFAULT_DOMAIN,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "token": account_activation_token.make_token(user),
                },
            )
            return render(request, "account/registration/registration-success.html")
       
    return render(request, "account/registration/register.html", {"form": registerform})


def account_activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_object_or_404(User, pk=uid)
    except:
        return render(request, "error-pages/404-page.html")

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        if not Personal_Details.objects.filter(user=user):
            Personal_Details.objects.create(
                user = user,
                full_name = user.first_name + ' ' + user.last_name,
                email = user.email,
                resume_name = 'Resume 1',
            )
        login(request, user)
        return redirect("/")
    else:
        if user:
            user.delete()
            messages.error(request, "Verification Authentication Timeout")
        else:
            messages.messages.error(request, "User/Account does not exist")
        return render(request, "error-pages/404-page.html")


@login_required(login_url="login")
def home(request):
    personal_detail = Personal_Details.objects.filter(user=request.user.id).last()
    profile = Profile.objects.filter(personal_detail=personal_detail).last()
    profile_form = ProfileForm(instance=profile)
    personal_detail_form = PersonalDetailsForm(instance=personal_detail)
    feedbacks = Feedback.objects.filter(personal_detail=personal_detail)
    skill_form = SkillForm()
    link_form = LinkForm(instance=personal_detail)
    skill_levels = Skill_Level.objects.all()
    skills = Skills.objects.filter(personal_detail=personal_detail)
    experiences = Experience.objects.filter(personal_detail=personal_detail)
    experience_form = ExperienceForm()
    projects = Project.objects.filter(personal_detail=personal_detail)
    project_form = ProjectForm()
    educations = Education.objects.filter(personal_detail=personal_detail)
    education_form = EducationForm()
    language_levels = Language_Level.objects.all()
    languages = Language.objects.filter(personal_detail=personal_detail)
    language_form = LanguageForm()
    references = Reference.objects.filter(personal_detail=personal_detail)
    reference_form = ReferenceForm()
    awards = Award.objects.filter(personal_detail=personal_detail)
    award_form = AwardForm()
    organisations = Organisation.objects.filter(personal_detail=personal_detail)
    organisation_form = OrganisationForm
    certificates = Certificate.objects.filter(personal_detail=personal_detail)
    certificate_form = CertificateForm()
    interests = Interest.objects.filter(personal_detail=personal_detail)
    interest_form = InterestForm()
    publications = Publication.objects.filter(personal_detail=personal_detail)
    publication_form = PublicationForm()
    context = {'personal_detail':personal_detail, 'profile_form':profile_form, 'personal_detail_form':personal_detail_form, 'skill_form':skill_form, 'skill_levels':skill_levels, 'link_form':link_form, 'skills':skills, 'experiences':experiences, 'experience_form':experience_form, 'projects':projects, 'project_form':project_form, 'educations':educations, 'education_form':education_form, 'language_levels':language_levels, 'languages':languages, 'language_form':language_form, 'references':references, 'reference_form':reference_form, 'awards':awards, 'award_form':award_form, 'organisations':organisations, 'organisation_form':organisation_form, 'certificates':certificates, 'certificate_form':certificate_form, 'interests':interests, 'interest_form':interest_form, 'publications':publications, 'publication_form':publication_form, 'feedbacks':feedbacks, 'profile':profile }
    return render(request, 'pages/home.html', context)



@login_required(login_url="login")
def Resume(request, feedback_id):
    if Personal_Details.objects.filter(feedback_id=feedback_id, user=request.user).exists():
        personal_detail = Personal_Details.objects.get(feedback_id=feedback_id, user=request.user)
        feedbacks = Feedback.objects.filter(personal_detail=personal_detail)
        profile = Profile.objects.filter(personal_detail=personal_detail).last()
        profile_form = ProfileForm(instance=profile)
        personal_detail_form = PersonalDetailsForm(instance=personal_detail)
        skill_form = SkillForm()
        link_form = LinkForm(instance=personal_detail)
        skill_levels = Skill_Level.objects.all()
        skills = Skills.objects.filter(personal_detail=personal_detail)
        experiences = Experience.objects.filter(personal_detail=personal_detail)
        experience_form = ExperienceForm()
        projects = Project.objects.filter(personal_detail=personal_detail)
        project_form = ProjectForm()
        educations = Education.objects.filter(personal_detail=personal_detail)
        education_form = EducationForm()
        language_levels = Language_Level.objects.all()
        languages = Language.objects.filter(personal_detail=personal_detail)
        language_form = LanguageForm()
        references = Reference.objects.filter(personal_detail=personal_detail)
        reference_form = ReferenceForm()
        awards = Award.objects.filter(personal_detail=personal_detail)
        award_form = AwardForm()
        organisations = Organisation.objects.filter(personal_detail=personal_detail)
        organisation_form = OrganisationForm
        certificates = Certificate.objects.filter(personal_detail=personal_detail)
        certificate_form = CertificateForm()
        interests = Interest.objects.filter(personal_detail=personal_detail)
        interest_form = InterestForm()
        publications = Publication.objects.filter(personal_detail=personal_detail)
        publication_form = PublicationForm()
        context = {'personal_detail':personal_detail, 'profile_form':profile_form, 'personal_detail_form':personal_detail_form, 'skill_form':skill_form, 'skill_levels':skill_levels, 'link_form':link_form, 'skills':skills, 'experiences':experiences, 'experience_form':experience_form, 'projects':projects, 'project_form':project_form, 'educations':educations, 'education_form':education_form, 'language_levels':language_levels, 'languages':languages, 'language_form':language_form, 'references':references, 'reference_form':reference_form, 'awards':awards, 'award_form':award_form, 'organisations':organisations, 'organisation_form':organisation_form, 'certificates':certificates, 'certificate_form':certificate_form, 'interests':interests, 'interest_form':interest_form, 'publications':publications, 'publication_form':publication_form, 'feedbacks':feedbacks, 'profile':profile}
        return render(request, 'pages/home.html', context)

def deleteResume(request, feedback_id):
    if Personal_Details.objects.filter(user=request.user).count() > 1:
        resume = Personal_Details.objects.get(feedback_id=feedback_id)
        resume.delete()
        return redirect('/')
    else:
        messages.error(request, 'There must be at least a resume remaining.')
        return redirect('/')


def person_details(request, pk):
    user = request.user
    if Personal_Details.objects.filter(user=user, pk=pk).exists():
        personal_detail = Personal_Details.objects.get(user=user, pk=pk)
        personal_details_form = PersonalDetailsForm(instance=personal_detail)
    else:
        personal_details_form = PersonalDetailsForm()
    if request.method == "POST":
        if Personal_Details.objects.filter(user=user).exists():
            personal_details_form = PersonalDetailsForm(request.POST, instance=personal_detail)
        else:
            personal_details_form = PersonalDetailsForm(request.POST)
        if personal_details_form.is_valid():
            form = personal_details_form.save(commit=False)
            form.user = user
            form.save()
            return redirect('Resume', feedback_id=personal_detail.feedback_id)
        else:
            messages.error(request, personal_details_form.errors)
            return redirect('Resume', feedback_id=personal_detail.feedback_id)

        

def profile(request, pk):
    user = request.user
    if Personal_Details.objects.filter(user=user, pk=pk).exists():
        personal_detail = Personal_Details.objects.get(user=user, pk=pk)
        if Profile.objects.filter(personal_detail=personal_detail).exists():
            profile = Profile.objects.get(personal_detail=personal_detail)
            profile_form = ProfileForm(instance=profile)
        else:
            profile_form = ProfileForm()
        if request.method == "POST":
            if Profile.objects.filter(personal_detail=personal_detail).exists():
                profile_form = ProfileForm(request.POST, instance=profile)
            else:
                profile_form = ProfileForm(request.POST)
            if profile_form.is_valid():
                form = profile_form.save(commit=False)
                form.personal_detail = personal_detail
                form.save()
                return redirect('Resume', feedback_id=personal_detail.feedback_id)
            else:
                messages.error(request, profile_form.errors)
                return redirect('Resume', feedback_id=personal_detail.feedback_id)




def addSkill(request, pk):
    user = request.user
    if Personal_Details.objects.filter(user=user, pk=pk).exists():
        personal_detail = Personal_Details.objects.get(user=user, pk=pk)
        skill_form = SkillForm()
        if request.method == "POST":
            skill_form = SkillForm(request.POST)
        if skill_form.is_valid():
            form = skill_form.save(commit=False)
            form.personal_detail = personal_detail
            form.save()
            return redirect('Resume', feedback_id=personal_detail.feedback_id)
        else:
            messages.error(request, skill_form.errors)
            return redirect('Resume', feedback_id=personal_detail.feedback_id)
    
def getSkill(request, pk, feedback_id):
    skill = Skills.objects.get(id=pk)
    skill_name = skill.skill_name
    skill_info = skill.skill_information
    if skill.skill_level:
        skill_level_id = skill.skill_level.id
        skill_level = Skill_Level.objects.get(id=skill_level_id).name
    else:
        skill_level_id = ''
        skill_level = ''
    
    response = JsonResponse(
        {
            "skill_name": skill_name ,
            "skill_info": skill_info,
            "skill_level": skill_level,
            "skill_level_id":skill_level_id,
        }
        )
    return response

def updateSkill(request, pk, feedback_id):
    skill = Skills.objects.get(id=pk)
    skill_form = SkillForm(request.POST, instance=skill)
    if skill_form.is_valid():
        form = skill_form.save(commit=False)  
        form.save()
        return redirect('Resume', feedback_id=feedback_id)
    messages.error(request, skill_form.errors)
    return redirect('Resume', feedback_id=feedback_id)


def deleteSkill(request, pk, feedback_id):
    skill = Skills.objects.get(id=pk)
    skill.delete()
    return redirect('Resume', feedback_id=feedback_id)


def addExperience(request, pk):
    user = request.user
    if Personal_Details.objects.filter(user=user, pk=pk).exists():
        personal_detail = Personal_Details.objects.get(id=pk, user=user)
        experience_form = ExperienceForm()
        if request.method == "POST":
            experience_form = ExperienceForm(request.POST)
        if experience_form.is_valid():
            form = experience_form.save(commit=False)
            form.personal_detail = personal_detail
            form.save()
            return redirect('Resume', feedback_id=personal_detail.feedback_id)
        else:
            messages.error(request, experience_form.errors)
            return redirect('Resume', feedback_id=personal_detail.feedback_id)


def getExperience(request, pk, feedback_id):
    experience = Experience.objects.get(id=pk)
    experience_job_title = experience.experience_job_title
    experience_employer = experience.employer
    experience_city = experience.experience_city
    experience_country = experience.experience_country
    experience_start_date = experience.experience_start_date
    experience_end_date = experience.experience_end_date
    experience_description = experience.experience_description
    experience_current = experience.experience_current
    experience_link = experience.experience_link
    experience_month_year_only = experience.experience_month_year_only
    experience_year_only = experience.experience_year_only
    response = JsonResponse(
        {
            "experience_job_title": experience_job_title ,
            "experience_employer": experience_employer,
            "experience_city": experience_city,
            "experience_country":experience_country,
            "experience_start_date":experience_start_date,
            "experience_end_date": experience_end_date,
            "experience_description":experience_description,
            "experience_current": experience_current,
            "experience_link": experience_link,
            "experience_month_year_only": experience_month_year_only,
            "experience_year_only": experience_year_only,
        }
        )
    return response


def updateExperience(request, pk, feedback_id):
    experience = Experience.objects.get(id=pk)
    experience_form = ExperienceForm(request.POST, instance=experience)
    if experience_form.is_valid():
        form = experience_form.save(commit=False)  
        form.save()
        return redirect('Resume', feedback_id=feedback_id)
    messages.error(request, experience_form.errors)
    return redirect('Resume', feedback_id=feedback_id)


def deleteExperience(request, pk, feedback_id):
    experience = Experience.objects.get(id=pk)
    experience.delete()
    return redirect('Resume', feedback_id=feedback_id)


def addProject(request, pk):
    user = request.user
    if Personal_Details.objects.filter(user=user, pk=pk).exists():
        personal_detail = Personal_Details.objects.get(user=user, pk=pk)  
        project_form = ProjectForm()
        if request.method == "POST":
            project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            form = project_form.save(commit=False)
            form.personal_detail = personal_detail
            form.save()
            return redirect('Resume', feedback_id=personal_detail.feedback_id)
        else:
            messages.error(request, project_form.errors)
            return redirect('Resume', feedback_id=personal_detail.feedback_id)

def getProject(request, pk, feedback_id):
    project = Project.objects.get(id=pk)
    project_project_title = project.project_title
    project_subtitle = project.subtitle
    project_start_date = project.project_start_date
    project_end_date = project.project_end_date
    project_description = project.project_description
    project_current = project.project_current
    project_link = project.project_link
    project_month_year_only = project.project_month_year_only
    project_year_only = project.project_year_only
    response = JsonResponse(
        {
            "project_project_title": project_project_title ,
            "project_subtitle": project_subtitle,
            "project_start_date": project_start_date,
            "project_end_date":project_end_date,
            "project_description":project_description,
            "project_current": project_current,
            "project_link":project_link,
            "project_month_year_only": project_month_year_only,
            "project_year_only": project_year_only,
        }
        )
    return response


def updateProject(request, pk, feedback_id):
    project = Project.objects.get(id=pk)
    project_form = ProjectForm(request.POST, instance=project)
    if project_form.is_valid():
        form = project_form.save(commit=False)  
        form.save()
        return redirect('Resume', feedback_id=feedback_id)
    messages.error(request, project_form.errors)
    return redirect('Resume', feedback_id=feedback_id)


def deleteProject(request, pk, feedback_id):
    project = Project.objects.get(id=pk)
    project.delete()
    return redirect('Resume', feedback_id=feedback_id)


def addEducation(request, pk):
    user = request.user
    if Personal_Details.objects.filter(user=user, pk=pk).exists():
        personal_detail = Personal_Details.objects.get(id=pk, user=user)
        education_form = EducationForm()
        if request.method == "POST":
            education_form = EducationForm(request.POST)
        if education_form.is_valid():
            form = education_form.save(commit=False)
            form.personal_detail = personal_detail
            form.save()
            return redirect('Resume', feedback_id=personal_detail.feedback_id)
        else:
            messages.error(request, education_form.errors)
            return redirect('Resume', feedback_id=personal_detail.feedback_id)

def getEducation(request, pk, feedback_id):
    education = Education.objects.get(id=pk)
    education_school = education.school
    education_degree = education.degree
    education_city = education.education_city
    education_country = education.education_country
    education_start_date = education.education_start_date
    education_end_date = education.education_end_date
    education_description = education.education_description
    education_current = education.education_current
    education_link = education.education_link
    education_month_year_only = education.education_month_year_only
    education_year_only = education.education_year_only
    response = JsonResponse(
        {
            "education_school": education_school ,
            "education_degree": education_degree,
            "education_city": education_city,
            "education_country":education_country,
            "education_start_date":education_start_date,
            "education_end_date": education_end_date,
            "education_description":education_description,
            "education_current": education_current,
            "education_link": education_link,
            "education_month_year_only": education_month_year_only,
            "education_year_only": education_year_only,
        }
        )
    return response


def updateEducation(request, pk, feedback_id):
    education = Education.objects.get(id=pk)
    education_form = EducationForm(request.POST, instance=education)
    if education_form.is_valid():
        form = education_form.save(commit=False)  
        form.save()
        return redirect('Resume', feedback_id=feedback_id)
    messages.error(request, education_form.errors)
    return redirect('Resume', feedback_id=feedback_id)


def deleteEducation(request, pk, feedback_id):
    education = Education.objects.get(id=pk)
    education.delete()
    return redirect('Resume', feedback_id=feedback_id)


def addLanguage(request, pk):
    user = request.user
    if Personal_Details.objects.filter(user=user, pk=pk).exists():
        personal_detail = Personal_Details.objects.get(id=pk, user=user)
        language_form = LanguageForm()
        if request.method == "POST":
            language_form = LanguageForm(request.POST)
        if language_form.is_valid():
            form = language_form.save(commit=False)
            form.personal_detail = personal_detail
            form.save()
            return redirect('Resume', feedback_id=personal_detail.feedback_id)
        else:
            messages.error(request, language_form.errors)
            return redirect('Resume', feedback_id=personal_detail.feedback_id)
    
def getLanguage(request, pk, feedback_id):
    language = Language.objects.get(id=pk)
    language_name = language.language
    language_additional_information = language.language_additional_information
    if language.language_level:
        language_level_id = language.language_level.id
        language_level = Language_Level.objects.get(id=language_level_id).name
    else:
        language_level_id = ''
        language_level = ''
    
    response = JsonResponse(
        {
            "language_name": language_name ,
            "language_additional_information": language_additional_information,
            "language_level": language_level,
            "language_level_id":language_level_id,
        }
        )
    return response

def updateLanguage(request, pk, feedback_id):
    language = Language.objects.get(id=pk)
    language_form = LanguageForm(request.POST, instance=language)
    if language_form.is_valid():
        form = language_form.save(commit=False)  
        form.save()
        return redirect('Resume', feedback_id=feedback_id)
    messages.error(request, language_form.errors)
    return redirect('Resume', feedback_id=feedback_id)


def deleteLanguage(request, pk, feedback_id):
    language = Language.objects.get(id=pk)
    language.delete()
    return redirect('Resume', feedback_id=feedback_id)


def addReference(request, pk):
    user = request.user
    if Personal_Details.objects.filter(user=user, pk=pk).exists():
        personal_detail = Personal_Details.objects.get(id=pk, user=user)
        reference_form = ReferenceForm()
        if request.method == "POST":
            reference_form = ReferenceForm(request.POST)
        if reference_form.is_valid():
            form = reference_form.save(commit=False)
            form.personal_detail = personal_detail
            form.save()
            return redirect('Resume', feedback_id=personal_detail.feedback_id)
        else:
            messages.error(request, reference_form.errors)
            return redirect('Resume', feedback_id=personal_detail.feedback_id)

def getReference(request, pk, feedback_id):
    reference = Reference.objects.get(id=pk)
    reference_name = reference.reference_name
    reference_job_title = reference.reference_job_title
    reference_organisation = reference.reference_organisation
    reference_phone = reference.reference_phone
    reference_email = reference.reference_email
    reference_link = reference.reference_link
    response = JsonResponse(
        {
            "reference_name": reference_name ,
            "reference_job_title": reference_job_title,
            "reference_organisation": reference_organisation,
            "reference_phone":reference_phone,
            "reference_email":reference_email,
            "reference_link": reference_link,
        }
        )
    return response


def updateReference(request, pk, feedback_id):
    reference = Reference.objects.get(id=pk)
    reference_form = ReferenceForm(request.POST, instance=reference)
    if reference_form.is_valid():
        form = reference_form.save(commit=False)  
        form.save()
        return redirect('Resume', feedback_id=feedback_id)
    messages.error(request, reference_form.errors)
    return redirect('Resume', feedback_id=feedback_id)


def deleteReference(request, pk, feedback_id):
    reference = Reference.objects.get(id=pk)
    reference.delete()
    return redirect('Resume', feedback_id=feedback_id)

def addAward(request, pk):
    user = request.user
    if Personal_Details.objects.filter(user=user).exists():
        personal_detail = Personal_Details.objects.get(id=pk, user=user)
        award_form = AwardForm()
        if request.method == "POST":
            award_form = AwardForm(request.POST)
        if award_form.is_valid():
            form = award_form.save(commit=False)
            form.personal_detail = personal_detail
            form.save()
            return redirect('Resume', feedback_id=personal_detail.feedback_id)
        else:
            messages.error(request, award_form.errors)
            return redirect('Resume', feedback_id=personal_detail.feedback_id)

def getAward(request, pk, feedback_id):
    award = Award.objects.get(id=pk)
    award_name = award.award
    award_issuer = award.issuer
    award_description = award.award_description
    award_date = award.award_date
    award_link = award.award_link
    award_month_year_only = award.award_month_year_only
    award_year_only = award.award_year_only
    response = JsonResponse(
        {
            "award_name": award_name ,
            "award_issuer": award_issuer,
            "award_description": award_description,
            "award_date":award_date,
            "award_link":award_link,
            "award_month_year_only":award_month_year_only,
            "award_year_only":award_year_only,
        }
        )
    return response


def updateAward(request, pk, feedback_id):
    award = Award.objects.get(id=pk)
    award_form = AwardForm(request.POST, instance=award)
    if award_form.is_valid():
        form = award_form.save(commit=False)  
        form.save()
        return redirect('Resume', feedback_id=feedback_id)
    messages.error(request, award_form.errors)
    return redirect('Resume', feedback_id=feedback_id)


def deleteAward(request, pk, feedback_id):
    award = Award.objects.get(id=pk)
    award.delete()
    return redirect('Resume', feedback_id=feedback_id)


def addOrganisation(request, pk):
    user = request.user
    if Personal_Details.objects.filter(user=user, pk=pk).exists():
        personal_detail = Personal_Details.objects.get(id=pk, user=user)
        organisation_form = OrganisationForm()
        if request.method == "POST":
            organisation_form = OrganisationForm(request.POST)
        if organisation_form.is_valid():
            form = organisation_form.save(commit=False)
            form.personal_detail = personal_detail
            form.save()
            return redirect('Resume', feedback_id=personal_detail.feedback_id)
        else:
            messages.error(request, organisation_form.errors)
            return redirect('Resume', feedback_id=personal_detail.feedback_id)


def getOrganisation(request, pk, feedback_id):
    organisation = Organisation.objects.get(id=pk)
    organisation_position = organisation.position
    organisation_organization = organisation.organisation
    organisation_city = organisation.organisation_city
    organisation_country = organisation.organisation_country
    organisation_start_date = organisation.organisation_start_date
    organisation_end_date = organisation.organisation_end_date
    organisation_description = organisation.organisation_description
    organisation_current = organisation.organisation_current
    organisation_link = organisation.organisation_link
    organisation_month_year_only = organisation.organisation_month_year_only
    organisation_year_only = organisation.organisation_year_only
    response = JsonResponse(
        {
            "organisation_position": organisation_position ,
            "organisation_organization": organisation_organization,
            "organisation_city": organisation_city,
            "organisation_country":organisation_country,
            "organisation_start_date":organisation_start_date,
            "organisation_end_date": organisation_end_date,
            "organisation_description":organisation_description,
            "organisation_current": organisation_current,
            "organisation_link": organisation_link,
            "organisation_month_year_only": organisation_month_year_only,
            "organisation_year_only": organisation_year_only,
        }
        )
    return response


def updateOrganisation(request, pk, feedback_id):
    organisation = Organisation.objects.get(id=pk)
    organisation_form = OrganisationForm(request.POST, instance=organisation)
    if organisation_form.is_valid():
        form = organisation_form.save(commit=False)  
        form.save()
        return redirect('Resume', feedback_id=feedback_id)
    messages.error(request, organisation_form.errors)
    return redirect('Resume', feedback_id=feedback_id)

def deleteOrganisation(request, pk, feedback_id):
    organisation = Organisation.objects.get(id=pk)
    organisation.delete()
    return redirect('Resume', feedback_id=feedback_id)


def addCertificate(request, pk):
    user = request.user
    if Personal_Details.objects.filter(user=user, pk=pk).exists():
        personal_detail = Personal_Details.objects.get(id=pk, user=user)
        certificate_form = CertificateForm()
        if request.method == "POST":
            certificate_form = CertificateForm(request.POST)
        if certificate_form.is_valid():
            form = certificate_form.save(commit=False)
            form.personal_detail = personal_detail
            form.save()
            return redirect('Resume', feedback_id=personal_detail.feedback_id)
        else:
            messages.error(request, certificate_form.errors)
            return redirect('Resume', feedback_id=personal_detail.feedback_id)

def getCertificate(request, pk, feedback_id):
    ceritficate = Certificate.objects.get(id=pk)
    ceritficate_name = ceritficate.certificate
    ceritficate_additional_information = ceritficate.certificate_additional_information
    ceritficate_link = ceritficate.certificate_link
    response = JsonResponse(
        {
            "ceritficate_name": ceritficate_name ,
            "ceritficate_additional_information": ceritficate_additional_information,
            "ceritficate_link": ceritficate_link,
        }
        )
    return response


def updateCertificate(request, pk, feedback_id):
    ceritficate = Certificate.objects.get(id=pk)
    ceritficate_form = CertificateForm(request.POST, instance=ceritficate)
    if ceritficate_form.is_valid():
        form = ceritficate_form.save(commit=False)  
        form.save()
        return redirect('Resume', feedback_id=feedback_id)
    messages.error(request, ceritficate_form.errors)
    return redirect('Resume', feedback_id=feedback_id)


def deleteCertificate(request, pk, feedback_id):
    ceritficate = Certificate.objects.get(id=pk)
    ceritficate.delete()
    return redirect('Resume', feedback_id=feedback_id)


def addInterest(request, pk):
    user = request.user
    if Personal_Details.objects.filter(user=user, pk=pk).exists():
        personal_detail = Personal_Details.objects.get(id=pk, user=user)
        interest_form = InterestForm()
        if request.method == "POST":
            interest_form = InterestForm(request.POST)
        if interest_form.is_valid():
            form = interest_form.save(commit=False)
            form.personal_detail = personal_detail
            form.save()
            return redirect('Resume', feedback_id=personal_detail.feedback_id)
        else:
            messages.error(request, interest_form.errors)
            return redirect('Resume', feedback_id=personal_detail.feedback_id)

def getInterest(request, pk, feedback_id):
    interest = Interest.objects.get(id=pk)
    interest_name = interest.interest
    interest_additional_information = interest.interest_additional_information
    interest_link = interest.interest_link
    response = JsonResponse(
        {
            "interest_name": interest_name ,
            "interest_additional_information": interest_additional_information,
            "interest_link": interest_link,
        }
        )
    return response


def updateInterest(request, pk, feedback_id):
    interest = Interest.objects.get(id=pk)
    interest_form = InterestForm(request.POST, instance=interest)
    if interest_form.is_valid():
        form = interest_form.save(commit=False)  
        form.save()
        return redirect('Resume', feedback_id=feedback_id)
    messages.error(request, interest_form.errors)
    return redirect('Resume', feedback_id=feedback_id)


def deleteInterest(request, pk, feedback_id):
    interest = Interest.objects.get(id=pk)
    interest.delete()
    return redirect('Resume', feedback_id=feedback_id)

    
def addPublication(request, pk):
    user = request.user
    if Personal_Details.objects.filter(user=user, pk=pk).exists():
        personal_detail = Personal_Details.objects.get(id=pk, user=user)
        publication_form = PublicationForm()
        if request.method == "POST":
            publication_form = PublicationForm(request.POST)
        if publication_form.is_valid():
            form = publication_form.save(commit=False)
            form.personal_detail = personal_detail
            form.save()
            return redirect('Resume', feedback_id=personal_detail.feedback_id)
        else:
            messages.error(request, publication_form.errors)
            return redirect('Resume', feedback_id=personal_detail.feedback_id)

def getPublication(request, pk, feedback_id):
    publication = Publication.objects.get(id=pk)
    publication_publisher = publication.publisher
    publication_name = publication.publication_title
    publication_date = publication.publication_date
    publication_description = publication.publication_description
    publication_link = publication.publication_link
    publication_month_year_only = publication.publication_month_year_only
    publication_year_only = publication.publication_year_only
    response = JsonResponse(
        {
            "publication_publisher": publication_publisher ,
            "publication_name": publication_name,
            "publication_date": publication_date,
            "publication_description":publication_description,
            "publication_link":publication_link,
            "publication_month_year_only": publication_month_year_only,
            "publication_year_only":publication_year_only,
        }
        )
    return response


def updatePublication(request, pk, feedback_id):
    publication = Publication.objects.get(id=pk)
    publication_form = PublicationForm(request.POST, instance=publication)
    if publication_form.is_valid():
        form = publication_form.save(commit=False)  
        form.save()
        return redirect('Resume', feedback_id=feedback_id)
    messages.error(request, publication_form.errors)
    return redirect('Resume', feedback_id=feedback_id)


def deletePublication(request, pk, feedback_id):
    publication = Publication.objects.get(id=pk)
    publication.delete()
    return redirect('Resume', feedback_id=feedback_id)

def resumeFeedback(request, feedback_id):
    if Personal_Details.objects.filter(feedback_id=feedback_id).exists():
        personal_detail = Personal_Details.objects.get(feedback_id=feedback_id)
        profile = Profile.objects.filter(personal_detail=personal_detail).last()
        skills = Skills.objects.filter(personal_detail=personal_detail)
        experiences = Experience.objects.filter(personal_detail=personal_detail)
        projects = Project.objects.filter(personal_detail=personal_detail)
        educations = Education.objects.filter(personal_detail=personal_detail)
        languages = Language.objects.filter(personal_detail=personal_detail)
        references = Reference.objects.filter(personal_detail=personal_detail)
        awards = Award.objects.filter(personal_detail=personal_detail)
        organisations = Organisation.objects.filter(personal_detail=personal_detail)
        certificates = Certificate.objects.filter(personal_detail=personal_detail)
        interests = Interest.objects.filter(personal_detail=personal_detail)
        publications = Publication.objects.filter(personal_detail=personal_detail)
        feedback_form = FeedbackForm()
        if request.method == "POST":
            feedback_form = FeedbackForm(request.POST)
            if feedback_form.is_valid:
                form = feedback_form.save(commit=False)
                form.personal_detail = personal_detail
                form.save()
                return redirect("resumeFeedback", feedback_id=feedback_id)
            else:
                messages.error(request, feedback_form.errors)
                return redirect("resumeFeedback", feedback_id=feedback_id)

        context = {'personal_detail':personal_detail, 'skills':skills, 'profile':profile, 'experiences':experiences, 'projects':projects, 'educations':educations, 'languages':languages,  'references':references, 'awards':awards, 'organisations':organisations, 'certificates':certificates,  'interests':interests, 'publications':publications, 'feedback_form':feedback_form}
        return render(request, 'pages/resume-feedback.html', context)
