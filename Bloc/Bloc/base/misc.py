import math
from .models import Event
from django.utils import timezone


def haversine_distance(lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers
    earth_radius = 6371.0

    # Convert degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Haversine formula
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Calculate distance
    distance = earth_radius * c
    return distance

# # Example usage
# lat1 = 36.736857345511105
# lon1 = 10.242784461187462
# lat2 = 36.74411793429305
# lon2 = 10.234242617777499
# distance = haversine_distance(lat1, lon1, lat2, lon2)



def get_nearby_pref_cat_events(user):
    user_profile = user.profile
    preferred_categories = user_profile.prefered_categories.all()
    user_lat = user_profile.lat
    user_lon = user_profile.long
    max_distance_km = user_profile.events_distance

    nearby_events = []

    current_datetime = timezone.now()

    for category in preferred_categories:
        for event in category.event_set.filter(end_date__gte=current_datetime.date()):
            event_lat = event.lat
            event_lon = event.long

            distance = haversine_distance(user_lat, user_lon, event_lat, event_lon)
            if distance <= max_distance_km and distance  <= event.distance:
                nearby_events.append(event)

    # Sort events by category name
    nearby_events.sort(key=lambda event: event.event_category.name)

    return nearby_events

def get_all_nearby_events(user):
    user_profile = user.profile
    user_lat = user_profile.lat
    user_lon = user_profile.long
    max_distance_km = user_profile.events_distance

    nearby_events = []

    for event in Event.objects.all():
        event_lat = event.lat
        event_lon = event.long

        distance = haversine_distance(user_lat, user_lon, event_lat, event_lon)
        if distance <= max_distance_km and distance  <= event.distance:
            nearby_events.append(event)

    return nearby_events