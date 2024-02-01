import sys

from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self.setFixedSize(650, 450)
        self.setWindowTitle('Большая задача по Maps API. Часть №1')

    def get_map(self):  # Получение изображения
        return ''

    def show_map(self):  # Вывод
        map_image = self.get_map()
        pixmap = QPixmap(map_image)
        self.image.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())
