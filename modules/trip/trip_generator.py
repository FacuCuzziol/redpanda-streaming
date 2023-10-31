import uuid
import time
from datetime import datetime, timedelta
import random

# Define an enum for trip distance min and max constants
class TripDistanceLimits:
    MIN_DISTANCE = 1000
    MAX_DISTANCE = 10000
    MIN_DURATION = 60
    MAX_DURATION = 3600


class Trip:
    def __init__(self, trip_duration, trip_distance):
        self.trip_id = str(uuid.uuid4())
        self.user_id = str(uuid.uuid4())
        self._trip_duration = trip_duration
        self._trip_distance = trip_distance 
        
    @property
    def end_timestamp(self):
        return int(time.time())
    
    @property
    def start_timestamp(self):
        return self.end_timestamp - self._trip_duration
    
    @property
    def trip_duration(self):
        return self._trip_duration
    
    @property
    def trip_distance(self):
        return self._trip_distance
    
    @property
    def trip_price(self):
        #Adjust the calculation as needed based on pricing logic 
        return round((self.trip_duration/3600)*10 + (self.trip_distance/1000)*5,2)
    
def generate_trip() :
    trip_duration = random.randint(TripDistanceLimits.MIN_DURATION,TripDistanceLimits.MAX_DURATION)
    trip_distance = random.randint(TripDistanceLimits.MIN_DISTANCE,TripDistanceLimits.MAX_DISTANCE)
    trip = Trip(trip_duration, trip_distance)
    #Dict representation of the trip
    trip_data = {
        "trip_id": trip.trip_id,
        "user_id": trip.user_id,
        "start_timestamp": trip.start_timestamp,
        "end_timestamp": trip.end_timestamp,
        "trip_duration": trip.trip_duration,
        "trip_distance": trip.trip_distance,
        "trip_price": trip.trip_price
    }
    return trip_data