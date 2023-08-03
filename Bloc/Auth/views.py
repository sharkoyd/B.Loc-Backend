from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import Profile


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    data = request.data
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirm_password')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    distance = data.get('distance')
    prefered_categories = data.get('prefered_categories')
    if password != confirm_password:
        return Response({'error': 'Passwords do not match'})
    else:
        try:
            user = User.objects.create_user(
                username=email, email=email, password=password,
                first_name=first_name, last_name=last_name
            )
            user.save()
            profile = Profile.objects.create(user=user, events_distance=distance, prefered_categories=prefered_categories)
            profile.save()
            return Response({'success': 'User created successfully'})
        except IntegrityError:
            return Response({'error': 'User with that email already exists'})
