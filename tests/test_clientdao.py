import unittest
from client import Client
from client_dao import ClientDAO

class TestClientDAO(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dao = ClientDAO(db_name="test_db_unit")
        cls.dao.collection.delete_many({})  

    def test_add_client(self):
        client = Client("Omar", 25, "Débutant")
        self.dao.add_client(client)

        clients = self.dao.get_all_clients()
        self.assertEqual(len(clients), 1)
        self.assertEqual(clients[0].nom, "Omar")

    def test_add_multiple_clients(self):
        self.dao.collection.delete_many({})
        self.dao.add_client(Client("Amina", 30, "Avancé"))
        self.dao.add_client(Client("Ali", 28, "Moyen"))

        clients = self.dao.get_all_clients()
        self.assertEqual(len(clients), 2)

    @classmethod
    def tearDownClass(cls):
        cls.dao.collection.delete_many({})
        cls.dao.close()

if __name__ == "__main__":
    unittest.main()

# python -m unittest discover tests
