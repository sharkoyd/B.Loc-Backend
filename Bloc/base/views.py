from django.shortcuts import render
# Create your views here.
from rest_framework.response import Response
from .models import Event
from rest_framework.decorators import api_view, permission_classes

from .misc import get_nearby_pref_cat_events,get_all_nearby_events

@api_view(['POST'])
def location(request):
    data = request.data
    lat = data.get('lat')
    long = data.get('long')
    user = request.user
    user.profile.lat = lat
    user.profile.long = long
    user.profile.save()
    return Response({'success': 'Location saved successfully'})





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
    start_time = data.get('start_time')
    end_time = data.get('end_time')
    event_category = data.get('event_category')
    picture = data.get('picture')
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    creator = request.user
    link = data.get('link')
    distance = data.get('distance')
    event = Event.objects.create(event_name=event_name,lat=lat,long=long,start_time=start_time,end_time=end_time,event_category=event_category,picture=picture,start_date=start_date,end_date=end_date,creator=creator,link=link,distance=distance)
    event.save()
    return Response({'success': 'Event created successfully'})