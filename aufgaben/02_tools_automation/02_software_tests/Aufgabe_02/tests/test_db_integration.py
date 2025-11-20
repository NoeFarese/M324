import unittest
import docker
import time
from src.db import Db
from src.models import User

class TestDb(unittest.TestCase):
    MONGO_IMAGE = "mongo:latest"
    MONGO_PORT = 27017

    def setUp(self):
        self.client = docker.from_env()
        self.container = self.client.containers.run(
            self.MONGO_IMAGE,
            detach=True,
            ports={f"{self.MONGO_PORT}/tcp": self.MONGO_PORT},
            name="test-mongo-db",
            remove=True
        )
        time.sleep(5)
        self.db = Db(f"mongodb://localhost:{self.MONGO_PORT}/")

    def tearDown(self):
        self.container.stop()

    def test_set_and_get_user(self):
        user = User(name="Cassius Thundercock", mail="bodycam_off@sincevietnam.com")
        self.db.set_user(user)
        retrieved_user = self.db.get_user()
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(user.name, retrieved_user.name)
        self.assertEqual(user.mail, retrieved_user.mail)


if __name__ == "__main__":
    unittest.main()
