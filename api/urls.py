from django.urls import path
from . import views

urlpatterns =  [
    path('', views.apiOverview, name='apiOverview'),
    path('current-user/', views.currentUser, name='currentUser'),
    path('update-account/', views.userProfileUpdate, name='update-user'),
    path('delete-account/', views.deleteAccount, name='delete_account'),
    # path('create-resume/', views.createResume, name='create_resume'),
    path('get-resume/<int:pk>/', views.getResume, name='get_resume'),
    path('delete-resume/<int:pk>/', views.deleteResume, name='delete_resume'),
    path('get-skill/<int:pk>/', views.getSkill, name='get_skill'),
    path('update-skill/<int:pk>/<int:personal_detail_pk>/', views.updateSkill, name='update_skill'),
    path('delete-skill/<int:pk>/<int:personal_detail_pk>/', views.deleteSkill, name='delete_skill'),
]