import requests
import json

year = 2020
league_id = 1037955
url = "https://fantasy.espn.com/apis/v3/games/ffl/seasons/"+str(year)+"/segments/0/leagues/"+str(league_id)

response = requests.get(url)
pretty_json = json.loads(response.text)
print(json.dumps(pretty_json, indent=2))

print(response.json())
