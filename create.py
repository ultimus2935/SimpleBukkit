import os
import json
import requests

config = json.load(open('config.json', 'r'))

# URL for jar file
url = 'https://papermc.io/api/v1/paper/'+ config['server_version'] +'/latest/download'

# Downloading jar file
r = requests.get(url)
if r.status_code == 200:
    with open('server.jar', 'wb') as f: 
        f.write(r.content)
        print('Finished!')

else: print('Error: '+ str(r.status_code) + '\nYou entered a unsupported version. Try correcting the error in the config.json file')

# Running the jar file to create the eula.txt
ram_size = config['alloted_ram']

os.system(f"java -Xmx{ram_size} -Xms{ram_size} -jar server.jar nogui")

# Accepting EULA
with open('eula.txt', 'r') as file: filedata = file.read()
filedata = filedata.replace('eula=false', 'eula=true')
with open('eula.txt', 'w') as file: file.write(filedata)

print("Dont mind the error, your server is ready. Please run the start.bat to turn it on.\nIt may take longer than usual the first time you turn it on.")