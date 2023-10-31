# mage-streaming



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