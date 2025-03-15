import json

from ui import Ui_MainWindow

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets

app = QApplication([])
MainWindow = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

notes = {}

def add_note():
    note_name, ok = QInputDialog.getText(MainWindow, "Додати замітку", "Назва замітки: ")
    if ok and note_name !="":
        notes[note_name] = {"текст":"", "теги": []}
        ui.listWidget.addItem(note_name)
        #ui.listWidget_2.clear()
        print(notes)

def show_note():
    key = ui.listWidget.selectedItems()[0].text()
    ui.textEdit.setText(notes[key]["текст"])
    ui.listWidget_2.clear()
    ui.listWidget_2.addItems(notes[key]["теги"])

def save_note():
    if ui.listWidget.selectedItem():
        key = ui.listWidget.selectedItems()[0].text()
        notes[key]["text"] = ui.textEdit.toPlainText()
        with open("notes_data.json", "w") as file:
            json.dump(notes,file,sort_keys = True, ensure_ascii = False)
        print(notes)
    else:
        print("Замітка для збереження не вибрана!")

def del_note():
    if ui.listWidget.selectedItems():
        key = ui.listWidget.selectedItems()[0].text()
        del notes[key]
        ui.listWidget.clear()
        ui.listWidget_2.clear()
        ui.textEdit.clear()
        ui.listWidget.addItems(notes)
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys = True, ensure_ascii = False)
        print(notes)
    else:
        print("Не вибрали замітку")

        


ui.pushButton.clicked.connect(add_note)



MainWindow.show()
app.exec_()
