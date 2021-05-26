import os
import re
import json
from pyngrok import conf, ngrok

config = json.load(open('test_config.json', 'r'))

# Gets the authtoken from then the json file
authtoken = config['ngrok_authtoken']

# Logs into ngrok with the authtoken
conf.get_default().auth_token = authtoken

# Sets the default ngrok region 
conf.get_default().region = 'us'  # Change this to whichever region thats best for you

# Connect to ngrok
url = ngrok.connect(25565, 'tcp')
print('\nServer Address: ' + ((str(url).split('"')[1::2])[0]).replace('tcp://', ''))

# Starting minecraft server
print("Starting Server...")

ram_size = config['alloted_ram']
os.system(f"java -Xmx{ram_size} -Xms{ram_size} -jar server.jar nogui")