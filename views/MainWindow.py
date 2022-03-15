from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QFrame


class MainWindow(QMainWindow):
    def __init__(self, controller):
        super(MainWindow, self).__init__()

        self.controller = controller
        self.model = self.controller.model

        self.mainLayout = QHBoxLayout()
        self.mainFrame = QFrame()

        self.setWindowTitle(self.model.title)
        self.setWindowIcon(self.model.icon)

    def main(self):
        self.mainLayout.addWidget(self.mainFrame)
        self.setCentralWidget(self.mainFrame)
        self.show()
