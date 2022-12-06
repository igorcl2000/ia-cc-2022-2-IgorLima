import sys
from PyQt5 import QtCore,uic
from PyQt5.QtWidgets import QApplication, QComboBox, \
    QPushButton, QLabel, QMessageBox
from PyQt5.QtGui import QIcon

NUM_OF_NEURONS = 10


class Gui:
    def __init__(self):
        # loading widgets elements from ui file
        self.window = uic.loadUi("character_recognition.ui")

        # Getting widget references
        self.black = QIcon("black.png")
        self.white = QIcon("white.png")
        self.font_cb = self.window.findChild(QComboBox, "fontComboBox")
        self.character_cb = self.window.findChild(QComboBox, "characterComboBox")
        self.train_pb = self.window.findChild(QPushButton, "trainPushButton")
        self.run_pb = self.window.findChild(QPushButton, "runPushButton")

        # Connecting Signals
        self.character_cb.currentIndexChanged.connect(self.on_character_combobox_current_index_changed)
        self.train_pb.clicked.connect(self.on_train_pushbutton_clicked)
        self.run_pb.clicked.connect(self.on_run_pushbutton_clicked)

        # Input list starts with -1 values
        # which means a white screen
        self.inputs = []
        for i in range(80):
            self.inputs.append(-1)

        # list of object pixels
        # each pixels is a QPushButton with an icon
        self.pixels = []
        self.populate_pixels_list()

        # Create and populate training_set
        self.training_set = []
        self.font_a = []
        self.font_j = []
        self.populate_training_set('font_a.txt', self.font_a)
        self.populate_training_set('font_j.txt', self.font_j)

        # Training neural network
        self.neutral_network = []

    def on_character_combobox_current_index_changed(self):
        if int(self.character_cb.currentText()) == -1:
            aux = []
            for i in range(len(self.inputs)):
                aux.append(-1)
            self.inputs = list(aux)
            self.update_display()
        else:
            if self.font_cb.currentText() == 'Fonte A':
                self.inputs = self.font_a[int(self.character_cb.currentText())]
                self.update_display()
            elif self.font_cb.currentText() == 'Fonte J':
                self.inputs = self.font_j[int(self.character_cb.currentText())]
                self.update_display()
    def on_pixel_00_clicked(self):
        if self.pixels[0].toolTip() == "white":
            self.pixels[0].setIcon(self.black)
            self.pixels[0].setToolTip("black")
            self.inputs[0] = 1
        else:
            self.pixels[0].setIcon(self.white)
            self.pixels[0].setToolTip("white")
            self.inputs[0] = -1

    def on_pixel_01_clicked(self):
        if self.pixels[1].toolTip() == "white":
            self.pixels[1].setIcon(self.black)
            self.pixels[1].setToolTip("black")
            self.inputs[1] = 1
        else:
            self.pixels[1].setIcon(self.white)
            self.pixels[1].setToolTip("white")
            self.inputs[1] = -1

    def on_pixel_02_clicked(self):
        if self.pixels[2].toolTip() == "white":
            self.pixels[2].setIcon(self.black)
            self.pixels[2].setToolTip("black")
            self.inputs[2] = 1
        else:
            self.pixels[2].setIcon(self.white)
            self.pixels[2].setToolTip("white")
            self.inputs[2] = -1

    def on_pixel_03_clicked(self):
        if self.pixels[3].toolTip() == "white":
            self.pixels[3].setIcon(self.black)
            self.pixels[3].setToolTip("black")
            self.inputs[3] = 1
        else:
            self.pixels[3].setIcon(self.white)
            self.pixels[3].setToolTip("white")
            self.inputs[3] = -1

    def on_pixel_04_clicked(self):
        if self.pixels[4].toolTip() == "white":
            self.pixels[4].setIcon(self.black)
            self.pixels[4].setToolTip("black")
            self.inputs[4] = 1
        else:
            self.pixels[4].setIcon(self.white)
            self.pixels[4].setToolTip("white")
            self.inputs[4] = -1

    def on_pixel_05_clicked(self):
        if self.pixels[5].toolTip() == "white":
            self.pixels[5].setIcon(self.black)
            self.pixels[5].setToolTip("black")
            self.inputs[5] = 1
        else:
            self.pixels[5].setIcon(self.white)
            self.pixels[5].setToolTip("white")
            self.inputs[5] = -1

    def on_pixel_06_clicked(self):
        if self.pixels[6].toolTip() == "white":
            self.pixels[6].setIcon(self.black)
            self.pixels[6].setToolTip("black")
            self.inputs[6] = 1
        else:
            self.pixels[6].setIcon(self.white)
            self.pixels[6].setToolTip("white")
            self.inputs[6] = -1

    def on_pixel_07_clicked(self):
        if self.pixels[7].toolTip() == "white":
            self.pixels[7].setIcon(self.black)
            self.pixels[7].setToolTip("black")
            self.inputs[7] = 1
        else:
            self.pixels[7].setIcon(self.white)
            self.pixels[7].setToolTip("white")
            self.inputs[7] = -1

    def on_pixel_10_clicked(self):
        if self.pixels[8].toolTip() == "white":
            self.pixels[8].setIcon(self.black)
            self.pixels[8].setToolTip("black")
            self.inputs[8] = 1
        else:
            self.pixels[8].setIcon(self.white)
            self.pixels[8].setToolTip("white")
            self.inputs[8] = -1

    def on_pixel_11_clicked(self):
        if self.pixels[9].toolTip() == "white":
            self.pixels[9].setIcon(self.black)
            self.pixels[9].setToolTip("black")
            self.inputs[9] = 1
        else:
            self.pixels[9].setIcon(self.white)
            self.pixels[9].setToolTip("white")
            self.inputs[9] = -1

    def on_pixel_12_clicked(self):
        if self.pixels[10].toolTip() == "white":
            self.pixels[10].setIcon(self.black)
            self.pixels[10].setToolTip("black")
            self.inputs[10] = 1
        else:
            self.pixels[10].setIcon(self.white)
            self.pixels[10].setToolTip("white")
            self.inputs[10] = -1

    def on_pixel_13_clicked(self):
        if self.pixels[11].toolTip() == "white":
            self.pixels[11].setIcon(self.black)
            self.pixels[11].setToolTip("black")
            self.inputs[11] = 1
        else:
            self.pixels[11].setIcon(self.white)
            self.pixels[11].setToolTip("white")
            self.inputs[11] = -1

    def on_pixel_14_clicked(self):
        if self.pixels[12].toolTip() == "white":
            self.pixels[12].setIcon(self.black)
            self.pixels[12].setToolTip("black")
            self.inputs[12] = 1
        else:
            self.pixels[12].setIcon(self.white)
            self.pixels[12].setToolTip("white")
            self.inputs[12] = -1

    def on_pixel_15_clicked(self):
        if self.pixels[13].toolTip() == "white":
            self.pixels[13].setIcon(self.black)
            self.pixels[13].setToolTip("black")
            self.inputs[13] = 1
        else:
            self.pixels[13].setIcon(self.white)
            self.pixels[13].setToolTip("white")
            self.inputs[13] = -1

    def on_pixel_16_clicked(self):
        if self.pixels[14].toolTip() == "white":
            self.pixels[14].setIcon(self.black)
            self.pixels[14].setToolTip("black")
            self.inputs[14] = 1
        else:
            self.pixels[14].setIcon(self.white)
            self.pixels[14].setToolTip("white")
            self.inputs[14] = -1

    def on_pixel_17_clicked(self):
        if self.pixels[15].toolTip() == "white":
            self.pixels[15].setIcon(self.black)
            self.pixels[15].setToolTip("black")
            self.inputs[15] = 1
        else:
            self.pixels[15].setIcon(self.white)
            self.pixels[15].setToolTip("white")
            self.inputs[15] = -1

    def on_pixel_20_clicked(self):
        if self.pixels[16].toolTip() == "white":
            self.pixels[16].setIcon(self.black)
            self.pixels[16].setToolTip("black")
            self.inputs[16] = 1
        else:
            self.pixels[16].setIcon(self.white)
            self.pixels[16].setToolTip("white")
            self.inputs[16] = -1

    def on_pixel_21_clicked(self):
        if self.pixels[17].toolTip() == "white":
            self.pixels[17].setIcon(self.black)
            self.pixels[17].setToolTip("black")
            self.inputs[17] = 1
        else:
            self.pixels[17].setIcon(self.white)
            self.pixels[17].setToolTip("white")
            self.inputs[17] = -1

    def on_pixel_22_clicked(self):
        if self.pixels[18].toolTip() == "white":
            self.pixels[18].setIcon(self.black)
            self.pixels[18].setToolTip("black")
            self.inputs[18] = 1
        else:
            self.pixels[18].setIcon(self.white)
            self.pixels[18].setToolTip("white")
            self.inputs[18] = -1

    def on_pixel_23_clicked(self):
        if self.pixels[19].toolTip() == "white":
            self.pixels[19].setIcon(self.black)
            self.pixels[19].setToolTip("black")
            self.inputs[19] = 1
        else:
            self.pixels[19].setIcon(self.white)
            self.pixels[19].setToolTip("white")
            self.inputs[19] = -1

    def on_pixel_24_clicked(self):
        if self.pixels[20].toolTip() == "white":
            self.pixels[20].setIcon(self.black)
            self.pixels[20].setToolTip("black")
            self.inputs[20] = 1
        else:
            self.pixels[20].setIcon(self.white)
            self.pixels[20].setToolTip("white")
            self.inputs[20] = -1

    def on_pixel_25_clicked(self):
        if self.pixels[21].toolTip() == "white":
            self.pixels[21].setIcon(self.black)
            self.pixels[21].setToolTip("black")
            self.inputs[21] = 1
        else:
            self.pixels[21].setIcon(self.white)
            self.pixels[21].setToolTip("white")
            self.inputs[21] = -1

    def on_pixel_26_clicked(self):
        if self.pixels[22].toolTip() == "white":
            self.pixels[22].setIcon(self.black)
            self.pixels[22].setToolTip("black")
            self.inputs[22] = 1
        else:
            self.pixels[22].setIcon(self.white)
            self.pixels[22].setToolTip("white")
            self.inputs[22] = -1

    def on_pixel_27_clicked(self):
        if self.pixels[23].toolTip() == "white":
            self.pixels[23].setIcon(self.black)
            self.pixels[23].setToolTip("black")
            self.inputs[23] = 1
        else:
            self.pixels[23].setIcon(self.white)
            self.pixels[23].setToolTip("white")
            self.inputs[23] = -1

    def on_pixel_30_clicked(self):
        if self.pixels[24].toolTip() == "white":
            self.pixels[24].setIcon(self.black)
            self.pixels[24].setToolTip("black")
            self.inputs[24] = 1
        else:
            self.pixels[24].setIcon(self.white)
            self.pixels[24].setToolTip("white")
            self.inputs[24] = -1

    def on_pixel_31_clicked(self):
        if self.pixels[25].toolTip() == "white":
            self.pixels[25].setIcon(self.black)
            self.pixels[25].setToolTip("black")
            self.inputs[25] = 1
        else:
            self.pixels[25].setIcon(self.white)
            self.pixels[25].setToolTip("white")
            self.inputs[25] = -1

    def on_pixel_32_clicked(self):
        if self.pixels[26].toolTip() == "white":
            self.pixels[26].setIcon(self.black)
            self.pixels[26].setToolTip("black")
            self.inputs[26] = 1
        else:
            self.pixels[26].setIcon(self.white)
            self.pixels[26].setToolTip("white")
            self.inputs[26] = -1

    def on_pixel_33_clicked(self):
        if self.pixels[27].toolTip() == "white":
            self.pixels[27].setIcon(self.black)
            self.pixels[27].setToolTip("black")
            self.inputs[27] = 1
        else:
            self.pixels[27].setIcon(self.white)
            self.pixels[27].setToolTip("white")
            self.inputs[27] = -1

    def on_pixel_34_clicked(self):
        if self.pixels[28].toolTip() == "white":
            self.pixels[28].setIcon(self.black)
            self.pixels[28].setToolTip("black")
            self.inputs[28] = 1
        else:
            self.pixels[28].setIcon(self.white)
            self.pixels[28].setToolTip("white")
            self.inputs[28] = -1

    def on_pixel_35_clicked(self):
        if self.pixels[29].toolTip() == "white":
            self.pixels[29].setIcon(self.black)
            self.pixels[29].setToolTip("black")
            self.inputs[29] = 1
        else:
            self.pixels[29].setIcon(self.white)
            self.pixels[29].setToolTip("white")
            self.inputs[29] = -1

    def on_pixel_36_clicked(self):
        if self.pixels[30].toolTip() == "white":
            self.pixels[30].setIcon(self.black)
            self.pixels[30].setToolTip("black")
            self.inputs[30] = 1
        else:
            self.pixels[30].setIcon(self.white)
            self.pixels[30].setToolTip("white")
            self.inputs[30] = -1

    def on_pixel_37_clicked(self):
        if self.pixels[31].toolTip() == "white":
            self.pixels[31].setIcon(self.black)
            self.pixels[31].setToolTip("black")
            self.inputs[31] = 1
        else:
            self.pixels[31].setIcon(self.white)
            self.pixels[31].setToolTip("white")
            self.inputs[31] = -1

    def on_pixel_40_clicked(self):
        if self.pixels[32].toolTip() == "white":
            self.pixels[32].setIcon(self.black)
            self.pixels[32].setToolTip("black")
            self.inputs[32] = 1
        else:
            self.pixels[32].setIcon(self.white)
            self.pixels[32].setToolTip("white")
            self.inputs[32] = -1

    def on_pixel_41_clicked(self):
        if self.pixels[33].toolTip() == "white":
            self.pixels[33].setIcon(self.black)
            self.pixels[33].setToolTip("black")
            self.inputs[33] = 1
        else:
            self.pixels[33].setIcon(self.white)
            self.pixels[33].setToolTip("white")
            self.inputs[33] = -1

    def on_pixel_42_clicked(self):
        if self.pixels[34].toolTip() == "white":
            self.pixels[34].setIcon(self.black)
            self.pixels[34].setToolTip("black")
            self.inputs[34] = 1
        else:
            self.pixels[34].setIcon(self.white)
            self.pixels[34].setToolTip("white")
            self.inputs[34] = -1

    def on_pixel_43_clicked(self):
        if self.pixels[35].toolTip() == "white":
            self.pixels[35].setIcon(self.black)
            self.pixels[35].setToolTip("black")
            self.inputs[35] = 1
        else:
            self.pixels[35].setIcon(self.white)
            self.pixels[35].setToolTip("white")
            self.inputs[35] = -1

    def on_pixel_44_clicked(self):
        if self.pixels[36].toolTip() == "white":
            self.pixels[36].setIcon(self.black)
            self.pixels[36].setToolTip("black")
            self.inputs[36] = 1
        else:
            self.pixels[36].setIcon(self.white)
            self.pixels[36].setToolTip("white")
            self.inputs[36] = -1

    def on_pixel_45_clicked(self):
        if self.pixels[37].toolTip() == "white":
            self.pixels[37].setIcon(self.black)
            self.pixels[37].setToolTip("black")
            self.inputs[37] = 1
        else:
            self.pixels[37].setIcon(self.white)
            self.pixels[37].setToolTip("white")
            self.inputs[37] = -1

    def on_pixel_46_clicked(self):
        if self.pixels[38].toolTip() == "white":
            self.pixels[38].setIcon(self.black)
            self.pixels[38].setToolTip("black")
            self.inputs[38] = 1
        else:
            self.pixels[38].setIcon(self.white)
            self.pixels[38].setToolTip("white")
            self.inputs[38] = -1

    def on_pixel_47_clicked(self):
        if self.pixels[39].toolTip() == "white":
            self.pixels[39].setIcon(self.black)
            self.pixels[39].setToolTip("black")
            self.inputs[39] = 1
        else:
            self.pixels[39].setIcon(self.white)
            self.pixels[39].setToolTip("white")
            self.inputs[39] = -1

    def on_pixel_50_clicked(self):
        if self.pixels[40].toolTip() == "white":
            self.pixels[40].setIcon(self.black)
            self.pixels[40].setToolTip("black")
            self.inputs[40] = 1
        else:
            self.pixels[40].setIcon(self.white)
            self.pixels[40].setToolTip("white")
            self.inputs[40] = -1

    def on_pixel_51_clicked(self):
        if self.pixels[41].toolTip() == "white":
            self.pixels[41].setIcon(self.black)
            self.pixels[41].setToolTip("black")
            self.inputs[41] = 1
        else:
            self.pixels[41].setIcon(self.white)
            self.pixels[41].setToolTip("white")
            self.inputs[41] = -1

    def on_pixel_52_clicked(self):
        if self.pixels[42].toolTip() == "white":
            self.pixels[42].setIcon(self.black)
            self.pixels[42].setToolTip("black")
            self.inputs[42] = 1
        else:
            self.pixels[42].setIcon(self.white)
            self.pixels[42].setToolTip("white")
            self.inputs[42] = -1

    def on_pixel_53_clicked(self):
        if self.pixels[43].toolTip() == "white":
            self.pixels[43].setIcon(self.black)
            self.pixels[43].setToolTip("black")
            self.inputs[43] = 1
        else:
            self.pixels[43].setIcon(self.white)
            self.pixels[43].setToolTip("white")
            self.inputs[43] = -1

    def on_pixel_54_clicked(self):
        if self.pixels[44].toolTip() == "white":
            self.pixels[44].setIcon(self.black)
            self.pixels[44].setToolTip("black")
            self.inputs[44] = 1
        else:
            self.pixels[44].setIcon(self.white)
            self.pixels[44].setToolTip("white")
            self.inputs[44] = -1

    def on_pixel_55_clicked(self):
        if self.pixels[45].toolTip() == "white":
            self.pixels[45].setIcon(self.black)
            self.pixels[45].setToolTip("black")
            self.inputs[45] = 1
        else:
            self.pixels[45].setIcon(self.white)
            self.pixels[45].setToolTip("white")
            self.inputs[45] = -1

    def on_pixel_56_clicked(self):
        if self.pixels[46].toolTip() == "white":
            self.pixels[46].setIcon(self.black)
            self.pixels[46].setToolTip("black")
            self.inputs[46] = 1
        else:
            self.pixels[46].setIcon(self.white)
            self.pixels[46].setToolTip("white")
            self.inputs[46] = -1

    def on_pixel_57_clicked(self):
        if self.pixels[47].toolTip() == "white":
            self.pixels[47].setIcon(self.black)
            self.pixels[47].setToolTip("black")
            self.inputs[47] = 1
        else:
            self.pixels[47].setIcon(self.white)
            self.pixels[47].setToolTip("white")
            self.inputs[47] = -1

    def on_pixel_60_clicked(self):
        if self.pixels[48].toolTip() == "white":
            self.pixels[48].setIcon(self.black)
            self.pixels[48].setToolTip("black")
            self.inputs[48] = 1
        else:
            self.pixels[48].setIcon(self.white)
            self.pixels[48].setToolTip("white")
            self.inputs[48] = -1

    def on_pixel_61_clicked(self):
        if self.pixels[49].toolTip() == "white":
            self.pixels[49].setIcon(self.black)
            self.pixels[49].setToolTip("black")
            self.inputs[49] = 1
        else:
            self.pixels[49].setIcon(self.white)
            self.pixels[49].setToolTip("white")
            self.inputs[49] = -1

    def on_pixel_62_clicked(self):
        if self.pixels[50].toolTip() == "white":
            self.pixels[50].setIcon(self.black)
            self.pixels[50].setToolTip("black")
            self.inputs[50] = 1
        else:
            self.pixels[50].setIcon(self.white)
            self.pixels[50].setToolTip("white")
            self.inputs[50] = -1

    def on_pixel_63_clicked(self):
        if self.pixels[51].toolTip() == "white":
            self.pixels[51].setIcon(self.black)
            self.pixels[51].setToolTip("black")
            self.inputs[51] = 1
        else:
            self.pixels[51].setIcon(self.white)
            self.pixels[51].setToolTip("white")
            self.inputs[51] = -1

    def on_pixel_64_clicked(self):
        if self.pixels[52].toolTip() == "white":
            self.pixels[52].setIcon(self.black)
            self.pixels[52].setToolTip("black")
            self.inputs[52] = 1
        else:
            self.pixels[52].setIcon(self.white)
            self.pixels[52].setToolTip("white")
            self.inputs[52] = -1

    def on_pixel_65_clicked(self):
        if self.pixels[53].toolTip() == "white":
            self.pixels[53].setIcon(self.black)
            self.pixels[53].setToolTip("black")
            self.inputs[53] = 1
        else:
            self.pixels[53].setIcon(self.white)
            self.pixels[53].setToolTip("white")
            self.inputs[53] = -1

    def on_pixel_66_clicked(self):
        if self.pixels[54].toolTip() == "white":
            self.pixels[54].setIcon(self.black)
            self.pixels[54].setToolTip("black")
            self.inputs[54] = 1
        else:
            self.pixels[54].setIcon(self.white)
            self.pixels[54].setToolTip("white")
            self.inputs[54] = -1

    def on_pixel_67_clicked(self):
        if self.pixels[55].toolTip() == "white":
            self.pixels[55].setIcon(self.black)
            self.pixels[55].setToolTip("black")
            self.inputs[55] = 1
        else:
            self.pixels[55].setIcon(self.white)
            self.pixels[55].setToolTip("white")
            self.inputs[55] = -1

    def on_pixel_70_clicked(self):
        if self.pixels[56].toolTip() == "white":
            self.pixels[56].setIcon(self.black)
            self.pixels[56].setToolTip("black")
            self.inputs[56] = 1
        else:
            self.pixels[56].setIcon(self.white)
            self.pixels[56].setToolTip("white")
            self.inputs[56] = -1

    def on_pixel_71_clicked(self):
        if self.pixels[57].toolTip() == "white":
            self.pixels[57].setIcon(self.black)
            self.pixels[57].setToolTip("black")
            self.inputs[57] = 1
        else:
            self.pixels[57].setIcon(self.white)
            self.pixels[57].setToolTip("white")
            self.inputs[57] = -1

    def on_pixel_72_clicked(self):
        if self.pixels[58].toolTip() == "white":
            self.pixels[58].setIcon(self.black)
            self.pixels[58].setToolTip("black")
            self.inputs[58] = 1
        else:
            self.pixels[58].setIcon(self.white)
            self.pixels[58].setToolTip("white")
            self.inputs[58] = -1

    def on_pixel_73_clicked(self):
        if self.pixels[59].toolTip() == "white":
            self.pixels[59].setIcon(self.black)
            self.pixels[59].setToolTip("black")
            self.inputs[59] = 1
        else:
            self.pixels[59].setIcon(self.white)
            self.pixels[59].setToolTip("white")
            self.inputs[59] = -1

    def on_pixel_74_clicked(self):
        if self.pixels[60].toolTip() == "white":
            self.pixels[60].setIcon(self.black)
            self.pixels[60].setToolTip("black")
            self.inputs[60] = 1
        else:
            self.pixels[60].setIcon(self.white)
            self.pixels[60].setToolTip("white")
            self.inputs[60] = -1

    def on_pixel_75_clicked(self):
        if self.pixels[61].toolTip() == "white":
            self.pixels[61].setIcon(self.black)
            self.pixels[61].setToolTip("black")
            self.inputs[61] = 1
        else:
            self.pixels[61].setIcon(self.white)
            self.pixels[61].setToolTip("white")
            self.inputs[61] = -1

    def on_pixel_76_clicked(self):
        if self.pixels[62].toolTip() == "white":
            self.pixels[62].setIcon(self.black)
            self.pixels[62].setToolTip("black")
            self.inputs[62] = 1
        else:
            self.pixels[62].setIcon(self.white)
            self.pixels[62].setToolTip("white")
            self.inputs[62] = -1

    def on_pixel_77_clicked(self):
        if self.pixels[63].toolTip() == "white":
            self.pixels[63].setIcon(self.black)
            self.pixels[63].setToolTip("black")
            self.inputs[63] = 1
        else:
            self.pixels[63].setIcon(self.white)
            self.pixels[63].setToolTip("white")
            self.inputs[63] = -1

    def on_pixel_80_clicked(self):
        if self.pixels[64].toolTip() == "white":
            self.pixels[64].setIcon(self.black)
            self.pixels[64].setToolTip("black")
            self.inputs[64] = 1
        else:
            self.pixels[64].setIcon(self.white)
            self.pixels[64].setToolTip("white")
            self.inputs[64] = -1

    def on_pixel_81_clicked(self):
        if self.pixels[65].toolTip() == "white":
            self.pixels[65].setIcon(self.black)
            self.pixels[65].setToolTip("black")
            self.inputs[65] = 1
        else:
            self.pixels[65].setIcon(self.white)
            self.pixels[65].setToolTip("white")
            self.inputs[65] = -1

    def on_pixel_82_clicked(self):
        if self.pixels[66].toolTip() == "white":
            self.pixels[66].setIcon(self.black)
            self.pixels[66].setToolTip("black")
            self.inputs[66] = 1
        else:
            self.pixels[66].setIcon(self.white)
            self.pixels[66].setToolTip("white")
            self.inputs[66] = -1

    def on_pixel_83_clicked(self):
        if self.pixels[67].toolTip() == "white":
            self.pixels[67].setIcon(self.black)
            self.pixels[67].setToolTip("black")
            self.inputs[67] = 1
        else:
            self.pixels[67].setIcon(self.white)
            self.pixels[67].setToolTip("white")
            self.inputs[67] = -1

    def on_pixel_84_clicked(self):
        if self.pixels[68].toolTip() == "white":
            self.pixels[68].setIcon(self.black)
            self.pixels[68].setToolTip("black")
            self.inputs[68] = 1
        else:
            self.pixels[68].setIcon(self.white)
            self.pixels[68].setToolTip("white")
            self.inputs[68] = -1

    def on_pixel_85_clicked(self):
        if self.pixels[69].toolTip() == "white":
            self.pixels[69].setIcon(self.black)
            self.pixels[69].setToolTip("black")
            self.inputs[69] = 1
        else:
            self.pixels[69].setIcon(self.white)
            self.pixels[69].setToolTip("white")
            self.inputs[69] = -1

    def on_pixel_86_clicked(self):
        if self.pixels[70].toolTip() == "white":
            self.pixels[70].setIcon(self.black)
            self.pixels[70].setToolTip("black")
            self.inputs[70] = 1
        else:
            self.pixels[70].setIcon(self.white)
            self.pixels[70].setToolTip("white")
            self.inputs[70] = -1

    def on_pixel_87_clicked(self):
        if self.pixels[71].toolTip() == "white":
            self.pixels[71].setIcon(self.black)
            self.pixels[71].setToolTip("black")
            self.inputs[71] = 1
        else:
            self.pixels[71].setIcon(self.white)
            self.pixels[71].setToolTip("white")
            self.inputs[71] = -1

    def on_pixel_90_clicked(self):
        if self.pixels[72].toolTip() == "white":
            self.pixels[72].setIcon(self.black)
            self.pixels[72].setToolTip("black")
            self.inputs[72] = 1
        else:
            self.pixels[72].setIcon(self.white)
            self.pixels[72].setToolTip("white")
            self.inputs[72] = -1

    def on_pixel_91_clicked(self):
        if self.pixels[73].toolTip() == "white":
            self.pixels[73].setIcon(self.black)
            self.pixels[73].setToolTip("black")
            self.inputs[73] = 1
        else:
            self.pixels[73].setIcon(self.white)
            self.pixels[73].setToolTip("white")
            self.inputs[73] = -1

    def on_pixel_92_clicked(self):
        if self.pixels[74].toolTip() == "white":
            self.pixels[74].setIcon(self.black)
            self.pixels[74].setToolTip("black")
            self.inputs[74] = 1
        else:
            self.pixels[74].setIcon(self.white)
            self.pixels[74].setToolTip("white")
            self.inputs[74] = -1

    def on_pixel_93_clicked(self):
        if self.pixels[75].toolTip() == "white":
            self.pixels[75].setIcon(self.black)
            self.pixels[75].setToolTip("black")
            self.inputs[75] = 1
        else:
            self.pixels[75].setIcon(self.white)
            self.pixels[75].setToolTip("white")
            self.inputs[75] = -1

    def on_pixel_94_clicked(self):
        if self.pixels[76].toolTip() == "white":
            self.pixels[76].setIcon(self.black)
            self.pixels[76].setToolTip("black")
            self.inputs[76] = 1
        else:
            self.pixels[76].setIcon(self.white)
            self.pixels[76].setToolTip("white")
            self.inputs[76] = -1

    def on_pixel_95_clicked(self):
        if self.pixels[77].toolTip() == "white":
            self.pixels[77].setIcon(self.black)
            self.pixels[77].setToolTip("black")
            self.inputs[77] = 1
        else:
            self.pixels[77].setIcon(self.white)
            self.pixels[77].setToolTip("white")
            self.inputs[77] = -1

    def on_pixel_96_clicked(self):
        if self.pixels[78].toolTip() == "white":
            self.pixels[78].setIcon(self.black)
            self.pixels[78].setToolTip("black")
            self.inputs[78] = 1
        else:
            self.pixels[78].setIcon(self.white)
            self.pixels[78].setToolTip("white")
            self.inputs[78] = -1

    def on_pixel_97_clicked(self):
        if self.pixels[79].toolTip() == "white":
            self.pixels[79].setIcon(self.black)
            self.pixels[79].setToolTip("black")
            self.inputs[79] = 1
        else:
            self.pixels[79].setIcon(self.white)
            self.pixels[79].setToolTip("white")
            self.inputs[79] = -1
    
    def on_run_pushbutton_clicked(self):
        # if self.neutral_network == []:
        #     QMessageBox.warning(QMessageBox(), "Aviso", "Execute o treinamento")
        #     return
        print("Run clicked")
        print(self.training_set[0][2][0]) # [0-9] font A [0-9] numbers [0] inputs
        print(self.training_set[19][2][0]) # [10-19] font J [0-9] numbers [0] inputs

    def on_train_pushbutton_clicked(self):
        i = 0
        for n in range(10):
            print (self.inputs [i:i+8])
            i += 8
        print('gime space')

    def populate_pixels_list(self):
        # Hard coding: display 10x8
        for i in range(10):
            for j in range(8):
                self.pixels.append(self.window.findChild(
                    QPushButton, "pixel"+str(i+1)+str(j+1)))
                self.pixels[-1].clicked.connect(getattr(self, "on_pixel_" + str(i) + str(j) + "_clicked"))

    def populate_training_set(self, path, font):
        f = open(path).readlines()
        aux = []
        for line in f:
            if line.startswith("#"):
                if aux:
                    font.append(list(aux))
                aux = []
            else:
                for x in line.split(","):
                    aux.append(int(x))

        # Activation for each Neuron.
        # For example: neuron  #0 must be activated (output = 1) only
        # with the first training pair, corresponding to the number #0.
        # For the other training pairs (of other numbers), this neuron must
        # present output equal to -1.
        for i in range(NUM_OF_NEURONS):
            aux = []
            for j in range(len(font)):
                if i == j:
                    aux.append((font[j], 1))
                else:
                    aux.append((font[j], -1))
            self.training_set.append(aux)

    def update_display(self):
        for p in range(len(self.pixels)):
            if self.inputs[p] == 1:
                self.pixels[p].setIcon(self.black)
                self.pixels[p].setToolTip("black")
            else:
                self.pixels[p].setIcon(self.white)
                self.pixels[p].setToolTip("white")

        

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    gui = Gui()

    #.