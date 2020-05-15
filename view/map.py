# -*- coding:utf-8 -*-
'''
@Description: 地图界面
@Author: lamborghini1993
@Date: 2020-05-11 16:47:30
@UpdateDate: 2020-05-15 21:00:40
'''
from enum import Enum

from PyQt5 import QtCore, QtGui, QtWidgets

from logic import astar


class Map(Enum):
    # START = (0, 221, 0)
    START = (164, 63, 204)
    BLANK = (255, 255, 255)
    WALL = (128, 128, 128)
    GOAL = (238, 68, 0)
    # HAS_VISIT = (175, 238, 238)
    HAS_VISIT = (0, 122, 245)
    WILL_VISIT = (152, 251, 152)


class Label(QtWidgets.QLabel):
    def __init__(self, flag: int, pos, parent=None):
        super().__init__(parent)
        self._pos = pos
        self._flag = flag
        self._line = []
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
        self.update()

    def add_line(self, _line):
        self._line.append(_line)
        self.update()

    def _update_flag(self, _flag: Map):
        self.flag = _flag
        self.parent().update_last_label(self)

    @property
    def pos(self):
        return self._pos

    def clear(self, containe_wall: bool = False):
        self._line = []
        if self._flag not in (Map.START, Map.GOAL):
            if containe_wall or self._flag != Map.WALL:
                self._flag = Map.BLANK
        self.update()

    def paintEvent(self, e):
        super().paintEvent(e)
        if self._flag not in Map:
            return
        p = QtGui.QPainter(self)
        color = self._flag.value
        p.fillRect(0, 0, self.width(), self.height(), QtGui.QColor(*color))
        if not self._line:
            return
        pen = QtGui.QPen(QtGui.QColor(255, 200, 50))
        pen.setWidth(2)
        p.setPen(pen)
        x1, y1 = self.width()/2, self.height()/2
        for (bx, by) in self._line:
            x2, y2 = x1+bx*x1, y1+by*y1
            p.drawLine(x1, y1, x2, y2)

    def dragEnterEvent(self, e):
        super().dragEnterEvent(e)
        e.accept()
        e.acceptProposedAction()
        _flag = getattr(e.mimeData(), "__flag", None)
        if not _flag:
            return

        if _flag in (Map.START, Map.GOAL):
            if self.flag == Map.BLANK:
                self._update_flag(_flag)
                self.parent().update_start_goal(self.pos, _flag)
            return

        if _flag == Map.BLANK and self._flag == Map.BLANK:
            self._update_flag(Map.WALL)
            return

        if _flag == Map.WALL and self._flag == Map.WALL:
            self._update_flag(Map.BLANK)
            return

    def dragLeaveEvent(self, e):
        super().dragLeaveEvent(e)
        e.accept()
        if self.parent().flag in (Map.START, Map.GOAL) and self._flag == self.parent().flag:
            self.parent().last_label = self
            return

        if self.parent().flag == Map.BLANK and self._flag == Map.BLANK:
            self.parent().last_label = self
            return

        if self.parent().flag == Map.WALL and self._flag == Map.WALL:
            self.parent().last_label = self
            return


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

    def resize_map(self, w: int, h: int):
        self._h = h
        self._w = w
        self._start = (20, 15)
        self._gold = (30, 15)
        self._last_label = None
        self._generate_map()

    def update_start_goal(self, pos, _flag):
        if _flag == Map.START:
            self._start = pos
        elif _flag == Map.GOAL:
            self._gold = pos

    def get_map_info(self):
        walls = []
        for label in self._widget.values():
            _flag = label.flag
            if _flag == Map.WALL:
                walls.append(label.pos)
        return self._w, self._h, self._start, self._gold, walls

    def update_last_label(self, label: Label):
        if not (self.flag and self._last_label):
            return
        if self._flag in (Map.START, Map.GOAL):
            self._last_label.flag = Map.BLANK

    def _remove(self):
        for widget in self._widget.values():
            self._gridLayout.removeWidget(widget)
            widget.setParent(None)
        self._widget = {}

    def _generate_map(self):
        self._remove()
        for x in range(self._w):
            for y in range(self._h):
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

    def _astar_call(self, _type, pos):
        if _type == astar.RESULT:
            if not pos:
                return
            for i in range(len(pos)-1):
                pos0 = pos[i]
                pos1 = pos[i+1]
                self._widget[pos0].add_line(_minu(pos0, pos1))
                self._widget[pos1].add_line(_minu(pos1, pos0))
            return
        label = self._widget[pos]
        if label.flag in (Map.BLANK, Map.WILL_VISIT):
            if _type == astar.WILL_VISIT:
                label.flag = Map.WILL_VISIT
            elif _type == astar.HAS_VISIT:
                label.flag = Map.HAS_VISIT

    def clear(self, containe_wall: bool = False):
        for label in self._widget.values():
            if label.flag == Map.BLANK:
                continue
            label.clear(containe_wall)


def _minu(pos0, pos1):
    return (pos1[0]-pos0[0], pos1[1]-pos0[1])
