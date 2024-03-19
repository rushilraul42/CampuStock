import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout
from Payment import PaymentWindow  # Import PaymentWindow from Payment.py

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

            quantity.textChanged.connect(self.calculate_total)  # Connect textChanged signal to calculate_total method

            self.table.setItem(row_position, 0, item_name)
            self.table.setItem(row_position, 1, price)
            self.table.setCellWidget(row_position, 2, quantity)
            self.table.setItem(row_position, 3, total_cost)

        calculate_button = QPushButton("Calculate Total", self)
        calculate_button.clicked.connect(self.calculate_total)

        self.proceed_to_pay_button = QPushButton("Proceed to Pay", self)
        self.proceed_to_pay_button.clicked.connect(self.proceed_to_pay)

        self.layout.addWidget(self.table)
        self.layout.addWidget(calculate_button)
        self.layout.addWidget(self.proceed_to_pay_button)

        self.total_cost_label = QLabel("Total Cost: $0.00", self)  # Initialize label with initial total cost
        self.layout.addWidget(self.total_cost_label)

        self.setLayout(self.layout)

        self.setGeometry(100, 100, 800, 400)  # Increased window width
        self.setWindowTitle("Item List")
        self.show()

    def calculate_total(self):
        total_cost = 0
        for row in range(self.table.rowCount()):
            price_text = self.table.item(row, 1).text().replace("$", "")
            quantity_text = self.table.cellWidget(row, 2).text()

            try:
                price = float(price_text)
                quantity = int(quantity_text)  # Convert quantity to an integer
                total = calculate_total_cost(price, quantity)
                total_cost += total
                self.table.item(row, 3).setText("${:.2f}".format(total))
            except ValueError:
                # Handle the case where quantity is not a valid integer
                pass

        self.total_cost_label.setText(f"Total Cost: ${total_cost:.2f}")  # Update the total cost label

    def proceed_to_pay(self):
        total_cost = float(self.total_cost_label.text().replace("Total Cost: $", ""))
        payment_window = PaymentWindow(total_cost)
        payment_window.show()  # Show payment window


if __name__ == '__main__':
    app = QApplication(sys.argv)
    item_list_app = ItemListApp()
    sys.exit(app.exec_())
