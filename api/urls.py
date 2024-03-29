from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
    
urlpatterns =  [
    path('', views.apiOverview, name='apiOverview'),
    path('register/', views.registerUser, name='api_register'),
    path('login/', views.userLogin, name='api_login'),
    path('logout/', views.userLogout, name='api_logout'),
    path('download-pdf/<int:pk>/', views.downloadPDF, name='download_pdf'),
    path('create-feedback/<int:pk>/', views.createFeedback, name='api_create_feedback'),
    path('resume/<int:pk>/feedbacks/', views.resumeFeedbacks, name='api_resume_feedbacks'),
    path('get-resume-profile/<int:pk>/', views.getProfile, name='api_get_profile'),
    path('resume-profile/<int:pk>/', views.createUpdateProfile, name='api_create_update_profile'),
    path('current-user/', views.currentUser, name='api_currentUser'),
    path('update-account/', views.userProfileUpdate, name='api_update-user'),
    path('delete-account/', views.deleteAccount, name='api_delete_account'),
    path('create-resume/', views.createResume, name='api_create_resume'),
    path('get-resume/<int:pk>/', views.getResume, name='api_get_resume'),
    path('delete-resume/<int:pk>/', views.deleteResume, name='api_delete_resume'),
    path('create-skill/<int:personal_detail_pk>/', views.create_skill, name='api_create_skill'),
    path('get-skill/<int:pk>/', views.getSkill, name='api_get_skill'),
    path('update-skill/<int:pk>/<int:personal_detail_pk>/', views.updateSkill, name='api_update_skill'),
    path('delete-skill/<int:pk>/<int:personal_detail_pk>/', views.deleteSkill, name='api_delete_skill'),
    path('create-experience/<int:personal_detail_pk>/', views.createExperience, name='api_create_experience'),
    path('get-experience/<int:pk>/', views.getExperience, name='api_get_experience'),
    path('update-experience/<int:pk>/<int:personal_detail_pk>/', views.updateExperience, name='api_update_experience'),
    path('delete-experience/<int:pk>/<int:personal_detail_pk>/', views.deleteExperience, name='api_delete_experience'),
    path('create-project/<int:personal_detail_pk>/', views.createProject, name='api_create_project'),
    path('get-project/<int:pk>/', views.getProject, name='api_get_project'),
    path('update-project/<int:pk>/<int:personal_detail_pk>/', views.updateProject, name='api_update_project'),
    path('delete-project/<int:pk>/<int:personal_detail_pk>/', views.deleteProject, name='api_delete_project'),
    path('create-education/<int:personal_detail_pk>/', views.createEducation, name='api_create_education'),
    path('get-education/<int:pk>/', views.getEducation, name='api_get_education'),
    path('update-education/<int:pk>/<int:personal_detail_pk>/', views.updateEducation, name='api_update_education'),
    path('delete-education/<int:pk>/<int:personal_detail_pk>/', views.deleteEducation, name='api_delete_education'),
    path('create-language/<int:personal_detail_pk>/', views.createLanguage, name='api_create_language'),
    path('get-language/<int:pk>/', views.getLanguage, name='api_get_language'),
    path('update-language/<int:pk>/<int:personal_detail_pk>/', views.updateLanguage, name='api_update_language'),
    path('delete-language/<int:pk>/<int:personal_detail_pk>/', views.deleteLanguage, name='api_delete_language'),
    path('create-reference/<int:personal_detail_pk>/', views.createReference, name='api_create_reference'),
    path('get-reference/<int:pk>/', views.getReference, name='api_get_reference'),
    path('update-reference/<int:pk>/<int:personal_detail_pk>/', views.updateReference, name='api_update_reference'),
    path('delete-reference/<int:pk>/<int:personal_detail_pk>/', views.deleteReference, name='api_delete_reference'),
    path('create-award/<int:personal_detail_pk>/', views.createAward, name='api_create_award'),
    path('get-award/<int:pk>/', views.getAward, name='api_get_award'),
    path('update-award/<int:pk>/<int:personal_detail_pk>/', views.updateAward, name='api_update_award'),
    path('delete-award/<int:pk>/<int:personal_detail_pk>/', views.deleteAward, name='api_delete_award'),
    path('create-certificate/<int:personal_detail_pk>/', views.createCertificate, name='api_create_certificate'),
    path('get-certificate/<int:pk>/', views.getCertificate, name='api_get_certificate'),
    path('update-certificate/<int:pk>/<int:personal_detail_pk>/', views.updateCertificate, name='api_update_certificate'),
    path('delete-certificate/<int:pk>/<int:personal_detail_pk>/', views.deleteCertificate, name='api_delete_certificate'),
    path('create-interest/<int:personal_detail_pk>/', views.createInterest, name='api_create_interest'),
    path('get-interest/<int:pk>/', views.getInterest, name='api_get_interest'),
    path('update-interest/<int:pk>/<int:personal_detail_pk>/', views.updateInterest, name='api_update_interest'),
    path('delete-interest/<int:pk>/<int:personal_detail_pk>/', views.deleteInterest, name='api_delete_interest'),
    path('create-publication/<int:personal_detail_pk>/', views.createPublication, name='api_create_publication'),
    path('get-publication/<int:pk>/', views.getPublication, name='api_get_publication'),
    path('update-publication/<int:pk>/<int:personal_detail_pk>/', views.updatePublication, name='api_update_publication'),
    path('delete-publication/<int:pk>/<int:personal_detail_pk>/', views.deletePublication, name='api_delete_publication'),

    #JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
