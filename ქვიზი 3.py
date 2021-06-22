import requests
import json
import sqlite3

con = sqlite3.connect('dogs_db.sqlite')
c = con.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS dogs

            (australian VARCHAR(30),
            buhund VARCHAR(30),
            bulldog VARCHAR(30),
            spaniel VARCHAR(30),
            terrier VARCHAR(30)
            )''')


url = 'https://dog.ceo/api/breeds/list/all'
r = requests.get(url)
print(r.status_code)
print(r.headers)
print(r.text)


res = r.json()
with open('dogs.json', 'w') as f:
    json.dump(res, f, indent=4)

all_rows = []

for i in res['message']:
    australian = i['australian']
    buhund = i['buhund']
    bulldog = i['bulldog']
    spaniel = i['spaniel']
    terrier = i['terrier']
    row = (australian, buhund, bulldog, spaniel, terrier)
    all_rows.append(row)


c.executemany('INSERT INTO dogs (australian, buhund, bulldog, spaniel, terrier) VALUES (?, ?, ?, ?, ?)', all_rows)
con.commit()
con.close()