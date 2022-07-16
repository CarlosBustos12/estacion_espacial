from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://admin:admin@cluster0.zeapb.mongodb.net/?retryWrites=true&w=majority'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["bdd_prueba_sofka"]
    except ConnectionError:
        print('Error de conexion con la bdd')
    return db