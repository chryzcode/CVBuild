from uuid import UUID
from .models import *

def userResumes(request):
    if request.user.is_authenticated:
        url = request.path
        if type(url.split("/")[1]) == UUID:
            if (url.split("/")[1] and Personal_Details.objects.filter(feedback_id=url.split("/")[1]).exists()):
                feedback_id = url.split("/")[1]

                resume = Personal_Details.objects.exclude(feedback_id=feedback_id).filter(user=request.user)
            else:
                resume = Personal_Details.objects.filter(user=request.user)
            return {'userResumes': resume}
        else:
            return {'userResumes': None}
    else:
        return {'userResumes': None}
    