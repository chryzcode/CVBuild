from django.urls import path

from .views import MyPerson, MyLanguage, MyAward, MyExperience, MyEducation, MySkills, Resume , MyProject, CreateAccount
from .views import EditPerson, EditSkills, EditLanguage, EditAward, EditExperience, EditEducation, EditProject

urlpatterns = [
    path('add_person/', MyPerson.as_view(), name = 'create_user'),
    path('edit_person/<int:pk>', EditPerson, name = 'edit_user'),
    path('add_language/', MyLanguage.as_view(), name = 'create_language'),
    path('edit_language/<int:pk>', EditLanguage, name = 'edit_language'),
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
    path('register/', CreateAccount.as_view(), name='register'),
]