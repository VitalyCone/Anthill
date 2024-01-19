from PySide6.QtWidgets import QDialog, QDialogButtonBox

from src.Planner.Planner import Planner
from src.UI.windows.ui_start_game_dialog import Ui_GameStartDialog
from src.agents.AgentDispatcher import AgentDispatcher
from src.agents import AgentDispatcher
from src.scene.Scene import Scene


class StartGameDialog(QDialog, Ui_GameStartDialog):

    def __init__(self, dispatcher: AgentDispatcher, scene: Scene,
                 anthill_num: int, apples_num: int, spdr_num: int, ants_num: int, entities_settings: dict):
        super().__init__()
        self.show_model = False

        self.entities_settings = entities_settings

        self.planner = Planner(dispatcher, scene, anthill_num, apples_num, spdr_num, ants_num, self.entities_settings)

        self.setupUi(self)

        self.ants_num_input.setText(str(ants_num))
        self.spiders_num_input.setText(str(spdr_num))
        self.apples_num_input.setText(str(apples_num))

        self.show()
        self.exec()

    def reject(self):
        super().reject()
        self.close()

    def accept(self):
        super().accept()
        self.close()
        self.planner.set_start_nums(self.planner.anthill_num,
                                    int(self.apples_num_input.text()),
                                    int(self.spiders_num_input.text()),
                                    int(self.ants_num_input.text()))
        self.planner.start_system()
        self.show_model = True
