import requests
import json


def test_request():
  session_id = get_session_id()
  get_url(session_id)

def get_url(session_id):
  url = f"http://127.0.0.1:9999/session/{session_id}/url"

  payload = json.dumps({
    "url": "file:///home/dmorais/repo/training/search-jobs/src/resources/playground.html"
  })
  headers = {
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.text)

def get_session_id():
    url = "http://127.0.0.1:9999/session"

    payload = json.dumps({
      "desiredCapabilities": {
          "browserName": "firefox",
          "marionette": True,
          "acceptInsecureCerts": True
      }}
    )
    print(payload)
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("sessionId")
