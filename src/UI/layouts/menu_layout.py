from PyQt6.QtWidgets import QVBoxLayout, QBoxLayout


class MenuLayout(QVBoxLayout):

    def __init__(self, direction: 'QBoxLayout.Direction'):
        super().__init__(direction)
        self.init_UI()

    def init_UI(self):
        pass
