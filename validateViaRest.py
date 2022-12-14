
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
md5ofContent =  configParser.get('AzureFiles', 'md5')
i = 0
af = AzureFiles(connectionString)
for i in range(numberOfShares):
    af.validate_remote_file('pvcclaim' + str(i+1), 'test.html', 'test.html', md5ofContent)
