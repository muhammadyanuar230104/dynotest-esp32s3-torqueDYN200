import math
import pyqtgraph as pg
import numpy as np
from pyqtgraph import PlotWidget as PGPlotWidget
from PySide6.QtCore import QTimer

class Widget5(PGPlotWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setBackground('w')
        self.showGrid(x=True, y=True)
        # Labels
        self.setTitle("Grafik Torque & Power (HP) vs RPM", color='k', size='14pt')
        self.setLabel('left', 'Torque (N.m) & Power (HP)', color='k')
        self.setLabel('bottom', 'RPM (x100)', color='k')
        # Text Items
        self.max_label = pg.TextItem("", anchor=(0, 0), color='k')
        self.addItem(self.max_label)
        #tambahkan axis kanan untuk power (hp)
        self.right_axis_view = pg.ViewBox()
        self.getPlotItem().scene().addItem(self.right_axis_view)
        self.getPlotItem().getAxis('right').linkToView(self.right_axis_view)
        self.right_axis_view.setXLink(self.getPlotItem())
        self.getPlotItem().showAxis('right')
        #ini label angka saja
        self.getPlotItem().getAxis('right').setLabel('Power (HP)', color='b')
        self.getPlotItem().getAxis('right').setPen(pg.mkPen('b'))
        #matikan grid dari axis kanan
        self.getPlotItem().getAxis('right').setGrid(False) 
        # hubungkan update views dengan resize signal
        self.getPlotItem().vb.sigResized.connect(self.update_views)    
        #Tambahkan garis torque (hijau) dan power (biru) serta legenda kanan
        self.torque_curve = self.plot(pen=pg.mkPen('g', width=2), name='Torque')
        self.power_curve = self.plot(pen=pg.mkPen('b', width=2), name='Power (HP)')
        self.right_axis_view.addItem(self.power_curve)  
        #buat dan tambahkan legend
        self.legend = pg.LegendItem(offset=(-10, -10))
        self.legend.setParentItem(self.getPlotItem().vb)
        self.legend.addItem(self.torque_curve, "Torque")
        self.legend.addItem(self.power_curve, "Power (HP)")      
        #atur posisi Legend 
        self.legend.anchor((1, 1), (1, 1))
        # Data
        self.rpm_data = []
        self.torque_data = []
        self.power_data = []
        # Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self._refresh_plot)
        self.timer.start(50)
        # Axis range default
        self.setXRange(0, 20)
        self.setLimits(xMin=0, xMax=1000)
        self.setYRange(0, 8)
        self.setLimits(yMin=0, yMax=1000)
        #agar sumbu kanan tidak terpotong
        self.getPlotItem().getAxis('right').setWidth(40)
        #set default axis limits
        self.right_y_max = 1
        self.right_axis_view.setYRange(0, self.right_y_max)
        self.right_axis_view.setLimits(yMin=0)
        # Garis vertikal & horizontal untuk hover
        self.vline = pg.InfiniteLine(angle=90, movable=False, pen=pg.mkPen('k', style=pg.QtCore.Qt.DashLine))
        self.hline = pg.InfiniteLine(angle=0, movable=False, pen=pg.mkPen('k', style=pg.QtCore.Qt.DashLine))
        self.addItem(self.vline, ignoreBounds=True)
        self.addItem(self.hline, ignoreBounds=True)
        # Label untuk menunjukkan data saat hover
        self.hover_label = pg.TextItem("", anchor=(0, 1), color='k')
        self.addItem(self.hover_label)
        # Enable mouse tracking
        self.proxy = pg.SignalProxy(self.scene().sigMouseMoved, rateLimit=60, slot=self._on_mouse_moved)  
    def update_views(self):
        self.right_axis_view.setGeometry(self.getPlotItem().vb.sceneBoundingRect())
        self.right_axis_view.linkedViewChanged(self.getPlotItem().vb, self.right_axis_view.XAxis)
    def append_data(self, rpm: int, torque: float, power: int):
        try:
            self.rpm_data.append(rpm)
            self.torque_data.append(torque)
            self.power_data.append(power)
            # Limit to 10,000 points
            self.rpm_data = self.rpm_data[-10000:]
            self.torque_data = self.torque_data[-10000:]
            self.power_data = self.power_data[-10000:]
            # Update the axis limits dynamically based on data
            self.update_axis_limits()
        except Exception as e:
            print("[append_data error]", e)
    def _refresh_plot(self):
        if not self.rpm_data:
            return
        # Convert RPM and Power
        rpm_scaled = [r / 100 for r in self.rpm_data]
        power_in_hp = [(p * 1.341) / 1000 for p in self.power_data]
        # Update curves
        self.torque_curve.setData(rpm_scaled, self.torque_data)
        self.power_curve.setData(rpm_scaled, power_in_hp)
        try:
            # Max values and RPMs
            max_torque = max(self.torque_data)
            idx_torque = self.torque_data.index(max_torque)
            rpm_torque = self.rpm_data[idx_torque]
            #mac power
            max_power_raw = max(self.power_data)
            max_power_hp = (max_power_raw * 1.341) / 1000
            idx_power = self.power_data.index(max_power_raw)
            rpm_power = self.rpm_data[idx_power]
            #set label dan nama keterangan
            self.max_label.setText(
                f"Max Torque = {max_torque:.2f} Nm at RPM = {rpm_torque}\n"
                f"Max Power = {max_power_hp:.3f} HP at RPM = {rpm_power}"
            )
            self.max_label.setPos(
            self.getViewBox().viewRange()[0][0] + 1,
            self.getViewBox().viewRange()[1][1] - 0.1)
        except Exception as e:
            print(f"[max label error] {e}")
        #cek dan update batas atas agar garis dan label sejajar
        if max_power_hp > self.right_y_max:
            self.right_y_max = max_power_hp * 1.1
        #tambahkan ini agar label sejajar
        self.right_axis_view.setYRange(0, self.right_y_max)
        self.right_axis_view.setLimits(yMin=0)
        #update label sumbu k anan (ticks)
        if self.right_y_max <= 1:
            y_ticks_power = [(i / 10, f"{i / 10:.1f}") for i in range(0, 11)] #interval 0.1
        else:
            step = round(self.right_y_max / 10, 1)
            power_max = math.ceil(self.right_y_max / step) * step
            y_ticks_power = [(round(i * step, 1), f"{round(i * step, 1):.1f}") 
                            for i in range(0, int(power_max / step) + 1)]
            #power_max_int = math.ceil(self.right_y_max)
            #y_ticks_power = [(i, str(i)) for i in range(0, power_max_int + 1, max(1, power_max_int // 10))]
        self.getPlotItem().getAxis('right').setTicks([y_ticks_power])
    def update_axis_limits(self):
        if not self.rpm_data:
            return
        # nilai maksimum label bawah
        max_rpm = max(self.rpm_data) / 100  # Convert RPM to x1000
        x_max = max(max_rpm * 1.1, 20)
        self.setXRange(0, x_max) #view tetap
        x_max_int = math.ceil(x_max)
        ticks = [(i, str(i)) for i in range(0, x_max_int + 1, max(1, x_max_int // 20))]
        self.getPlotItem().getAxis('bottom').setTicks([ticks])
        #update label sumbu y kiri
        max_torque = max(self.torque_data)
        y_max = max(max_torque * 1.1, 8)
        self.setYRange(0, y_max)
        y_max_int = math.ceil(y_max)
        y_ticks = [(i, str(i)) for i in range(0, y_max_int + 1, max(1, y_max_int // 10))]
        self.getPlotItem().getAxis('left').setTicks([y_ticks])
    def reset_data(self):
        self.rpm_data = []
        self.torque_data = []
        self.power_data = []
        self._refresh_plot()
    def _on_mouse_moved(self, evt):
        if len(self.rpm_data) == 0 or len(self.power_data) == 0:
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
            if idx < len(self.torque_data) and idx < len(self.power_data):
                torque_val = self.torque_data[idx]
                power_val = (self.power_data[idx] * 1.341) / 1000
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
                        <b>Power:</b> {self.power_data [idx]} → {power_val:.2f} HP
                    </div>
                    """
                )
                self.hover_label.setPos(x, y)
                self.hover_label.setVisible(True)
            else:
                self.hover_label.setVisible(False)
                self.vline.setVisible(False)
                self.hline.setVisible(False)