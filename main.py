import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from main_ui import Ui_MainWindow as Ui_main
from addEditCoffeeForm import Ui_MainWindow as Ui_form


class Coffee(QMainWindow, Ui_main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect('data/coffee.sqlite')
        self.manage = None
        self.add_btn.clicked.connect(self.add)
        self.edit_btn.clicked.connect(self.edit)
        self.delete_btn.clicked.connect(self.delete)
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

    def add(self):
        self.manage = Manage(self, self.sender().text())
        self.manage.show()

    def edit(self):
        if self.table.item(self.table.currentRow(), 0):
            data = []
            for col in range(self.table.columnCount()):
                data.append(str(self.table.item(self.table.currentRow(), col).text()))
            self.manage = Manage(self, self.sender().text(), *data)
            self.manage.show()

    def delete(self):
        if self.table.item(self.table.currentRow(), 0):
            self.con.cursor().execute(f'DELETE FROM coffee WHERE id = '
                                      f'{str(self.table.item(self.table.currentRow(), 0).text())}')
            self.con.commit()
            self.display_data()

    def closeEvent(self, event):
        if self.manage:
            self.manage.close()
        self.con.close()


class Manage(QMainWindow, Ui_form):
    def __init__(self, coffee, action, *data):
        super().__init__()
        self.setupUi(self)
        self.coffee, self.action = coffee, action
        roast = self.coffee.con.cursor().execute('SELECT roast FROM roasts').fetchall()
        self.roast.addItems([elem[0] for elem in roast])
        self.texture.addItems(['молотый', 'в зернах'])
        if self.action == 'Edit':
            self.id = int(data[0])
            self.type.setText(data[1])
            self.roast.setCurrentText(data[2])
            self.texture.setCurrentText(data[3])
            self.taste.setText(data[4])
            self.price.setText(data[5])
            self.volume.setText(data[6])
        self.save_btn.clicked.connect(self.change_values)

    def change_values(self):
        self.statusbar.showMessage('')
        if self.price.text().isdigit() and self.volume.text().isdigit():
            res = self.coffee.con.cursor().execute(f'SELECT id FROM types WHERE type = "{self.type.text()}"').fetchone()
            if not res:
                self.coffee.con.cursor().execute(f'INSERT INTO types(type) VALUES ("{self.type.text()}")')
            res = self.coffee.con.cursor().execute(f'SELECT id FROM volumes WHERE volume = '
                                                   f'"{self.volume.text()}"').fetchone()
            if not res:
                self.coffee.con.cursor().execute(f'INSERT INTO volumes(volume) VALUES ("{self.volume.text()}")')
            self.coffee.con.commit()
            if self.action == 'Edit':
                self.coffee.con.cursor().execute(f'UPDATE coffee SET type = (SELECT id FROM types WHERE type = '
                                                 f'"{self.type.text()}"), roast = (SELECT id FROM roasts WHERE roast = '
                                                 f'"{self.roast.currentText()}"), texture = '
                                                 f'"{self.texture.currentText()}", taste = "{self.taste.text()}", '
                                                 f'price = {self.price.text()}, volume = (SELECT id FROM volumes WHERE '
                                                 f'volume = {self.volume.text()}) WHERE id = {self.id}')
            else:
                self.coffee.con.cursor().execute(f'INSERT INTO coffee(type, roast, texture, taste, price, volume) '
                                                 f'VALUES ((SELECT id FROM types WHERE type = "{self.type.text()}"), '
                                                 f'(SELECT id FROM roasts WHERE roast = "{self.roast.currentText()}"), '
                                                 f'"{self.texture.currentText()}", "{self.taste.text()}", '
                                                 f'{self.price.text()}, (SELECT id FROM volumes WHERE volume = '
                                                 f'{self.volume.text()}))')
            self.coffee.con.commit()
            self.coffee.display_data()
        else:
            self.statusbar.showMessage('Incorrect input')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec_())
