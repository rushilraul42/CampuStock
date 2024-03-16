import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout

# Function to calculate total cost
def calculate_total_cost(price_per_week, num_weeks):
    return price_per_week * num_weeks

class RentList(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.items = [
            {"item": "Drafter", "price_per_week": 5.0},
            {"item": "Eng Math 1", "price_per_week": 8.0},
            {"item": "Eng Math 2", "price_per_week": 8.0},
            {"item": "Eng Math 3", "price_per_week": 8.0},
            {"item": "BEE", "price_per_week": 6.0},
            {"item": "DBMS", "price_per_week": 10.0},
            {"item": "DSA", "price_per_week": 9.0},
            {"item": "CNND", "price_per_week": 11.0},
            {"item": "PCOM", "price_per_week": 7.0},
        ]

        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Item", "Price Per Week", "No. of Weeks", "Total Cost"])

        # Adjust column width
        self.table.setColumnWidth(0, 150)  # Setting the width of the "Item" column

        self.layout = QVBoxLayout()

        for item in self.items:
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)

            item_name = QTableWidgetItem(item["item"])
            price_per_week = QTableWidgetItem("${:.2f}".format(item["price_per_week"]))
            num_weeks = QLineEdit(self)
            total_cost = QTableWidgetItem("")

            self.table.setItem(row_position, 0, item_name)
            self.table.setItem(row_position, 1, price_per_week)
            self.table.setCellWidget(row_position, 2, num_weeks)
            self.table.setItem(row_position, 3, total_cost)

        calculate_button = QPushButton("Calculate Total", self)
        calculate_button.clicked.connect(self.calculate_total)

        self.layout.addWidget(self.table)
        self.layout.addWidget(calculate_button)

        self.setLayout(self.layout)

        self.setGeometry(100, 100, 600, 400)  # Set window size
        self.setWindowTitle("Rent List")
        self.show()

    def calculate_total(self):
        for row in range(self.table.rowCount()):
            price_per_week = float(self.table.item(row, 1).text().replace("$", ""))
            num_weeks = float(self.table.cellWidget(row, 2).text())
            total_cost = calculate_total_cost(price_per_week, num_weeks)
            self.table.item(row, 3).setText("${:.2f}".format(total_cost))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    rent_list_app = RentList()
    sys.exit(app.exec_())
