from pymongo import MongoClient
from client import Client

class ClientDAO:
    def __init__(self, uri="mongodb://localhost:27017", db_name="testDB"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db["clients"]

    def add_client(self, client):
        if not isinstance(client, Client):
            raise TypeError("client doit être une instance de Client")

        data = {
            "nom": client.nom,
            "age": client.age,
            "niveau": client.niveau
        }
        self.collection.insert_one(data)
        print(f"Client ajouté : {client.nom}")

    def get_all_clients(self):
        clients = []
        for doc in self.collection.find({}, {"_id": 0}):
            clients.append(Client(doc["nom"], doc["age"], doc["niveau"]))
        return clients

    def close(self):
        self.client.close()
