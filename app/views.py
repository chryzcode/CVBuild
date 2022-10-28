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


def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

class ViewPdf(View):
    def get(self, request, *args, **kwargs):
        resume = Personal_Details.objects.get(pk= self.kwargs['id'])
        data = {'resume': resume}
        pdf = render_to_pdf('pdf-template.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class DownloadPdf(View):
    def get(self, request, *args, **kwargs):
        resume = Personal_Details.objects.get(pk= self.kwargs['id'])
        data = {'resume': resume}
        pdf = render_to_pdf('pdf-template.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = resume.resume_name
        content = "attachment; filename='%s'" %(filename)
        response['Content-Disposition'] = content
        return response

def custom_error_404(request, exception):
    return render(request, "error-pages/404-page.html")


def custom_error_500(request):
    return render(request, "error-pages/500-page.html")
    
def account_login(request):
    context = {}
    # if request.user.is_authenticated:
    #     return redirect("/")

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
    subject = f"Request for Your CV Build Account to be Deleted"
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
    # if request.user.is_authenticated:
    #     return redirect("/")
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
            user.email_user(subject=subject, message=message)
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
    context = {'personal_detail':personal_detail, 'profile_form':profile_form, 'personal_detail_form':personal_detail_form, 'skill_form':skill_form, 'skill_levels':skill_levels, 'link_form':link_form, 'skills':skills, 'experiences':experiences, 'experience_form':experience_form, 'projects':projects, 'project_form':project_form, 'educations':educations, 'education_form':education_form, 'language_levels':language_levels, 'languages':languages, 'language_form':language_form, 'references':references, 'reference_form':reference_form, 'awards':awards, 'award_form':award_form, 'organisations':organisations, 'organisation_form':organisation_form, 'certificates':certificates, 'certificate_form':certificate_form, 'interests':interests, 'interest_form':interest_form, 'publications':publications, 'publication_form':publication_form, 'feedbacks':feedbacks}
    return render(request, 'pages/home.html', context)



@login_required(login_url="login")
def otherResume(request, feedback_id):
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
        context = {'personal_detail':personal_detail, 'profile_form':profile_form, 'personal_detail_form':personal_detail_form, 'skill_form':skill_form, 'skill_levels':skill_levels, 'link_form':link_form, 'skills':skills, 'experiences':experiences, 'experience_form':experience_form, 'projects':projects, 'project_form':project_form, 'educations':educations, 'education_form':education_form, 'language_levels':language_levels, 'languages':languages, 'language_form':language_form, 'references':references, 'reference_form':reference_form, 'awards':awards, 'award_form':award_form, 'organisations':organisations, 'organisation_form':organisation_form, 'certificates':certificates, 'certificate_form':certificate_form, 'interests':interests, 'interest_form':interest_form, 'publications':publications, 'publication_form':publication_form, 'feedbacks':feedbacks}
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
            return redirect('home')
        else:
            messages.error(request, personal_details_form.errors)
            return redirect('/')

        

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
                return redirect('home')
            else:
                messages.error(request, profile_form.errors)
                return redirect('/')




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
            return redirect('home')
        else:
            messages.error(request, skill_form.errors)
            return redirect('/')
    
def getSkill(request, pk):
    skill = Skills.objects.get(id=pk)
    skill_name = skill.skill
    skill_info = skill.information
    if skill.level:
        skill_level_id = skill.level.id
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

def updateSkill(request, pk):
    skill = Skills.objects.get(id=pk)
    skill_form = SkillForm(request.POST, instance=skill)
    if skill_form.is_valid():
        form = skill_form.save(commit=False)  
        form.save()
        return redirect('home')
    messages.error(request, skill_form.errors)
    return redirect("/")


def deleteSkill(request, pk):
    skill = Skills.objects.get(id=pk)
    skill.delete()
    return redirect('/')


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
            return redirect('/')
        else:
            messages.error(request, experience_form.errors)
            return redirect('/')


def getExperience(request, pk):
    experience = Experience.objects.get(id=pk)
    experience_job_title = experience.job_title
    experience_employer = experience.employer
    experience_city = experience.city
    experience_country = experience.country
    experience_start_date = experience.start_date
    experience_end_date = experience.end_date
    experience_description = experience.experience_description
    experience_current = experience.current
    experience_link = experience.link
    experience_month_year_only = experience.month_year_only
    experience_year_only = experience.year_only
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


def updateExperience(request, pk):
    experience = Experience.objects.get(id=pk)
    experience_form = ExperienceForm(request.POST, instance=experience)
    if experience_form.is_valid():
        form = experience_form.save(commit=False)  
        form.save()
        return redirect('home')
    messages.error(request, experience_form.errors)
    return redirect("/")


def deleteExperience(request, pk):
    experience = Experience.objects.get(id=pk)
    experience.delete()
    return redirect('/')


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
            return redirect('/')
        else:
            messages.error(request, project_form.errors)
            return redirect('/')

def getProject(request, pk):
    project = Project.objects.get(id=pk)
    project_project_title = project.project_title
    project_subtitle = project.subtitle
    project_start_date = project.start_date
    project_end_date = project.end_date
    project_description = project.project_description
    project_current = project.current
    project_link = project.link
    project_month_year_only = project.month_year_only
    project_year_only = project.year_only
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


def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    project_form = ProjectForm(request.POST, instance=project)
    if project_form.is_valid():
        form = project_form.save(commit=False)  
        form.save()
        return redirect('home')
    messages.error(request, project_form.errors)
    return redirect("/")


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    project.delete()
    return redirect('/')


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
            return redirect('home')
        else:
            messages.error(request, education_form.errors)
            return redirect('/')

def getEducation(request, pk):
    education = Education.objects.get(id=pk)
    education_school = education.school
    education_degree = education.degree
    education_city = education.city
    education_country = education.country
    education_start_date = education.start_date
    education_end_date = education.end_date
    education_description = education.description
    education_current = education.current
    education_link = education.link
    education_month_year_only = education.month_year_only
    education_year_only = education.year_only
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


def updateEducation(request, pk):
    education = Education.objects.get(id=pk)
    education_form = EducationForm(request.POST, instance=education)
    if education_form.is_valid():
        form = education_form.save(commit=False)  
        form.save()
        return redirect('home')
    messages.error(request, education_form.errors)
    return redirect("/")


def deleteEducation(request, pk):
    education = Education.objects.get(id=pk)
    education.delete()
    return redirect('/')


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
            return redirect('home')
        else:
            messages.error(request, language_form.errors)
            return redirect('/')
    
def getLanguage(request, pk):
    language = Language.objects.get(id=pk)
    language_name = language.language
    language_additional_information = language.additional_information
    if language.level:
        language_level_id = language.level.id
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

def updateLanguage(request, pk):
    language = Language.objects.get(id=pk)
    language_form = LanguageForm(request.POST, instance=language)
    if language_form.is_valid():
        form = language_form.save(commit=False)  
        form.save()
        return redirect('home')
    messages.error(request, language_form.errors)
    return redirect("/")


def deleteLanguage(request, pk):
    language = Language.objects.get(id=pk)
    language.delete()
    return redirect('/')


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
            return redirect('/')
        else:
            messages.error(request, reference_form.errors)
            return redirect('/')

def getReference(request, pk):
    reference = Reference.objects.get(id=pk)
    reference_name = reference.reference_name
    reference_job_title = reference.job_title
    reference_organisation = reference.organisation
    reference_phone = reference.phone
    reference_email = reference.email
    reference_link = reference.link
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


def updateReference(request, pk):
    reference = Reference.objects.get(id=pk)
    reference_form = ReferenceForm(request.POST, instance=reference)
    if reference_form.is_valid():
        form = reference_form.save(commit=False)  
        form.save()
        return redirect('home')
    messages.error(request, reference_form.errors)
    return redirect("/")


def deleteReference(request, pk):
    reference = Reference.objects.get(id=pk)
    reference.delete()
    return redirect('/')


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
            return redirect('/')
        else:
            messages.error(request, award_form.errors)
            return redirect('/')

def getAward(request, pk):
    award = Award.objects.get(id=pk)
    award_name = award.award
    award_issuer = award.issuer
    award_description = award.description
    award_date = award.date
    award_link = award.link
    response = JsonResponse(
        {
            "award_name": award_name ,
            "award_issuer": award_issuer,
            "award_description": award_description,
            "award_date":award_date,
            "award_link":award_link,
        }
        )
    return response


def updateAward(request, pk):
    award = Award.objects.get(id=pk)
    award_form = AwardForm(request.POST, instance=award)
    if award_form.is_valid():
        form = award_form.save(commit=False)  
        form.save()
        return redirect('home')
    messages.error(request, award_form.errors)
    return redirect("/")


def deleteAward(request, pk):
    award = Award.objects.get(id=pk)
    award.delete()
    return redirect('/')


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
            return redirect('home')
        else:
            messages.error(request, organisation_form.errors)
            return redirect('/')


def getOrganisation(request, pk):
    organisation = Organisation.objects.get(id=pk)
    organisation_position = organisation.position
    organisation_organization = organisation.organisation
    organisation_city = organisation.city
    organisation_country = organisation.country
    organisation_start_date = organisation.start_date
    organisation_end_date = organisation.end_date
    organisation_description = organisation.description
    organisation_current = organisation.current
    organisation_link = organisation.link
    organisation_month_year_only = organisation.month_year_only
    organisation_year_only = organisation.year_only
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


def updateOrganisation(request, pk):
    organisation = Organisation.objects.get(id=pk)
    organisation_form = OrganisationForm(request.POST, instance=organisation)
    if organisation_form.is_valid():
        form = organisation_form.save(commit=False)  
        form.save()
        return redirect('home')
    messages.error(request, organisation_form.errors)
    return redirect("/")


def deleteOrganisation(request, pk):
    organisation = Organisation.objects.get(id=pk)
    organisation.delete()
    return redirect('/')


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
            return redirect('/')
        else:
            messages.error(request, certificate_form.errors)
            return redirect('/')

def getCertificate(request, pk):
    ceritficate = Certificate.objects.get(id=pk)
    ceritficate_name = ceritficate.certificate
    ceritficate_additional_information = ceritficate.additional_information
    ceritficate_link = ceritficate.link
    response = JsonResponse(
        {
            "ceritficate_name": ceritficate_name ,
            "ceritficate_additional_information": ceritficate_additional_information,
            "ceritficate_link": ceritficate_link,
        }
        )
    return response


def updateCertificate(request, pk):
    ceritficate = Certificate.objects.get(id=pk)
    ceritficate_form = CertificateForm(request.POST, instance=ceritficate)
    if ceritficate_form.is_valid():
        form = ceritficate_form.save(commit=False)  
        form.save()
        return redirect('home')
    messages.error(request, ceritficate_form.errors)
    return redirect("/")


def deleteCertificate(request, pk):
    ceritficate = Certificate.objects.get(id=pk)
    ceritficate.delete()
    return redirect('/')


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
            return redirect('/')
        else:
            messages.error(request, interest_form.errors)
            return redirect('/')

def getInterest(request, pk):
    interest = Interest.objects.get(id=pk)
    interest_name = interest.interest
    interest_additional_information = interest.additional_information
    interest_link = interest.link
    response = JsonResponse(
        {
            "interest_name": interest_name ,
            "interest_additional_information": interest_additional_information,
            "interest_link": interest_link,
        }
        )
    return response


def updateInterest(request, pk):
    interest = Interest.objects.get(id=pk)
    interest_form = InterestForm(request.POST, instance=interest)
    if interest_form.is_valid():
        form = interest_form.save(commit=False)  
        form.save()
        return redirect('home')
    messages.error(request, interest_form.errors)
    return redirect("/")


def deleteInterest(request, pk):
    interest = Interest.objects.get(id=pk)
    interest.delete()
    return redirect('/')

    
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
            return redirect('/')
        else:
            messages.error(request, publication_form.errors)
            return redirect('/')

def getPublication(request, pk):
    publication = Publication.objects.get(id=pk)
    publication_publisher = publication.publisher
    publication_name = publication.title
    publication_date = publication.date
    publication_description = publication.description
    publication_link = publication.link
    response = JsonResponse(
        {
            "publication_publisher": publication_publisher ,
            "publication_name": publication_name,
            "publication_date": publication_date,
            "publication_description":publication_description,
            "publication_link":publication_link
        }
        )
    return response


def updatePublication(request, pk):
    publication = Publication.objects.get(id=pk)
    publication_form = PublicationForm(request.POST, instance=publication)
    if publication_form.is_valid():
        form = publication_form.save(commit=False)  
        form.save()
        return redirect('home')
    messages.error(request, publication_form.errors)
    return redirect("/")


def deletePublication(request, pk):
    publication = Publication.objects.get(id=pk)
    publication.delete()
    return redirect('/')

def resumeFeedback(request, feedback_id):
    if Personal_Details.objects.filter(feedback_id=feedback_id).exists():
        Personal_Details.objects.get(feedback_id=feedback_id)
        return render(request, 'pages/resume-feedback.html')