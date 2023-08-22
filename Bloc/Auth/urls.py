from django.urls import path,include
from .views import register,profile_exist , finish_signup



from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('register/',register ),
    path('profile_exist/',profile_exist ),
    path('finish_signup/',finish_signup ),
]
