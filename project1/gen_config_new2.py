
import json

dict={
  "pois": [
    {
      "id": 1,
      "screen_name": "KamalaHarris",
      "lang": "en",
      "count": 500,
      "finished": 0,
      "reply_finished": 0
    },{
      "id": 2,
      "screen_name": "SecAzar",
      "lang": "en",
      "count": 500,
      "finished": 0,
      "reply_finished": 0
    },{
      "id": 2,
      "screen_name": "XavierBecerra",
      "lang": "en",
      "count": 500,
      "finished": 0,
      "reply_finished": 0
    },{
      "id": 2,
      "screen_name": "GovKathyHochul",
      "lang": "en",
      "count": 500,
      "finished": 0,
      "reply_finished": 0
    },{
      "id": 2,
      "screen_name": "JoseNarroR",
      "lang": "es",
      "count": 500,
      "finished": 0,
      "reply_finished": 0
    },{
      "id": 2,
      "screen_name": "Chertorivski",
      "lang": "es",
      "count": 500,
      "finished": 0,
      "reply_finished": 0
    },{
      "id": 2,
      "screen_name": "IHSgov",
      "lang": "hi",
      "count": 500,
      "finished": 0,
      "reply_finished": 0
    },{
      "id": 2,
      "screen_name": "drharshvardhan",
      "lang": "hi",
      "count": 500,
      "finished": 0,
      "reply_finished": 0
    },{
      "id": 2,
      "screen_name": "mansukhmandviya",
      "lang": "hi",
      "count": 500,
      "finished": 0,
      "reply_finished": 0
    },{
      "id": 2,
      "screen_name": "DrPRChoudhary",
      "lang": "hi",
      "count": 500,
      "finished": 0,
      "reply_finished": 0
    }
  ],
 "keywords": [
   {
      "id": 1,
      "name": "XavierBecerre",
      "count": 500,
      "lang": "en",
      "finished": 0
    }
]
}#  vaccine
with open('config_2.json', 'w') as outfile:
    json.dump(dict, outfile)

with open('config_2.json', 'r') as outfile:
    config = json.load(outfile)

print(config)