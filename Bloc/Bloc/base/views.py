import base64
from django.shortcuts import render
# Create your views here.
from rest_framework.response import Response
from .models import Event
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .misc import get_nearby_pref_cat_events,get_all_nearby_events
from django.http import HttpResponse
from .models import EventCategory  # Import your models
from django.utils import timezone
from datetime import datetime
import pytz  # For timezone support
from django.core.files.base import ContentFile

@api_view(['PATCH'])
def location(request):
    data = request.data
    lat = data.get('lat')
    long = data.get('long')
    user = request.user
    user.profile.lat = lat
    user.profile.long = long
    user.profile.save()
    return HttpResponse('Location saved successfully' , status = 200) 





@api_view(['GET'])
def home(request):
    user = request.user
    nearby_pref_cat_events=get_nearby_pref_cat_events(user)
    all_nearby_events=get_all_nearby_events(user)
    return Response({'nearby_pref_cat_events': nearby_pref_cat_events,'all_nearby_events':all_nearby_events})

@api_view(['POST'])
def create_event(request):
    data = request.data
    event_name = data.get('event_name')
    lat = data.get('lat')
    long = data.get('long')
    location_name = data.get('location_name')
    event_category = data.get('event_category')
    picture = data.get('picture')
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    parsed_startdatetime = datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%S.%f")
    parsed_enddatetime = datetime.strptime(end_date, "%Y-%m-%dT%H:%M:%S.%f")
    aware_startdatetime = parsed_startdatetime.replace(tzinfo=pytz.utc)
    aware_enddatetime = parsed_enddatetime.replace(tzinfo=pytz.utc)
    link = data.get('link')
    distance = data.get('distance')
    creator = request.user
    event_category = EventCategory.objects.filter(name__in=event_category.lower())
    event_category = event_category.first()

    try: 
        
        event = Event.objects.create(event_name=event_name,lat=lat,long=long,location_name = location_name , event_category=event_category, creator = creator, start_date=aware_startdatetime,end_date=aware_enddatetime,link=link,distance=distance)
        event.save()
        event.save_picture_from_base64(picture)
        return HttpResponse('Event created successfully' , status = 200)
    except Exception as error: 
         print (error)
         return HttpResponse('Something went wrong' , status = 400)
    


