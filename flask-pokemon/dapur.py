import pandas as pd
import requests

df = pd.read_csv('Pokemon.csv')
dfsimisimi = pd.read_csv('similarity.csv')
print(dfsimisimi.iloc[0])


def getRecomendation(inputFav):
    input = inputFav.lower()
    #get index
    indexFav = df[df['Name'].apply(lambda a : a.lower()) == input].index
    
    if len(indexFav) == 0:
        print("Nama Pokemon tidak ditemukan") 
    else:
        indexFav = indexFav[0]
        print(indexFav)
    
        listMirip = list(enumerate(dfsimisimi.iloc[indexFav])) # enumerate untuk manampilkan indexnya !!!!!!!!!!!!!!!!!!!!!!
        listMirip = sorted(listMirip, key = lambda x: x[1], reverse=True) # select tuple ke 1, ke 0 adalah indexnya
        top6mirip = listMirip[:7]
        name = []
        id_rekom = []
        for i, simi in top6mirip:
            print("index pokemon ke : ", i)
#             print(df.iloc[i])
            print(df.iloc[i]['Name'])
            id_rekom.append(i)
            name.append(df.iloc[i]['Name'].lower())
            print("-"*50)
        return id_rekom, name
daftarID, daftarNama = getRecomendation('Pidgeotto')

url_only = "https://pokeapi.co/api/v2/pokemon/"
def getLinkSpriter(nama):
    response = requests.get(url_only+nama)
    if response:
        jsonresponse = response.json()
        name = jsonresponse['name']
        sprite = jsonresponse['sprites']['front_shiny']
        print(name)
        print(sprite)
        return sprite
    else: return "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRyFMb9_wK_fZtfi-EJjh2d2hVe-j5K-BuuKRAihvg6Q0CvNf15&s"   
getLinkSpriter('pikachu')

def getType(nama):
    x = df[df['Name'] == nama]
    x = x['Type 1'].to_numpy()[0]
    return x

tipe = getType('Pikachu')
print(tipe)

def getTypeViaID(id):
    x = df.iloc[id]
    x = x['Type 1']
    return x

tipe2 = getTypeViaID(2)
print(tipe2)

def getLegend(nama):
    x = df[df['Name'] == nama]
    x = x['Legendary'].to_numpy()[0]
    return x

legend = getLegend('Pikachu')
print(legend)

def getLegendViaID(id):
    x = df.iloc[id]
    x = x['Legendary']
    return x

legend2 = getLegendViaID(793)
print(legend2)
