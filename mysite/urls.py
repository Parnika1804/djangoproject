from django.urls import path
from django.contrib.auth import views as auth_views
from myapp import views
from django.contrib import admin


urlpatterns = [
    # Authentication URLs
    path('logout/', views.custom_logout, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Django's default login view
    path('signup/', views.signup_view, name='signup'),  # Custom signup view for user registration

    # Protected Views
    path('report/', views.report_view, name='report'),  # Only accessible if logged in
    path('settings/', views.settings_view, name='settings'),  # Only accessible if logged in

    # Home page
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
]
