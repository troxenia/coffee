import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect('coffee.sqlite')
        self.display_data()

    def display_data(self):
        data = self.con.cursor().execute('SELECT coffee.id, types.type, roasts.roast, coffee.texture, coffee.taste, '
                                         'coffee.price, volumes.volume FROM coffee '
                                         'JOIN types ON types.id = coffee.type JOIN roasts ON roasts.id = coffee.roast '
                                         'JOIN volumes ON volumes.id = coffee.volume').fetchall()
        self.table.setColumnCount(len(data[0]))
        self.table.setHorizontalHeaderLabels(['ID', 'название сорта', 'степень обжарки', 'молотый/в зернах',
                                              'описание вкуса', 'цена', 'объем упаковки'])
        self.table.setRowCount(0)
        for i, row in enumerate(data):
            self.table.setRowCount(
                self.table.rowCount() + 1)
            for j, elem in enumerate(row):
                self.table.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.table.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec_())
