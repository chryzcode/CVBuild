from django.urls import path
from . import views

urlpatterns =  [
    path('', views.apiOverview, name='apiOverview'),
    path('current-user/', views.currentUser, name='currentUser'),
    path('update-account/', views.userProfileUpdate, name='update-user'),
    path('delete-account', views.deleteAccount, name='delete_account'),
]