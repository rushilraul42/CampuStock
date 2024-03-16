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
            {"item": "Pen", "price": 1.5},
            {"item": "Pencil", "price": 0.8},
            {"item": "Scale", "price": 2.5},
            {"item": "Rounder", "price": 3.0},
            {"item": "Eraser", "price": 0.5},
            {"item": "Single Sided Sheets", "price": 4.0},
            {"item": "Double Sided Sheets", "price": 6.0},
            {"item": "Experiment Headers", "price": 2.0},
            {"item": "Assignment Headers", "price": 1.5},
            {"item": "College Files", "price": 7.0},
            {"item": "Normal Files", "price": 5.5},
            {"item": "Drafter", "price": 8.0},
            {"item": "Drawing Books", "price": 10.0},
            {"item": "Mechanical Pencils", "price": 2.0},
        ]

        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Item", "Price", "Quantity", "Total Cost"])

        # Adjust column width
        self.table.setColumnWidth(0, 200)  # Setting the width of the "Item" column

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

        self.setGeometry(100, 100, 800, 400)  # Increased window width
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
