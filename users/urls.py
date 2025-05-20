from django.urls import path
from rest_framework_simplejwt.views import  TokenObtainPairView
from .views import RegisterView, ProfileView, ChangePasswordView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('change-password/', ChangePasswordView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  
]
