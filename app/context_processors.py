from .models import *

def userResumes(request):
    if request.user.is_authenticated:
        resume = Personal_Details.objects.filter(user=request.user)
        return {'userResumes': resume}
    else:
        return {'userResumes': None}
    