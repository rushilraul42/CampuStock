from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
impor

class PaymentWindow(QWidget):
    def __init__(self, total_cost):
        super().__init__()
        self.init_ui(total_cost)

    def init_ui(self, total_cost):
        self.total_cost = total_cost

        self.layout = QVBoxLayout()

        # Label to display total cost
        self.total_cost_label = QLabel(f"Total Cost: ${self.total_cost:.2f}", self)
        self.layout.addWidget(self.total_cost_label)

        # Horizontal layout for the "Pay" button
        self.button_layout = QHBoxLayout()
        self.pay_button = QPushButton("Pay", self)
        self.button_layout.addWidget(self.pay_button)
        self.layout.addLayout(self.button_layout)

        self.setLayout(self.layout)
        self.setWindowTitle("Payment")
        self.show()

