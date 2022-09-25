import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

with open('./itune.json','w') as j:
    j.write(json.dumps(response.json(), indent=4))
    j.close()
