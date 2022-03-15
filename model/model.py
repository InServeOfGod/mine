import json
import os

from PyQt5.QtGui import QIcon


class Model:
    def __init__(self):
        self.root = os.getcwd()
        self.config = self.read()

        self.encoding = "UTF-8"
        self.title = "Mayın"
        self.icon = QIcon(os.path.join(self.root, "./assets/img/bomb.png"))
        self.btn_width = 32
        self.btn_height = 32
        self.btn_icon = QIcon(os.path.join(self.root, "./assets/img/radioactivity.png"))
        self.secure_icon = QIcon(os.path.join(self.root, "./assets/img/shield.png"))

        self.easy = 30
        self.medium = 40
        self.hard = 50
        self.veteran = 60
        self.difficulty = self.medium

    def new(self) -> None:
        """
        ayarları sıfırlar
        :rtype: None
        """
        self.config = {

        }

        self._write()

    def _write(self) -> None:
        """
        Sınıf içerisinde dosyaya yazmak için kullanılmalıdır.
        :rtype: None
        """
        dumping = json.dumps(self.config, indent=4, sort_keys=True)

        with open(os.path.join(self.root, "model", "config.json"), "w", encoding=self.encoding) as f:
            f.write(dumping)

        style = f"""

            """

        field = """@charset "UTF-8";"""

        with open(os.path.join(self.root, "./assets/css/style.min.css"), 'w', encoding=self.encoding) as f:
            f.write(field)

    def update(self, key: str, value: any) -> None:
        """
        Belli bir ayarı değiştirmek ve kaydetmek için kullanılır
        :rtype: None
        """
        self.config = self.read()
        self.config[key] = value
        self._write()

    def read(self) -> dict:
        """
        Ayarları okutur ve geri döndürür
        :rtype: dict
        """
        with open(os.path.join(self.root, "model", "config.json")) as f:
            json_data = f.read()
            dict_data = json.loads(json_data)
            self.config = dict_data
            return dict_data

    def read_stylesheets(self) -> str:
        """
        json dosyasından alınıp css dosyasına yazılan verileri döndürür
        :rtype: str
        """
        with open(os.path.join(self.root, "./assets/css/style.min.css"), encoding=self.encoding) as f:
            return f.read()
