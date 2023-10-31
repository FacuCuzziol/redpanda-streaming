import argparse
import logging
import sys
import json
import time
from kafka import KafkaProducer
from kafka.errors import KafkaError
import modules.trip.trip_generator as trip_generator


# Define a custom exception for handling Kafka errors
class KafkaProducerError(Exception):
    pass

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Define an enum for message format
class MessageFormat:
    JSON = "json"
    AVRO = "avro"  # If you use Avro, you need to set up a schema registry.


# Command-line argument parser
def parse_args():
    parser = argparse.ArgumentParser(description='Kafka producer')
    parser.add_argument(
        "--bootstrap-servers",
        default="localhost:19092",
        help="Kafka broker address (comma-separated)"
    )
    parser.add_argument('--topic', required=True, help='Kafka topic to produce messages to')
    parser.add_argument('--message-format',default=MessageFormat.JSON, help='Message format (json/avro)')
    parser.add_argument('--message-count', type=int, default=10000, help='Number of messages to send')
    parser.add_argument('--message-interval', type=float, default=0.1, help='Interval between messages (in seconds)')
    return parser.parse_args()

def on_success(metadata):
    logger.info(f"Message produces to topic '{metadata.topic}' at offset {metadata.offset}")
    
def on_error(e):
    logger.error(f"Error sending message: {e}")
    raise KafkaProducerError(f"Failed to produce message: {e}")
    

def produce_messages(producer, topic, message_count, message_interval):
    for i in range(1,message_count+1):
        msg = trip_generator.generate_trip()
        json_msg = json.dumps(msg).encode("utf-8")
        future = producer.send(topic, value=json_msg)
        future.add_callback(on_success)
        future.add_errback(on_error)
        time.sleep(message_interval)


def main():
    args = parse_args()
    try:
        producer = KafkaProducer(bootstrap_servers=args.bootstrap_servers)
        produce_messages(
            producer,
            args.topic,
            args.message_count,
            args.message_interval
            )
    except KafkaError as e:
        logger.error(f"Kafka error: {e}")
    except Exception as e:
        logger.error(f"An unexcepted error occurred: {e}")
    finally:
        producer.close()

if __name__ == "__main__":
    main()