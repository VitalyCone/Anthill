# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'system_settings.ui'
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

class Ui_SystemSettingsWindow(object):
    def setupSystemSettingsUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.return_button_system_settings = QPushButton(self.centralwidget)
        self.return_button_system_settings.setObjectName(u"return_button_agent_settings")
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

        self.gridLayout.addWidget(self.return_button_system_settings, 5, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.start_ants_num_label = QLabel(self.centralwidget)
        self.start_ants_num_label.setObjectName(u"start_ants_num_label")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_ants_num_label.sizePolicy().hasHeightForWidth())
        self.start_ants_num_label.setSizePolicy(sizePolicy)
        self.start_ants_num_label.setStyleSheet(u"QLabel{\n"
"  font-family: Inter,sans-serif;\n"
"  font-size: 24px;\n"
"  align-items: center;\n"
"  border: 2px solid #111;\n"
"  border-radius: 8px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.start_ants_num_label)

        self.start_ants_num_input_line = QLineEdit(self.centralwidget)
        self.start_ants_num_input_line.setObjectName(u"start_ants_num_input_line")
        sizePolicy.setHeightForWidth(self.start_ants_num_input_line.sizePolicy().hasHeightForWidth())
        self.start_ants_num_input_line.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.start_ants_num_input_line)

        self.start_ants_num_submit_button = QPushButton(self.centralwidget)
        self.start_ants_num_submit_button.setObjectName(u"start_ants_num_submit_button")
        sizePolicy.setHeightForWidth(self.start_ants_num_submit_button.sizePolicy().hasHeightForWidth())
        self.start_ants_num_submit_button.setSizePolicy(sizePolicy)
        self.start_ants_num_submit_button.setMaximumSize(QSize(16777215, 40))
        self.start_ants_num_submit_button.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_3.addWidget(self.start_ants_num_submit_button)

        self.current_start_ants_num = QLabel(self.centralwidget)
        self.current_start_ants_num.setObjectName(u"current_start_ants_num")
        sizePolicy.setHeightForWidth(self.current_start_ants_num.sizePolicy().hasHeightForWidth())
        self.current_start_ants_num.setSizePolicy(sizePolicy)
        self.current_start_ants_num.setStyleSheet(u"QLabel{\n"
"  font-family: Inter,sans-serif;\n"
"  font-size: 24px;\n"
"  align-items: center;\n"
"  border: 2px solid #111;\n"
"  border-radius: 8px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.current_start_ants_num)


        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_apple_gap = QLabel(self.centralwidget)
        self.label_apple_gap.setObjectName(u"label_apple_gap")
        sizePolicy.setHeightForWidth(self.label_apple_gap.sizePolicy().hasHeightForWidth())
        self.label_apple_gap.setSizePolicy(sizePolicy)
        self.label_apple_gap.setStyleSheet(u"QLabel{\n"
"  font-family: Inter,sans-serif;\n"
"  font-size: 24px;\n"
"  align-items: center;\n"
"  border: 2px solid #111;\n"
"  border-radius: 8px;\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.label_apple_gap)

        self.apples_gap_input_line = QLineEdit(self.centralwidget)
        self.apples_gap_input_line.setObjectName(u"apples_gap_input_line")
        sizePolicy.setHeightForWidth(self.apples_gap_input_line.sizePolicy().hasHeightForWidth())
        self.apples_gap_input_line.setSizePolicy(sizePolicy)
        self.apples_gap_input_line.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.apples_gap_input_line)

        self.apples_gap_submit_button = QPushButton(self.centralwidget)
        self.apples_gap_submit_button.setObjectName(u"apples_gap_submit_button")
        sizePolicy.setHeightForWidth(self.apples_gap_submit_button.sizePolicy().hasHeightForWidth())
        self.apples_gap_submit_button.setSizePolicy(sizePolicy)
        self.apples_gap_submit_button.setMaximumSize(QSize(16777215, 40))
        self.apples_gap_submit_button.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_2.addWidget(self.apples_gap_submit_button)

        self.current_apples_gap = QLabel(self.centralwidget)
        self.current_apples_gap.setObjectName(u"current_apples_gap")
        sizePolicy.setHeightForWidth(self.current_apples_gap.sizePolicy().hasHeightForWidth())
        self.current_apples_gap.setSizePolicy(sizePolicy)
        self.current_apples_gap.setLayoutDirection(Qt.LeftToRight)
        self.current_apples_gap.setStyleSheet(u"QLabel{\n"
"  font-family: Inter,sans-serif;\n"
"  font-size: 24px;\n"
"  align-items: center;\n"
"  border: 2px solid #111;\n"
"  border-radius: 8px;\n"
"}")
        self.current_apples_gap.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_2.addWidget(self.current_apples_gap)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.spider_gap_label = QLabel(self.centralwidget)
        self.spider_gap_label.setObjectName(u"spider_gap_label")
        sizePolicy.setHeightForWidth(self.spider_gap_label.sizePolicy().hasHeightForWidth())
        self.spider_gap_label.setSizePolicy(sizePolicy)
        self.spider_gap_label.setStyleSheet(u"QLabel{\n"
"  font-family: Inter,sans-serif;\n"
"  font-size: 24px;\n"
"  align-items: center;\n"
"  border: 2px solid #111;\n"
"  border-radius: 8px;\n"
"}")

        self.horizontalLayout.addWidget(self.spider_gap_label)

        self.spider_gap_input_line = QLineEdit(self.centralwidget)
        self.spider_gap_input_line.setObjectName(u"spider_gap_input_line")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.spider_gap_input_line.sizePolicy().hasHeightForWidth())
        self.spider_gap_input_line.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.spider_gap_input_line)

        self.spiders_gap_submit_button = QPushButton(self.centralwidget)
        self.spiders_gap_submit_button.setObjectName(u"spiders_gap_submit_button")
        sizePolicy.setHeightForWidth(self.spiders_gap_submit_button.sizePolicy().hasHeightForWidth())
        self.spiders_gap_submit_button.setSizePolicy(sizePolicy)
        self.spiders_gap_submit_button.setMaximumSize(QSize(16777215, 40))
        self.spiders_gap_submit_button.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout.addWidget(self.spiders_gap_submit_button)

        self.current_spiders_gap = QLabel(self.centralwidget)
        self.current_spiders_gap.setObjectName(u"current_spiders_gap")
        sizePolicy.setHeightForWidth(self.current_spiders_gap.sizePolicy().hasHeightForWidth())
        self.current_spiders_gap.setSizePolicy(sizePolicy)
        self.current_spiders_gap.setStyleSheet(u"QLabel{\n"
"  font-family: Inter,sans-serif;\n"
"  font-size: 24px;\n"
"  align-items: center;\n"
"  border: 2px solid #111;\n"
"  border-radius: 8px;\n"
"}")

        self.horizontalLayout.addWidget(self.current_spiders_gap)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.starts_spiders_num_label = QLabel(self.centralwidget)
        self.starts_spiders_num_label.setObjectName(u"starts_spiders_num_label")
        sizePolicy.setHeightForWidth(self.starts_spiders_num_label.sizePolicy().hasHeightForWidth())
        self.starts_spiders_num_label.setSizePolicy(sizePolicy)
        self.starts_spiders_num_label.setStyleSheet(u"QLabel{\n"
"  font-family: Inter,sans-serif;\n"
"  font-size: 24px;\n"
"  align-items: center;\n"
"  border: 2px solid #111;\n"
"  border-radius: 8px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.starts_spiders_num_label)

        self.start_spiders_num_input_line = QLineEdit(self.centralwidget)
        self.start_spiders_num_input_line.setObjectName(u"start_spiders_num_input_line")
        sizePolicy.setHeightForWidth(self.start_spiders_num_input_line.sizePolicy().hasHeightForWidth())
        self.start_spiders_num_input_line.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.start_spiders_num_input_line)

        self.start_spiders_num_submit_button = QPushButton(self.centralwidget)
        self.start_spiders_num_submit_button.setObjectName(u"start_spiders_num_submit_button")
        sizePolicy.setHeightForWidth(self.start_spiders_num_submit_button.sizePolicy().hasHeightForWidth())
        self.start_spiders_num_submit_button.setSizePolicy(sizePolicy)
        self.start_spiders_num_submit_button.setMaximumSize(QSize(16777215, 40))
        self.start_spiders_num_submit_button.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_4.addWidget(self.start_spiders_num_submit_button)

        self.current_start_spiders_num = QLabel(self.centralwidget)
        self.current_start_spiders_num.setObjectName(u"current_start_spiders_num")
        sizePolicy.setHeightForWidth(self.current_start_spiders_num.sizePolicy().hasHeightForWidth())
        self.current_start_spiders_num.setSizePolicy(sizePolicy)
        self.current_start_spiders_num.setStyleSheet(u"QLabel{\n"
"  font-family: Inter,sans-serif;\n"
"  font-size: 24px;\n"
"  align-items: center;\n"
"  border: 2px solid #111;\n"
"  border-radius: 8px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.current_start_spiders_num)


        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.starts_apples_num_label = QLabel(self.centralwidget)
        self.starts_apples_num_label.setObjectName(u"starts_apples_num_label")
        sizePolicy.setHeightForWidth(self.starts_apples_num_label.sizePolicy().hasHeightForWidth())
        self.starts_apples_num_label.setSizePolicy(sizePolicy)
        self.starts_apples_num_label.setStyleSheet(u"QLabel{\n"
"  font-family: Inter,sans-serif;\n"
"  font-size: 24px;\n"
"  align-items: center;\n"
"  border: 2px solid #111;\n"
"  border-radius: 8px;\n"
"}")

        self.horizontalLayout_5.addWidget(self.starts_apples_num_label)

        self.start_apples_num_input_line = QLineEdit(self.centralwidget)
        self.start_apples_num_input_line.setObjectName(u"start_apples_num_input_line")
        sizePolicy.setHeightForWidth(self.start_apples_num_input_line.sizePolicy().hasHeightForWidth())
        self.start_apples_num_input_line.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.start_apples_num_input_line)

        self.start_apples_num_submit_button = QPushButton(self.centralwidget)
        self.start_apples_num_submit_button.setObjectName(u"start_apples_num_submit_button")
        sizePolicy.setHeightForWidth(self.start_apples_num_submit_button.sizePolicy().hasHeightForWidth())
        self.start_apples_num_submit_button.setSizePolicy(sizePolicy)
        self.start_apples_num_submit_button.setMaximumSize(QSize(16777215, 40))
        self.start_apples_num_submit_button.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_5.addWidget(self.start_apples_num_submit_button)

        self.current_start_apples_num = QLabel(self.centralwidget)
        self.current_start_apples_num.setObjectName(u"current_start_apples_num")
        sizePolicy.setHeightForWidth(self.current_start_apples_num.sizePolicy().hasHeightForWidth())
        self.current_start_apples_num.setSizePolicy(sizePolicy)
        self.current_start_apples_num.setStyleSheet(u"QLabel{\n"
"  font-family: Inter,sans-serif;\n"
"  font-size: 24px;\n"
"  align-items: center;\n"
"  border: 2px solid #111;\n"
"  border-radius: 8px;\n"
"}")

        self.horizontalLayout_5.addWidget(self.current_start_apples_num)


        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateSystemSettingsUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateSystemSettingsUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.return_button_system_settings.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.start_ants_num_label.setText(QCoreApplication.translate("MainWindow", u"Start Number of Ants <\u041f\u043e\u043a\u0430 \u043d\u0435 \u0440\u0430\u0431\u043e\u0442\u0430\u0435\u0442>", None))
        self.start_ants_num_submit_button.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.current_start_ants_num.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_apple_gap.setText(QCoreApplication.translate("MainWindow", u"Time Gap Between Apple Spawns", None))
        self.apples_gap_submit_button.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.current_apples_gap.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.spider_gap_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Gap Between Spider Spawns &lt;\u041f\u043e\u043a\u0430 \u043d\u0435 \u0440\u0430\u0431\u043e\u0442\u0430\u0435\u0442&gt;</p></body></html>", None))
        self.spiders_gap_submit_button.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.current_spiders_gap.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.starts_spiders_num_label.setText(QCoreApplication.translate("MainWindow", u"Start Number of Spiders <\u041f\u043e\u043a\u0430 \u043d\u0435 \u0440\u0430\u0431\u043e\u0442\u0430\u0435\u0442>", None))
        self.start_spiders_num_submit_button.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.current_start_spiders_num.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.starts_apples_num_label.setText(QCoreApplication.translate("MainWindow", u"Start Number of Apples <\u041f\u043e\u043a\u0430 \u043d\u0435 \u0440\u0430\u0431\u043e\u0442\u0430\u0435\u0442>", None))
        self.start_apples_num_submit_button.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.current_start_apples_num.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

