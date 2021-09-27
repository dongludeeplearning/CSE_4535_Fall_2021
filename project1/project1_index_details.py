import pickle
a={
"ip": "3.138.246.80",
"port": "8983",
"covid_keywords": ["covid", "corona", "coronavirus","quarentena", "hospital", "covidresources", "rt-pcr", "वैश्विकमहामारी"],
"vaccine_keywords": ["anticuerpos", "vaccine mandate", "eficacia de la vacuna",
             "vacuna covid", "covidvaccine", "zycov-d", "vaccines", "#largestvaccinedrive",
             "vaccination", "dosis de vacuna", "moderna",
             "campaña de vacunación", "vaccineshortage", "vacunar", "covid vaccine",
             "efectos secundarios de la vacuna","कोविशील्ड", "hydroxychloroquine", "efficacy", "टीके", "टीकाकरण", "वैक्सीनेशन",
             "shots", "covishield", "vaccine", "antibody", "j&j vaccine", "booster shot",
             "वैक्सीन पासपोर्ट", "covidvaccination", "दूसरी खुराक", "inyección de refuerzo",
             "astrazeneca", "टीकाकरण अभियान", "vacunacovid19", "johnson & johnson",
             "पहली खुराक", "sinopharm", "immunity", "vaccination drive",
             "inmunización", "vaccine dose", "we4vaccine", "पूर्ण टीकाकरण",
             "vaccine passports", "एंटीबॉडी", "vacunado", "vacunarse",
             "johnson", "efecto secundario", "astra zeneca", "yomevacunoseguro",
             "injection", "cdc", "वैक्सीन के साइड इफेक्ट",
             "getvaxxed", "teeka", "टीका", "herd immunity", "वैक्सीन जनादेश", "vaccinepassports",
             "estrategiadevacunación", "ivermectin", "cansino", "vacunas", "vaccinehesitancy",
             "sputnik", "johnson & johnson’s janssen", "unvaccinated", "janssen", "sputnik v",
             "vacunaton", "seconddose", "कोवेक्सिन", "getvaccinatednow", "tikakaran", "कोविशिल्ड",
             "खुराक", "covaxine", "mrna", "first dose", "वाइरस", "booster shots", "dosis",
             "side effect", "रोग प्रतिरोधक शक्ति", "jab", "get vaccinated", "vaccinessavelives",
             "pinchazo", "vaccinesideeffects", "vaccinated", "कोविड का टीका", "खराब असर",
             "vacunación", "vकोवैक्सिन", "tikautsav", "efectos secundariosv", "remdesivir",
             "vcovid19vaccine", "eficacia", "anticuerpo", "vaccinequity", "vaccinesamvaad",
             "फाइजर", "vaccinesamvad", "covid-19 vaccine", "pasaporte de vacuna",
             "largestvaccinationdrive", "firstdose", "doses', 'vacuna",
             "la inmunidad de grupo", "कोवैक्सीनv", "vaccine side effects",
             "कोविन", "vaccinationdrive", "clinical trial", "vaccinemandate",
             "segunda dosis", "cowin", "vaccinate", "clinical trials",
             "fully vaccinated", "johnson and johnson", "primera dosis",
             "largestvaccinedrive", "vaccine hesitancy", "वैक्सीन", "प्रभाव",
             "vacunacion", "second dose", "sabkovaccinemuftvaccine", "लसीकरण",
             "vaccineswork", "वैक्\u200dसीन", "दुष्प्रभाव", "pfizer", "vaccine efficacy",
             "टीका लगवाएं", "एमआरएनए वैक्सीन", "antibodies", "getvaccinated", "covidshield",
             "booster", "टीका_जीत_का", "vaccine jab", "vaccine passport", "vaccinepassport",
             "mrna vaccine", "inmunidad", "एस्ट्राजेनेका", "mandato de vacuna", "astrazenca",
             "vacúnate", "vacuna para el covid-19", "vacunada", "side effects",
             "dose", "novavax", "j&j", "covaxin", "fullyvaccinated", "sputnikv",
             "कोविड टीका", "completamente vacunado", "novaccinepassports", "sinovac"
             ],
"core": "IRF21P1"
}

with open('project1_index_details.pickle', 'wb') as f:
    pickle.dump(a, f, protocol=pickle.HIGHEST_PROTOCOL)

with open('project1_index_details.pickle', 'rb') as f:
    b = pickle.load(f)

print( b)





