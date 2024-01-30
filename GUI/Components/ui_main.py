# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(467, 337)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color:rgba(45, 50, 77, 1);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.add_button = QPushButton(self.centralwidget)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setGeometry(QRect(280, 10, 171, 41))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.add_button.setFont(font1)
        self.add_button.setCursor(QCursor(Qt.ArrowCursor))
        self.add_button.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgba(10,94,239,0.8);\n"
"border: 2px solid #3B3B3B;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(88, 127, 255,0.8);\n"
"}\n"
"QPushButton{\n"
"background-color: rgba(95,94,239,0.8);\n"
"border-radius: 8px;\n"
"border: 1px solid #3B3B3B;\n"
"color: white;\n"
"}")
        self.delete_button = QPushButton(self.centralwidget)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setGeometry(QRect(160, 280, 111, 41))
        self.delete_button.setFont(font1)
        self.delete_button.setCursor(QCursor(Qt.ArrowCursor))
        self.delete_button.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgba(10,94,239,0.8);\n"
"border: 2px solid #3B3B3B;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(88, 127, 255,0.8);\n"
"}\n"
"QPushButton{\n"
"background-color: rgba(95,94,239,0.8);\n"
"border-radius: 8px;\n"
"border: 1px solid #3B3B3B;\n"
"color: white;\n"
"}")
        self.clear_button = QPushButton(self.centralwidget)
        self.clear_button.setObjectName(u"clear_button")
        self.clear_button.setGeometry(QRect(10, 280, 111, 41))
        self.clear_button.setFont(font1)
        self.clear_button.setCursor(QCursor(Qt.ArrowCursor))
        self.clear_button.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgba(10,94,239,0.8);\n"
"border: 2px solid #3B3B3B;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(88, 127, 255,0.8);\n"
"}\n"
"QPushButton{\n"
"background-color: rgba(95,94,239,0.8);\n"
"border-radius: 8px;\n"
"border: 1px solid #3B3B3B;\n"
"color: white;\n"
"}")
        self.result_button = QPushButton(self.centralwidget)
        self.result_button.setObjectName(u"result_button")
        self.result_button.setGeometry(QRect(280, 250, 171, 71))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.result_button.sizePolicy().hasHeightForWidth())
        self.result_button.setSizePolicy(sizePolicy)
        self.result_button.setFont(font1)
        self.result_button.setCursor(QCursor(Qt.ArrowCursor))
        self.result_button.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgba(5, 143, 5, 0.8);\n"
"border: 2px solid #3B3B3B;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(10, 190, 10, 0.8);\n"
"}\n"
"QPushButton{\n"
"background-color: rgba(7, 177, 7, 0.8);\n"
"border-radius: 8px;\n"
"border: 1px solid #3B3B3B;\n"
"color: white;\n"
"}")
        self.length_input = QLineEdit(self.centralwidget)
        self.length_input.setObjectName(u"length_input")
        self.length_input.setGeometry(QRect(280, 70, 171, 31))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.length_input.setFont(font2)
        self.length_input.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.8);\n"
"border-radius: 3px;\n"
"border: 1px solid #383838;\n"
"color: #000000;\n"
"padding: 5px;")
        self.error_label = QLabel(self.centralwidget)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setGeometry(QRect(280, 120, 161, 91))
        self.error_label.setFont(font2)
        self.error_label.setStyleSheet(u"color: rgba(227, 38, 38, 1);")
        self.error_label.setScaledContents(False)
        self.error_label.setAlignment(Qt.AlignCenter)
        self.error_label.setWordWrap(True)
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        __qtablewidgetitem.setBackground(QColor(255, 255, 255));
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 10, 261, 251))
        self.tableWidget.setFont(font1)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet(u"QHeaderView::section:last {\n"
"        background-color: rgba(255, 255, 255, 0.9);\n"
"        color: black;\n"
"        border: 1px solid #3B3B3B;\n"
"		 border-top-right-radius: 10px;\n"
"		padding: 1px;\n"
"    }\n"
"QHeaderView::section:first {\n"
"        background-color: rgba(255, 255, 255, 0.9);\n"
"        color: black;\n"
"        border: 1px solid #3B3B3B;\n"
"		 border-top-left-radius: 10px;\n"
"		padding: 1px;\n"
"    }\n"
"QTableWidget{\n"
"background-color:rgba(123, 88, 182, 1);\n"
"border-radius: 8px;\n"
"color: white;\n"
"}")
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(32)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.add_button.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MetallOPT", None))
        self.add_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.delete_button.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.result_button.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
        self.length_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u043d\u0430 \u043f\u043b\u0435\u0442\u0438", None))
        self.error_label.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0440\u0435\u0437\u043e\u043a", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None));
    # retranslateUi

