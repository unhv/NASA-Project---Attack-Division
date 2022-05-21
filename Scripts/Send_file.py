# updated the client_send_file_class1.py to send a file forever, you will need to still input the ip address of your machine and the remote machine but thats all.
import logging
import time

import cfdp
from cfdp.transport import UdpTransport
from cfdp.filestore import NativeFileStore


logging.basicConfig(level=logging.DEBUG)

config = cfdp.Config(
    local_entity=cfdp.LocalEntity(
        2, "127.0.0.1:5552"),
    remote_entities=[cfdp.RemoteEntity(
        1, "127.0.0.1:5551")],
    filestore=NativeFileStore("../files/client"),
    transport=UdpTransport())

cfdp_entity = cfdp.CfdpEntity(config)

try:
    While True:
       transaction_id = cfdp_entity.put(
        destination_id=1,
        source_filename="/medium.txt",
        destination_filename="/medium.txt",
        transmission_mode=cfdp.TransmissionMode.UNACKNOWLEDGED)
       time.sleep(15)
except KeyboardInterrupt:
    print('Press Control-C to exit')
    pass
# uncomment the sections below to test suspend and freeze

# cfdp_entity.suspend(transaction_id)
# time.sleep(0.1)
# input("Transaction suspended. Press enter to resume")
# cfdp_entity.resume(transaction_id)

# cfdp_entity.freeze(receiving_entity_id=1)
# time.sleep(0.1)
# input("Transaction frozen. Press enter to unfreeze")
# cfdp_entity.thaw(receiving_entity_id=1)

# cfdp_entity.suspend(transaction_id)
# time.sleep(0.1)
# input("Transaction suspended. Press enter to cancel")
# cfdp_entity.cancel(transaction_id)

while not cfdp_entity.is_complete(transaction_id):
    time.sleep(0.1)

input("Press <Enter> to finish.\n")
cfdp_entity.shutdown()