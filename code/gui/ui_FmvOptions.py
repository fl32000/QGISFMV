# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_FmvOptions.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OptionsDialog(object):

    def setupUi(self, OptionsDialog):
        OptionsDialog.setObjectName("OptionsDialog")
        OptionsDialog.resize(461, 561)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imgFMV/images/custom-options.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        OptionsDialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(OptionsDialog)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(OptionsDialog)
        self.tabWidget.setObjectName("tabWidget")
        self.Magnifier_tab = QtWidgets.QWidget()
        self.Magnifier_tab.setObjectName("Magnifier_tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Magnifier_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.Magnifier_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.sl_Size = QtWidgets.QSlider(self.Magnifier_tab)
        self.sl_Size.setMinimum(100)
        self.sl_Size.setMaximum(500)
        self.sl_Size.setSliderPosition(250)
        self.sl_Size.setOrientation(QtCore.Qt.Horizontal)
        self.sl_Size.setObjectName("sl_Size")
        self.verticalLayout_2.addWidget(self.sl_Size)
        self.label_2 = QtWidgets.QLabel(self.Magnifier_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.sb_factor = QtWidgets.QSpinBox(self.Magnifier_tab)
        self.sb_factor.setMinimum(2)
        self.sb_factor.setMaximum(5)
        self.sb_factor.setObjectName("sb_factor")
        self.verticalLayout_2.addWidget(self.sb_factor)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.Magnifier_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.rB_Square_m = QtWidgets.QRadioButton(self.Magnifier_tab)
        self.rB_Square_m.setObjectName("rB_Square_m")
        self.gridLayout_3.addWidget(self.rB_Square_m, 0, 1, 1, 1)
        self.rB_Circle_m = QtWidgets.QRadioButton(self.Magnifier_tab)
        self.rB_Circle_m.setChecked(True)
        self.rB_Circle_m.setObjectName("rB_Circle_m")
        self.gridLayout_3.addWidget(self.rB_Circle_m, 0, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.tabWidget.addTab(self.Magnifier_tab, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("QGroupBox { font-weight: bold; }")
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.poly_width = QtWidgets.QSpinBox(self.groupBox)
        self.poly_width.setMinimum(1)
        self.poly_width.setMaximum(10)
        self.poly_width.setProperty("value", 3)
        self.poly_width.setObjectName("poly_width")
        self.horizontalLayout_4.addWidget(self.poly_width)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        self.poly_pen = gui.QgsColorButton(self.groupBox)
        self.poly_pen.setColor(QtGui.QColor(252, 215, 108))
        self.poly_pen.setAllowOpacity(True)
        self.poly_pen.setDefaultColor(QtGui.QColor(252, 215, 108))
        self.poly_pen.setObjectName("poly_pen")
        self.horizontalLayout_4.addWidget(self.poly_pen)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        self.poly_brush = gui.QgsColorButton(self.groupBox)
        self.poly_brush.setColor(QtGui.QColor(252, 215, 108, 100))
        self.poly_brush.setAllowOpacity(True)
        self.poly_brush.setDefaultColor(QtGui.QColor(252, 215, 108, 100))
        self.poly_brush.setObjectName("poly_brush")
        self.horizontalLayout_3.addWidget(self.poly_brush)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setStyleSheet("QGroupBox { font-weight: bold; }")
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.point_width = QtWidgets.QSpinBox(self.groupBox_2)
        self.point_width.setMinimum(1)
        self.point_width.setMaximum(20)
        self.point_width.setProperty("value", 10)
        self.point_width.setObjectName("point_width")
        self.horizontalLayout_7.addWidget(self.point_width)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.point_pen = gui.QgsColorButton(self.groupBox_2)
        self.point_pen.setColor(QtGui.QColor(220, 20, 60))
        self.point_pen.setAllowOpacity(True)
        self.point_pen.setDefaultColor(QtGui.QColor(220, 20, 60))
        self.point_pen.setObjectName("point_pen")
        self.horizontalLayout_7.addWidget(self.point_pen)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setStyleSheet("QGroupBox { font-weight: bold; }")
        self.groupBox_3.setFlat(True)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.lines_width = QtWidgets.QSpinBox(self.groupBox_3)
        self.lines_width.setMinimum(1)
        self.lines_width.setMaximum(10)
        self.lines_width.setProperty("value", 3)
        self.lines_width.setObjectName("lines_width")
        self.horizontalLayout_8.addWidget(self.lines_width)
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_8.addWidget(self.label_12)
        self.lines_pen = gui.QgsColorButton(self.groupBox_3)
        self.lines_pen.setColor(QtGui.QColor(252, 215, 108))
        self.lines_pen.setAllowOpacity(True)
        self.lines_pen.setDefaultColor(QtGui.QColor(252, 215, 108))
        self.lines_pen.setObjectName("lines_pen")
        self.horizontalLayout_8.addWidget(self.lines_pen)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_4.setStyleSheet("QGroupBox { font-weight: bold; }")
        self.groupBox_4.setFlat(True)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.measures_width = QtWidgets.QSpinBox(self.groupBox_4)
        self.measures_width.setMinimum(1)
        self.measures_width.setMaximum(10)
        self.measures_width.setProperty("value", 3)
        self.measures_width.setObjectName("measures_width")
        self.horizontalLayout_6.addWidget(self.measures_width)
        self.label_14 = QtWidgets.QLabel(self.groupBox_4)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_6.addWidget(self.label_14)
        self.measures_pen = gui.QgsColorButton(self.groupBox_4)
        self.measures_pen.setColor(QtGui.QColor(185, 224, 175))
        self.measures_pen.setAllowOpacity(True)
        self.measures_pen.setDefaultColor(QtGui.QColor(185, 224, 175))
        self.measures_pen.setObjectName("measures_pen")
        self.horizontalLayout_6.addWidget(self.measures_pen)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_13 = QtWidgets.QLabel(self.groupBox_4)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_5.addWidget(self.label_13)
        self.measures_brush = gui.QgsColorButton(self.groupBox_4)
        self.measures_brush.setColor(QtGui.QColor(185, 224, 175, 100))
        self.measures_brush.setAllowOpacity(True)
        self.measures_brush.setDefaultColor(QtGui.QColor(185, 224, 175, 100))
        self.measures_brush.setObjectName("measures_brush")
        self.horizontalLayout_5.addWidget(self.measures_brush)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3.addWidget(self.groupBox_4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pushButton = QtWidgets.QPushButton(OptionsDialog)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(OptionsDialog)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton.pressed.connect(OptionsDialog.SaveOptions)
        self.sl_Size.sliderMoved['int'].connect(OptionsDialog.showSizeTip)
        QtCore.QMetaObject.connectSlotsByName(OptionsDialog)

    def retranslateUi(self, OptionsDialog):
        _translate = QtCore.QCoreApplication.translate
        OptionsDialog.setWindowTitle(_translate("OptionsDialog", "Options"))
        self.label_3.setText(_translate("OptionsDialog", "Maximum size in pixels"))
        self.label_2.setText(_translate("OptionsDialog", "Magnification factor"))
        self.label.setText(_translate("OptionsDialog", "Shape "))
        self.rB_Square_m.setText(_translate("OptionsDialog", "Square"))
        self.rB_Circle_m.setText(_translate("OptionsDialog", "Circle"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Magnifier_tab), _translate("OptionsDialog", "Magnifier"))
        self.groupBox.setTitle(_translate("OptionsDialog", "Polygons"))
        self.label_4.setText(_translate("OptionsDialog", "Width"))
        self.label_10.setText(_translate("OptionsDialog", "Pen Color"))
        self.label_11.setText(_translate("OptionsDialog", "brush Color"))
        self.groupBox_2.setTitle(_translate("OptionsDialog", "Points"))
        self.label_5.setText(_translate("OptionsDialog", "Width"))
        self.label_8.setText(_translate("OptionsDialog", "Pen Color"))
        self.groupBox_3.setTitle(_translate("OptionsDialog", "Lines"))
        self.label_6.setText(_translate("OptionsDialog", "Width"))
        self.label_12.setText(_translate("OptionsDialog", "Pen Color"))
        self.groupBox_4.setTitle(_translate("OptionsDialog", "Measures"))
        self.label_7.setText(_translate("OptionsDialog", "Width"))
        self.label_14.setText(_translate("OptionsDialog", "Pen Color"))
        self.label_13.setText(_translate("OptionsDialog", "brush Color"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("OptionsDialog", "Drawings"))
        self.pushButton.setText(_translate("OptionsDialog", "Accept"))


from qgis import gui
from QGIS_FMV.gui import resources_rc
