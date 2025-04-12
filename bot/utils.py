import json
from os import getenv

from dotenv import load_dotenv

load_dotenv()
RAPID_KEY = getenv('RAPID_KEY')
def dowloand_instagram():
	import requests

	url = "https://instagram-downloader-download-instagram-stories-videos4.p.rapidapi.com/convert"

	querystring = {"url": "https://www.instagram.com/p/CxLWFNksXOE/?igsh=MWc3b3ZkbHoxa2YyOQ=="}

	headers = {
		"x-rapidapi-key": RAPID_KEY,
		"x-rapidapi-host": "instagram-downloader-download-instagram-stories-videos4.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)
	result = json.loads(response.text)
	return result
ins