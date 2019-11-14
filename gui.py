import logging
import sys
import os

from PySide2.QtWidgets import QDialog, QApplication, QFileDialog
from PySide2.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout
from PySide2.QtWidgets import QLineEdit, QLabel, QPushButton, QDoubleSpinBox, QSpinBox, QMessageBox
from PySide2.QtCore import Slot, Qt
from PySide2.QtGui import QFontMetrics

class Hackgui(QDialog):
    seismic_file_name = None
    seismic_data = None
    data = None
    def __init__(self, parent=None):
        """Constructor"""
        super(Hackgui, self).__init__(parent)
        self.setWindowTitle("Trace Infill")
        self.setMinimumSize(300, 300)

        main_layout = QVBoxLayout()

        main_layout.addLayout(self.create_status_bar())
        main_layout.addLayout(self.run_fill())
        self.setLayout(main_layout)
    def create_status_bar(self):
        input_layout = QHBoxLayout()
        lbl = QLabel("Input ssf:")
        self.seismic_file_name = QLineEdit()
        self.seismic_file_name.setReadOnly(True)
        self.seismic_file_name.setStyleSheet('color: gray; background-color: transparent; border: 1px solid #cccccc')
        load_vt_button = QPushButton('Load ssf')
        load_vt_button.clicked.connect(self.load_ssf)
        input_layout.addWidget(lbl)
        input_layout.addWidget(self.seismic_file_name)
        input_layout.addWidget(load_vt_button)
        return input_layout
    def load_ssf(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open ssf",
                                                   "..",
                                                   "ssf (*.ssf)")
        if os.path.isfile(file_name):
            #self.post_status(f'Loading Seismic ssf: {file_name}')
            self.seismic_file_name.setText(file_name)
            self.seismic_data = self.load_data()
            #self.post_status(f'Loading Seismic Complete')

        else:
            self.seismic_file_name.setText(self.not_loaded_text)
            self.seismic_data = None
    def load_data(self):
        #/glb/am/sepco/seis/epw_ua_seisproc_scratch_0034/jpdata/epw_imaging/saltcrawler_18/Engin_Alkan/FOR_CHRISTIAN
        vt = GeoIoVolume(seismic_file_name) #change code for ssf to numpy
        data = vt.get_float()
        return self.data
    def run_fill(self):
        input_layout = QHBoxLayout()
        run_alg = QPushButton('Run')
        run_alg.clicked.connect(self.execute)
        input_layout.addWidget(run_alg)
        return input_layout
    def execute(self):
        pass
        
app = QApplication([])
form = Hackgui()
form.show()
sys.exit(app.exec_())
