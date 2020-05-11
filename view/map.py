# -*- coding:utf-8 -*-
'''
@Description: 地图界面
@Author: lamborghini1993
@Date: 2020-05-11 16:47:30
@UpdateDate: 2020-05-11 21:25:41
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
        # self.setMouseTracking(True)
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
        self.parent().update_last_label(self)
        self.update()

    @property
    def pos(self):
        return self._pos

    def paintEvent(self, e):
        super().paintEvent(e)
        if self._flag not in Map:
            return
        p = QtGui.QPainter(self)
        color = self._flag.value
        p.fillRect(0, 0, self.width(), self.height(), QtGui.QColor(*color))

    def dragEnterEvent(self, e):
        super().dragEnterEvent(e)
        e.accept()
        e.acceptProposedAction()
        _flag = getattr(e.mimeData(), "__flag", None)
        if not _flag:
            return

        print("enter:", self._pos, _flag, end=" | ")

        if _flag in (Map.START, Map.GOAL):
            if self.flag == Map.BLANK:
                print("1", self.flag, _flag)
                self.flag = _flag
            return

        if _flag in (Map.BLANK, Map.WALL):
            if self.flag != _flag:
                print("2", self.flag, _flag)
                self.flag = _flag
            return

    def dragLeaveEvent(self, e):
        super().dragLeaveEvent(e)
        e.accept()
        # _flag = getattr(e.mimeData(), "__flag", None)
        # if not _flag:
        #     return
        self.parent().last_label = self
        # print("enter:", self._pos, _flag)

    def eventFilter(self, e):
        super().eventFilter(e)
        print("eventFilter:", self._pos)

    # def enterEvent(self, e):
    #     super().enterEvent(e)
    #     if not self.parent().flag:
    #         return
    #     print("enter", self.parent().flag)

    #     if self.parent().flag in (Map.START, Map.GOAL):
    #         if self.flag == Map.BLANK:
    #             self.flag = self.parent().flag
    #         return

    #     if self.parent().flag in (Map.BLANK, Map.WALL):
    #         if self.flag != self.parent().flag:
    #             self.flag = self.parent().flag
    #         return

    # def leaveEvent(self, e):
    #     super().leaveEvent(e)
    #     # print("leaveEvent:", self._pos)

    # def mousePressEvent(self, e):
    #     super().mousePressEvent(e)
    #     self.parent().flag = self._flag
    #     print("mousePressEvent...", self._pos, self._flag)
    #     e.accept()

    # def mouseMoveEvent(self, e):
    #     super().mouseMoveEvent(e)
    #     # print("mouseMoveEvent...", self._pos)

    # def mouseReleaseEvent(self, e):
    #     super().mouseReleaseEvent(e)
    #     self.parent().flag = None
    #     print("mouseReleaseEvent...", self._pos, self._flag)


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
        self.setAcceptDrops(True)

    def resize_map(self, h: int, w: int):
        self._h = h
        self._w = w
        self._start = (20, 15)
        self._gold = (30, 15)
        self._last_label = None
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

    @property
    def last_label(self):
        return self._last_label

    @last_label.setter
    def last_label(self, label: Label):
        self._last_label = label

    def update_last_label(self, label: Label):
        if not self.flag:
            return
        if self._last_label.flag == Map.START and self._flag == Map.START:
            self._last_label.flag = Map.BLANK
            self._last_label.update()

    def mousePressEvent(self, e):
        super().mousePressEvent(e)
        item = self.childAt(e.pos())
        if not isinstance(item, Label):
            return
        drag = QtGui.QDrag(self)
        mine_data = QtCore.QMimeData()
        setattr(mine_data, "__flag", item._flag)
        drag.setMimeData(mine_data)
        self.flag = item._flag
        result = drag.exec(QtCore.Qt.MoveAction)

    def mouseReleaseEvent(self, e):
        super().mousePressEvent(e)
        self.flag = None

    def dragEnterEvent(self, e):
        super().dragEnterEvent(e)
        e.accept()