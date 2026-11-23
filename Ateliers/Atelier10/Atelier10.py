import random
from maya import cmds
import maya.OpenMayaUI as omui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QGridLayout,
    QGroupBox,
    QSpinBox,
    QLabel,
    QVBoxLayout,
    QWidget,
)
from shiboken6 import wrapInstance
 
def maya_main_window():
    pointer = omui.MQtUtil.mainWindow()
    return wrapInstance(int(pointer), QWidget)
 
class Cactus(QWidget):

    def __init__(self):
        super().__init__(maya_main_window())
        self.setWindowFlags(Qt.Window)

        # Crée un array pour les cactus instances (vide parce qu'on l'utilise seuelement dans update_cactus())
        self.cactus_instances = []
        self.build_ui()
 
    def build_ui(self):
        self.setWindowTitle("Cactus Tool")
        self.setMinimumWidth(300)
        self.layout = QVBoxLayout(self)
        self.create_spinbox()
 
    def create_spinbox(self):

        cactus_group = QGroupBox("Plantation")
        cactus_layout = QGridLayout(cactus_group)

        self.cactus = QSpinBox()
        self.cactus.setRange(1, 250)
        self.cactus.setValue(1)

        cactus_layout.addWidget(QLabel("Cactus :"))
        cactus_layout.addWidget(self.cactus)

        self.layout.addWidget(cactus_group)

        # Déclenche la fonciton update_cactus dans la valeur du QSpinBox est modifiée
        self.cactus.valueChanged.connect(self.update_cactus)

    def update_cactus(self):

        # Prend la sélection de maya pour créer les nouveaux cactus
        selection = cmds.ls(selection=True, transforms=True)

        # La valeur de new_plantation est celle du QSpinBox -1 parce qu'on veut créer des nouveaux cactus et le QSpinBox compte le cactus original
        new_plantation = int(self.cactus.value() - 1)

        # Supprime les cactus de trop (si la valeur de cactus_instances (nouveaux cactus) est plus grand que celle de new_plantation (la valeur du QSpinBox -1))
        while len(self.cactus_instances) > new_plantation:
            # Transforme un objet aléatoire parmi les nouveaux cactus en "remove_cactus" et supprime cet objet
            remove_cactus = self.cactus_instances.pop(random.randrange(len(self.cactus_instances)))
            if cmds.objExists(remove_cactus):
                cmds.delete(remove_cactus)

        # Si rien n'est sélectionné, on arrête la fonction
        if not selection:
            return

        # On dit que la sélection est 
        original_cactus = selection[0]

        # Ajoute un nouveau cactus si le nombre de cactus demandé par le QSpinBox est plus petit que le nombre de cactus existant
        while len(self.cactus_instances) < new_plantation:

                # Crée l'instance new-cactus et lui donne le nom du cactus original + un numéro.
                new_cactus = cmds.instance(original_cactus, name=f"{original_cactus}_#")[0]

                # Donne dans valerus random en translation au nouveau cactus
                cmds.setAttr(f"{new_cactus}.translate", random.uniform(-10.0, 10.0), random.uniform(0.0, 0.0), random.uniform(-10.0, 10.0), type="double3")

                # Update le array de cactus instances
                self.cactus_instances.append(new_cactus)

                # Re-sélectionne l'objet original parce maya sélectionne automatiquement la dernière instance créée
                cmds.select(selection, replace=True)

def show_cactus():
    cactus_window = Cactus()
    cactus_window.show()
 
show_cactus()   