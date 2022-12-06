import sys
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QApplication, QLabel, QAction, QSpinBox, QPushButton
#definindo a quantidade de dinheiro
def dinheiro_pouco():
    dinheiro = dinheiro_sb.value()
    if dinheiro <= 30:
        return 1
    if dinheiro > 30 and dinheiro < 50:
        return (50 - dinheiro) / 20
    if dinheiro >= 50:
        return 0
def dinheiro_razoavel():
    dinheiro = dinheiro_sb.value()
    if dinheiro <= 30:
        return 0
    if dinheiro > 30 and dinheiro < 50:
        return (dinheiro - 30) / 20
    if dinheiro < 70 and dinheiro > 50:
        return (70 - dinheiro) / 20
    if dinheiro >= 70:
        return 0
def dinheiro_adquado():
    dinheiro = dinheiro_sb.value()
    if dinheiro <= 50:
        return 0
    if dinheiro > 50 and dinheiro < 70:
        return (dinheiro - 50) / 20
    if dinheiro >= 70:
        return 1
#definido a quantidade de pessoas
def pessoal_insuficiente():
    pessoa = pessoas_sb.value()
    if pessoa <= 30:
        return 1
    if pessoa > 30 and pessoa < 70:
        return (70 - pessoa) / 40
    if pessoa >= 70:
        return 0
def pessoal_satisfatorio():
    pessoa = pessoas_sb.value()
    if pessoa <= 30:
        return 0
    if pessoa >= 70:
        return 1
    if pessoa > 30 and pessoa < 70:
        return (pessoa - 30) / 40
#definição de regras
def regras(vet):# RISCOS
    if(dinheiro_pouco() > pessoal_insuficiente()):
        alto = dinheiro_pouco()
    else:
        alto = pessoal_insuficiente()
    if(dinheiro_pouco() < pessoal_satisfatorio()):
        alto2 = dinheiro_pouco()
    else:
        alto2 = pessoal_satisfatorio()
    # Alto
    if(alto < alto2):
        vet[2] = alto
    else:
        vet[2] = alto2
    # Medio
    if(dinheiro_razoavel() < pessoal_satisfatorio()):
        vet[1] = dinheiro_razoavel()
    else:
        vet[1] = pessoal_satisfatorio()
    # Baixo
    if(dinheiro_adquado() < pessoal_satisfatorio()):
        vet[0] = dinheiro_adquado()
    else:
        vet[0] = pessoal_satisfatorio()
#riscos
def risco(valor):
    if valor >= 0 or valor < 50:
        return 'Baixo'
    if valor >= 50 or valor < 70:
        return 'Medio'
    if valor >= 70:
        return 'Alto'

def on_calcular_pushbutton_clicked():
    intervalos = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    vet = [0, 0, 0]
    regras(vet)
    numerador = 0; denominador = 0; count = 0; j = 0
    for i in intervalos:
        if(count == 3 or count == 6):
            j += 1

        count += 1
        numerador += i*vet[j]
        denominador += vet[j]
    if denominador != 0:
        calc = numerador/denominador
    elif denominador == 0:
        calc = 0



    risco_label2.setText(risco(calc)+': '+(str(calc)))
if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    window = uic.loadUi("logica_fuzzy.ui")
    dinheiro_label = window.findChild(QLabel, 'dinheiroLabel')
    dinheiro_label.setVisible(True)

    pessoas_label = window.findChild(QLabel, 'pessoasLabel')
    pessoas_label.setVisible(True)

    risco_label = window.findChild(QLabel, 'riscoLabel')
    risco_label.setVisible(True)

    risco_label2 = window.findChild(QLabel, 'riscoLabel2')
    risco_label2.setVisible(True)

    dinheiro_sb = window.findChild(QSpinBox, 'dinheiroSpinBox')
    dinheiro_sb.setVisible(True)

    pessoas_sb = window.findChild(QSpinBox, 'pessoasSpinBox')
    pessoas_sb.setVisible(True)

    calcular_btn = window.findChild(QPushButton, 'calcularPushButton')
    calcular_btn.clicked.connect(on_calcular_pushbutton_clicked)

    window.show()   
    #print('teste')
    sys.exit(app.exec_())