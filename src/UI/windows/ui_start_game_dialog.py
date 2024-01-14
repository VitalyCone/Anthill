# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'game_start_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_GameStartDialog(object):
    def setupUi(self, GameStartDialog):
        if not GameStartDialog.objectName():
            GameStartDialog.setObjectName(u"GameStartDialog")
        GameStartDialog.resize(400, 300)
        GameStartDialog.setMinimumSize(QSize(400, 300))
        GameStartDialog.setMaximumSize(QSize(400, 300))
        self.verticalLayout_2 = QVBoxLayout(GameStartDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(GameStartDialog)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(u"QLabel{\n"
"  font-family: Inter,sans-serif;\n"
"  font-size: 24px;\n"
"  align-items: center;\n"
"  border: 2px solid #111;\n"
"  border-radius: 8px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.label)

        self.ants_num_input = QLineEdit(GameStartDialog)
        self.ants_num_input.setObjectName(u"ants_num_input")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ants_num_input.sizePolicy().hasHeightForWidth())
        self.ants_num_input.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.ants_num_input)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(GameStartDialog)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet(u"QLabel{\n"
"  font-family: Inter,sans-serif;\n"
"  font-size: 24px;\n"
"  align-items: center;\n"
"  border: 2px solid #111;\n"
"  border-radius: 8px;\n"
"}")

        self.horizontalLayout.addWidget(self.label_2)

        self.spiders_num_input = QLineEdit(GameStartDialog)
        self.spiders_num_input.setObjectName(u"spiders_num_input")
        sizePolicy1.setHeightForWidth(self.spiders_num_input.sizePolicy().hasHeightForWidth())
        self.spiders_num_input.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.spiders_num_input)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(GameStartDialog)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet(u"QLabel{\n"
"  font-family: Inter,sans-serif;\n"
"  font-size: 24px;\n"
"  align-items: center;\n"
"  border: 2px solid #111;\n"
"  border-radius: 8px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.apples_num_input = QLineEdit(GameStartDialog)
        self.apples_num_input.setObjectName(u"apples_num_input")
        sizePolicy1.setHeightForWidth(self.apples_num_input.sizePolicy().hasHeightForWidth())
        self.apples_num_input.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.apples_num_input)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.buttonBox = QDialogButtonBox(GameStartDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStyleSheet(u"QPushButton {\n"
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
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(GameStartDialog)
        self.buttonBox.accepted.connect(GameStartDialog.accept)
        self.buttonBox.rejected.connect(GameStartDialog.reject)

        QMetaObject.connectSlotsByName(GameStartDialog)
    # setupUi

    def retranslateUi(self, GameStartDialog):
        GameStartDialog.setWindowTitle(QCoreApplication.translate("GameStartDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("GameStartDialog", u"Starting number of ants", None))
        self.label_2.setText(QCoreApplication.translate("GameStartDialog", u"Starting number of spiders", None))
        self.label_3.setText(QCoreApplication.translate("GameStartDialog", u"Starting number of apples", None))
    # retranslateUi

