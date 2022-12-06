import sys, random
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QApplication, QComboBox, \
    QPushButton, QLineEdit, QLabel


def on_cross_pushbutton_clicked():
    if method_combo_box.currentText() == "Corte Simples":
        offsprings = simple_cut_crossover()
        son1_label_3.setVisible(False)
        son2_label_3.setVisible(False)
    else:
        offsprings = pmx_crossover()
        son1_label_3.setVisible(True)
        son2_label_3.setVisible(True)

    son1_label_1.setText(offsprings[0])
    son1_label_2.setText(offsprings[1])
    son1_label_3.setText(offsprings[2])
    son2_label_1.setText(offsprings[3])
    son2_label_2.setText(offsprings[4])
    son2_label_3.setText(offsprings[5])


def on_method_combobox_current_text_changed():
    pmx = ['A','B','C','D','E','F','G','H','I','J']

    if method_combo_box.currentText() == "Corte Simples":
        father_line_edit.setInputMask('BBBBBBBBBB')
        father_line_edit.setText('0000000000')
        mother_line_edit.setInputMask('BBBBBBBBBB')
        mother_line_edit.setText('0000000000')
    else:
        father_line_edit.setInputMask('AAAAAAAAAA')
        random.shuffle(pmx)
        father_line_edit.setText(''.join(pmx))
        mother_line_edit.setInputMask('AAAAAAAAAA')
        random.shuffle(pmx)
        mother_line_edit.setText(''.join(pmx))
    #print('combo box changed')

def pmx_crossover():
    # Esta função está retornando 6 valores.
    # Ao criar o corpo da função você deve ordená-los de acordo com
    # as linhas 17 a 22 deste arquivo.

    father_original = father_line_edit.text()
    father_list = list(father_original)

    mother_original = mother_line_edit.text()
    mother_list = list(mother_original)

    cut_points = [random.randint(1, len(father_list)-1)]
    cut_point = random.randint(1, len(father_list)-1)

    while cut_points.__contains__(cut_point):
        cut_point = random.randint(1, len(father_list)-1)

    if cut_point > cut_points[0]:
        cut_points.append(cut_point)
    else:
        cut_points.append(cut_points[0])
        cut_points[0] = cut_point

    d_mother = {}
    d_father = {}

    for i in range(len(father_list)):
        if cut_points[0] <=  i < cut_points[1]:
            d_father.update({father_list[i]: mother_list[i]})
            d_mother.update({mother_list[i]: father_list[i]})

    aux_d_father = dict (d_father)
    for k, v in aux_d_father.items():
        if d_mother.__contains__(k):
            d_father.update({d_mother[k]:v})
            d_mother.update({v:d_mother[k]})
            del d_father[k]
            del d_mother[k]

    for i in range(len(mother_list)):
        if d_father.__contains__(mother_list[i]):
            mother_list[i] = d_father[mother_list[i]]
        if d_mother.__contains__(father_list[i]):
            father_list[i] = d_mother[father_list[i]]

    mother = ''.join(mother_list)
    father = ''.join(father_list)

    return father[:cut_points[0]],\
           mother_original[cut_points[0]:cut_points[1]], \
           father[cut_points[1]:], \
           mother[:cut_points[0]], \
           father_original[cut_points[0]:cut_points[1]], \
           mother[cut_points[1]:]
    #return '','','','','',''


def simple_cut_crossover():

    father = father_line_edit.text();
    mother = mother_line_edit.text();
    cut_point = random.randint(0, len(father))

    return father[:cut_point], mother[cut_point:], '', mother[:cut_point], father[cut_point:], ''


    #return '','','','','',''


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)

    # Loading widgets elements from ui file
    window = uic.loadUi("crossover_operation.ui")
    window.show()

    # Getting widgets elements
    father_line_edit = window.findChild(QLineEdit, 'fatherLineEdit')
    mother_line_edit = window.findChild(QLineEdit, 'motherLineEdit')
    son1_label_1 = window.findChild(QLabel, 'son1Label1')
    son1_label_2 = window.findChild(QLabel, 'son1Label2')
    son1_label_3 = window.findChild(QLabel, 'son1Label3')
    son2_label_1 = window.findChild(QLabel, 'son2Label1')
    son2_label_2 = window.findChild(QLabel, 'son2Label2')
    son2_label_3 = window.findChild(QLabel, 'son2Label3')
    method_combo_box = window.findChild(QComboBox, 'methodComboBox')
    cross_push_button = window.findChild(QPushButton, 'crossPushButton')

    # Connecting
    cross_push_button.clicked.connect(on_cross_pushbutton_clicked)
    method_combo_box.currentTextChanged.connect(on_method_combobox_current_text_changed)

    sys.exit(app.exec_())