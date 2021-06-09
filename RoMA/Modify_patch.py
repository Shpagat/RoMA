import requests

mark_url = 'http://64.227.121.66:8080/mark/1'

mark = {
  "data": {
    "attributes": {
      "identifier": 0,
      "switch": True,
      "patient_id": 1
    },
    "type": "Mark",
    "id": "1"

  }
}
result = requests.patch(mark_url, json=mark)
mark_id = result.json()['data']['id']

