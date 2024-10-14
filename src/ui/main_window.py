from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Photogrammetry Assistant")

        # Центральный виджет
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Вертикальный layout
        layout = QVBoxLayout(central_widget)

        # Заголовок
        title_label = QLabel("Добро пожаловать в Photogrammetry Assistant!", self)
        layout.addWidget(title_label)

        # Кнопка для выбора задачи
        choose_task_button = QPushButton("Выбрать задачу", self)
        choose_task_button.clicked.connect(self.choose_task)  # Подключение функции
        layout.addWidget(choose_task_button)

    def choose_task(self):
        # TODO: Реализовать логику выбора задачи
        print("Выбрана задача")