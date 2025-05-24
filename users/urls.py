from django.urls import path
from rest_framework_simplejwt.views import  TokenObtainPairView
from .views import LogoutView, MyTokenObtainPairView, RegisterView, ProfileView, ChangePasswordView, UserProfileDetailView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('change-password/', ChangePasswordView.as_view()),
    path('profile/<int:pk>/', UserProfileDetailView.as_view(), name='profile-detail'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
