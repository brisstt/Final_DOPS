#Final_OPS

import os #Sistema operativo
location = "C:/Users/51987/Desktop/proyecto_parcial/python/dataset"

##Validar que la carpeta exista##
if not os.path.exists(location):
    ##En caso mi carpeta exista no exista, voy a crear una nueva
    os.mkdir(location) #mkdir => make a directory
else:
    #Si la carpeta existe, entonces borramos contenido
    for root, dirs, files in os.walk(location, topdown=False):
        for name in files:
            os.remove(os.path.join(root,name))#Elimino todos los archivos
        for name in dirs:
            os.rmdir(os.path.join(root,name)) #elimina carpetas

from kaggle.api.kaggle_api_extended import KaggleApi

#Para autenticacion correcta colocar el api en
api= KaggleApi()
api.authenticate()

print(api.dataset_list(search='sukhmandeepsinghbrar'))#solo para buscar los diferentes datasets que existen
#nombre data set 7/ nombre del archivo , nombre del archivo xd
api.dataset_download_file('sukhmandeepsinghbrar/most-subscribed-youtube-channel', 'Most Subscribed YouTube Channels_exported.csv',path='dataset')