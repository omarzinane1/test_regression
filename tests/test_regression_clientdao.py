import unittest
from client import Client
from client_dao import ClientDAO

class TestRegressionClientDAO(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Initialisation de la base MongoDB de test"""
        cls.dao = ClientDAO(db_name="test_db_regression")
        cls.dao.collection.delete_many({})  # Nettoyer avant les tests

        cls.reference_data = [
            {"nom": "Omar", "age": 25, "niveau": "Débutant"},
            {"nom": "Amina", "age": 30, "niveau": "Avancé"},
            {"nom": "Ali", "age": 28, "niveau": "Moyen"},
        ]

        cls.dao.collection.insert_many(cls.reference_data)

    def test_regression_clients(self):
        """
        Test de régression : Vérification de contenu MongoDB n a pas changé
        après des modifications du code.
        """
        current_data = list(self.dao.collection.find({}, {"_id": 0}))

        current_data.sort(key=lambda x: x["nom"])
        expected_data = sorted(self.reference_data, key=lambda x: x["nom"])

        self.assertEqual(current_data, expected_data,
                         "Les données dans MongoDB ont changé (régression détectée)")

    @classmethod
    def tearDownClass(cls):
        """Nettoyage après les tests"""
        cls.dao.collection.delete_many({})
        cls.dao.close()


if __name__ == "__main__":
    unittest.main()
