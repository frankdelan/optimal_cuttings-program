# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_settings.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(353, 199)
        Dialog.setStyleSheet(u"background-color:rgba(45, 50, 77, 1);")
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 10, 151, 41))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.8);\n"
"border-radius: 3px;\n"
"border: 1px solid #383838;\n"
"color: #000000;\n"
"padding: 5px;")
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(10, 70, 151, 41))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.8);\n"
"border-radius: 3px;\n"
"border: 1px solid #383838;\n"
"color: #000000;\n"
"padding: 5px;")
        self.add_button = QPushButton(Dialog)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setGeometry(QRect(180, 10, 161, 101))
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
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 130, 191, 51))
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgba(227, 38, 38, 1);")
        self.back_button = QPushButton(Dialog)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(220, 150, 121, 41))
        self.back_button.setFont(font1)
        self.back_button.setCursor(QCursor(Qt.ArrowCursor))
        self.back_button.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgba(151, 10, 10, 0.8);\n"
"border: 2px solid #3B3B3B;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:rgba(202, 13, 13, 0.8);\n"
"}\n"
"QPushButton{\n"
"background-color: rgba(209, 66, 66, 0.8);\n"
"border-radius: 8px;\n"
"border: 1px solid #3B3B3B;\n"
"color: white;\n"
"}")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"MetallOPT", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u0440\u0435\u0437\u043e\u043a", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.add_button.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label.setText("")
        self.back_button.setText(QCoreApplication.translate("Dialog", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f", None))
    # retranslateUi

