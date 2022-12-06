import sys, random
from PyQt5 import QtCore,uic
from PyQt5.QtWidgets import QApplication, QComboBox,QPushButton, QLineEdit, QLabel, QMessageBox
#final
def a(str_n, b, ha):
    e_l = list(str_n)
    d = list(b)
    l_m = list(ha)
    n = 0
    for i in range(len(e_l)):
        for j in range(len(d)):
            if n > (len(d) - 1) or i > (len(e_l)-1) or j > (len(d)-1) : continue
            elif (e_l[i] == d[j]):
                e_l[i] = l_m[n]
                del (d[j])
                del (l_m[n])
                n += 1
    str_n = "".join(e_l)
    b = "".join(d)
    ha = "".join(l_m)
    return str_n, b, ha
def compare_changes(str_n, b):
    e_l = list(str_n)
    d = list(b)
    n = 0
    for i in range(len(e_l)):
        for j in range(len(d)):
            if n > (len(d) - 1) or i > (len(e_l)-1) or j > (len(d)-1) : continue
            elif (e_l[i] == d[j]):
                del (d[j])
                del (e_l[i])
    str_n = "".join(e_l)
    b = "".join(d)
    return str_n, b
def on_cross_pushbutton_clicked():
    if len(daddy_line_edit.text()) != 10 or len(daddy_line_edit.text()) != 10:
        QMessageBox.warning(QMessageBox(), "AVISO", "Entrada deve conter 10 caracteres")
        return
    if method_combo_box.currentText() == "Corte Simples":
        simple_cut_crossover(1)
        filhao1_label_3.setText("")
        filhao2_label_3.setText("")
    elif method_combo_box.currentText() == "Corte Duplo":
        simple_cut_crossover(2)
    elif method_combo_box.currentText() == "PMX":
        if len(daddy_line_edit.text()) != len(set(daddy_line_edit.text())) \
                or len(mammy_line_edit.text()) != len(set(mammy_line_edit.text())):
            QMessageBox.warning(QMessageBox(), "AVISO", "Entrada deve conter valores unicos")
            return
        pmx_crossover()
def on_method_combobox_current_text_changed():
    if method_combo_box.currentText() == "PMX":
        daddy_line_edit.setInputMask("AAAAAAAAAA")
        mammy_line_edit.setInputMask("AAAAAAAAAA")
        daddy_line_edit.setText("ABCDEFGHIJ")
        mammy_line_edit.setText("KLMNOPQRST")
    else:
        daddy_line_edit.setInputMask("BBBBBBBBBB")
        mammy_line_edit.setInputMask("BBBBBBBBBB")
        daddy_line_edit.setText("0000000000")
        mammy_line_edit.setText("1111111111")
def pmx_crossover():
    cuts = 2
    trades = 1
    papi = daddy_line_edit.text()
    mami = mammy_line_edit.text()
    parts = random.sample(range(1, len(papi)), cuts)
    parts.sort()
    choose = random.sample(range(0, len(parts)+1), trades)
    filhao_1 = []
    for i in range (len(parts)+1):
        filhao_1.append(0)
        if i == 0:
            filhao_1[i] = papi[:parts[0]]
        elif i == len(parts):
            filhao_1[i] = papi[parts[i-1]:]
        else:
            filhao_1[i] = papi[parts[i-1]:parts[i]]
    filhao_2 = []
    for i in range(len(parts) + 1):
        filhao_2.append(0)
        if i == 0:
            filhao_2[i] = mami[:parts[0]]
        elif i == len(parts):
            filhao_2[i] = mami[parts[i - 1]:]
        else:
            filhao_2[i] = mami[parts[i - 1]:parts[i]]
    filhao_x = filhao_1.copy()
    filhao_1_muda_1 = ""
    filhao_1_muda_2 = ""
    for i in range(len(choose)):
        filhao_1[choose[i]] = filhao_2[choose[i]]
        filhao_1_muda_2 += filhao_2[choose[i]]
        filhao_2[choose[i]] = filhao_x[choose[i]]
        filhao_1_muda_1 += filhao_x[choose[i]]
    tchegarotos = compare_changes(filhao_1_muda_1, filhao_1_muda_2)
    filhao_1_muda_1 = tchegarotos[0]
    filhao_1_muda_2 = tchegarotos[1]
    filhao_2_muda_1 = filhao_1_muda_2
    filhao_2_muda_2 = filhao_1_muda_1
    for i in range(len(filhao_1)):
        if i == choose[0]:
            continue
        tchegarotos = a(filhao_1[i], filhao_1_muda_2, filhao_1_muda_1)
        filhao_1[i] = [0]
        filhao_1_muda_2 = tchegarotos[1]
        filhao_1_muda_1 = tchegarotos[2]
    for i in range(len(filhao_2)):
        if i == choose[0]:
            continue
        tchegarotos = a(filhao_2[i], filhao_2_muda_2, filhao_2_muda_1)
        filhao_2[i] = tchegarotos[0]
        filhao_2_muda_2 = tchegarotos[1]
        filhao_2_muda_1 = tchegarotos[2]
    print(filhao_1)
    filhao1_label_1.setText(filhao_1[0])
    filhao1_label_2.setText(filhao_1[1])
    filhao1_label_3.setText(filhao_1[2])
    filhao2_label_1.setText(filhao_2[0])
    filhao2_label_2.setText(filhao_2[1])
    filhao2_label_3.setText(filhao_2[2])
def simple_cut_crossover(cuts):
    trades = 1
    papi = daddy_line_edit.text()
    mami = mammy_line_edit.text()
    parts = random.sample(range(1, len(papi)), cuts)
    parts.sort()
    choose = random.sample(range(0, len(parts)+1), trades)
    filhao_1 = []
    for i in range (len(parts)+1):
        filhao_1.append(0)
        if i == 0:
            filhao_1[i] = papi[:parts[0]]
        elif i == len(parts):
            filhao_1[i] = papi[parts[i-1]:]
        else:
            filhao_1[i] = papi[parts[i-1]:parts[i]]
    filhao_2 = []
    for i in range(len(parts) + 1):
        filhao_2.append(0)
        if i == 0:
            filhao_2[i] = mami[:parts[0]]
        elif i == len(parts):
            filhao_2[i] = mami[parts[i - 1]:]
        else:
            filhao_2[i] = mami[parts[i - 1]:parts[i]]
    filhao_x = filhao_1.copy()
    for i in range(len(choose)):
        filhao_1[choose[i]] = filhao_2[choose[i]]
        filhao_2[choose[i]] = filhao_x[choose[i]]
    filhao1_label_1.setText(filhao_1[0])
    filhao1_label_2.setText(filhao_1[1])
    filhao2_label_1.setText(filhao_2[0])
    filhao2_label_2.setText(filhao_2[1])
    if cuts == 2:
        filhao1_label_3.setText(filhao_1[2])
        filhao2_label_3.setText(filhao_2[2])
if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    window = uic.loadUi(r"crossover_operation.ui")
    window.show()
    daddy_line_edit = window.findChild(QLineEdit, 'daddyLineEdit')
    mammy_line_edit = window.findChild(QLineEdit, 'mammyLineEdit')
    filhao1_label_1 = window.findChild(QLabel, 'filhao1Label1')
    filhao1_label_2 = window.findChild(QLabel, 'filhao1Label2')
    filhao1_label_3 = window.findChild(QLabel, 'filhao1Label3')
    filhao2_label_1 = window.findChild(QLabel, 'filhao2Label1')
    filhao2_label_2 = window.findChild(QLabel, 'filhao2Label2')
    filhao2_label_3 = window.findChild(QLabel, 'filhao2Label3')
    method_combo_box = window.findChild(QComboBox, 'methodComboBox')
    cross_push_button = window.findChild(QPushButton, 'crossPushButton')
    cross_push_button.clicked.connect(on_cross_pushbutton_clicked)
    method_combo_box.currentTextChanged.connect(on_method_combobox_current_text_changed)
    sys.exit(app.exec_())

    #.