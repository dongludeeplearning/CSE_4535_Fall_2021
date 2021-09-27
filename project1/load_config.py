import json

with open('config.json', 'r') as outfile:
    config = json.load(outfile)
    pois = config["pois"]
    keywords = config["keywords"]
    #pois[0]["reply_finished"] = 0
for i in range(len(pois)):
    print(pois[i])
#print(len( keywords))
# for j in range(len( keywords)):
#      print( keywords[j])