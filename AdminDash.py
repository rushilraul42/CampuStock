import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from Inventory import InventoryWindow  # Import InventoryWindow from Inventory.py
from Docs import DocsWindow  # Import DocsWindow from Docs.py
from StudentData import StudentDataWindow  # Import StudentDataWindow from StudentData.py
from Purchase import PurchaseWindow  # Import PurchaseWindow from Purchase.py

class AdminDashboard(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        inventory_button = QPushButton("Inventory")
        inventory_button.clicked.connect(self.open_inventory)
        self.layout.addWidget(inventory_button)

        docs_button = QPushButton("Documents")
        docs_button.clicked.connect(self.open_docs)
        self.layout.addWidget(docs_button)

        student_data_button = QPushButton("Student Data")
        student_data_button.clicked.connect(self.open_student_data)
        self.layout.addWidget(student_data_button)

        purchases_button = QPushButton("Purchases")
        purchases_button.clicked.connect(self.open_purchases)
        self.layout.addWidget(purchases_button)

        self.setLayout(self.layout)

        self.setWindowTitle("Admin Dashboard")
        self.setGeometry(100, 100, 300, 200)

    def open_inventory(self):
        inventory_window = InventoryWindow()
        inventory_window.show()

    def open_docs(self):
        docs_window = DocsWindow()
        docs_window.show()

    def open_student_data(self):
        student_data_window = StudentDataWindow()
        student_data_window.show()

    def open_purchases(self):
        purchases_window = PurchaseWindow()
        purchases_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    admin_dashboard = AdminDashboard()
    admin_dashboard.show()
    sys.exit(app.exec_())
