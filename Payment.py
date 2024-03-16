import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

class PaymentWindow(QWidget):
    def __init__(self, total_cost):
        super().__init__()

        self.total_cost = total_cost

        self.init_ui()

    def init_ui(self):
        total_label = QLabel(f'Total Cost: ${self.total_cost:.2f}')

        pay_button = QPushButton('Pay')
        pay_button.clicked.connect(self.pay)

        layout = QVBoxLayout()
        layout.addWidget(total_label)
        layout.addWidget(pay_button)

        self.setLayout(layout)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Payment Window')

    def pay(self):
        # Implement payment logic here
        print(f'Payment Successful! Amount: ${self.total_cost:.2f}')
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Replace this with the total_cost calculated in the ItemListApp
    total_cost_from_calculate_window = 50.0

    payment_window = PaymentWindow(total_cost_from_calculate_window)
    payment_window.show()

    sys.exit(app.exec_())
