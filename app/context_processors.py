from uuid import UUID
from .models import *

def userResumes(request):
    if request.user.is_authenticated:
        url = request.path             
        resume = Personal_Details.objects.filter(user=request.user)
        return {'userResumes': resume}
    else:
        return {'userResumes': None}
    