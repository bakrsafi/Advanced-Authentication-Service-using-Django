from django.urls import path
from .views import UserRegistrationView , CustomLoginView, UserProfileView , LogoutView, ChangePasswordView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('signup/', UserRegistrationView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),

]
