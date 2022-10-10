from gettext import install
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

# Create your views here.

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


@login_required(login_url="/account/login/")
def account_logout(request):
    logout(request)
    return redirect("/")


@login_required(login_url="/account/login/")
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
        login(request, user)
        return redirect("/")
    else:
        if user:
            user.delete()
            messages.error(request, "Verification Authentication Timeout")
        else:
            messages.messages.error(request, "User/Account does not exist")
        return render(request, "error-pages/404-page.html")

def home(request):
    personal_detail = Personal_Details.objects.filter(user=request.user.id).last()
    profile = Profile.objects.filter(personal_detail=personal_detail).last()
    profile_form = ProfileForm(instance=profile)
    personal_details_form = PersonalDetailsForm(instance=personal_detail)
    skill_form = SkillForm
    link_form = LinkForm(instance=personal_detail)
    skill_levels = Skill_Level.objects.all()
    skills = Skills.objects.filter(personal_detail=personal_detail.id)
    context = {'personal_details':personal_detail, 'profile_form':profile_form, 'personal_details_form':personal_details_form, 'skill_form':skill_form, 'skill_levels':skill_levels, 'link_form':link_form, 'skills':skills}
    return render(request, 'pages/home.html', context)



def person_details(request):
    user = request.user
    if Personal_Details.objects.filter(user=user).exists():
        personal_detail = Personal_Details.objects.filter(user=user).last()
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

def profile(request):
    user = request.user
    if Personal_Details.objects.filter(user=user).exists():
        personal_detail = Personal_Details.objects.filter(user=user).last()
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




def addSkill(request):
    user = request.user
    if Personal_Details.objects.filter(user=user).exists():
        personal_detail = Personal_Details.objects.filter(user=user).last()
        skill_form = SkillForm()
        if request.method == "POST":
            skill_form = SkillForm(request.POST)
        if skill_form.is_valid():
            form = skill_form.save(commit=False)
            form.personal_detail = personal_detail
            form.save()
            return redirect('home')
        print(skill_form.errors)
        messages.error(request, skill_form.errors)
        return redirect('/')
    
def getSkill(request, pk):
    skill = Skills.objects.get(id=pk)
    skill_name = skill.skill
    skill_info = skill.information
    skill_level = skill.level.name
    skill_level_id = skill.level.id
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
    messages.error(request, 'an error')
    return redirect("/")


def deleteSkill(request, pk):
    skill = Skills.objects.get(id=pk)
    skill.delete()
    return redirect('/')

