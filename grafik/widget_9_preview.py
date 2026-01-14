import math
import pyqtgraph as pg
import numpy as np
from pyqtgraph import PlotWidget as PGPlotWidget
from PySide6.QtCore import QTimer

class Widget9TorqueOnly(PGPlotWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setBackground('w')
        self.showGrid(x=True, y=True)
        # Labels
        self.setTitle("Grafik Torque vs RPM", color='k', size='14pt')
        self.setLabel('left', 'Torque (N.m)', color='g')
        self.setLabel('bottom', 'RPM (x100)', color='k')
        #max label torque
        self.max_label = pg.TextItem("", anchor=(0,0), color='k')
        self.addItem(self.max_label)
        # Plot line for torque
        self.torque_curve = self.plot(pen=pg.mkPen('g', width=2), name='Torque')
        # Data
        self.rpm_data = []
        self.torque_data = []
        # Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self._refresh_plot)
        self.timer.start(50)
        # Axis defaults
        self.setXRange(0, 20)
        self.getPlotItem().vb.setLimits(xMin=0)
        self.setLimits(xMin=0, xMax=1000)
        self.setYRange(0, 10)
        self.getPlotItem().vb.setLimits(yMin=0)
        self.setLimits(yMin=0, yMax=1000)
        #garis vertikal dan horizontal untuk hover
        self.vline = pg.InfiniteLine(angle=90, movable=False, pen=pg.mkPen('k', style=pg.QtCore.Qt.DashLine))
        self.hline = pg.InfiniteLine(angle=0, movable=False, pen=pg.mkPen('k', style=pg.QtCore.Qt.DashLine))
        self.addItem(self.vline, ignoreBounds=True)
        self.addItem(self.hline, ignoreBounds=True)
        # Text max label
        self.hover_label = pg.TextItem("", anchor=(0,1), color='k')
        self.addItem(self.hover_label)
        #mouse tracking
        self.proxy = pg.SignalProxy(self.scene().sigMouseMoved, rateLimit=60, slot=self._on_mouse_moved)
    def append_data(self, rpm: int, torque: float):
        try:
            self.rpm_data.append(rpm)
            self.torque_data.append(torque)
            #limits data until 10000 point
            self.rpm_data = self.rpm_data[-10000:]
            self.torque_data = self.torque_data[-10000:]
            self._update_axis_limits()
        except Exception as e:
            print("[append_data error]", e)
    def _refresh_plot(self):
        if not self.rpm_data:
            return
        #konversi data
        rpm_scaled = [r / 100 for r in self.rpm_data]
        #perbarui grafik
        self.torque_curve.setData(rpm_scaled, self.torque_data)
        try:
            max_torque = max(self.torque_data)
            index = self.torque_data.index(max_torque)
            rpm = self.rpm_data[index]
            #posisi dan nama keterangan
            self.max_label.setText(
                f"Max Torque = {max_torque:.2f} Nm at RPM = {rpm}"
            )
            self.max_label.setPos(
                self.getViewBox().viewRange()[0][0] + 1,
                self.getViewBox().viewRange()[1][1] - 0.1,
            )
        except Exception as e:
            print("[max label error]", e)
    def _update_axis_limits(self):
        if not self.rpm_data:
            return
        #update label sumbu bawah
        max_rpm = max(self.rpm_data) / 100
        x_max = max(max_rpm * 1.1, 20)
        self.setXRange(0, x_max)   
        #update label sumbu bawah
        x_max_int = math.ceil(x_max)
        x_ticks = [(i, str(i)) for i in range(0, x_max_int + 1, max(1, x_max_int // 20))]
        self.getPlotItem().getAxis('bottom').setTicks([x_ticks])
        #update label sumbu kiri
        max_torque = max(self.torque_data)
        y_max = max(max_torque * 1.1, 10)
        self.setYRange(0, y_max)
        # Ticks
        if y_max <=1:
            y_ticks = [(i / 10, f"{i / 10:.1f}") for i in range(0, 11)] #interval 0.1
        else:
            y_max_int = math.ceil(y_max)
            y_ticks = [(i, str(i)) for i in range(0, y_max_int + 1, max(1, y_max_int // 10))]
        self.getPlotItem().getAxis('left').setTicks([y_ticks])
    def reset_data(self):
        self.rpm_data.clear()
        self.torque_data.clear()
        self._refresh_plot()
    def _on_mouse_moved(self, evt):
        if len(self.rpm_data) == 0 or len(self.torque_data) == 0:
            return
        pos = evt[0]  # PyQtGraph wraps the event
        if not self.sceneBoundingRect().contains(pos):
            self.hover_label.setVisible(False)
            self.vline.setVisible(False)
            self.hline.setVisible(False)
            return 
        mouse_point = self.getPlotItem().vb.mapSceneToView(pos)
        x = mouse_point.x()
        y = mouse_point.y()
        view_x_range, view_y_range = self.getPlotItem().vb.viewRange()
        # Cek apakah mouse di luar batas view grafik
        if not (view_x_range[0] <= x <= view_x_range[1]) or not (view_y_range[0] <= y <= view_y_range[1]):
            self.hover_label.setVisible(False)
            self.vline.setVisible(False)
            self.hline.setVisible(False)
            return
        # Tampilkan garis vertikal dan horizontal
        self.vline.setVisible(True)
        self.hline.setVisible(True)
        self.vline.setPos(x)
        self.hline.setPos(y)
        # Cari index terdekat berdasarkan posisi x (RPM)
        if self.rpm_data:
            rpm_divided = np.array(self.rpm_data) / 100
            idx = (np.abs(rpm_divided - x)).argmin()
            # filter kalau data kosong
            if x < np.min(rpm_divided) or x > np.max(rpm_divided):
                self.hover_label.setVisible(False)
                return
            if idx < len(self.rpm_data) and idx < len(self.torque_data):
                torque_val = self.torque_data[idx]
                rpm_val = self.rpm_data[idx]
                # Gunakan HTML untuk membuat tooltip stylish
                self.hover_label.setHtml(
                    f"""
                    <div style="
                        background-color: blue;
                        border: 1px solid white;
                        border-radius: 4px;
                        padding: 4px;
                        font-size: 10pt;
                        color: white;
                    ">
                        <b>RPM:</b> {int(rpm_val)} → {rpm_val/100:.2f} x100<br>
                        <b>Torque:</b> {torque_val:.1f} Nm<br>
                    </div>
                    """
                )
                self.hover_label.setPos(x, y)
                self.hover_label.setVisible(True)
            else:
                self.hover_label.setVisible(False)
                self.vline.setVisible(False)
                self.hline.setVisible(False)