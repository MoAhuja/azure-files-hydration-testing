
from azure_files_manager import AzureFiles 
import configparser

# Parse config
configParser = configparser.RawConfigParser()   
configFilePath = "settings.cfg"
configParser.read(configFilePath)

#read config
connectionString = configParser.get('AzureFiles', 'connectionString')
prefix = configParser.get('AzureFiles', 'shareNamePrefix')
numberOfShares = int(configParser.get('AzureFiles', 'numberOfShares'))

i = 0
af = AzureFiles(connectionString)
for i in range(numberOfShares):
    af.upload_local_file('test.html', 'pvcclaim' + str(i+1), 'test.html')