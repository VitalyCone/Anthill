from PySide6.QtWidgets import QDialog, QDialogButtonBox

from src.UI.windows.ui_simple_dialog import Ui_SimpleDiag


class SimpleDiag(QDialog, Ui_SimpleDiag):

    def __init__(self, text):
        super().__init__()
        self.setupSimpleDiagUi(self)
        self.simpl_diag_label.setText(text)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.show()
        self.exec()

