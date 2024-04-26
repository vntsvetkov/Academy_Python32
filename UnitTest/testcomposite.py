import unittest
from composite import File, Folder


class TestFile(unittest.TestCase):

    def setUp(self):
        print("Вызов метода setUp перед тестом")
        self.file = File("Файл 1", 360)

    def test_get_size(self):
        self.assertEqual(self.file.get_size(), 360)

    def tearDown(self):
        print("Вызов метода tearDown после тестов")


class TestFolder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.folder = Folder("Папка 1")

    def test_add_folder(self):
        f = Folder("Папка 2")
        f.add(File("Файл 1", 200))
        self.folder.add(f)
        self.assertIn(f, self.folder.get_container())

    def test_add_file(self):
        f = File("Файл 1", 300)
        self.folder.add(f)
        self.assertIn(f, self.folder.get_container())

    def test_get_size(self):
        self.assertEqual(self.folder.get_size(), 500)

    @classmethod
    def tearDownClass(cls):
        ...


if __name__ == '__main__':
    unittest.main()
