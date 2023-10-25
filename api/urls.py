from django.urls import path
from . import views

urlpatterns =  [
    path('', views.apiOverview, name='apiOverview'),
    path('register/', views.register_user, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('create-feedback/<int:pk>/', views.createFeedback, name='create_feedback'),
    path('resume/<int:pk>/feedbacks/', views.resumeFeedbacks, name='resume_feedbacks'),
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
]