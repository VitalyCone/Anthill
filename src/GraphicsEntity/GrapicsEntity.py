from copy import copy

from PySide6.QtCore import QPointF, QRectF, QRect
from PySide6.QtGui import QPainter, QImage, QPen, QColor
from PySide6.QtWidgets import QGraphicsItem, QWidget, QStyleOptionGraphicsItem
from math import degrees


class GraphicsEntity(QGraphicsItem):
    """
    Класс кастомного объекта QGraphics API
    """
    def __init__(self, geo: list, sprite: str, rotation: float):
        super().__init__()
        self.geo = geo
        self.u = rotation
        self.setPos(copy(geo[0]), copy(geo[1]))
        self.setRotation(degrees(copy(rotation)))
        self.sprite = QImage(sprite)
        self.graph_scene = None
        self.rect = QRectF(0, 0, 20, 20)

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget = None):
        """
        Oтрисовывает графический объект и задает ему позицию на графической сцене
        :param painter:
        :param option:
        :param widget:
        :return:
        """
        painter.drawImage(self.boundingRect(), self.sprite)
        self.setPos(self.geo[0], self.geo[1])
        self.update()

    def delete_entity(self):
        """
        Удаляет графическую сущность. Вызывается при удалении агента
        """
        self.graph_scene.removeItem(self)
        self.update()

    def setRect(self, rect: QRectF):
        self.rect = rect
        self.update()

    def boundingRect(self):
        """
        Возвращает размер отрисовываемого графического объекта
        """
        # FIXME: Предоставить каждому виду сущностей свой размер(изменяемый)
        return self.rect

