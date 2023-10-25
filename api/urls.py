from django.urls import path
from . import views

urlpatterns =  [
    path('', views.apiOverview, name='apiOverview'),
    path('register/', views.register_user, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('create-feedback/<int:pk>/', views.createFeedback, name='create_feedback'),
    path('resume/<int:pk>/feedbacks/', views.resumeFeedbacks, name='resume_feedbacks'),
    path('get-resume-profile/<int:pk>/', views.getProfile, name='get_profile'),
    path('resume-profile/<int:pk>/', views.createUpdateProfile, name='create_update_profile'),
    path('current-user/', views.currentUser, name='currentUser'),
    path('update-account/', views.userProfileUpdate, name='update-user'),
    path('delete-account/', views.deleteAccount, name='delete_account'),
    path('create-resume/', views.createResume, name='create_resume'),
    path('get-resume/<int:pk>/', views.getResume, name='get_resume'),
    path('delete-resume/<int:pk>/', views.deleteResume, name='delete_resume'),
    path('create-skill/<int:personal_detail_pk>/', views.create_skill, name='create_skill'),
    path('get-skill/<int:pk>/', views.getSkill, name='get_skill'),
    path('update-skill/<int:pk>/<int:personal_detail_pk>/', views.updateSkill, name='update_skill'),
    path('delete-skill/<int:pk>/<int:personal_detail_pk>/', views.deleteSkill, name='delete_skill'),
    path('create-experience/<int:personal_detail_pk>/', views.createExperience, name='create_experience'),
    path('get-experience/<int:pk>/', views.getExperience, name='get_experience'),
    path('update-experience/<int:pk>/<int:personal_detail_pk>/', views.updateExperience, name='update_experience'),
    path('delete-experience/<int:pk>/<int:personal_detail_pk>/', views.deleteExperience, name='delete_experience'),
    path('create-project/<int:personal_detail_pk>/', views.createProject, name='create_project'),
    path('get-project/<int:pk>/', views.getProject, name='get_project'),
    path('update-project/<int:pk>/<int:personal_detail_pk>/', views.updateProject, name='update_project'),
    path('delete-project/<int:pk>/<int:personal_detail_pk>/', views.deleteProject, name='delete_project'),
    path('create-education/<int:personal_detail_pk>/', views.createEducation, name='create_education'),
    path('get-education/<int:pk>/', views.getEducation, name='get_education'),
    path('update-education/<int:pk>/<int:personal_detail_pk>/', views.updateEducation, name='update_education'),
    path('delete-education/<int:pk>/<int:personal_detail_pk>/', views.deleteEducation, name='delete_education'),
    path('create-language/<int:personal_detail_pk>/', views.createLanguage, name='create_language'),
    path('get-language/<int:pk>/', views.getLanguage, name='get_language'),
    path('update-language/<int:pk>/<int:personal_detail_pk>/', views.updateLanguage, name='update_language'),
    path('delete-language/<int:pk>/<int:personal_detail_pk>/', views.deleteLanguage, name='delete_language'),
    path('create-reference/<int:personal_detail_pk>/', views.createReference, name='create_reference'),
    path('get-reference/<int:pk>/', views.getReference, name='get_reference'),
    path('update-reference/<int:pk>/<int:personal_detail_pk>/', views.updateReference, name='update_reference'),
    path('delete-reference/<int:pk>/<int:personal_detail_pk>/', views.deleteReference, name='delete_reference'),
]
