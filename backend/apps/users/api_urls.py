from django.urls import path

from backend.apps.users import views

app_name = 'users'
urlpatterns = [
    path('current/', views.CurrentUserView.as_view(), name='current_user'),
    path('token/', views.AuthTokenView.as_view(), name='user_token'),
    # path('registration/', views.RegistrationView.as_view(), name='user_registration'),
    # path('profile/password_change/', views.ChangeUserPassView.as_view(), name='user_password_change'),
]
