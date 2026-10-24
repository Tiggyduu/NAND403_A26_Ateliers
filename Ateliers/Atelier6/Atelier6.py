import random
from maya import cmds
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QLabel
)

class RandomGenerator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Atelier 4")
        self.setMinimumWidth(400)
        self.build_ui()
    
    def build_ui(self):
        layout = QVBoxLayout(self)

        # Longueur de la cloture (répétition)
        number_of_fence = QHBoxLayout()
        number_of_fence.addWidget(QLabel("Number of fence"))
        self.input_number_of_fence = QLineEdit("0")
        number_of_fence.addWidget(self.input_number_of_fence)
        layout.addLayout(number_of_fence)

        # Bouton "create"
        self.create_button = QPushButton("Create")
        self.create_button.clicked.connect(self.create_object)
        layout.addWidget(self.create_button)

    def create_object(self):

        # Permet le Ctrl Z
        cmds.undoInfo(openChunk=True)

        try:

            # Transforme le QLineEdit en int
            number_of_fence = int(self.input_number_of_fence.text())
            # Initialise le offset à 0
            offset_x = 0

            for fence in range(number_of_fence):

                # Crée le pole
                fence_pole = cmds.polyCube()[0]
                cmds.move(0 + offset_x, 6, 0, fence_pole)
                cmds.scale(1, 12, 1, fence_pole)

                # Crée la barre du bas
                bottom_bar = cmds.polyCube()[0]
                cmds.move(6.5 + offset_x, 3, 0, bottom_bar)
                cmds.scale(12, 1, 1, bottom_bar)

                # Cré la barre du haut
                top_bar = cmds.polyCube()[0]
                cmds.move(6.5 + offset_x, 9, 0, top_bar)
                cmds.scale(12, 1, 1, top_bar)

                # Ajoute un offset pour la prochaine cloture
                offset_x = offset_x + 13

        finally:

            cmds.undoInfo(closeChunk=True)


def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = RandomGenerator()
    tool_window.show()

main()