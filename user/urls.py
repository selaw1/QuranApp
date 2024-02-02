from django.contrib.auth import views as auth_views
from django.urls import path

from user import views

app_name = "user"
urlpatterns = [
    # Register / Login-Logout
    path('signup/', views.UserCreateView.as_view() ,name='registration'),
    path('activate/<slug:uidb64>/<slug:token>', views.account_activation ,name='activate'),
    path('login/', auth_views.LoginView.as_view(template_name='user/registration/login.html', redirect_authenticated_user=True) ,name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/user/login/'), name='logout'),
]
