from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QTextEdit, QPushButton, QMessageBox

# Les différentes naming convention
    
    ### snake case ###
    # this_is_snake_case

    ### camel case ###
    # thisIsCamelCase

    ### pascal case ###
    # ThisIsPascalCase

 
class MessageBoard(QWidget): # QWidget est la classe mère et MessageBoard hérite de ses composantes
    def __init__(self): # Constructeur
        super().__init__() # Constructeur du parent QWidget (super = superclass (classe supérieure))
        self.setWindowTitle("Message board") 
        self.create_ui()

    def create_ui(self):
        layout = QVBoxLayout(self)
        label = QLabel("Message board")
        layout.addWidget(label)

        # add QTextEdit
        self.text = QTextEdit()
        self.text.setPlaceholderText("Enter a message...")
        layout.addWidget(self.text)

        # add QPushButton
        self.button = QPushButton("Show")
        layout.addWidget(self.button)
        self.button.clicked.connect(self.on_click)

    def on_click(self):
        print("on click called")

        message = self.text.toPlainText()

        # add QMesageBox
        QMessageBox.warning(self, "Warning", message)

def main():
    global widget
    try:
        widget.close()
    except Exception:
        pass
    widget = MessageBoard()
    widget.show()
 
main()