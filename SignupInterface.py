import random
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout

# Function to calculate total cost
def calculate_total_cost(price, quantity):
    return price * quantity

class ItemListApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.items = [
            {"item": "Pen", "price": round(random.uniform(0.5, 2.0), 2)},
            {"item": "Pencil", "price": round(random.uniform(0.3, 1.5), 2)},
            {"item": "Scale", "price": round(random.uniform(1.0, 3.0), 2)},
            {"item": "Rounder", "price": round(random.uniform(1.5, 4.0), 2)},
            {"item": "Eraser", "price": round(random.uniform(0.2, 0.8), 2)},
            {"item": "Single Sided Sheets", "price": round(random.uniform(2.0, 5.0), 2)},
            {"item": "Double Sided Sheets", "price": round(random.uniform(3.0, 7.0), 2)},
            {"item": "Experiment Headers", "price": round(random.uniform(1.5, 4.0), 2)},
            {"item": "Assignment Headers", "price": round(random.uniform(1.0, 3.0), 2)},
            {"item": "College Files", "price": round(random.uniform(4.0, 8.0), 2)},
            {"item": "Normal Files", "price": round(random.uniform(3.0, 6.0), 2)},
            {"item": "Drafter", "price": round(random.uniform(5.0, 10.0), 2)},
            {"item": "Drawing Books", "price": round(random.uniform(6.0, 12.0), 2)},
            {"item": "Mechanical Pencils", "price": round(random.uniform(2.0, 5.0), 2)},
        ]

        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Item", "Price", "Quantity", "Total Cost"])

        self.layout = QVBoxLayout()

        for item in self.items:
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)

            item_name = QTableWidgetItem(item["item"])
            price = QTableWidgetItem("${:.2f}".format(item["price"]))
            quantity = QLineEdit(self)
            total_cost = QTableWidgetItem("")

            self.table.setItem(row_position, 0, item_name)
            self.table.setItem(row_position, 1, price)
            self.table.setCellWidget(row_position, 2, quantity)
            self.table.setItem(row_position, 3, total_cost)

        calculate_button = QPushButton("Calculate Total", self)
        calculate_button.clicked.connect(self.calculate_total)

        self.layout.addWidget(self.table)
        self.layout.addWidget(calculate_button)

        self.setLayout(self.layout)

        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle("Item List")
        self.show()

    def calculate_total(self):
        for row in range(self.table.rowCount()):
            price = float(self.table.item(row, 1).text().replace("$", ""))
            quantity = float(self.table.cellWidget(row, 2).text())
            total_cost = calculate_total_cost(price, quantity)
            self.table.item(row, 3).setText("${:.2f}".format(total_cost))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    item_list_app = ItemListApp()
    sys.exit(app.exec_())
