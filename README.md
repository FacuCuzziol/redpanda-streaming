# Redpanda streaming POC



# Setup
Install the required dependencies with the following command (do this in a virtual environment):
```
pip install -r requirements.txt
```
Start the Redpanda cluster with `docker-compose up`
# Producer
This module sends randomly generated trips data to a Redpanda topic. The process can be executed specifying the following parameters in the console:
- `--topic`: Name of the topic where the data will be sent. Default: `trips`
- `--message-count`: Number of messages to be sent. Default: `1000`
- `--message-interval`: Interval in seconds between messages. Default: `0.1`

This module can be executed with the following command:
```
python3 -m modules.producer.producer --topic orders --message-count 1000 --message-interval 0.05
```

## Trips data
The `trip_generator` module creates random data that can be published by the producer. To generate a new record, use the `generate_trip` function inside that module. The output from that function is a dict with the following information
- `trip_id`: randomly generated UUID as a unique identifier for the trip.
- `user_id`: randomly generated UUID as a unique identifier for the user.
- `end_timestamp`: current_timestamp at the time of processing.
- `start_timestamp`: randomly generated start timestamp based on difference between the end_timestamp and a random trip_duration (from 60s to 3600s as an example).
- `trip_duration`: random number from 60 to 3600 (in seconds) for the trip duration.
- `trip_distance`: random number (in meters) from the whole trip.
- `trip_price`: this value is calculated based on trip_distance and trip_duration.
#### Trip price
This value is calculated based on distance and duration values from the trip. To achieve this, we set a `cost-per-hour` ($10 by default) and
a `cost-per-km` ($5 by default)

$$ \mathit{trip \textunderscore price} = \frac{trip \textunderscore duration}{3600}\cdot cost \textunderscore per \textunderscore hour + \frac{trip \textunderscore distance}{1000}\cdot cost \textunderscore per \textunderscore km$$

