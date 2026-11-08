from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QTextEdit, QPushButton, QMessageBox
 
class MessageBoard(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Message board") 
        self.create_ui()

    def create_ui(self):
        layout = QVBoxLayout(self)
        label = QLabel("Message board")
        layout.addWidget(label)

        self.text = QTextEdit()
        self.text.setPlaceholderText("Enter a message...")
        layout.addWidget(self.text)

        self.button = QPushButton("Show")
        layout.addWidget(self.button)
        self.button.clicked.connect(self.on_click)

    def on_click(self):
        print("on click called")

        message = self.text.toPlainText()

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