import azure.functions as func
import logging
from typing import List

app = func.FunctionApp()

@app.event_hub_message_trigger(arg_name="azeventhub", event_hub_name="eventhub-func-test",
                               connection="haileyeventhubfunctest_RootManageSharedAccessKey_EVENTHUB") 
def eventhub_trigger(azeventhub: func.EventHubEvent):
    #logging.info('Python EventHub trigger processed an event: %s',
                #azeventhub.get_body().decode('utf-8'))
    
    # 事件详细信息
    logging.info('Event Hub Trigger Function processed an event.')
    logging.info('Event Body: %s', azeventhub.get_body().decode('utf-8'))

    # 提取 Event Hub 元数据
    logging.info('Enqueued Time: %s', azeventhub.enqueued_time)
    logging.info('Partition Key: %s', azeventhub.partition_key)
    logging.info('Sequence Number: %s', azeventhub.sequence_number)
    logging.info('Offset: %s', azeventhub.offset)
    

