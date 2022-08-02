from datetime import datetime, timedelta, timezone
import json, jwt, os, requests

class WeatherKit:
	def __init__(self):
		self.headers = self.get_headers()
		self.endpoint = "https://weatherkit.apple.com/api/v1/weather/en"

	def get_headers(self):
		alg = "ES256"
		teamId = os.environ.get("WeatherKitTeamId")
		appId = os.environ.get('WeatherKitAppId')
		keyId = os.environ.get('WeatherKitKeyId')
		keyPath = os.environ.get('WeatherKitKeyPath')

		payload = {
			'iss': teamId,
			'iat': datetime.now(tz=timezone.utc),
			'exp': datetime.now(tz=timezone.utc) + timedelta(hours=1),
			'sub': appId
		}

		key_file = open(f'{keyPath}AuthKey_{keyId}.p8')
		key = key_file.read()
		key_file.close()

		header = {
			'alg': alg,
			'kid': keyId,
			'id': f'{teamId}.{appId}'
		}

		token = jwt.encode(payload, key, alg, header)

		return {
			'Authorization': f'Bearer {token}'
		}

	def get_weather(self, latitude, longitude, query_parameters):
		url = f"{self.endpoint}/{latitude}/{longitude}?{'&'.join(query_parameters)}"

		response = requests.get(url=url, headers=self.headers)

		return json.loads(response.text)