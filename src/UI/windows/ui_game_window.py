# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gamepbIRnp.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_GameWindow(object):
    def setupGameUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scene_widget = QWidget(self.centralwidget)
        self.scene_widget.setObjectName(u"scene_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scene_widget.sizePolicy().hasHeightForWidth())
        self.scene_widget.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.scene_widget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.return_button_game = QPushButton(self.centralwidget)
        self.return_button_game.setObjectName(u"return_button_game")
        self.return_button_game.setMinimumSize(QSize(0, 40))
        self.return_button_game.setStyleSheet(u"QPushButton {\n"
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
"QPushButton:focus {\n"
"  background-color: #51b533;\n"
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

        self.horizontalLayout.addWidget(self.return_button_game)

        self.restart_system = QPushButton(self.centralwidget)
        self.restart_system.setObjectName(u"restart_system")
        self.restart_system.setMinimumSize(QSize(0, 40))
        self.restart_system.setStyleSheet(u"QPushButton {\n"
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
"QPushButton:focus {\n"
"  background-color: #51b533;\n"
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

        self.horizontalLayout.addWidget(self.restart_system)

        self.export_ontology_button = QPushButton(self.centralwidget)
        self.export_ontology_button.setObjectName(u"export_ontology_button")
        self.export_ontology_button.setMinimumSize(QSize(0, 40))
        self.export_ontology_button.setStyleSheet(u"QPushButton {\n"
"  align-items: center;\n"
"  background-color: #c2fab1;\n"
"  border: 2px solid #111;\n"
"  border-radius: 8px;\n"
"  box-sizing: border-box;\n"
"  color: #111;\n"
"  cursor: pointer;\n"
"  display: flex;\n"
"  font-family: Inter,sans-serif;\n"
"  font-size: 14px;\n"
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
"QPushButton:focus {\n"
"  background-color: #51b533;\n"
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
        self.export_ontology_button.setText(u"Export ontology")

        self.horizontalLayout.addWidget(self.export_ontology_button)

        self.mas_on_of = QPushButton(self.centralwidget)
        self.mas_on_of.setObjectName(u"mas_on_of")
        self.mas_on_of.setMinimumSize(QSize(0, 40))
        self.mas_on_of.setStyleSheet(u"QPushButton {\n"
"  align-items: center;\n"
"  background-color: #c2fab1;\n"
"  border: 2px solid #111;\n"
"  border-radius: 8px;\n"
"  box-sizing: border-box;\n"
"  color: #111;\n"
"  cursor: pointer;\n"
"  display: flex;\n"
"  font-family: Inter,sans-serif;\n"
"  font-size: 12px;\n"
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
"QPushButton: after {\n"
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
"QPushButton:focus {\n"
"  background-color: #51b533;\n"
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

        self.horizontalLayout.addWidget(self.mas_on_of)

        self.pause_button = QPushButton(self.centralwidget)
        self.pause_button.setObjectName(u"pause_button")
        self.pause_button.setMinimumSize(QSize(0, 40))
        self.pause_button.setStyleSheet(u"QPushButton {\n"
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
"QPushButton:focus {\n"
"  background-color: #51b533;\n"
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

        self.horizontalLayout.addWidget(self.pause_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateGameUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateGameUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.return_button_game.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.restart_system.setText(QCoreApplication.translate("MainWindow", u"Restart", None))
        self.mas_on_of.setText(QCoreApplication.translate("MainWindow", u"Collective intelligence: on", None))
        self.pause_button.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
    # retranslateUi

