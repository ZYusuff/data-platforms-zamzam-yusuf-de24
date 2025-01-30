from quixstreams import Application

app = Application(
    broker_address="localhost_9092", 
    consumer_group="text-splitter", 
    auto_offset_reset= "earliest"
    )


jokes_topic = app.topic(name="jokes", value_deserializer="json")

sdf = app.dataframe(topic=jokes_topic)

# def print_message(message):
#     print(message)
# sdf.update(print_message)
# De tre raderna ovan motsvara raden nedan!

sdf.update(lambda message: print(message))


if __name__ ==  '__main__':
    app.run()