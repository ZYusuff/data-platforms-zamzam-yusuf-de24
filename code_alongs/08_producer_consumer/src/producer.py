# This is used to handle file paths. It's a way to refer to files on your computer in a clear and flexible way.
from pathlib import Path

# This lets the code work with JSON data, which is a common format for storing and exchanging data (like in a file).
import json

# This is for "pretty-printing" the data, so it's easier to read when printed out.
from pprint import pprint

# This imports a tool called quixstreams. It helps send and receive messages from Kafka, which is like a big message broker that lets different parts of a program or different programs talk to each other.
from quixstreams import Application

# This sets up a path to find the folder that holds the "data" (in this case, a folder above the current folder where the script is running). It will look for a folder called data to store or find the jokes.json file.
data_path = Path(__file__).parents[1] / "data"

print (data_path)

# This opens the jokes.json file in read mode. It assumes that the file exists in the data folder.
with open(data_path / "jokes.json", "r") as file:
    # This loads the data from the jokes.json file into the jokes variable. It's like reading the jokes into the program, so you can work with them.
    jokes = json.load(file)

# This prints the jokes data in a more readable format (just to check what's inside).
pprint(jokes)

# This sets up a connection to Kafka. Kafka is a system used to send messages between different applications or parts of an application. The script connects to Kafka running on localhost (which means your own computer) at port 9092. It’s also creating a "consumer group" named text-splitter, which can be used to read messages from Kafka.
app = Application (broker_address="localhost:9092", consumer_group="text-splitter")

# This creates a "topic" called jokes in Kafka. Topics are like channels where messages are sent.
# The value_serializer="json" tells Kafka that the messages sent to this topic will be in JSON format (so it knows how to pack/unpack them).
jokes_topic = app.topic(name = "jokes", value_serializer = "json")

# MAIN PART OF THE CODE:
# print (jokes_topic)
# This defines the main part of the program that will run when the script is executed.
def main():
    # This starts a "producer". A producer is responsible for sending messages to Kafka. It opens a connection to Kafka and is ready to send data.
    with app.get_producer() as producer:
        print(producer)
        
        # This loops through each joke in the jokes list that was read from the jokes.json file.
        for joke in jokes:
            # For each joke, this line prepares the message that will be sent to Kafka. It takes:
            # joke["joke_id"] as the key (used to group or identify related messages).
            # The whole joke as the value (the actual content of the message).
            # The serialize() method converts the joke into a format Kafka understands (JSON in this case).
            kafka_msg = jokes_topic.serialize(key=joke["joke_id"], value=joke)

            # This just prints out the key and value of the message that will be sent, so you can see it in the output.
            print(kafka_msg.key, kafka_msg.value)

            # This sends the message to the Kafka topic named jokes. The key and value are sent to Kafka, where other consumers (programs) might be reading them.
            producer.produce(
                topic="jokes", key=str(kafka_msg.key), value= kafka_msg.value
                )
# RUNNING THE SCRIPT:
# run this code only when executing this script and not when importing this module
# This ensures that the main() function runs only when this script is run directly (not when imported into another script).
if __name__ == '__main__':
    # pprint(jokes)
    # This actually runs the main() function, which sends the jokes to Kafka.docker
    main()