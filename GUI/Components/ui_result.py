# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_result.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QDialog,
    QHeaderView, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(613, 317)
        Dialog.setStyleSheet(u"background-color:rgba(45, 50, 77, 1);")
        self.path_input = QLineEdit(Dialog)
        self.path_input.setObjectName(u"path_input")
        self.path_input.setGeometry(QRect(440, 10, 161, 31))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(True)
        self.path_input.setFont(font)
        self.path_input.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.5);\n"
"border-radius: 3px;\n"
"border: 1px solid #383838;\n"
"color: #000000;\n"
"padding: 5px;")
        self.path_input.setReadOnly(True)
        self.choose_button = QPushButton(Dialog)
        self.choose_button.setObjectName(u"choose_button")
        self.choose_button.setGeometry(QRect(440, 40, 161, 41))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.choose_button.setFont(font1)
        self.choose_button.setCursor(QCursor(Qt.ArrowCursor))
        self.choose_button.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgba(10,94,239,0.8);\n"
"border: 2px solid #3B3B3B;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(88, 127, 255,0.8);\n"
"}\n"
"QPushButton{\n"
"background-color: rgba(95,94,239,0.8);\n"
"border-bottom-right-radius: 8px;\n"
"border-bottom-left-radius: 8px;\n"
"border: 1px solid #3B3B3B;\n"
"color: white;\n"
"}")
        self.download_button = QPushButton(Dialog)
        self.download_button.setObjectName(u"download_button")
        self.download_button.setGeometry(QRect(440, 220, 161, 81))
        self.download_button.setFont(font1)
        self.download_button.setCursor(QCursor(Qt.ArrowCursor))
        self.download_button.setStyleSheet(u"QPushButton:hover{\n"
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
        self.tableWidget = QTableWidget(Dialog)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        __qtablewidgetitem.setBackground(QColor(255, 255, 255));
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 10, 421, 291))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(14)
        self.tableWidget.setFont(font2)
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
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setHighlightSections(True)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"MetallOPT", None))
        self.path_input.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u043f\u0443\u0442\u044c", None))
        self.choose_button.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.download_button.setText(QCoreApplication.translate("Dialog", u"\u0421\u043a\u0430\u0447\u0430\u0442\u044c", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0447\u0435\u0442\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"\u041e\u0441\u0442\u0430\u0442\u043e\u043a", None));
    # retranslateUi

