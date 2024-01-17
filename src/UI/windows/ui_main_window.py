# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_menujAZlBc.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupMainWindowUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setMinimumSize(QSize(1080, 1080))
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"	background-color: #F0F0F0\n"
"	color: #F0F0F0\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setAlignment(Qt.AlignCenter)
        self.verticalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.settings_button = QPushButton(self.widget_2)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setMaximumSize(QSize(354, 100))
        self.settings_button.setStyleSheet(u"QPushButton {\n"
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
"  height: 100px;\n"
"  line-height: 300px;\n"
"  max-width: 300%;\n"
"  padding: 0 25px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"}")

        self.verticalLayout_3.addWidget(self.settings_button)

        self.start_button = QPushButton(self.widget_2)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setMaximumSize(QSize(354, 100))
        self.start_button.setStyleSheet(u"QPushButton {\n"
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
"  height: 100px;\n"
"  justify-content: left;\n"
"  line-height: 300px;\n"
"  max-width: 300%;\n"
"  padding: 0 25px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"}")

        self.verticalLayout_3.addWidget(self.start_button)

        self.mas_info_button = QPushButton(self.widget_2)
        self.mas_info_button.setObjectName(u"mas_info_button")
        self.mas_info_button.setMaximumSize(QSize(354, 100))
        self.mas_info_button.setStyleSheet(u"QPushButton {\n"
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
"  height: 100px;\n"
"  justify-content: left;\n"
"  line-height: 300px;\n"
"  max-width: 300%;\n"
"  padding: 0 25px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"}")

        self.verticalLayout_3.addWidget(self.mas_info_button)

        self.graph_button = QPushButton(self.widget_2)
        self.graph_button.setObjectName(u"graph_button")
        self.graph_button.setMaximumSize(QSize(354, 100))
        self.graph_button.setStyleSheet(u"QPushButton {\n"
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
"  height: 100px;\n"
"  justify-content: left;\n"
"  line-height: 300px;\n"
"  max-width: 300%;\n"
"  padding: 0 25px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"}")

        self.verticalLayout_3.addWidget(self.graph_button)

        self.help_button = QPushButton(self.widget_2)
        self.help_button.setObjectName(u"help_button")
        self.help_button.setStyleSheet(u"QPushButton {\n"
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
"  height: 100px;\n"
"  justify-content: left;\n"
"  line-height: 300px;\n"
"  max-width: 300%;\n"
"  padding: 0 25px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"}")

        self.verticalLayout_3.addWidget(self.help_button)

        self.exit_button = QPushButton(self.widget_2)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setMaximumSize(QSize(354, 100))
        self.exit_button.setStyleSheet(u"QPushButton {\n"
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
"  height: 100px;\n"
"  justify-content: left;\n"
"  line-height: 300px;\n"
"  max-width: 300%;\n"
"  padding: 0 25px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"}")
        self.exit_button.setIconSize(QSize(16, 16))
        self.exit_button.setCheckable(False)
        self.exit_button.setAutoRepeat(False)
        self.exit_button.setAutoExclusive(False)
        self.exit_button.setAutoDefault(False)
        self.exit_button.setFlat(False)

        self.verticalLayout_3.addWidget(self.exit_button)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(48, -1, -1, -1)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel{\n"
"  font-family: Inter,sans-serif;\n"
"  font-size: 20px;\n"
"}")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel{\n"
"  font-family: Inter,sans-serif;\n"
"  font-size: 16px;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.label_2)

        self.image_label = QLabel(self.widget)
        self.image_label.setObjectName(u"image_label")
        self.label.setStyleSheet(u"QLabel{\n"
"        border-radius: 10px;\n"
"    }\n"
"")
        sizePolicy.setHeightForWidth(self.image_label.sizePolicy().hasHeightForWidth())
        self.image_label.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.image_label)


        self.horizontalLayout.addWidget(self.widget)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setStyleSheet(u"QLabel{\n"
"  font-family: Inter,sans-serif;\n"
"  font-size: 12px;\n"
"}")

        self.verticalLayout_2.addWidget(self.label_4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateMainUi(MainWindow)

        self.exit_button.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateMainUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.settings_button.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Start/Continue", None))
        self.mas_info_button.setText(QCoreApplication.translate("MainWindow", u"Desicion making log", None))
        self.graph_button.setText(QCoreApplication.translate("MainWindow", u"Results", None))
        self.help_button.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.exit_button.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:700;\">Ants VS Spiders</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Training course on emergent intelligence</span></p><p><span style=\" font-size:10pt;\">Collective intelligence wins!</span></p></body></html>", None))
        self.image_label.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Collective intelligence, 2024 \u24b8</span></p></body></html>", None))
    # retranslateUi

