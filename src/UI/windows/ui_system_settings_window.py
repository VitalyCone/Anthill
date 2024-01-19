# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'system_settingscSnvcD.ui'
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

class Ui_SystemSettingsWindow(object):
    def setupSystemSettingsUi(self, SystemSettingsWindow):
        if not SystemSettingsWindow.objectName():
            SystemSettingsWindow.setObjectName(u"SystemSettingsWindow")
        self.centralwidget = QWidget(SystemSettingsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.start_ants_num_label = QLabel(self.widget)
        self.start_ants_num_label.setObjectName(u"start_ants_num_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.start_ants_num_label.sizePolicy().hasHeightForWidth())
        self.start_ants_num_label.setSizePolicy(sizePolicy1)
        self.start_ants_num_label.setStyleSheet(u"QLabel{\n"
"  font-family: Inter,sans-serif;\n"
"  font-size: 50px;\n"
"  align-items: center;\n"
"  border: 2px solid #111;\n"
"  border-radius: 8px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.start_ants_num_label)

        self.start_ants_num_input_line = QLineEdit(self.widget)
        self.start_ants_num_input_line.setObjectName(u"start_ants_num_input_line")
        sizePolicy1.setHeightForWidth(self.start_ants_num_input_line.sizePolicy().hasHeightForWidth())
        self.start_ants_num_input_line.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(50)
        self.start_ants_num_input_line.setFont(font)

        self.horizontalLayout_3.addWidget(self.start_ants_num_input_line)


        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_apple_gap = QLabel(self.widget)
        self.label_apple_gap.setObjectName(u"label_apple_gap")
        sizePolicy1.setHeightForWidth(self.label_apple_gap.sizePolicy().hasHeightForWidth())
        self.label_apple_gap.setSizePolicy(sizePolicy1)
        self.label_apple_gap.setStyleSheet(u"QLabel{\n"
"  font-family: Inter,sans-serif;\n"
"  font-size: 50px;\n"
"  align-items: center;\n"
"  border: 2px solid #111;\n"
"  border-radius: 8px;\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.label_apple_gap)

        self.apples_gap_input_line = QLineEdit(self.widget)
        self.apples_gap_input_line.setObjectName(u"apples_gap_input_line")
        sizePolicy1.setHeightForWidth(self.apples_gap_input_line.sizePolicy().hasHeightForWidth())
        self.apples_gap_input_line.setSizePolicy(sizePolicy1)
        self.apples_gap_input_line.setFont(font)
        self.apples_gap_input_line.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.apples_gap_input_line)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.spider_gap_label = QLabel(self.widget)
        self.spider_gap_label.setObjectName(u"spider_gap_label")
        sizePolicy1.setHeightForWidth(self.spider_gap_label.sizePolicy().hasHeightForWidth())
        self.spider_gap_label.setSizePolicy(sizePolicy1)
        self.spider_gap_label.setStyleSheet(u"QLabel{\n"
"  font-family: Inter,sans-serif;\n"
"  font-size: 50px;\n"
"  align-items: center;\n"
"  border: 2px solid #111;\n"
"  border-radius: 8px;\n"
"}")

        self.horizontalLayout.addWidget(self.spider_gap_label)

        self.spider_gap_input_line = QLineEdit(self.widget)
        self.spider_gap_input_line.setObjectName(u"spider_gap_input_line")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.spider_gap_input_line.sizePolicy().hasHeightForWidth())
        self.spider_gap_input_line.setSizePolicy(sizePolicy2)
        self.spider_gap_input_line.setFont(font)

        self.horizontalLayout.addWidget(self.spider_gap_input_line)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.starts_spiders_num_label = QLabel(self.widget)
        self.starts_spiders_num_label.setObjectName(u"starts_spiders_num_label")
        sizePolicy1.setHeightForWidth(self.starts_spiders_num_label.sizePolicy().hasHeightForWidth())
        self.starts_spiders_num_label.setSizePolicy(sizePolicy1)
        self.starts_spiders_num_label.setStyleSheet(u"QLabel{\n"
"  font-family: Inter,sans-serif;\n"
"  font-size: 50px;\n"
"  align-items: center;\n"
"  border: 2px solid #111;\n"
"  border-radius: 8px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.starts_spiders_num_label)

        self.start_spiders_num_input_line = QLineEdit(self.widget)
        self.start_spiders_num_input_line.setObjectName(u"start_spiders_num_input_line")
        sizePolicy1.setHeightForWidth(self.start_spiders_num_input_line.sizePolicy().hasHeightForWidth())
        self.start_spiders_num_input_line.setSizePolicy(sizePolicy1)
        self.start_spiders_num_input_line.setFont(font)

        self.horizontalLayout_4.addWidget(self.start_spiders_num_input_line)


        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.starts_apples_num_label = QLabel(self.widget)
        self.starts_apples_num_label.setObjectName(u"starts_apples_num_label")
        sizePolicy1.setHeightForWidth(self.starts_apples_num_label.sizePolicy().hasHeightForWidth())
        self.starts_apples_num_label.setSizePolicy(sizePolicy1)
        self.starts_apples_num_label.setStyleSheet(u"QLabel{\n"
"  font-family: Inter,sans-serif;\n"
"  font-size: 50px;\n"
"  align-items: center;\n"
"  border: 2px solid #111;\n"
"  border-radius: 8px;\n"
"}")

        self.horizontalLayout_5.addWidget(self.starts_apples_num_label)

        self.start_apples_num_input_line = QLineEdit(self.widget)
        self.start_apples_num_input_line.setObjectName(u"start_apples_num_input_line")
        sizePolicy1.setHeightForWidth(self.start_apples_num_input_line.sizePolicy().hasHeightForWidth())
        self.start_apples_num_input_line.setSizePolicy(sizePolicy1)
        self.start_apples_num_input_line.setFont(font)

        self.horizontalLayout_5.addWidget(self.start_apples_num_input_line)


        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.error_label_system_settings = QLabel(self.widget)
        self.error_label_system_settings.setObjectName(u"label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.error_label_system_settings.sizePolicy().hasHeightForWidth())
        self.error_label_system_settings.setSizePolicy(sizePolicy3)

        self.verticalLayout_2.addWidget(self.error_label_system_settings)


        self.verticalLayout.addWidget(self.widget)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.return_button_system_settings = QPushButton(self.centralwidget)
        self.return_button_system_settings.setObjectName(u"return_button_system_settings")
        self.return_button_system_settings.setMaximumSize(QSize(16777215, 40))
        self.return_button_system_settings.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_6.addWidget(self.return_button_system_settings)

        self.submit_editing_system_settings = QPushButton(self.centralwidget)
        self.submit_editing_system_settings.setObjectName(u"submit_editing_system_settings")
        self.submit_editing_system_settings.setMinimumSize(QSize(0, 40))
        self.submit_editing_system_settings.setMaximumSize(QSize(16777215, 40))
        self.submit_editing_system_settings.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_6.addWidget(self.submit_editing_system_settings)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        SystemSettingsWindow.setCentralWidget(self.centralwidget)

        self.retranslateSystemSettingsUi(SystemSettingsWindow)

        QMetaObject.connectSlotsByName(SystemSettingsWindow)
    # setupUi

    def retranslateSystemSettingsUi(self, SystemSettingsWindow):
        SystemSettingsWindow.setWindowTitle(QCoreApplication.translate("SystemSettingsWindow", u"MainWindow", None))
        self.start_ants_num_label.setText(QCoreApplication.translate("SystemSettingsWindow", u"<html><head/><body><p>Start Number of Ants</p></body></html>", None))
        self.label_apple_gap.setText(QCoreApplication.translate("SystemSettingsWindow", u"Time Gap Between Apple Spawns", None))
        self.spider_gap_label.setText(QCoreApplication.translate("SystemSettingsWindow", u"<html><head/><body><p>Gap Between Spider Spawns</p></body></html>", None))
        self.starts_spiders_num_label.setText(QCoreApplication.translate("SystemSettingsWindow", u"<html><head/><body><p>Start Number of Spiders</p></body></html>", None))
        self.starts_apples_num_label.setText(QCoreApplication.translate("SystemSettingsWindow", u"Start Number of Apples", None))
        self.error_label_system_settings.setText(QCoreApplication.translate("SystemSettingsWindow", u"<html><head/><body><p><span style=\" font-size:14pt; color:#aa0000;\">Incorrect data format</span></p></body></html>", None))
        self.return_button_system_settings.setText(QCoreApplication.translate("SystemSettingsWindow", u"Return", None))
        self.submit_editing_system_settings.setText(QCoreApplication.translate("SystemSettingsWindow", u"Submit Editing", None))
    # retranslateUi

