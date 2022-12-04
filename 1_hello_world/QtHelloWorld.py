# realizando as importações necessárias
from PyQt5.QtWidgets import QApplication, QLabel

if __name__ == "__main__":
    # Criando a janela da aplicação
    app = QApplication([])

    # Criando o rótulo
    label = QLabel("Hello World")
    label.show()

    # Executando a janela
    app.exec_()