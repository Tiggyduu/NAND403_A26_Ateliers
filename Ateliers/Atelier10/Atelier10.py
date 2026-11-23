import random
from maya import cmds
import maya.OpenMayaUI as omui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QFormLayout,
    QSpinBox,
    QDoubleSpinBox,
    QPushButton,
    QMessageBox
)
from shiboken6 import wrapInstance
 
def maya_main_window():
    pointer = omui.MQtUtil.mainWindow()
    return wrapInstance(int(pointer), QWidget)

class Scatter(QWidget):

    def __init__(self):
        super().__init__(maya_main_window())
        self.setWindowFlags(Qt.Window)
        self.setWindowTitle("Scatter")
        self.setMinimumWidth(250)
        self.source = None
        self.group = None
        self.build_ui()

    def build_ui(self):
        layout = QVBoxLayout(self)
        form = QFormLayout()
        layout.addLayout(form)

        self.count_spin = QSpinBox()
        self.count_spin.setRange(1, 100)
        self.count_spin.setValue(10)
        self.count_spin.valueChanged.connect(self.on_value_changed)
        form.addRow("Copies", self.count_spin)

        self.radius_spin = QDoubleSpinBox()
        self.radius_spin.setRange(1.0, 50.0)
        self.radius_spin.setValue(10.0)
        self.radius_spin.valueChanged.connect(self.on_value_changed)
        form.addRow("Radius", self.radius_spin)

        self.seed_spin = QSpinBox()
        self.seed_spin.setRange(0, 9999)
        self.seed_spin.valueChanged.connect(self.on_value_changed)
        form.addRow("Seed", self.seed_spin)

        scatter_button = QPushButton("Scatter")
        scatter_button.clicked.connect(self.scatter)
        layout.addWidget(scatter_button)

    def on_value_changed(self):
        if self.source and cmds.objExists(self.source):
            if self.group and cmds.objExists(self.group):
                cmds.delete(self.group)
            cmds.select(self.source, replace=True)
            self.scatter()

    def scatter(self):
        selection = cmds.ls(selection=True, transforms=True)
        if not selection:
            QMessageBox.warning(self, "Scatter", "Select an object first.")
            return
        source = selection[0]
        self.source = source

        cmds.undoInfo(openChunk=True)
        try:
            random.seed(self.seed_spin.value())
            radius = self.radius_spin.value()
            group = cmds.group(empty=True, name="scatter_grp")
            self.group = group
            for i in range(self.count_spin.value()):
                copy = cmds.duplicate(source)[0]
                copy = cmds.parent(copy, group)[0]
                x = random.uniform(-radius, radius)
                z = random.uniform(-radius, radius)
                cmds.move(x, 0, z, copy, relative=True)
        finally:
            cmds.undoInfo(closeChunk=True)


def show_tool():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = Scatter()
    tool_window.show()


show_tool()