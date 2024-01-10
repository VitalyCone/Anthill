from copy import copy

from PyQt6.QtCore import QPointF, QRectF, QRect
from PyQt6.QtGui import QPainter, QImage, QPen, QColor
from PyQt6.QtWidgets import QGraphicsItem, QWidget, QStyleOptionGraphicsItem
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

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget = None):
        painter.drawImage(self.boundingRect(), self.sprite)
        self.setPos(self.geo[0], self.geo[1])
        self.setRotation(self.u)
        self.update()

    def delete_entity(self):
        self.graph_scene.removeItem(self)

    def boundingRect(self):
        return QRectF(0, 0, 20, 20)
