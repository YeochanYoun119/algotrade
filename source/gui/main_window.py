from PyQt5.QtWidgets import *
from source.gui.account import AccountPage
from source.gui.auto_trade import AutoTradePage
from source.gui.data_visualization import DataVisualizationPage
from source.gui.login import LoginDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        login_dialog = LoginDialog(self)
        login_dialog.move(500, 300)
        login_dialog.exec()

        # login process page

        # login_dialog.exec()
        # main widget general setting
        main_widget = QWidget()
        main_widget.setMinimumSize(800, 450)
        main_widget_layout = QVBoxLayout()
        main_widget.setLayout(main_widget_layout)
        self.setCentralWidget(main_widget)

        # main widget add components
        page_buttons = PageButtons()
        self.stack_widget = QStackedWidget()
        # self.stack_widget.setStyleSheet("background-color: red;")

        account_page = AccountPage()
        data_visualization_page = DataVisualizationPage()
        auto_trade_page = AutoTradePage()
        self.stack_widget.addWidget(account_page)
        self.stack_widget.addWidget(data_visualization_page)
        self.stack_widget.addWidget(auto_trade_page)

        page_each_button = [button for button in page_buttons.children() if type(button) is PageButtons.PageButton]
        print(page_each_button[0].name)
        # page_each_button[0].clicked.connect(lambda x: self.stack_widget.setCurrentIndex(0))
        # page_each_button[1].clicked.connect(lambda x: self.stack_widget.setCurrentIndex(1))
        # page_each_button[2].clicked.connect(lambda x: self.stack_widget.setCurrentIndex(2))
        page_each_button[0].clicked.connect(self.set_1)
        page_each_button[1].clicked.connect(self.set_2)
        page_each_button[2].clicked.connect(self.set_3)

        main_widget_layout.addWidget(page_buttons)
        main_widget_layout.addWidget(self.stack_widget)

    def set_1(self):
        self.stack_widget.setCurrentIndex(0)
        self.repaint()

    def set_2(self):
        self.stack_widget.setCurrentIndex(1)
        self.repaint()

    def set_3(self):
        self.stack_widget.setCurrentIndex(2)
        self.repaint()


class PageButtons(QWidget):
    class PageButton(QPushButton):
        def __init__(self, name):
            super().__init__(name)
            self.name = name
            self.setFixedSize(150, 30)

    def __init__(self):
        super().__init__()
        # button group general setting
        self.setFixedSize(450, 30)
        page_buttons_layout = QHBoxLayout()
        page_buttons_layout.setSpacing(0)
        page_buttons_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(page_buttons_layout)

        # add buttons to button group
        account_page_button = self.PageButton('account')
        data_visualization_button = self.PageButton('data visualization')
        auto_trade_button = self.PageButton('auto trade')
        page_buttons_layout.addWidget(account_page_button)
        page_buttons_layout.addWidget(data_visualization_button)
        page_buttons_layout.addWidget(auto_trade_button)


