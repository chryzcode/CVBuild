from django.urls import path

from .views import MyPerson, MyAward, MyExperience, MyEducation, MySkills, Resume , MyProject, CreateAccount
from .views import EditPerson, EditSkills, EditAward, EditExperience, EditEducation, EditProject
from .views import CreateAccount, UpdateAccount, UserDelete, PasswordsChangeView
from .views import DeletePerson, DeleteAwards, DeleteEducation, DeleteExperience, DeleteProject, DeleteSkills, DeleteProject
from .views import Volunteers, EditVolunteers, DeleteVolunteers, ViewPDF, DownloadPDF, ResumeDone, Portfolio

urlpatterns = [
    path('add_person/', MyPerson.as_view(), name = 'create_user'),
    path('add_volunteer/', Volunteers.as_view(), name = 'create_volunteer'),
    path('edit_volunteer/<int:pk>', EditVolunteers, name = 'edit_volunteer'),
    path('delete_volunteer/<str:pk>/', DeleteVolunteers, name='delete_volunteer'),
    path('edit_person/<int:pk>', EditPerson, name = 'edit_user'),
    path('add_award/', MyAward.as_view(), name = 'create_award'),
    path('edit_award/<int:pk>', EditAward, name = 'edit_award'),
    path('add_experience/', MyExperience.as_view(), name = 'create_experience'),
    path('edit_experience/<int:pk>', EditExperience, name = 'edit_experience'),
    path('add_education/', MyEducation.as_view(), name = 'create_education'),
    path('edit_education/<int:pk>', EditEducation, name = 'edit_education'),
    path('add_skills/', MySkills.as_view(), name = 'create_skills'),
    path('edit_skills/<int:pk>', EditSkills, name = 'edit_skills'),
    path('add_project/', MyProject.as_view(), name = 'create_project'),
    path('edit_project/<int:pk>', EditProject, name = 'edit_project'),
    path('', Resume, name='resume'),
    path('resume_done', ResumeDone, name='resume_done'),
    path('register/', CreateAccount.as_view(), name='register'),
    path('edit_profile/', UpdateAccount.as_view(), name='update_account'),
    path('user_delete/', UserDelete, name = 'user_delete'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html'), name='change_password'),
    path('delete_person/<str:pk>/', DeletePerson, name='delete_user'),
    path('delete_education/<str:pk>/', DeleteEducation, name='delete_education'),
    path('delete_skills/<str:pk>/', DeleteSkills, name='delete_skills'),
    path('delete_experience/<str:pk>/', DeleteExperience, name='delete_experience'),
    path('delete_awards/<str:pk>/', DeleteAwards, name='delete_awards'),
    path('delete_project/<str:pk>/', DeleteProject, name='delete_project'),
    path('resume_preview', ViewPDF.as_view(), name='resume_preview'), 
    path('download_resume', DownloadPDF.as_view(), name='download_resume'),
    path('portfolio/<username>', Portfolio, name='portfolio'),
]