# -*- coding: utf-8 -*-
import os
import time

################################################################################
## Form generated from reading UI file 'graphs.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QThread)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform, QMovie)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLayout, QMainWindow,
                               QPushButton, QSizePolicy, QVBoxLayout, QWidget, QDialog, QLabel)

from src.utils.Graphs.MplWidget import MplWidget


class Ui_GraphsWindow(object):
    def setupGraphsUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 862))
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        y_names = ['Accumulated energy of ants', 'Accumulated energy of spiders',
                   'Energy of anthill', 'Number of messages']
        self.graph_1 = MplWidget(y_names[0])
        self.graph_1.setObjectName(u"graph_1")

        self.horizontalLayout_3.addWidget(self.graph_1)

        self.graph_2 = MplWidget(y_names[1])
        self.graph_2.setObjectName(u"graph_2")

        self.horizontalLayout_3.addWidget(self.graph_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.graph_3 = MplWidget(y_names[2])
        self.graph_3.setObjectName(u"graph_3")

        self.horizontalLayout_2.addWidget(self.graph_3)

        self.graph_4 = MplWidget(y_names[3])
        self.graph_4.setObjectName(u"graph_4")

        self.horizontalLayout_2.addWidget(self.graph_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addWidget(self.widget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.return_button_graphs = QPushButton(self.centralwidget)
        self.return_button_graphs.setObjectName(u"return_button_graphs")
        self.return_button_graphs.setMinimumSize(QSize(0, 40))
        self.return_button_graphs.setStyleSheet(u"QPushButton {\n"
"  align-items: center;\n"
"  background-color: #c2fab1;\n"
"  border: 2px solid #111;\n"
"  border-radius: 8px;\n"
"  box-sizing: border-box;\n"
"  color: #111;\n"
"  cursor: pointer;\n"
"  display: flex;\n"
"  font-family: Inter,sans-serif;\n"
"  font-size: 16px;\n"
"  justify-content: center;\n"
"  padding: 0 25px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"}\n"
"\n"
"QPushButton:after {\n"
"  background-color: #111;\n"
"  border-radius: 8px;\n"
"  content: \"\";\n"
"  display: block;\n"
"  left: 0;\n"
"  position: absolute;\n"
"  top: -2px;\n"
"  transform: translate(8px, 8px);\n"
"  transition: transform .2s ease-out;\n"
"  z-index: -1;\n"
"}\n"
"\n"
"QPushButton:hover:after {\n"
"  transform: translate(0, 0);\n"
"}\n"
"\n"
"QPushButton:active {\n"
"  background-color: #c2fab1;\n"
"  outline: 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  outline: 0;\n"
"}\n"
""
                        "\n"
"@media (min-width: 768px) {\n"
"  QPushButton {\n"
"    padding: 0 40px;\n"
"  }\n"
"}")

        self.horizontalLayout.addWidget(self.return_button_graphs)

        self.download_graphs_button = QPushButton(self.centralwidget)
        self.download_graphs_button.setObjectName(u"download_graphs_button")
        self.download_graphs_button.setMinimumSize(QSize(0, 40))
        self.download_graphs_button.setStyleSheet(u"QPushButton {\n"
"  align-items: center;\n"
"  background-color: #c2fab1;\n"
"  border: 2px solid #111;\n"
"  border-radius: 8px;\n"
"  box-sizing: border-box;\n"
"  color: #111;\n"
"  cursor: pointer;\n"
"  display: flex;\n"
"  font-family: Inter,sans-serif;\n"
"  font-size: 16px;\n"
"  justify-content: center;\n"
"  padding: 0 25px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"}\n"
"\n"
"QPushButton:after {\n"
"  background-color: #111;\n"
"  border-radius: 8px;\n"
"  content: \"\";\n"
"  display: block;\n"
"  left: 0;\n"
"  position: absolute;\n"
"  top: -2px;\n"
"  transform: translate(8px, 8px);\n"
"  transition: transform .2s ease-out;\n"
"  z-index: -1;\n"
"}\n"
"\n"
"QPushButton:hover:after {\n"
"  transform: translate(0, 0);\n"
"}\n"
"\n"
"QPushButton:active {\n"
"  background-color: #c2fab1;\n"
"  outline: 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  outline: 0;\n"
"}\n"
""
                        "\n"
"@media (min-width: 768px) {\n"
"  QPushButton {\n"
"    padding: 0 40px;\n"
"  }\n"
"}")

        self.horizontalLayout.addWidget(self.download_graphs_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateGraphsUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateGraphsUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.return_button_graphs.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.download_graphs_button.setText(QCoreApplication.translate("MainWindow", u"Download Graphs", None))
    # retranslateUi


