# -*- coding:utf-8 -*-
'''
@Description: 地图界面
@Author: lamborghini1993
@Date: 2020-05-11 16:47:30
@UpdateDate: 2020-05-11 20:13:59
'''
from enum import Enum
from PyQt5 import QtWidgets, QtGui, QtCore


class Map(Enum):
    START = (0, 221, 0)
    BLANK = (255, 255, 255)
    WALL = (128, 128, 128)
    GOAL = (238, 68, 0)
    HAS_VISIT = (175, 238, 238)
    WILL_VISIT = (152, 251, 152)


class Label(QtWidgets.QLabel):
    def __init__(self, flag: int, pos, parent=None):
        super().__init__(parent)
        self._pos = pos
        self._flag = flag
        # self.setText("A")
        self.setAcceptDrops(True)
        self.setMinimumSize(QtCore.QSize(20, 20))
        self.setMaximumSize(QtCore.QSize(20, 20))

    @property
    def flag(self) -> Map:
        return self._flag

    @flag.setter
    def flag(self, _flag: Map):
        if self._flag not in Map:
            return
        self._flag = _flag

    def paintEvent(self, e):
        super().paintEvent(e)
        if self._flag not in Map:
            return
        p = QtGui.QPainter(self)
        color = self._flag.value
        p.fillRect(0, 0, self.width(), self.height(), QtGui.QColor(*color))

    def dragEnterEvent(self, e):
        super().dragEnterEvent(e)
        print("enter:", self._pos)

    def dragLeaveEvent(self, e):
        super().dragLeaveEvent(e)
        print("leave:", self._pos)

    def enterEvent(self, e):
        super().enterEvent(e)
        print("enter", self.parent().flag)
        if not self.parent().flag:
            return

        if self.parent().flag in (Map.START, Map.GOAL):
            if self.flag == Map.BLANK:
                self.flag = self.parent().flag
            return

        if self.parent().flag in (Map.BLANK, Map.WALL):
            if self.flag != self.parent().flag:
                self.flag = self.parent().flag
            return

    def leaveEvent(self, e):
        super().leaveEvent(e)
        # print("leaveEvent:", self._pos)

    def mousePressEvent(self, e):
        super().mousePressEvent(e)
        self.parent().flag = self._flag
        print("mousePressEvent...", self._pos, self._flag)

    def mouseMoveEvent(self, e):
        super().mouseMoveEvent(e)
        # print("mouseMoveEvent...", self._pos)

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)
        self.parent().flag = None
        print("mouseReleaseEvent...", self._pos, self._flag)

    def _change_flag(self, _flag):
        if self.parent().flag == Map.START:

            return

        if _flag == Map.BLANK:
            return
        self._flag = _flag


class CMapFrame(QtWidgets.QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._init()
        self._h = 0
        self._w = 0
        self._flag = None
        self._widget = {}

    def _init(self):
        self._gridLayout = QtWidgets.QGridLayout(self)
        self._gridLayout.setContentsMargins(0, 0, 0, 0)
        self._gridLayout.setSpacing(1)

    def resize_map(self, h: int, w: int):
        self._h = h
        self._w = w
        self._start = (20, 15)
        self._gold = (30, 15)
        self._generate_map()

    def _remove(self):
        for widget in self._widget.values():
            self._gridLayout.removeWidget(widget)
            widget.setParent(None)
        self._widget = {}

    def _generate_map(self):
        self._remove()
        for x in range(self._h):
            for y in range(self._w):
                label = Label(Map.BLANK, (x, y), self)
                self._gridLayout.addWidget(label, y, x)
                self._widget[(x, y)] = label

        self._widget[self._start].flag = Map.START
        self._widget[self._gold].flag = Map.GOAL

    @property
    def flag(self) -> Map:
        return self._flag

    @flag.setter
    def flag(self, _flag: Map):
        self._flag = _flag
