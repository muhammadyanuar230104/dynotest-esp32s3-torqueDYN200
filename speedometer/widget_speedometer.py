#widget_speedomter.py
#kiri (RPM) 
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QPixmap, QPen, QFont, QColor, QBrush, QLinearGradient, QRadialGradient, QConicalGradient
from PySide6.QtCore import Qt, QRectF, QTimer, QPointF, QPropertyAnimation, Property, QSize
import math

class SpeedometerWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._theme_color = "biru"
        self._value = 0
        self._display_value = 0
        self._max_value = 2000
        self._min_angle = 225
        self._max_angle = -45
        # Smooth animation using QPropertyAnimation
        self._anim = QPropertyAnimation(self, b"displayValue")
        self._anim.setDuration(300)
        # Refresh at 60Hz for smooth repaint
        self._timer = QTimer()
        self._timer.timeout.connect(self.update)
        self._timer.start(16)
    def sizeHint(self):
        return self.minimumSizeHint()
    def minimumSizeHint(self):
        return QSize(300, 300)
    def setValue(self, val):
        #hitung skala dinamis 
        if val > self._max_value:
            magnitude = 10 ** int(math.log10(val))
            self._max_value = math.ceil(val / magnitude) * magnitude
        self._value = val
        self._anim.stop()
        self._anim.setStartValue(self._display_value)
        self._anim.setEndValue(val)
        self._anim.start()
    def getDisplayValue(self):
        return self._display_value
    def setDisplayValue(self, val):
        self._display_value = val
        self.update()
    displayValue = Property(float, getDisplayValue, setDisplayValue)
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        size = min(self.width(), self.height()) - 20
        rect = QRectF(10, 10, size, size)
        center = rect.center()
        radius = size / 2
        # Draw background gradient
        gradient = QLinearGradient(rect.topLeft(), rect.bottomRight())
        if self._theme_color == "merah":
            gradient.setColorAt(0.0, QColor("#8B0000"))
            gradient.setColorAt(0.5, QColor("#FF6347"))
            gradient.setColorAt(1.0, QColor("#CD5C5C"))
        elif self._theme_color == "ocean":
            gradient.setColorAt(0.0, QColor("#2E8B57"))   # Sea green
            gradient.setColorAt(0.5, QColor("#20B2AA"))   # Light sea green
            gradient.setColorAt(1.0, QColor("#87CEFA"))   # Light sky blue
        elif self._theme_color == "sunset":
            gradient.setColorAt(0.0, QColor("#FF7E5F"))   # Coral
            gradient.setColorAt(0.5, QColor("#FD3A69"))   # Red-pink
            gradient.setColorAt(1.0, QColor("#8B0000"))   # Dark red
        elif self._theme_color == "midnight":
            gradient.setColorAt(0.0, QColor("#0F2027"))
            gradient.setColorAt(0.5, QColor("#203A43"))
            gradient.setColorAt(1.0, QColor("#2C5364"))
        elif self._theme_color == "neon":
            gradient.setColorAt(0.0, QColor("#0f0c29"))
            gradient.setColorAt(0.5, QColor("#302b63"))
            gradient.setColorAt(1.0, QColor("#00f9ff"))
        elif self._theme_color == "hijau":
            gradient.setColorAt(0.0, QColor("#006400"))
            gradient.setColorAt(0.5, QColor("#32CD32"))
            gradient.setColorAt(1.0, QColor("#7CFC00"))
        elif self._theme_color == "kuning":
            gradient.setColorAt(0.0, QColor("#FFD700"))
            gradient.setColorAt(0.5, QColor("#FFFF00"))
            gradient.setColorAt(1.0, QColor("#FFA500"))
        elif self._theme_color == "ungu":
            gradient.setColorAt(0.0, QColor("#4B0082"))
            gradient.setColorAt(0.5, QColor("#8A2BE2"))
            gradient.setColorAt(1.0, QColor("#9370DB"))
        elif self._theme_color == "sakura":
            gradient.setColorAt(0.0, QColor("#FFB7C5"))   # Sakura pink
            gradient.setColorAt(0.5, QColor("#FFC0CB"))   # Pink
            gradient.setColorAt(1.0, QColor("#FF69B4"))   # Hot pink
        elif self._theme_color == "shonen":
            gradient.setColorAt(0.0, QColor("#FF2400"))   # Scarlet red
            gradient.setColorAt(0.5, QColor("#FF4500"))   # Orange red
            gradient.setColorAt(1.0, QColor("#FFD700"))   # Gold
        elif self._theme_color == "akatsuki":
            gradient.setColorAt(0.0, QColor("#4B0082"))   # Indigo
            gradient.setColorAt(0.5, QColor("#800080"))   # Purple
            gradient.setColorAt(1.0, QColor("#FF0000"))   # Merah darah
        elif self._theme_color == "idol":
            gradient.setColorAt(0.0, QColor("#00CED1"))   # Dark turquoise
            gradient.setColorAt(0.5, QColor("#87CEEB"))   # Sky blue
            gradient.setColorAt(1.0, QColor("#E0FFFF"))   # Light cyan
        else: #default biru 
            gradient.setColorAt(0.0, QColor("#00008B"))  # Dark green
            gradient.setColorAt(0.5, QColor("#00BFFF"))  # Red
            gradient.setColorAt(1.0, QColor("#1E90FF"))  
        painter.setBrush(QBrush(gradient))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(rect)
        # Draw ticks and labels
        steps = 10
        minor_per_step = 5
        major_pen = QPen(Qt.black, 4)
        minor_penn = QPen(Qt.white, 2)
        for i in range(steps + 1):
            val = i * (self._max_value / steps)
            angle = self.valueToAngle(val)
            painter.setPen(major_pen)
            self.drawTick(painter, center, radius, angle, f"{val}", major=True)
            if i < steps:
                next_val = (i+1) * (self._max_value / steps)
                for j in range(1, minor_per_step):
                    sub_val = val + j * ((next_val - val) / minor_per_step)
                    sub_angle = self.valueToAngle(sub_val)
                    painter.setPen(minor_penn)
                    self.drawTick(painter, center, radius, sub_angle, label=None, major=False)    
        #draw red danger zone from 8000 to 10000
        danger_treshold = int(self._max_value * 0.8)
        color = QColor("#FF0000") if self._display_value >= danger_treshold else QColor("#FFFFFF")
        start_danger = self.valueToAngle(danger_treshold)
        end_danger = self.valueToAngle(self._max_value)
        span_danger = end_danger - start_danger
        danger_rect = QRectF(rect)
        danger_rect.adjust(10, 10, -10, -10)
        painter.setBrush(Qt.NoBrush)
        painter.setPen(QPen(QColor('#FF0000'), 8))
        painter.drawArc(danger_rect, int(start_danger *16), int (span_danger * 16))
        # Draw needle
        angle = self.valueToAngle(self._display_value)
        self.drawNeedle(painter, center, radius, angle)
        #draw highlight arc for needle movement (disini setelah needle)
        self.drawHighlightArc(painter, rect, radius)        
        # Center dot
        painter.setBrush(QColor("#222"))
        painter.setPen(QPen(QColor("#666"), 2))
        painter.drawEllipse(center, 12, 12)
        #inner circle with gradient
        gradient = QRadialGradient(center, 8)
        gradient.setColorAt(0.0, QColor("#999"))
        gradient.setColorAt(0.6, QColor("#555"))
        gradient.setColorAt(1.0, QColor("#222"))
        painter.setBrush(QBrush(gradient))
        painter.setPen(QPen(QColor("#000"), 1))
        painter.drawEllipse(center, 0, 8)
        # Value label (digital display)
        font = QFont("Digital", 24, QFont.Bold)
        painter.setFont(font)
        # Danger threshold logic
        danger_threshold = self._max_value * 0.8
        text_color = QColor("#FF3333") if self._display_value >= danger_threshold else QColor("#00FF00")
        # Ukuran kotak lebih ramping dan proporsional
        box_width = rect.width() * 0.35  # lebih ramping dari sebelumnya
        box_height = 38
        box_x = rect.center().x() - box_width / 2
        box_y = rect.bottom() - box_height - 14  # agak naik sedikit biar ada jarak
        display_rect = QRectF(box_x, box_y, box_width, box_height)
        # Background gradient box
        gradient = QLinearGradient(display_rect.topLeft(), display_rect.bottomRight())
        gradient.setColorAt(0, QColor("#222"))
        gradient.setColorAt(1, QColor("#444"))
        painter.setBrush(QBrush(gradient))
        painter.setPen(QPen(Qt.white, 1))
        painter.drawRoundedRect(display_rect, 10, 10)
        # Label "RPM" di atas kotak display
        label_font = QFont("Bahnschrift", 18, QFont.Bold)
        painter.setFont(label_font)
        label_text = "RPM"
        label_rect = QRectF(
            box_x,
            box_y - 24,  # naikkan 20px di atas kotak
            box_width,
            20
        )
        # Shadow layer (semi-transparent grey)
        shadow_color = QColor(0, 0, 0, 80)
        painter.setPen(shadow_color)
        painter.drawText(label_rect.adjusted(1, 1, 1, 1), Qt.AlignCenter, label_text)
        # Main text
        painter.setPen(Qt.white)
        painter.drawText(label_rect, Qt.AlignCenter, label_text)
        # Tulis nilai dalam kotak
        number_font = QFont("Digital", 24, QFont.Bold)
        painter.setFont(number_font)  # ← ini penting supaya font angka tetap besar dan digital
        painter.setPen(text_color)
        painter.drawText(display_rect, Qt.AlignCenter, f"{int(self._display_value)}")
    def setRPMCal(self, rpm_cal):
        if rpm_cal > self._max_value:
            magnitude = 10 ** int(math.log10(rpm_cal))
            self._max_value = math.ceil(rpm_cal / magnitude) * magnitude
            self.update()
    def drawTick(self, painter, center, radius, angle_deg, label=None, major=True):
        radians = math.radians(angle_deg)
        outer = QPointF(
            center.x() + radius * math.cos(radians),
            center.y() - radius * math.sin(radians)
        )
        inner_radius = radius - (15 if major else 7)
        inner = QPointF(
            center.x() + inner_radius * math.cos(radians),
            center.y() - inner_radius * math.sin(radians)
        )
        painter.drawLine(inner, outer)
        if major and label is not None:
            text_radius = radius - 35 #dari ticks
            text_pos = QPointF(
                center.x() + text_radius * math.cos(radians) - 10,
                center.y() - text_radius * math.sin(radians) + 5
            )
            #pengaturan font 
            tick_font = QFont("Arial", 12, QFont.Bold)
            painter.setFont(tick_font)
            painter.drawText(text_pos, f"{int(float(label))}")
    def drawNeedle(self, painter, center, radius, angle_deg):
        radians = math.radians(angle_deg)
        needle_len = radius - 55
        #posisi ujung jarum
        tip = QPointF(
            center.x() + needle_len * math.cos(radians),
            center.y() - needle_len * math.sin(radians)
        )
        #tambahkan bentuk segitiga
        side_offset = math.radians(90)
        base1 = QPointF(
            center.x() + 10 * math.cos(radians + side_offset),
            center.y() - 10 * math.sin(radians + side_offset)
        )
        base2 = QPointF(
            center.x() + 10 * math.cos(radians - side_offset),
            center.y() - 10 * math.sin(radians - side_offset)
        )
        needle_path = [tip, base1, base2]
        #warna dinamis
        color = QColor("#FF0000") if self._display_value >= self._max_value * 0.8 else QColor("#FFFFFF")
        painter.setBrush(QBrush(color))
        painter.setPen(QPen(color, 1))
        painter.drawPolygon(needle_path)
        #opsional core garis tengah
        painter.setPen(QPen(Qt.black,1))
        painter.drawLine(center, tip)
    def valueToAngle(self, value):
        ratio = (value - 0) / (self._max_value - 0)
        angle = self._min_angle + ratio * (self._max_angle - self._min_angle)
        return angle
    def drawHighlightArc(self, painter, rect, radius):
        if self._display_value <= 0:
            return
        arc_rect = QRectF(rect)
        arc_rect.adjust(10, 10, -10, -10)  # shrink rect for better positioning
        #sudut dari nilai
        angle_0 = self.valueToAngle(0)
        angle_current = self.valueToAngle(self._display_value)
        #ambil ambang bahaya dinamis
        danger_threshold = int(self._max_value * 0.8)
        angle_danger = self.valueToAngle(danger_threshold)
        if self._display_value <= danger_threshold:
            #seluruh arc hijau
            span_angle = angle_current - angle_0
            painter.setPen(QPen(QColor("#32CD32"), 8)) 
            painter.setBrush(Qt.NoBrush)
            painter.drawArc(arc_rect, int(angle_0 *16), int(span_angle *16)) 
        else:
            #arc hijau sampai danger threshold
            green_span = angle_danger - angle_0
            painter.setPen(QPen(QColor("#32CD32"), 8))
            painter.drawArc(arc_rect, int(angle_0 *16), int(green_span*16))
            #arc merah dari danger threshold
            red_span = angle_current - angle_danger
            painter.setPen(QPen(QColor("#FF0000"), 8)) 
            painter.drawArc(arc_rect, int(angle_danger * 16), int(red_span*16))
    def setTheme(self, theme_name: str):
            self._theme_color = theme_name.lower()
            self.update()

