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
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = CMapFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMaximumSize(QtCore.QSize(220, 16777215))
        self.frame_2.setStyleSheet("")
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
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.manhattan = QtWidgets.QRadioButton(self.groupBox_2)
        self.manhattan.setChecked(True)
        self.manhattan.setObjectName("manhattan")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.manhattan)
        self.verticalLayout_3.addWidget(self.manhattan)
        self.diagonal = QtWidgets.QRadioButton(self.groupBox_2)
        self.diagonal.setObjectName("diagonal")
        self.buttonGroup.addButton(self.diagonal)
        self.verticalLayout_3.addWidget(self.diagonal)
        self.diagonal_dis = QtWidgets.QRadioButton(self.groupBox_2)
        self.diagonal_dis.setObjectName("diagonal_dis")
        self.buttonGroup.addButton(self.diagonal_dis)
        self.verticalLayout_3.addWidget(self.diagonal_dis)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.step_int = UE4Slider(self.groupBox_2)
        self.step_int.setStyleSheet("color: rgb(255, 255, 255);")
        self.step_int.setObjectName("step_int")
        self.horizontalLayout_2.addWidget(self.step_int)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.start = QtWidgets.QPushButton(self.groupBox_2)
        self.start.setObjectName("start")
        self.horizontalLayout_3.addWidget(self.start)
        self.debug = QtWidgets.QPushButton(self.groupBox_2)
        self.debug.setEnabled(True)
        self.debug.setStyleSheet("")
        self.debug.setObjectName("debug")
        self.horizontalLayout_3.addWidget(self.debug)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.clear = QtWidgets.QPushButton(self.groupBox_2)
        self.clear.setEnabled(True)
        self.clear.setStyleSheet("")
        self.clear.setObjectName("clear")
        self.verticalLayout_3.addWidget(self.clear)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "A*自动寻路"))
        self.groupBox_3.setTitle(_translate("MainWindow", "操作说明"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "地图信息：\n"
"  紫色：起始点    红色：终点\n"
"  绿色：队列坐标  蓝色：已走坐标\n"
"地图操作：\n"
"  可鼠标拖动起始点和终点\n"
"  点击空白/墙壁拖动可填充\n"
"配置说明：\n"
"  可选三种走法\n"
"  可设置A*算法每次步数的间隔时间\n"
"  debug可做一步一步调试"))
        self.groupBox_2.setTitle(_translate("MainWindow", "配置"))
        self.manhattan.setText(_translate("MainWindow", "manhattan(曼哈顿走法)"))
        self.diagonal.setText(_translate("MainWindow", "diag-step(可走对角线-按步数)"))
        self.diagonal_dis.setText(_translate("MainWindow", "diag-dis(可走对角线-按距离)"))
        self.label.setText(_translate("MainWindow", "步数间隔时间："))
        self.start.setText(_translate("MainWindow", "开始"))
        self.debug.setText(_translate("MainWindow", "调试"))
        self.clear.setText(_translate("MainWindow", "清除"))
        self.new_map.setText(_translate("MainWindow", "新建"))
from view.map import CMapFrame
from xhpubqt.ue4slider import UE4Slider
