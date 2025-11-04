import unittest
from client import Client
from client_dao import ClientDAO

class TestRegressionClientDAO(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dao = ClientDAO(db_name="test_db_regression")
        cls.dao.collection.delete_many({})

        # Données de référence sans _id
        cls.reference_data = [
            {"nom": "Omar", "age": 25, "niveau": "Débutant"},
            {"nom": "Amina", "age": 30, "niveau": "Avancé"},
            {"nom": "Ali", "age": 28, "niveau": "Moyen"},
        ]

        # Insérer et récupérer les _id
        inserted = cls.dao.collection.insert_many(cls.reference_data)
        for doc, _id in zip(cls.reference_data, inserted.inserted_ids):
            doc["_id"] = _id 

    def test_regression_clients(self):
        current_data = list(self.dao.collection.find({}))

        # Trier par _id pour comparaison stable
        current_data.sort(key=lambda x: str(x["_id"]))
        expected_data = sorted(self.reference_data, key=lambda x: str(x["_id"]))

        self.assertEqual(
            current_data,
            expected_data,
            "⚠️ Les données dans MongoDB ont changé (régression détectée)"
        )

    @classmethod
    def tearDownClass(cls):
        cls.dao.collection.delete_many({})
        cls.dao.close()


if __name__ == "__main__":
    unittest.main()
