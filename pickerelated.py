import pickle
a = {
    "covid": ["covid","pandemic","virus","mask","death rate","quarantine","lockdown",
              "pandemia","máscara","cuarentena","índice de mortalidad","cierre de emergencia",
              "कोविड","वैश्विक महामारी","वाइरस","मुखौटा","मृत्यु - संख्या","संगरोध","लॉकडाउन"],
     "vaccine":["vaccine","vaccined","syndrome","pfizer","clinic","does",
                "vacuna","vacunada","síndrome","clínica","lo hace",
                "टीका","सिंड्रोम","फाइजर","क्लिनिक","करता है"]
    }
len(a["covid"]+a["vaccine"])

# with open('project1_keywords.pickle', 'wb') as f:
#     pickle.dump(a, f, protocol=pickle.HIGHEST_PROTOCOL)
# with open('project1_keywords.pickle', 'rb') as f:
#         b = pickle.load(f)
#
# print(a == b)
# print(b)


with open('crowdsourced_keywords .pickle', 'rb') as f:
    c = pickle.load(f)

print(c)
print(len(c['covid']))