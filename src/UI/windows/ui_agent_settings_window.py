# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'agent_settingsmCryjE.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_AgentSettingsWindow(object):
    def setupAgentSettingsUi(self, AgentSettingsWindow):
        if not AgentSettingsWindow.objectName():
            AgentSettingsWindow.setObjectName(u"AgentSettingsWindow")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AgentSettingsWindow.sizePolicy().hasHeightForWidth())
        AgentSettingsWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(AgentSettingsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.speed_label = QLabel(self.widget)
        self.speed_label.setObjectName(u"speed_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.speed_label.sizePolicy().hasHeightForWidth())
        self.speed_label.setSizePolicy(sizePolicy1)
        self.speed_label.setStyleSheet(u"QLabel{\n"
"  font-family: Inter,sans-serif;\n"
"  font-size: 50px;\n"
"  align-items: center;\n"
"  border: 2px solid #111;\n"
"  border-radius: 8px;\n"
"}")

        self.horizontalLayout.addWidget(self.speed_label)

        self.speed_input_line = QLineEdit(self.widget)
        self.speed_input_line.setObjectName(u"speed_input_line")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.speed_input_line.sizePolicy().hasHeightForWidth())
        self.speed_input_line.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(50)
        self.speed_input_line.setFont(font)

        self.horizontalLayout.addWidget(self.speed_input_line)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.radius_label = QLabel(self.widget)
        self.radius_label.setObjectName(u"radius_label")
        sizePolicy1.setHeightForWidth(self.radius_label.sizePolicy().hasHeightForWidth())
        self.radius_label.setSizePolicy(sizePolicy1)
        self.radius_label.setStyleSheet(u"QLabel{\n"
"  font-family: Inter,sans-serif;\n"
"  font-size: 50px;\n"
"  align-items: center;\n"
"  border: 2px solid #111;\n"
"  border-radius: 8px;\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.radius_label)

        self.radius_input_line = QLineEdit(self.widget)
        self.radius_input_line.setObjectName(u"radius_input_line")
        sizePolicy1.setHeightForWidth(self.radius_input_line.sizePolicy().hasHeightForWidth())
        self.radius_input_line.setSizePolicy(sizePolicy1)
        self.radius_input_line.setFont(font)
        self.radius_input_line.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.radius_input_line)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.error_label_agent_settings = QLabel(self.widget)
        self.error_label_agent_settings.setObjectName(u"error_label_agent_settings")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.error_label_agent_settings.sizePolicy().hasHeightForWidth())
        self.error_label_agent_settings.setSizePolicy(sizePolicy3)
        font1 = QFont()
        font1.setPointSize(16)
        self.error_label_agent_settings.setFont(font1)

        self.verticalLayout_2.addWidget(self.error_label_agent_settings)


        self.verticalLayout.addWidget(self.widget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.return_button_agent_settings = QPushButton(self.centralwidget)
        self.return_button_agent_settings.setObjectName(u"return_button_agent_settings")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.return_button_agent_settings.sizePolicy().hasHeightForWidth())
        self.return_button_agent_settings.setSizePolicy(sizePolicy4)
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

        self.horizontalLayout_3.addWidget(self.return_button_agent_settings)

        self.submit_editing_agent_settings = QPushButton(self.centralwidget)
        self.submit_editing_agent_settings.setObjectName(u"submit_editing_agent_settings")
        self.submit_editing_agent_settings.setMinimumSize(QSize(0, 40))
        self.submit_editing_agent_settings.setMaximumSize(QSize(16777215, 40))
        self.submit_editing_agent_settings.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_3.addWidget(self.submit_editing_agent_settings)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        AgentSettingsWindow.setCentralWidget(self.centralwidget)

        self.retranslateAgentSettingsUi(AgentSettingsWindow)

        QMetaObject.connectSlotsByName(AgentSettingsWindow)
    # setupUi

    def retranslateAgentSettingsUi(self, AgentSettingsWindow):
        AgentSettingsWindow.setWindowTitle(QCoreApplication.translate("AgentSettingsWindow", u"MainWindow", None))
        self.speed_label.setText(QCoreApplication.translate("AgentSettingsWindow", u"Speed", None))
        self.radius_label.setText(QCoreApplication.translate("AgentSettingsWindow", u"Radius", None))
        self.error_label_agent_settings.setText(QCoreApplication.translate("AgentSettingsWindow", u"<html><head/><body><p><span style=\" font-size:14pt; color:#aa0000;\">Incorrect data format</span></p></body></html>", None))
        self.return_button_agent_settings.setText(QCoreApplication.translate("AgentSettingsWindow", u"Return", None))
        self.submit_editing_agent_settings.setText(QCoreApplication.translate("AgentSettingsWindow", u"Submit editing", None))
    # retranslateUi

