#!/usr/bin/python
# -*- coding: utf-8 -*-
##import modules
#CREATE TREE UI
import toolutils
import soptoolutils
import sys
from PySide import QtGui, QtCore
import hou


# create Gui

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(1020, 250, 370, 500)
        self.setWindowTitle('TREE MAKER')
        self.setWindowIcon(QtGui.QIcon('/SCORPION/PYTHON/TREE_PAINTING/christmas-icon-tree-128.png'
                           ))
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setStyleSheet('QMainWindow{background-color:rgb(60, 60, 60)}'
                           )

        self.tree_image_label = QtGui.QLabel(self)
        self.tree_image_label.setGeometry(20, 0, 370, 500)
        self.tree_image_label.setPixmap(QtGui.QPixmap('/SCORPION/PYTHON/TREE_PAINTING/bg/tree_edited7.png'
                                        ))

        self.grnd_path_label = QtGui.QLabel('GROUND PATH', self)
        self.grnd_path_label.setGeometry(5, 120, 200, 30)
        self.grnd_path_label.setStyleSheet('QLabel{color:rgb(200,80,80)}'
                                           )

        self.grnd_path = QtGui.QLineEdit(self)
        self.grnd_path.setGeometry(100, 120, 190, 25)
        self.grnd_path_val()
        self.grnd_path.textChanged.connect(self.set_obj_mrg_path_text_input)
        self.grnd_path.setStyleSheet('QLineEdit{background-color:rgb(170,170,170);color:rgb(102,51,0);border:rgb(170,170,170)}'
                                     )

# CREATE BUTTONS

        self.grnd_path_btn = QtGui.QPushButton('SELECT GROUND', self)
        self.grnd_path_btn.setGeometry(10, 180, 140, 25)
        self.grnd_path_btn.clicked.connect(self.tree_viewer)
        self.grnd_path_btn.setStyleSheet('QPushButton{background-color:rgb(170,170,170);color:rgb(102,51,0)}'
                                         )                   

        self.confirm_btn = QtGui.QPushButton('CONFIRM', self)
        self.confirm_btn.setGeometry(154, 180, 80, 25)
        self.confirm_btn.clicked.connect(self.set_obj_mrg_path)
        self.confirm_btn.setStyleSheet('QPushButton{background-color:rgb(170,170,170);color:rgb(102,51,0)}'
                                       )

        self.paint_btn = QtGui.QPushButton('PAINT GROUND', self)
        self.paint_btn.setGeometry(10, 210, 110, 25)
        self.paint_btn.clicked.connect(self.paint_the_ground)
        self.paint_btn.setStyleSheet('QPushButton{background-color:rgb(170,170,170);color:rgb(102,51,0)}'
                                     )

        self.image_select_btn = QtGui.QPushButton('SELECT IMAGE', self)
        self.image_select_btn.setGeometry(124, 210, 110, 25)
        self.image_select_btn.clicked.connect(self.open_image)
        self.image_select_btn.setStyleSheet('QPushButton{background-color:rgb(170,170,170);color:rgb(102,51,0)}'
                                            )

        self.reset_btn = QtGui.QPushButton('RESET ALL', self)
        self.reset_btn.setGeometry(10, 240, 140, 25)
        self.reset_btn.clicked.connect(self.reset_all)
        self.reset_btn.setStyleSheet('QPushButton{background-color:rgb(170,170,170);color:rgb(102,51,0)}'
                                     )

# CREATE PARM LABEL

        self.tree_length_label = QtGui.QLabel('TREE HEIGHT', self)
        self.tree_length_label.setStyleSheet('QLabel{color:rgb(200,80,80)}'
                                             )
        self.tree_length_label.setGeometry(7, 290, 250, 30)

        self.fruits_label = QtGui.QLabel('ON/OFF FRUIT', self)
        self.fruits_label.setStyleSheet('QLabel{color:rgb(200,80,80)}')
        self.fruits_label.setGeometry(5, 320, 150, 30)

        self.tree_orint_label = QtGui.QLabel('ORIENTATION', self)
        self.tree_orint_label.setGeometry(9, 350, 250, 30)
        self.tree_orint_label.setStyleSheet('QLabel{color:rgb(200,80,80)}'
                                            )

        self.trunk_width_label = QtGui.QLabel('TRUNK WIDTH', self)
        self.trunk_width_label.setStyleSheet('QLabel{color:rgb(200,80,80)}'
                                             )
        self.trunk_width_label.setGeometry(5, 380, 250, 30)

# CREATE SLIDER

        self.tree_length_slider = QtGui.QSlider(self)
        self.tree_length_slider.setOrientation(QtCore.Qt.Horizontal)
        self.tree_length_slider.setGeometry(95, 300, 100, 8)
        self.tree_length_slider.setRange(0, 500)
        self.tree_length_slider.valueChanged.connect(self.tree_length_change)
        self.set_tree_length_slider_value()

        self.fruit_slider = QtGui.QSlider(self)
        self.fruit_slider.setOrientation(QtCore.Qt.Horizontal)
        self.fruit_slider.setGeometry(95, 330, 100, 8)
        self.fruit_slider.setRange(0, 1)
        self.fruit_slider.valueChanged.connect(self.fruit_change)
        self.set_fruit_slider_value()

        self.tree_orientation_slider = QtGui.QSlider(self)
        self.tree_orientation_slider.setOrientation(QtCore.Qt.Horizontal)
        self.tree_orientation_slider.setGeometry(95, 360, 100, 8)
        self.tree_orientation_slider.setRange(0, 10)
        self.tree_orientation_slider.valueChanged.connect(self.tree_orientation_change)
        self.set_tree_orientation_slider_value()

        self.trunk_width_slider = QtGui.QSlider(self)
        self.trunk_width_slider.setOrientation(QtCore.Qt.Horizontal)
        self.trunk_width_slider.setGeometry(95, 390, 100, 8)
        self.trunk_width_slider.setRange(0, 1000)
        self.trunk_width_slider.valueChanged.connect(self.trunk_width_change)
        self.set_trunk_width_slider_value()

# CREATE VALUE BOX

        self.tree_length_val = QtGui.QDoubleSpinBox(self)
        self.tree_length_val.setGeometry(200, 290, 50, 25)
        self.tree_length_val.setStyleSheet('QDoubleSpinBox{background-color:rgb(170,170,170);color:rgb(102,51,0)}'
                                           )
        self.tree_length_val_set()

        self.fruit_slider_val = QtGui.QSpinBox(self)
        self.fruit_slider_val.setGeometry(200, 320, 50, 25)
        self.fruit_slider_val.setStyleSheet('QSpinBox{background-color:rgb(170,170,170);color:rgb(102,51,0)}'
                                            )
        self.fruit_slider_val_set()

        self.tree_orientation_val = QtGui.QSpinBox(self)
        self.tree_orientation_val.setGeometry(200, 350, 50, 25)
        self.tree_orientation_val.setStyleSheet('QSpinBox{background-color:rgb(170,170,170);color:rgb(102,51,0)}'
                                                )
        self.tree_orientation_val_set()

        self.trunk_width_val = QtGui.QDoubleSpinBox(self)
        self.trunk_width_val.setGeometry(200, 380, 50, 25)
        self.trunk_width_val.setStyleSheet('QDoubleSpinBox{background-color:rgb(170,170,170);color:rgb(102,51,0)}'
                                           )
        self.trunk_width_val_set()

# CREATE RADIO BUTTON

        self.pscale = QtGui.QCheckBox(self)
        self.pscale.setGeometry(130, 420, 25, 25)

        self.pscale.stateChanged.connect(self.p_scale)

        self.orint = QtGui.QCheckBox(self)
        self.orint.setGeometry(130, 450, 25, 25)
        self.orint.stateChanged.connect(self.o_rient)

# CREATE RADIO BUTTON LABEL

        self.pscale.label = QtGui.QLabel('RANDOM HEIGHT', self)
        self.pscale.label.setStyleSheet('QLabel{color:rgb(200,80,80)}')
        self.pscale.label.setGeometry(5, 420, 100, 30)
        self.pscale.label = QtGui.QLabel('RANDOM ORIENT', self)
        self.pscale.label.setStyleSheet('QLabel{color:rgb(200,80,80)}')
        self.pscale.label.setGeometry(5, 450, 100, 30)

    def tree_length_val_set(self):
        h = self.tree_length_slider.value()
        height = h / 100.00
        self.tree_length_val.setValue(height)

    def fruit_slider_val_set(self):
        fruit = self.fruit_slider.value()
        self.fruit_slider_val.setValue(fruit)

    def tree_orientation_val_set(self):
        orint = self.tree_orientation_slider.value()
        self.tree_orientation_val.setValue(orint)

    def trunk_width_val_set(self):
        w = self.trunk_width_slider.value()
        width = w / 100.00
        self.trunk_width_val.setValue(width)

    def tree_viewer(self):
        grnd = hou.ui.curDesktop().createFloatingPanel(hou.paneTabType.TreeView)

    def set_obj_mrg_path(self):
        x = hou.selectedNodes()
        grnd = x[0]
        grnd_path = grnd.path()
        self.grnd_path.setText(grnd_path)
        obj_mrg = hou.node('/obj/geo1/GROUND')
        obj_mrg_path = obj_mrg.parm('objpath1')
        obj_mrg_path.set(grnd_path)

    def set_obj_mrg_path_text_input(self):
        path = self.sender().text()
        obj_mrg = hou.node('/obj/geo1/GROUND')
        obj_mrg_path = obj_mrg.parm('objpath1')
        obj_mrg_path.set(path)

    def grnd_path_val(self):
        grnd = hou.node('/obj/geo1/GROUND')
        grnd_path = grnd.parm('objpath1').eval()
        self.grnd_path.setText(grnd_path)

    def paint_the_ground(self):
        paint_node = hou.node('/obj/geo1//paint1')
        paint_node.setSelected(True, True, True)

    def open_image(self):
        switch_input_parm = hou.parm('/obj/geo1//switch2/input')
        switch_input_parm.set(0)
        fl = QtGui.QFileDialog.getOpenFileName()
        image_path = hou.parm('/obj/geo1//vopsop1/cmap')
        image_path.set(fl[0])

    def reset_all(self):
        switch_input_parm = hou.parm('/obj/geo1//switch2/input')
        switch_input_parm.set(1)
        paint_node = hou.node('/obj/geo1//paint1')
        x = hou.parmTuple('/obj/geo1//paint1/fg')
        x[0].set(0)
        x[1].set(0)
        x[2].set(0)
        hou.parm('/obj/geo1//paint1/flood').pressButton()
        y = hou.parmTuple('/obj/geo1//paint1/bg')
        y[0].set(0)
        y[1].set(0)
        y[2].set(0)
        hou.parm('/obj/geo1//paint1/flood').pressButton()

    def tree_length_change(self):
        slider_value = int(self.sender().value())
        treelen = slider_value / 100.00
        tree_length_parm = hou.parm('/obj/deciduoustree1/treesys1_lsystem1_generations'
                                    )
        tree_length_parm.set(treelen)
        self.tree_length_val.setValue(treelen)

    def tree_orientation_change(self):
        slider_value = int(self.sender().value())
        tree_orint_parm = hou.parm('/obj/deciduoustree1/treesys1_lsystem1_randseed')
        tree_orint_parm.set(slider_value)
        self.tree_orientation_val.setValue(slider_value)

    def trunk_width_change(self):
        slider_value = int(self.sender().value())
        trunkwidth = slider_value / 100.00
        trunkwidth_parm = hou.parm('/obj/deciduoustree1/attribcreate7_value1v')
        trunkwidth_parm.set(trunkwidth)
        self.trunk_width_val.setValue(trunkwidth)

    def fruit_change(self):
        slider_value = self.sender().value()
        fruit_parm = hou.parm('/obj/deciduoustree1/treesys1_switch1_input')
        fruit_parm.set(slider_value)
        self.fruit_slider_val.setValue(slider_value)

    def set_tree_length_slider_value(self):
        initial_tree_orint = hou.parm('/obj/deciduoustree1/treesys1_lsystem1_generations'
                                      )
        x = initial_tree_orint.eval() * 100
        self.tree_length_slider.setValue(x)

    def set_tree_orientation_slider_value(self):
        initial_tree_length = hou.parm('/obj/deciduoustree1/treesys1_lsystem1_randseed')
        x = initial_tree_length.eval()
        self.tree_orientation_slider.setValue(x)

    def set_trunk_width_slider_value(self):
        initial_trunkwidth = hou.parm('/obj/deciduoustree1/attribcreate7_value1v')
        x = initial_trunkwidth.eval() * 100
        self.trunk_width_slider.setValue(x)

    def set_fruit_slider_value(self):
        initial_fruit = hou.parm('/obj/deciduoustree1/treesys1_switch1_input')
        x = initial_fruit.eval()
        self.fruit_slider.setValue(x)

    def p_scale(self, state):
        if state == QtCore.Qt.Checked:
            x = hou.parm('/obj/geo1/attribwrangle_pscale/snippet')
            x.set('@pscale=rand(@ptnum)+.3;')
        else:
            x = hou.parm('/obj/geo1/attribwrangle_pscale/snippet')
            x.set('')

    def o_rient(self, state):
        if state == QtCore.Qt.Checked:
            x = hou.parm('/obj/geo1/attribwrangle_rotation/snippet')
            x.set('@P.y-=.2;vector axis = {0,1,0};vector nvec = normalize(axis);float rand = fit01(random(@ptnum+311),0,360);vector4 quat = quaternion(radians(rand), nvec);@orient = qmultiply({0,0,0,1}, quat);'
                  )
        else:

            x = hou.parm('/obj/geo1/attribwrangle_rotation/snippet')
            x.set('')


app = QtGui.QApplication.instance()
dialog = Window()
dialog.show()
