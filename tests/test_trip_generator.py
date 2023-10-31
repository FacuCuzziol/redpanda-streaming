import unittest
import sys 
from modules.trip.trip_generator import Trip, generate_trip, TripDistanceLimits
import configparser
import os
# Determine the path to the configuration file
config_file_path = 'config/config.ini'
# Initialize the configparser
config = configparser.ConfigParser()
# Read the configuration file
config.read(config_file_path)


class TestTripGenerator(unittest.TestCase):
    def setUp(self):
        # Set up common data for tests
        self.trip = Trip(trip_duration=3000, trip_distance=5000)
        
    def test_trip_properties(self):
        self.assertTrue(hasattr(self.trip, 'trip_id'))
        self.assertTrue(hasattr(self.trip, 'user_id'))
        self.assertEqual(self.trip.trip_duration, 3000)
        self.assertEqual(self.trip.trip_distance, 5000)
        self.assertEqual(self.trip.trip_price, 33.33) # Adjust based on pricing logic.
        
    def test_generate_trip(self):
        trip_data = generate_trip()
        expected_columns = set(config.get('trip_data', 'expected_columns').split(','))
        self.assertEqual(set(trip_data.keys()),expected_columns)
        
    def test_trip_distance_limits(self):
        self.assertGreaterEqual(self.trip.trip_distance, TripDistanceLimits.MIN_DISTANCE)
        self.assertLessEqual(self.trip.trip_distance, TripDistanceLimits.MAX_DISTANCE)
        
    def test_trip_duration_limits(self):
        self.assertGreaterEqual(self.trip.trip_duration, TripDistanceLimits.MIN_DURATION)
        self.assertLessEqual(self.trip.trip_duration, TripDistanceLimits.MAX_DURATION)

if __name__ == '__main__':
    unittest.main()