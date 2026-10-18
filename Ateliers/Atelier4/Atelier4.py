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
# J'ai ajouté quelques librairies pour que le UI ressemblent à l'exemple.

class RandomGenerator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Atelier 4")
        self.setMinimumWidth(400)
        self.build_ui()
    
    def build_ui(self):
        layout = QVBoxLayout(self)

        # Number of objects
        number_of_objects = QHBoxLayout() # Crée la boîte 
        number_of_objects.addWidget(QLabel("Number of objects")) # Ajoute un label devant
        self.input_number_of_objects = QLineEdit("1") # Met la valeur par défaut à 1
        self.input_number_of_objects.setFixedWidth(247) # Largeur de la boîte (247 pour qu'elle soit la même taille que les autres lignes)
        number_of_objects.addWidget(self.input_number_of_objects) # Ajoute la boîte
        layout.addLayout(number_of_objects) # Ajoute la boîte à la fenêtre

        # Position X
        position_x = QHBoxLayout() # Crée la boîte
        position_x.addWidget(QLabel("Position X (Min / Max)")) # Ajoute un label devant
        self.x_minimum = QLineEdit("0") # Met la valeur par défaut à 0
        self.x_maximum = QLineEdit("0")
        self.x_minimum.setFixedWidth(120) # Lageur de la boîte
        self.x_maximum.setFixedWidth(120)
        position_x.addWidget(self.x_minimum) # Ajoute la boîte
        position_x.addWidget(self.x_maximum)
        layout.addLayout(position_x) # Ajoute la boîte à la fenêtre

        # Position Y
        # C'est la même chose que pour X
        position_y = QHBoxLayout()
        position_y.addWidget(QLabel("Position Y (Min / Max)"))
        self.y_minimum = QLineEdit("0")
        self.y_maximum = QLineEdit("0")
        self.y_minimum.setFixedWidth(120)
        self.y_maximum.setFixedWidth(120)
        position_y.addWidget(self.y_minimum)
        position_y.addWidget(self.y_maximum)
        layout.addLayout(position_y)

        # Position Z
        # Encore pareil
        position_z = QHBoxLayout()
        position_z.addWidget(QLabel("Position Z (Min / Max)"))
        self.z_minimum = QLineEdit("0")
        self.z_maximum = QLineEdit("0")
        self.z_minimum.setFixedWidth(120)
        self.z_maximum.setFixedWidth(120)
        position_z.addWidget(self.z_minimum)
        position_z.addWidget(self.z_maximum)
        layout.addLayout(position_z)

        # Le paramètre de scale
        # Similaire à la position X,Y,Z
        scale = QHBoxLayout() # Crée une boîte pour entrer la valeur de scale
        scale.addWidget(QLabel("Scale (Min / Max)"))
        # Les valeurs par défaut sont de 1 pour que l'objet soit de taille normale
        self.scale_minimum = QLineEdit("1")
        self.scale_maximum = QLineEdit("1")
        self.scale_minimum.setFixedWidth(120)
        self.scale_maximum.setFixedWidth(120)
        scale.addWidget(self.scale_minimum)
        scale.addWidget(self.scale_maximum)
        layout.addLayout(scale)

        # Bouton "create"
        self.create_button = QPushButton("Create")
        self.create_button.clicked.connect(self.create_object)
        layout.addWidget(self.create_button)

    def create_object(self):

        try:

            number = int(self.input_number_of_objects.text()) # Crée une variable int avec le nombre d'objets
            # Crée un float avec la valeur min/max pour les X,Y,Z
            minimum_x = float(self.x_minimum.text())
            maximum_x = float(self.x_maximum.text())
            minimum_y = float(self.y_minimum.text())
            maximum_y = float(self.y_maximum.text())
            minimum_z = float(self.z_minimum.text())
            maximum_z = float(self.z_maximum.text())
            # Crée aussi un float mais pour le scale
            minimum_scale = float(self.scale_minimum.text())
            maximum_scale = float(self.scale_maximum.text())

        except ValueError:

            number = 1 # Met à 1 si le nombre n'est pas valide
            # Met les valeurs X,Y,Z à 0 si elles ne sont pas valides
            minimum_x = 0
            maximum_x = 0
            minimum_y = 0
            maximum_y = 0
            minimum_z = 0
            maximum_z = 0
            # Met les valeur à 1 si elles ne sont pas valides
            minimum_scale = 1
            maximum_scale = 1

        # Permet le Ctrl Z
        cmds.undoInfo(openChunk=True)

        try:

            for _ in range(number):

                forme = random.choice(["cube", "cylindre", "sphere"])

                if forme == "cube":

                    objet = cmds.polyCube()[0]

                elif forme == "cylindre":

                    objet = cmds.polyCylinder()[0]

                else:

                    objet = cmds.polySphere()[0]

                random_value = random.uniform(-10, 10)
                cmds.move(random_value, random_value, random_value, objet)

                # Position random
                position_x = random.uniform(minimum_x, maximum_x)
                position_y = random.uniform(minimum_y, maximum_y)
                position_z = random.uniform(minimum_z, maximum_z)
                cmds.move(position_x, position_y, position_z, objet)

                # Random scale pour les objets
                scale = random.uniform(minimum_scale, maximum_scale)
                # Met la même valeur pour les X,Y,Z
                cmds.scale(scale, scale, scale, objet)

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