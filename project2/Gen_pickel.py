import pickle

a={
    "ip": "3.138.246.80",
    "port": "9999",
    "name": "execute_query",
    "env": "prod"
}

with open('project2_index_details.pickle', 'wb') as f:
    pickle.dump(a, f, protocol=pickle.HIGHEST_PROTOCOL)

with open('project2_index_details.pickle', 'rb') as f:
    b = pickle.load(f)

print(b)