from django.urls import path

from magicai import views

app_name = "magicai"
urlpatterns = [
    path('', views.UserPromptView.as_view() ,name='user_prompt'),
]
