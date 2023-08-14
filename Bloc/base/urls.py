from django.urls import path,include
from .views import create_event , location , home,rateevent



from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('create_event/',create_event ),
    path('update_location/',location ),
    path('home/',home ),
    path('rateevent/',rateevent),
]
