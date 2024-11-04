

from azure.eventhub import EventHubProducerClient, EventData

# Set your Event Hub connection string and name
connection_str = "Endpoint=sb://hailey-eventhub-func-test.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=53DIO/rAVIqqwe2P0dNv1Tk+K9kvYkSRK+AEhBwbTEg=;EntityPath=eventhub-func-test"
eventhub_name = "eventhub-func-test"

# Create an instance of the EventHubProducerClient
producer = EventHubProducerClient.from_connection_string(connection_str)

# Create an event data object with your test event
event_data = EventData(b'Test event data')

# Send the test event to the event hub
with producer:
    producer.send_batch([event_data])