from PySide6.QtWidgets import QDialog, QDialogButtonBox, QLabel, QVBoxLayout

from src.Planner.Planner import Planner
from src.UI.windows.ui_simple_dialog import Ui_SimpleDiag
from src.UI.windows.ui_start_game_dialog import Ui_GameStartDialog
from src.agents.AgentDispatcher import AgentDispatcher
from src.agents import AgentDispatcher
from src.scene.Scene import Scene
from src.utils.ontology_utils.ontology_utils import OntologyModel, import_ontology_model


class StartGameDialog(QDialog, Ui_GameStartDialog, Ui_SimpleDiag):

    def __init__(self, dispatcher: AgentDispatcher, scene: Scene,
                 anthill_num: int, apples_num: int, spdr_num: int, ants_num: int, entities_settings: dict):
        super().__init__()
        self.show_model = False
        self.use_onto_model = OntologyModel.ontology_model is not None
        self.entities_settings = entities_settings
        if not self.use_onto_model:

            self.planner = Planner(dispatcher, scene, anthill_num, apples_num, spdr_num, ants_num,
                                   self.entities_settings)

            self.setupUi(self)

            self.import_ontology_button_agent_settings.clicked.connect(self.import_ontology)

            self.ants_num_input.setText(str(ants_num))
            self.spiders_num_input.setText(str(spdr_num))
            self.apples_num_input.setText(str(apples_num))
        else:
            self.planner = Planner(dispatcher, scene, anthill_num, apples_num, spdr_num, ants_num,
                                   self.entities_settings)
            self.setupUi(self)
            label = QLabel()
            label.setText(
                u"<html><head/><body><p><span style=\" font-size:14pt;\">Start with imported ontology model?</span></p></body></html>")
            vbox = QVBoxLayout()
            vbox.addWidget(label)
            self.setLayout(vbox)

        self.show()
        self.exec()

    def import_ontology(self):
        import_ontology_model()
        self.use_onto_model = True
        self.accept()

    def reject(self):
        super().reject()
        self.close()

    def accept(self):
        super().accept()
        self.close()
        if self.use_onto_model:
            try:
                self.planner.set_start_nums(self.planner.anthill_num,
                                        int(self.apples_num_input.text()),
                                        int(self.spiders_num_input.text()),
                                        int(self.ants_num_input.text()))
            except Exception:
                pass
            self.planner.start_system_with_onto_model()
            self.use_onto_model = OntologyModel.ontology_model = None
            self.show_model = True
        else:
            self.planner.set_start_nums(self.planner.anthill_num,
                                        int(self.apples_num_input.text()),
                                        int(self.spiders_num_input.text()),
                                        int(self.ants_num_input.text()))
            self.planner.start_system()
            self.show_model = True
