# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'simple_diagApdHuk.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QSizePolicy, QVBoxLayout, QWidget)

class Ui_SimpleDiag(object):
    def setupSimpleDiagUi(self, SimpleDiag):
        if not SimpleDiag.objectName():
            SimpleDiag.setObjectName(u"SimpleDiag")
        self.verticalLayout = QVBoxLayout(SimpleDiag)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.simpl_diag_label = QLabel(SimpleDiag)
        self.simpl_diag_label.setObjectName(u"simpl_diag_label")
        font = QFont()
        font.setPointSize(14)
        self.simpl_diag_label.setFont(font)

        self.verticalLayout.addWidget(self.simpl_diag_label)

        self.buttonBox = QDialogButtonBox(SimpleDiag)
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

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateSimpleDiagUi(SimpleDiag)
        self.buttonBox.accepted.connect(SimpleDiag.accept)
        self.buttonBox.rejected.connect(SimpleDiag.reject)

        QMetaObject.connectSlotsByName(SimpleDiag)
    # setupUi

    def retranslateSimpleDiagUi(self, SimpleDiag):
        SimpleDiag.setWindowTitle(QCoreApplication.translate("SimpleDiag", u"Dialog", None))
        self.simpl_diag_label.setText("")
    # retranslateUi

