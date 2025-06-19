# ui/style.py

def neon_style():
    return """
        QWidget {
            background-color: #0d0d0d;
            color: #e0e0e0;
            font-family: 'Segoe UI';
            font-size: 14px;
        }

        QListWidget {
            background-color: #111;
            border: none;
            color: #00e6e6;
        }

        QListWidget::item:selected {
            background-color: #00ffff;
            color: black;
            font-weight: bold;
        }

        QPushButton {
            background-color: #1a1a1a;
            color: #00ffcc;
            border: 1px solid #00ffcc;
            border-radius: 8px;
            padding: 6px 12px;
        }

        QPushButton:hover {
            background-color: #00ffcc;
            color: black;
        }

        QLineEdit, QTextEdit {
            background-color: #1c1c1c;
            color: #ffffff;
            border: 1px solid #00ccff;
            border-radius: 6px;
            padding: 4px;
        }

        QLabel {
            color: #ffffff;
            font-weight: bold;
        }

        QScrollBar:vertical {
            background: #0d0d0d;
            width: 12px;
            margin: 0px 0px 0px 0px;
        }

        QScrollBar::handle:vertical {
            background: #00ccff;
            min-height: 20px;
            border-radius: 6px;
        }

        QScrollBar::add-line:vertical,
        QScrollBar::sub-line:vertical {
            background: none;
        }
    """
