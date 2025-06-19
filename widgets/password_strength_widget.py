from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
)
from modules import password_strength

class PasswordStrengthWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Enter password here")

        self.check_button = QPushButton("Evaluate Strength")
        self.result_area = QTextEdit()
        self.result_area.setReadOnly(True)

        layout.addWidget(QLabel("Password Strength Evaluator"))
        layout.addWidget(self.input_field)
        layout.addWidget(self.check_button)
        layout.addWidget(QLabel("Results:"))
        layout.addWidget(self.result_area)

        self.setLayout(layout)

        self.check_button.clicked.connect(self.evaluate_strength)

    def evaluate_strength(self):
        password = self.input_field.text()
        result = password_strength.evaluate_password_strength(password)

        output = f"Score: {result['score']} / 5\n\n"
        output += "Feedback:\n"
        for msg in result["messages"]:
            output += f"- {msg}\n"

        self.result_area.setText(output)
