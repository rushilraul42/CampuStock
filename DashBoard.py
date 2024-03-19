import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import subprocess

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Dashboard")

        self.rent_button = QPushButton("Rent")
        self.buy_button = QPushButton("Buy")
        self.printout_button = QPushButton("Printout")

        self.rent_button.clicked.connect(self.open_rent_list)
        self.buy_button.clicked.connect(self.open_items_list)
        self.printout_button.clicked.connect(self.open_print_page)

        layout = QVBoxLayout()
        layout.addWidget(self.rent_button)
        layout.addWidget(self.buy_button)
        layout.addWidget(self.printout_button)

        self.setLayout(layout)

    def open_rent_list(self):
        subprocess.Popen(['python', 'RentList.py'])

    def open_items_list(self):
        subprocess.Popen(['python', 'ItemsList.py'])

    def open_print_page(self):
        subprocess.Popen(['python', 'Printout.py'])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dashboard = Dashboard()
    dashboard.show()
    sys.exit(app.exec_())
