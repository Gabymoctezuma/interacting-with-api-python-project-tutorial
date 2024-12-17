import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()
canciones=[]
popularidad=[]
duracion=[]

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    canciones.append(track['name'])
    popularidad.append(track['popularity'])
    duracion.append(track['duration_ms']/(1000*60)%60)