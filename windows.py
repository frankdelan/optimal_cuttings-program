from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidgetItem, QFileDialog

from GUI.Components.ui_main import Ui_MainWindow
from GUI.Components.ui_settings import Ui_Dialog as Ui_SettingWindow
from GUI.Components.ui_result import Ui_Dialog as Ui_ResultWindow

from utils.algorithm import get_optimal
from utils.pdf_generator import generate_pdf


class WindowBase:
    def set_screen_size(self, width, height):
        screens = QApplication.screens()
        if screens:
            screen_geometry = screens[0].availableGeometry()

            x = (screen_geometry.width() - self.width()) // 2
            y = (screen_geometry.height() - self.height()) // 2

            self.setGeometry(x, y, width, height)
            self.setFixedSize(self.width(), self.height())


class StartWindow(QMainWindow, WindowBase):
    def __init__(self):
        super(StartWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.set_screen_size(467, 337)

        self.ui.tableWidget.setColumnWidth(0, 0.5 * self.ui.tableWidget.width())
        self.ui.tableWidget.setColumnWidth(1, 0.2 * self.ui.tableWidget.width())

        self.ui.add_button.clicked.connect(self.add_button_clicked)
        self.ui.delete_button.clicked.connect(self.delete_button_clicked)
        self.ui.clear_button.clicked.connect(self.clear_button_clicked)
        self.ui.result_button.clicked.connect(self.result_button_clicked)

    def add_button_clicked(self):
        self.hide()
        settings_window = SettingsWindow(self)
        settings_window.exec()

    def result_button_clicked(self):
        try:
            length = int(self.ui.length_input.text())
        except ValueError:
            self.ui.error_label.setText("Некорректная длина!")
            return
        else:
            if length <= 0:
                self.ui.error_label.setText("Некорректный ввод!")
                return
            data = []
            for row in range(self.ui.tableWidget.rowCount()):
                segment = self.ui.tableWidget.item(row, 0)
                count = self.ui.tableWidget.item(row, 1)
                data.append([int(segment.text()), int(count.text())])
            if list(filter(lambda item: item[0] > length, data)):
                self.ui.error_label.setText("Некорректная длина!")
                return
            else:
                self.ui.error_label.setText("")
        self.hide()
        result_window = ResultWindow(length, data)
        result_window.exec()

    def add_data_to_table(self, data1, data2):
        row_position = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row_position)

        self.ui.tableWidget.setItem(row_position, 0, QTableWidgetItem(str(data1)))
        self.ui.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(data2)))

    def delete_button_clicked(self):
        selected_indexes = self.ui.tableWidget.selectionModel().selectedRows()
        for index in sorted(selected_indexes, reverse=True):
            self.ui.tableWidget.removeRow(index.row())

    def clear_button_clicked(self):
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)


class SettingsWindow(QDialog, WindowBase):
    def __init__(self, start_window):
        super(SettingsWindow, self).__init__()
        self.ui = Ui_SettingWindow()
        self.ui.setupUi(self)
        self.start_window = start_window

        self.set_screen_size(350, 200)

        self.ui.back_button.clicked.connect(self.back_button_clicked)
        self.ui.add_button.clicked.connect(self.add_data_button_clicked)

    def back_button_clicked(self):
        self.hide()
        self.start_window.show()

    def add_data_button_clicked(self):
        try:
            data1 = int(self.ui.lineEdit.text())
            data2 = int(self.ui.lineEdit_2.text())
        except ValueError:
            self.ui.label.setText("Некорректный ввод!")
            return
        else:
            if (data1 | data2) <= 0:
                self.ui.label.setText("Некорректный ввод!")
                return
            self.start_window.add_data_to_table(data1, data2)
            self.ui.lineEdit.clear()
            self.ui.lineEdit_2.clear()


class ResultWindow(QDialog, WindowBase):
    def __init__(self, length, data):
        super(ResultWindow, self).__init__()
        self.ui = Ui_ResultWindow()
        self.ui.setupUi(self)

        self.set_screen_size(613, 317)

        self.add_data_to_list(length, data)

        self.ui.tableWidget.setColumnWidth(0, 0.75 * self.ui.tableWidget.width())
        self.ui.tableWidget.setColumnWidth(1, 0.2 * self.ui.tableWidget.width())

        self.ui.download_button.clicked.connect(self.download_pdf)
        self.ui.choose_button.clicked.connect(self.choose_directory)

    def choose_directory(self):
        directory_path = QFileDialog.getExistingDirectory(self, "Выбрать директорию")
        if directory_path:
            self.ui.path_input.setText(directory_path)

    def add_data_to_list(self, length, data):
        self.result: list[list[tuple[int], int]] = get_optimal(length, data)
        for item in self.result:
            row_position = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row_position)

            combination: str = "][".join(map(str, item[0]))

            self.ui.tableWidget.setItem(row_position, 0, QTableWidgetItem(f"[{combination}]"))
            self.ui.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(item[1])))

    def download_pdf(self):
        generate_pdf(self.result, self.ui.path_input.text())
