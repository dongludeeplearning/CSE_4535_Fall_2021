#import tweepy
#import pickle
#import json
#
# auth = tweepy.OAuthHandler("ISkrSjEx0ML1H35UYdVZAXfS3", "z5wAiKfIlMzvabBf99eHVoM2qSEl9x2m46ypwZU6xKy7BYI8FD")
# auth.set_access_token("1432528446312304640-DRGnfgujqMNajxlWTQ7CHCdhiMvOSU", "dHBGfKReNC95oUyiOCZueDyGOJDidSHXX0pSYmb5JwCPa")
# api = tweepy.API(auth)
#
#
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
#
# user = api.get_user('JoeBiden')
# print(user.screen_name)
# print(user.followers_count)
# for friend in user.friends():
#     print(friend.screen_name)


"lang": "en"
"lang": "hi",
"lang": "es",



with open('project1/data/poi_1.pkl', 'rb') as f:
    c = pickle.load(f)
print(c)

# with open('project1/config.json', 'r') as outfile:
#     config= json.load(outfile)
# print(config)



'covid': ['quarentena', 'hospital', 'covidresources', 'rt-pcr', 'वैश्विकमहामारी',
           'oxygen', 'सुरक्षित रहें', 'stayhomestaysafe', 'covid19', 'quarantine', 'मास्क', 'face mask', 'covidsecondwaveinindia', 'flattenthecurve', 'corona virus', 'wuhan', 'cierredeemergencia', 'autoaislamiento', 'sintomas', 'covid positive', 'casos', 'कोविड मृत्यु', 'स्वयं चुना एकांत', 'stay safe', '#deltavariant', 'covid symptoms', 'sarscov2', 'covidiots', 'brote', 'alcohol en gel', 'disease', 'asintomático', 'टीकाकरण', 'encierro', 'covidiot', 'covidappropriatebehaviour', 'fever', 'pandemia de covid-19', 'wearamask', 'flatten the curve', 'oxígeno', 'desinfectante', 'super-spreader', 'ventilador', 'coronawarriors', 'quedate en casa', 'mascaras', 'mascara facial', 'trabajar desde casa', 'संगरोध', 'immunity', 'स्वयं संगरोध', 'डेल्टा संस्करण', 'mask mandate', 'health', 'dogajkidoori', 'travelban', 'cilindro de oxígeno', 'covid', 'staysafe', 'variant', 'yomequedoencasa', 'doctor', 'एंटीबॉडी', 'दूसरी लहर', 'distancia social', 'मुखौटा', 'covid test', 'अस्पताल', 'covid deaths', 'कोविड19', 'muvariant', 'susanadistancia', 'personal protective equipment', 'remdisivir', 'quedateencasa', 'asymptomatic', 'social distancing', 'distanciamiento social', 'cdc', 'transmission', 'epidemic', 'social distance', 'herd immunity', 'transmisión', 'सैनिटाइज़र', 'indiafightscorona', 'surgical mask', 'facemask', 'desinfectar', 'वायरस', 'संक्रमण', 'symptoms', 'सामाजिक दूरी', 'covid cases', 'ppe', 'sars', 'autocuarentena', 'प्रक्षालक', 'breakthechain', 'stayhomesavelives', 'coronavirusupdates', 'sanitize', 'covidinquirynow', 'कोरोना', 'workfromhome', 'outbreak', 'flu', 'sanitizer', 'distanciamientosocial', 'variante', 'कोविड 19', 'कोविड-19', 'covid pneumonia', 'कोविड', 'pandemic', 'icu', 'वाइरस', 'contagios', 'वेंटिलेटर', 'washyourhands', 'n95', 'stayhome', 'lavadodemanos', 'fauci', 'रोग प्रतिरोधक शक्ति', 'maskmandate', 'डेल्टा', 'कोविड महामारी', 'third wave', 'epidemia', 'fiebre', 'मौत', 'travel ban', 'फ़्लू', 'muerte', 'स्वच्छ', 'washhands', 'enfermedad', 'contagio', 'infección', 'faceshield', 'self-quarantine', 'remdesivir', 'oxygen cylinder', 'mypandemicsurvivalplan', 'कोविड के केस', 'delta variant', 'wuhan virus', 'लक्षण', 'corona', 'maskup', 'gocoronago', 'death', 'curfew', 'socialdistance', 'second wave', 'máscara', 'stayathome', 'positive', 'lockdown', 'propagación en la comunidad', 'तीसरी लहर', 'aislamiento', 'rtpcr', 'coronavirus', 'variante delta', 'distanciasocial', 'cubrebocas', 'घर पर रहें', 'socialdistancing', 'covidwarriors', 'प्रकोप', 'covid-19', 'stay home', 'संक्रमित', 'jantacurfew', 'cowin', 'कोरोनावाइरस', 'virus', 'distanciamiento', 'cuarentena', 'indiafightscovid19', 'healthcare', 'natocorona', 'मास्क पहनें', 'delta', 'ऑक्सीजन', 'wearmask', 'कोरोनावायरस', 'ventilator', 'pneumonia', 'maskupindia', 'ppe kit', 'sars-cov-2', 'testing', 'fightagainstcovid19',
           'महामारी', 'नियंत्रण क्षेत्र', 'who', 'mask', 'pandemia', 'deltavariant', 'वैश्विक महामारी', 'रोग', 'síntomas',
           'work from home', 'antibodies', 'masks', 'confinamiento',
           'flattening the curve', 'मुखौटा जनादेश', 'thirdwave', 'mascarilla',
           'usacubrebocas', 'covidemergency', 'inmunidad', 'cierre de emergencia',
           'self-isolation', 'स्वास्थ्य सेवा', 'सोशल डिस्टन्सिंग', 'isolation', 'cases', 'community spread',
           'unite2fightcorona', 'oxygencrisis', 'containment zones', 'homequarantine',
           'स्पर्शोन्मुख', 'लॉकडाउन', 'hospitalización', 'incubation period'],
 'vaccine': ['anticuerpos', 'vaccine mandate', 'eficacia de la vacuna',
             'vacuna covid', 'covidvaccine', 'zycov-d', 'vaccines', '#largestvaccinedrive',
             'vaccination', 'dosis de vacuna', 'moderna',
             'campaña de vacunación', 'vaccineshortage', 'vacunar', 'covid vaccine',
             'efectos secundarios de la vacuna',
             'कोविशील्ड', 'hydroxychloroquine', 'efficacy', 'टीके', 'टीकाकरण', 'वैक्सीनेशन',
             'shots', 'covishield', 'vaccine', 'antibody', 'j&j vaccine', 'booster shot',
             'वैक्सीन पासपोर्ट', 'covidvaccination', 'दूसरी खुराक', 'inyección de refuerzo',
             'astrazeneca', 'टीकाकरण अभियान', 'vacunacovid19', 'johnson & johnson',
             'पहली खुराक', 'sinopharm', 'immunity', 'vaccination drive',
             'inmunización', 'vaccine dose', 'we4vaccine', 'पूर्ण टीकाकरण',
             'vaccine passports', 'एंटीबॉडी', 'vacunado', 'vacunarse',
             'johnson', 'efecto secundario', 'astra zeneca', 'yomevacunoseguro',
             'injection', 'cdc', 'वैक्सीन के साइड इफेक्ट',
             'getvaxxed', 'teeka', 'टीका', 'herd immunity', 'वैक्सीन जनादेश', 'vaccinepassports',
             'estrategiadevacunación', 'ivermectin', 'cansino', 'vacunas', 'vaccinehesitancy',
             'sputnik', 'johnson & johnson’s janssen', 'unvaccinated', 'janssen', 'sputnik v',
             'vacunaton', 'seconddose', 'कोवेक्सिन', 'getvaccinatednow', 'tikakaran', 'कोविशिल्ड',
             'खुराक', 'covaxine', 'mrna', 'first dose', 'वाइरस', 'booster shots', 'dosis',
             'side effect', 'रोग प्रतिरोधक शक्ति', 'jab', 'get vaccinated', 'vaccinessavelives',
             'pinchazo', 'vaccinesideeffects', 'vaccinated', 'कोविड का टीका', 'खराब असर',
             'vacunación', 'कोवैक्सिन', 'tikautsav', 'efectos secundarios', 'remdesivir',
             'covid19vaccine', 'eficacia', 'anticuerpo', 'vaccinequity', 'vaccinesamvaad',
             'फाइजर', 'vaccinesamvad', 'covid-19 vaccine', 'pasaporte de vacuna',
             'largestvaccinationdrive', 'firstdose', 'doses', 'vacuna',
             'la inmunidad de grupo', 'कोवैक्सीन', 'vaccine side effects',
             'कोविन', 'vaccinationdrive', 'clinical trial', 'vaccinemandate',
             'segunda dosis', 'cowin', 'vaccinate', 'clinical trials',
             'fully vaccinated', 'johnson and johnson', 'primera dosis',
             'largestvaccinedrive', 'vaccine hesitancy', 'वैक्सीन', 'प्रभाव',
             'vacunacion', 'second dose', 'sabkovaccinemuftvaccine', 'लसीकरण',
             'vaccineswork', 'वैक्\u200dसीन', 'दुष्प्रभाव', 'pfizer', 'vaccine efficacy',
             'टीका लगवाएं', 'एमआरएनए वैक्सीन', 'antibodies', 'getvaccinated', 'covidshield',
             'booster', 'टीका_जीत_का', 'vaccine jab', 'vaccine passport', 'vaccinepassport',
             'mrna vaccine', 'inmunidad', 'एस्ट्राजेनेका', 'mandato de vacuna', 'astrazenca',
             'vacúnate', 'vacuna para el covid-19', 'vacunada', 'side effects',
             'dose', 'novavax', 'j&j', 'covaxin', 'fullyvaccinated', 'sputnikv',
             'कोविड टीका', 'completamente vacunado', 'novaccinepassports', 'sinovac'
             ]
 }