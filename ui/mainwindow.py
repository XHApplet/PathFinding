# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 484)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = CMapFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_4.addWidget(self.plainTextEdit)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.mapBox = QtWidgets.QGroupBox(self.frame_2)
        self.mapBox.setObjectName("mapBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.mapBox)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.mapBox)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.spinBoxW = QtWidgets.QSpinBox(self.mapBox)
        self.spinBoxW.setMinimum(2)
        self.spinBoxW.setMaximum(100)
        self.spinBoxW.setObjectName("spinBoxW")
        self.horizontalLayout_2.addWidget(self.spinBoxW)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.mapBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.spinBoxH = QtWidgets.QSpinBox(self.mapBox)
        self.spinBoxH.setMinimum(2)
        self.spinBoxH.setMaximum(100)
        self.spinBoxH.setObjectName("spinBoxH")
        self.horizontalLayout_3.addWidget(self.spinBoxH)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.create_map = QtWidgets.QPushButton(self.mapBox)
        self.create_map.setObjectName("create_map")
        self.verticalLayout_2.addWidget(self.create_map)
        self.verticalLayout.addWidget(self.mapBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.manhattan = QtWidgets.QRadioButton(self.groupBox_2)
        self.manhattan.setObjectName("manhattan")
        self.verticalLayout_3.addWidget(self.manhattan)
        self.diagonal = QtWidgets.QRadioButton(self.groupBox_2)
        self.diagonal.setObjectName("diagonal")
        self.verticalLayout_3.addWidget(self.diagonal)
        self.start = QtWidgets.QPushButton(self.groupBox_2)
        self.start.setObjectName("start")
        self.verticalLayout_3.addWidget(self.start)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.new_map = QtWidgets.QAction(MainWindow)
        self.new_map.setObjectName("new_map")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_3.setTitle(_translate("MainWindow", "操作说明"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "地图信息：\n"
"  可以创建地图大小\n"
"  范围：2-100"))
        self.mapBox.setTitle(_translate("MainWindow", "地图信息"))
        self.label.setText(_translate("MainWindow", "长"))
        self.label_2.setText(_translate("MainWindow", "宽"))
        self.create_map.setText(_translate("MainWindow", "创建"))
        self.groupBox_2.setTitle(_translate("MainWindow", "配置"))
        self.manhattan.setText(_translate("MainWindow", "manhattan(曼哈顿上下左右)"))
        self.diagonal.setText(_translate("MainWindow", "diagonal(可走对角线)"))
        self.start.setText(_translate("MainWindow", "开始"))
        self.new_map.setText(_translate("MainWindow", "新建"))
from view.map import CMapFrame