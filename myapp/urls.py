from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Home page (accessible by everyone)
    path('', views.home, name='home'),             

    # Authentication URLs
    path('login/', views.login_view, name='login'),  # Custom login view
    path('signup/', views.signup_view, name='signup'),  # Custom signup view
    path('logout/', views.logout_view, name='logout'),

    # Protected pages (only accessible by authenticated users)
    path('report/', views.report_view, name='report'),  # Protected report page
    path('settings/', views.settings_view, name='settings')  # Protected settings page
]
