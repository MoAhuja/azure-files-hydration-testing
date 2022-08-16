
from azure.core.exceptions import (
    ResourceExistsError,
    ResourceNotFoundError
)

from azure.storage.fileshare import (
    ShareServiceClient,
    ShareClient,
    ShareDirectoryClient,
    ShareFileClient
)
import hashlib

class AzureFiles():

    def __init__(self, connectionString):
        # Initial the azure file client
        self.serviceClient=ShareServiceClient.from_connection_string(connectionString)

    
    def upload_local_file(self,  local_file_path, share_name, destination_file_path):
        try:
            source_file = open(local_file_path, "rb")
            data = source_file.read()

            # Create a ShareFileClient from a connection string
            # file_client = ShareFileClient.from_connection_string(
            #     connection_string, share_name, dest_file_path)
        
            fileClient = self.serviceClient.get_share_client(share_name).get_file_client(destination_file_path)


            print("Uploading to:", share_name + "/" + destination_file_path)
            fileClient.upload_file(data)

        except ResourceExistsError as ex:
            print("ResourceExistsError:", ex.message)

        except ResourceNotFoundError as ex:
            print("ResourceNotFoundError:", ex.message)

    def validate_remote_file(self, share_name, remote_file_path, local_file_name, checksum):
        try:
           
            # Create a ShareFileClient from a connection string
            fileClient = self.serviceClient.get_share_client(share_name).get_file_client(remote_file_path)

       
           
            # Download the file from Azure into a stream
            stream = fileClient.download_file()
            # Write the stream to the local file
            md5Result = hashlib.md5(stream.readall()).hexdigest()

            if md5Result == checksum:
                print("Validating file '{0}/{1} - Match".format(share_name, remote_file_path))
            else:
                print("No match")

        except ResourceNotFoundError as ex:
            print("ResourceNotFoundError:", ex.message)
