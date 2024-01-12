# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'agent_settings.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_AgentSettingsWindow(object):
    def setupAgentSettingsUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.return_button_agent_settings = QPushButton(self.centralwidget)
        self.return_button_agent_settings.setObjectName(u"pushButton")
        self.return_button_agent_settings.setMaximumSize(QSize(16777215, 40))
        self.return_button_agent_settings.setStyleSheet(u"QPushButton {\n"
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
"  height:100px;\n"
"  left: 0;\n"
"  width: 100%;\n"
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
""
                        "}\n"
"\n"
"QPushButton:hover {\n"
"  outline: 0;\n"
"}\n"
"\n"
"@media (min-width: 768px) {\n"
"  QPushButton {\n"
"    padding: 0 40px;\n"
"  }\n"
"}")

        self.gridLayout.addWidget(self.return_button_agent_settings, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.speed_label = QLabel(self.centralwidget)
        self.speed_label.setObjectName(u"speed_label")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.speed_label.sizePolicy().hasHeightForWidth())
        self.speed_label.setSizePolicy(sizePolicy)
        self.speed_label.setStyleSheet(u"QLabel{\n"
"  font-family: Inter,sans-serif;\n"
"  font-size: 24px;\n"
"  align-items: center;\n"
"  border: 2px solid #111;\n"
"  border-radius: 8px;\n"
"}")

        self.horizontalLayout.addWidget(self.speed_label)

        self.speed_input_line = QLineEdit(self.centralwidget)
        self.speed_input_line.setObjectName(u"speed_input_line")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.speed_input_line.sizePolicy().hasHeightForWidth())
        self.speed_input_line.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.speed_input_line)

        self.speed_submit_button = QPushButton(self.centralwidget)
        self.speed_submit_button.setObjectName(u"speed_submit_button")
        sizePolicy.setHeightForWidth(self.speed_submit_button.sizePolicy().hasHeightForWidth())
        self.speed_submit_button.setSizePolicy(sizePolicy)
        self.speed_submit_button.setMaximumSize(QSize(16777215, 40))
        self.speed_submit_button.setStyleSheet(u"QPushButton {\n"
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
"  height:100px;\n"
"  left: 0;\n"
"  width: 100%;\n"
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
""
                        "}\n"
"\n"
"QPushButton:hover {\n"
"  outline: 0;\n"
"}\n"
"\n"
"@media (min-width: 768px) {\n"
"  QPushButton {\n"
"    padding: 0 40px;\n"
"  }\n"
"}")

        self.horizontalLayout.addWidget(self.speed_submit_button)

        self.current_speed_label = QLabel(self.centralwidget)
        self.current_speed_label.setObjectName(u"current_speed_label")
        sizePolicy.setHeightForWidth(self.current_speed_label.sizePolicy().hasHeightForWidth())
        self.current_speed_label.setSizePolicy(sizePolicy)
        self.current_speed_label.setStyleSheet(u"QLabel{\n"
"  font-family: Inter,sans-serif;\n"
"  font-size: 24px;\n"
"  align-items: center;\n"
"  border: 2px solid #111;\n"
"  border-radius: 8px;\n"
"}")

        self.horizontalLayout.addWidget(self.current_speed_label)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.radius_label = QLabel(self.centralwidget)
        self.radius_label.setObjectName(u"radius_label")
        sizePolicy.setHeightForWidth(self.radius_label.sizePolicy().hasHeightForWidth())
        self.radius_label.setSizePolicy(sizePolicy)
        self.radius_label.setStyleSheet(u"QLabel{\n"
"  font-family: Inter,sans-serif;\n"
"  font-size: 24px;\n"
"  align-items: center;\n"
"  border: 2px solid #111;\n"
"  border-radius: 8px;\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.radius_label)

        self.radius_input_line = QLineEdit(self.centralwidget)
        self.radius_input_line.setObjectName(u"radius_input_line")
        sizePolicy.setHeightForWidth(self.radius_input_line.sizePolicy().hasHeightForWidth())
        self.radius_input_line.setSizePolicy(sizePolicy)
        self.radius_input_line.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.radius_input_line)

        self.radius_submit_button = QPushButton(self.centralwidget)
        self.radius_submit_button.setObjectName(u"radius_submit_button")
        sizePolicy.setHeightForWidth(self.radius_submit_button.sizePolicy().hasHeightForWidth())
        self.radius_submit_button.setSizePolicy(sizePolicy)
        self.radius_submit_button.setMaximumSize(QSize(16777215, 40))
        self.radius_submit_button.setStyleSheet(u"QPushButton {\n"
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
"  height:100px;\n"
"  left: 0;\n"
"  width: 100%;\n"
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
""
                        "}\n"
"\n"
"QPushButton:hover {\n"
"  outline: 0;\n"
"}\n"
"\n"
"@media (min-width: 768px) {\n"
"  QPushButton {\n"
"    padding: 0 40px;\n"
"  }\n"
"}")

        self.horizontalLayout_2.addWidget(self.radius_submit_button)

        self.current_radius_label = QLabel(self.centralwidget)
        self.current_radius_label.setObjectName(u"current_radius_label")
        sizePolicy.setHeightForWidth(self.current_radius_label.sizePolicy().hasHeightForWidth())
        self.current_radius_label.setSizePolicy(sizePolicy)
        self.current_radius_label.setLayoutDirection(Qt.LeftToRight)
        self.current_radius_label.setStyleSheet(u"QLabel{\n"
"  font-family: Inter,sans-serif;\n"
"  font-size: 24px;\n"
"  align-items: center;\n"
"  border: 2px solid #111;\n"
"  border-radius: 8px;\n"
"}")
        self.current_radius_label.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_2.addWidget(self.current_radius_label)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)



        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateAgentSettingsUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateAgentSettingsUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.return_button_agent_settings.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.speed_label.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.speed_submit_button.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.current_speed_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.radius_label.setText(QCoreApplication.translate("MainWindow", u"Radius", None))
        self.radius_submit_button.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.current_radius_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

