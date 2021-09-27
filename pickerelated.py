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



{'covid': ['quarentena',
           'hospital',
           'covidresources',
           'rt-pcr',
           'वैश्विकमहामारी',
           'oxygen',
           'सुरक्षित रहें',
           'stayhomestaysafe',
           'covid19',
           'quarantine',
           'मास्क',
           'face mask',
           'covidsecondwaveinindia',
           'flattenthecurve',
           'corona virus',
           'wuhan',
           'cierredeemergencia',
           'autoaislamiento',
           'sintomas',
           'covid positive',
           'casos',
           'कोविड मृत्यु',
           'स्वयं चुना एकांत',
           'stay safe',
           '#deltavariant',
           'covid symptoms',
           'sarscov2',
           'covidiots',
           'brote',
           'alcohol en gel',
           'disease',
           'asintomático',
           'टीकाकरण',
           'encierro',
           'covidiot',
           'covidappropriatebehaviour',
           'fever',
           'pandemia de covid-19',
           'wearamask',
           'flatten the curve',
           'oxígeno',
           'desinfectante',
           'super-spreader',
           'ventilador',
           'coronawarriors',
           'quedate en casa',
           'mascaras',
           'mascara facial',
           'trabajar desde casa',
           'संगरोध',
           'immunity',
           'स्वयं संगरोध',
           'डेल्टा संस्करण',
           'mask mandate',
           'health',
           'dogajkidoori',
           'travelban',
           'cilindro de oxígeno',
           'covid',
           'staysafe',
           'variant',
           'yomequedoencasa',
           'doctor',
           'एंटीबॉडी',
           'दूसरी लहर',
           'distancia social',
           'मुखौटा',
           'covid test',
           'अस्पताल',
           'covid deaths',
           'कोविड19',
           'muvariant',
           'susanadistancia',
           'personal protective equipment',
           'remdisivir',
           'quedateencasa',
           'asymptomatic',
           'social distancing',
           'distanciamiento social',
           'cdc',
           'transmission',
           'epidemic',
           'social distance',
           'herd immunity',
           'transmisión',
           'सैनिटाइज़र',
           'indiafightscorona',
           'surgical mask',
           'facemask',
           'desinfectar',
           'वायरस',
           'संक्रमण',
           'symptoms',
           'सामाजिक दूरी',
           'covid cases',
           'ppe',
           'sars',
           'autocuarentena',
           'प्रक्षालक',
           'breakthechain',
           'stayhomesavelives',
           'coronavirusupdates',
           'sanitize',
           'covidinquirynow',
           'कोरोना',
           'workfromhome',
           'outbreak',
           'flu',
           'sanitizer',
           'distanciamientosocial',
           'variante',
           'कोविड 19',
           'कोविड-19',
           'covid pneumonia',
           'कोविड',
           'pandemic',
           'icu',
           'वाइरस',
           'contagios',
           'वेंटिलेटर',
           'washyourhands',
           'n95',
           'stayhome',
           'lavadodemanos',
           'fauci',
           'रोग प्रतिरोधक शक्ति',
           'maskmandate',
           'डेल्टा',
           'कोविड महामारी',
           'third wave',
           'epidemia',
           'fiebre',
           'मौत',
           'travel ban',
           'फ़्लू',
           'muerte',
           'स्वच्छ',
           'washhands',
           'enfermedad',
           'contagio',
           'infección',
           'faceshield',
           'self-quarantine',
           'remdesivir',
           'oxygen cylinder',
           'mypandemicsurvivalplan',
           'कोविड के केस',
           'delta variant',
           'wuhan virus',
           'लक्षण', 'corona',
           'maskup', 'gocoronago',
           'death', 'curfew',
           'socialdistance',
           'second wave',
           'máscara', 'stayathome',
           'positive', 'lockdown', 'propagación en la comunidad',
           'तीसरी लहर', 'aislamiento', 'rtpcr', 'coronavirus',
           'variante delta', 'distanciasocial', 'cubrebocas', 'घर पर रहें',
           'socialdistancing', 'covidwarriors', 'प्रकोप', 'covid-19', 'stay home',
           'संक्रमित', 'jantacurfew', 'cowin', 'कोरोनावाइरस', 'virus', 'distanciamiento',
           'cuarentena', 'indiafightscovid19', 'healthcare', 'natocorona', 'मास्क पहनें', 'delta', 'ऑक्सीजन',
           'wearmask', 'कोरोनावायरस', 'ventilator', 'pneumonia', 'maskupindia', 'ppe kit', 'sars-cov-2', 'testing',
           'fightagainstcovid19', 'महामारी', 'नियंत्रण क्षेत्र', 'who', 'mask', 'pandemia', 'deltavariant', 'वैश्विक महामारी',
           'रोग', 'síntomas', 'work from home', 'antibodies', 'masks', 'confinamiento', 'flattening the curve',
           'मुखौटा जनादेश', 'thirdwave', 'mascarilla', 'usacubrebocas', 'covidemergency', 'inmunidad',
           'cierre de emergencia', 'self-isolation', 'स्वास्थ्य सेवा', 'सोशल डिस्टन्सिंग', 'isolation', 'cases',
           'community spread', 'unite2fightcorona', 'oxygencrisis', 'containment zones', 'homequarantine',
           'स्पर्शोन्मुख', 'लॉकडाउन', 'hospitalización', 'incubation period'],


 'vaccine': [









 'antibodies', 'getvaccinated',
     'covidshield', 'booster', 'vaccine jab', 'vaccine passport', 'vaccinepassport',
     'side effects', 'dose','j&j','fullyvaccinated','novaccinepassports', 'sinovac',



     
           
           
     


'कोविशील्ड','टीके','टीकाकरण', 'वैक्सीनेशन', 'वैक्सीन पासपोर्ट','पहली खुराक','दूसरी खुराक', 'टीकाकरण अभियान','पूर्ण टीकाकरण',
            'एंटीबॉडी','वैक्सीन के साइड इफेक्ट', 'टीका','वैक्सीन जनादेश','कोवेक्सिन','कोविशिल्ड','खुराक', 'रोग प्रतिरोधक शक्ति','वाइरस',
            'कोविड का टीका','खराब असर','कोवैक्सिन','फाइजर', 'कोवैक्सीन','कोविन', 'वैक्सीन', 'प्रभाव','लसीकरण', 'वैक्\u200dसीन', 'दुष्प्रभाव',
     'टीका लगवाएं', 'एमआरएनए वैक्सीन', 'टीका_जीत_का', 'एस्ट्राजेनेका','कोविड टीका',



           , , ,












             ]}


"keywords": [
   {
      "id": 1,
      "name": "anticuerpos",
      "count": 500,
      "lang": "es",
      "country": "MEXICO",
      "finished": 0
    },{          #  vaccine
      "id": 2,
      "name": "vaccine mandate",
      "count": 500,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 3,
      "name": "eficacia de la vacuna",
      "count": 2000,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 4,
      "name": "vacuna covid",
      "count": 2000,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 5,
      "name": 'covidvaccine',
      "count": 2000,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 1,
      "name": "anticuerpos",
      "count": 500,
      "lang": "es",
      "country": "MEXICO",
      "finished": 0
    },{          #  vaccine
      "id": 2,
      "name": "vaccine mandate",
      "count": 500,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 3,
      "name": "eficacia de la vacuna",
      "count": 2000,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 4,
      "name": "vacuna covid",
      "count": 2000,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 5,
      "name": 'covidvaccine',
      "count": 2000,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 1,
      "name": "anticuerpos",
      "count": 500,
      "lang": "es",
      "country": "MEXICO",
      "finished": 0
    },{          #  vaccine
      "id": 2,
      "name": "vaccine mandate",
      "count": 500,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 3,
      "name": "eficacia de la vacuna",
      "count": 2000,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 4,
      "name": "vacuna covid",
      "count": 2000,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 5,
      "name": 'covidvaccine',
      "count": 2000,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 1,
      "name": "anticuerpos",
      "count": 500,
      "lang": "es",
      "country": "MEXICO",
      "finished": 0
    },{          #  vaccine
      "id": 2,
      "name": "vaccine mandate",
      "count": 500,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 3,
      "name": "eficacia de la vacuna",
      "count": 2000,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 4,
      "name": "vacuna covid",
      "count": 2000,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 5,
      "name": 'covidvaccine',
      "count": 2000,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 1,
      "name": "anticuerpos",
      "count": 500,
      "lang": "es",
      "country": "MEXICO",
      "finished": 0
    },{          #  vaccine
      "id": 2,
      "name": "vaccine mandate",
      "count": 500,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 3,
      "name": "eficacia de la vacuna",
      "count": 2000,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 4,
      "name": "vacuna covid",
      "count": 2000,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 5,
      "name": 'covidvaccine',
      "count": 2000,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 1,
      "name": "anticuerpos",
      "count": 500,
      "lang": "es",
      "country": "MEXICO",
      "finished": 0
    },{          #  vaccine
      "id": 2,
      "name": "vaccine mandate",
      "count": 500,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 3,
      "name": "eficacia de la vacuna",
      "count": 2000,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 4,
      "name": "vacuna covid",
      "count": 2000,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 5,
      "name": 'covidvaccine',
      "count": 2000,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 1,
      "name": "anticuerpos",
      "count": 500,
      "lang": "es",
      "country": "MEXICO",
      "finished": 0
    },{          #  vaccine
      "id": 2,
      "name": "vaccine mandate",
      "count": 500,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 3,
      "name": "eficacia de la vacuna",
      "count": 2000,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 4,
      "name": "vacuna covid",
      "count": 2000,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 5,
      "name": 'covidvaccine',
      "count": 2000,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 1,
      "name": "anticuerpos",
      "count": 500,
      "lang": "es",
      "country": "MEXICO",
      "finished": 0
    },{          #  vaccine
      "id": 2,
      "name": "vaccine mandate",
      "count": 500,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 3,
      "name": "eficacia de la vacuna",
      "count": 2000,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 4,
      "name": "vacuna covid",
      "count": 2000,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 5,
      "name": 'covidvaccine',
      "count": 2000,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 1,
      "name": "anticuerpos",
      "count": 500,
      "lang": "es",
      "country": "MEXICO",
      "finished": 0
    },{          #  vaccine
      "id": 2,
      "name": "vaccine mandate",
      "count": 500,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 3,
      "name": "eficacia de la vacuna",
      "count": 2000,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 4,
      "name": "vacuna covid",
      "count": 2000,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 5,
      "name": 'covidvaccine',
      "count": 2000,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 1,
      "name": "anticuerpos",
      "count": 500,
      "lang": "es",
      "country": "MEXICO",
      "finished": 0
    },{          #  vaccine
      "id": 2,
      "name": "vaccine mandate",
      "count": 500,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 3,
      "name": "eficacia de la vacuna",
      "count": 2000,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 4,
      "name": "vacuna covid",
      "count": 2000,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 5,
      "name": 'covidvaccine',
      "count": 2000,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 1,
      "name": "anticuerpos",
      "count": 500,
      "lang": "es",
      "country": "MEXICO",
      "finished": 0
    },{          #  vaccine
      "id": 2,
      "name": "vaccine mandate",
      "count": 500,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 3,
      "name": "eficacia de la vacuna",
      "count": 2000,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 4,
      "name": "vacuna covid",
      "count": 2000,
      "lang": "en",
      "country": "USA",
      "finished": 0
    },{
      "id": 5,
      "name": 'covidvaccine',
      "count": 2000,
      "lang": "en",
      "country": "USA",
      "finished": 0
    }
]

