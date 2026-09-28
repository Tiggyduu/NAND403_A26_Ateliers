from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

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

        # add QPushButton

    def on_click(self):
        print("on click called")
        # add QMesageBox

def main():
    global widget
    try:
        widget.close()
    except Exception:
        pass
    widget = MessageBoard()
    widget.show()
 
main()