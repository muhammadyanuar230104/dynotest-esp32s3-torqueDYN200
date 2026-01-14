import math
import pyqtgraph as pg
import numpy as np
from pyqtgraph import PlotWidget as PGPlotWidget
from PySide6.QtCore import QTimer

class Widget1(PGPlotWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setBackground('w')
        self.showGrid(x=True, y=True)
        # Tambahkan judul
        self.setTitle("Grafik Torque (N.m) & Power (kW) x RPM", color='k', size='16pt')
        self.setLabel('bottom', 'RPM (x100)', **{'color': 'k'})
        self.setLabel('left', 'Torque (N..m)', **{'color': 'g'})
        # TextItem untuk max value dan legend
        self.max_label = pg.TextItem("", anchor=(0, 0), color='k')
        self.addItem(self.max_label)
        # Tambahkan axis kanan untuk Power
        self.right_axis_view = pg.ViewBox()
        self.getPlotItem().scene().addItem(self.right_axis_view)
        self.getPlotItem().getAxis('right').linkToView(self.right_axis_view)
        self.right_axis_view.setXLink(self.getPlotItem())
        self.getPlotItem().showAxis('right')
        # Ini label angka aja
        self.getPlotItem().getAxis('right').setLabel('Power (kW)', color='b')
        self.getPlotItem().getAxis('right').setPen(pg.mkPen('b'))
        # MATIKAN grid dari axis kanan
        self.getPlotItem().getAxis('right').setGrid(False)  # 💥 PENTING!
        # Hubungkan update_views dengan resize signal
        self.getPlotItem().vb.sigResized.connect(self.update_views)  
        # Tambahkan garis Torque (hijau) dan Power (biru) serta legend kanan
        self.torque_curve = self.plot(pen=pg.mkPen('g', width=2), name='Torque')
        self.power_curve = self.plot(pen=pg.mkPen('b', width=2), name='Power')
        self.right_axis_view.addItem(self.power_curve)
        # Buat dan tambahkan legend
        self.legend = pg.LegendItem(offset=(-10, -10))  # Posisi relatif dari sudut kanan bawah
        self.legend.setParentItem(self.getPlotItem().vb)  # Tampilkan di ViewBox
        self.legend.addItem(self.torque_curve, "Torque")  # Tambahkan keterangan untuk Torque
        self.legend.addItem(self.power_curve, "Power")   # Tambahkan keterangan untuk Power    
        # Atur posisi legend secara manual
        self.legend.anchor((1, 1), (1, 1))  # Posisi kanan bawah dari ViewBox
        # Data
        self.data_rpm = []
        self.data_torque = []
        self.data_power = []
        # Timer refresh grafik
        self.timer = QTimer()
        self.timer.timeout.connect(self._refresh_plot)
        self.timer.start(50)
        # Saat init
        self.setYRange(0, 8)
        self.setLimits(yMin=0, yMax=1000)
        self.setXRange(0, 20)
        self.setLimits(xMin=0, xMax=1000)
        #agar sumbu kanan tidak terpotong
        self.getPlotItem().getAxis('right').setWidth(40)
        # Set default axis limits        
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
            self.data_rpm.append(rpm)
            self.data_torque.append(torque)
            self.data_power.append(power)
            #Limit to 10.000 points
            self.data_rpm = self.data_rpm[-10000:]
            self.data_torque = self.data_torque[-10000:]
            self.data_power = self.data_power[-10000:]
            self._update_axis_limits()
        except Exception as e:
            print("[append_data error]", e)
    def _refresh_plot(self):
        if not self.data_rpm:
            return
        # Konversi data
        power_in_kw = [p / 1000 for p in self.data_power]
        rpm_divided = [r / 100 for r in self.data_rpm]
        # Perbarui data plot
        self.torque_curve.setData(rpm_divided, self.data_torque)
        self.power_curve.setData(rpm_divided, power_in_kw)
        # Update label max torque & power
        try:
            max_torque = max(self.data_torque)
            index = self.data_torque.index(max_torque)
            rpm_torque = self.data_rpm[index]
            # Konversi power ke kW
            max_power = max(self.data_power) / 1000
            rpm_power = self.data_rpm[self.data_power.index(max(self.data_power))]
            # posisi dan nama keterangan
            self.max_label.setText(
                f"Max Torque = {max_torque:.2f} Nm at RPM = {rpm_torque}\n"
                f"Max Power = {max_power:.2f} kW at RPM = {rpm_power}"
            )
            self.max_label.setPos(
            self.getViewBox().viewRange()[0][0] + 1, 
            self.getViewBox().viewRange()[1][1] - 0.1)
        except Exception as e:
            print(f"[max label error] {e}")
        # Cek dan update batas atas sumbu kanan jika perlu
        if max_power > self.right_y_max:
            self.right_y_max = max_power * 1.1
        # ⬇️ Tambahkan ini agar garis dan label sejajar
        self.right_axis_view.setYRange(0, self.right_y_max)
        self.right_axis_view.setLimits(yMin=0)
        # Update label sumbu kanan (ticks)
        if self.right_y_max <= 1:
            y_ticks_power = [(i / 10, f"{i / 10:.1f}") for i in range(0, 11)] #interval 0.1
        else:
            step = round(self.right_y_max / 10, 1)
            power_max = math.ceil(self.right_y_max / step) * step
            y_ticks_power = [(round(i * step, 1), f"{round(i * step, 1):.1f}") 
                            for i in range(0, int(power_max / step) + 1)]
        #else:
        #    power_max_int = math.ceil(self.right_y_max)
        #    y_ticks_power = [(i, str(i)) for i in range(0, power_max_int + 1, max(1, power_max_int // 10))]
        self.getPlotItem().getAxis('right').setTicks([y_ticks_power])
    def _update_axis_limits(self):
        if not self.data_rpm:
            return
        #update label sumbu bawah
        max_rpm = max(self.data_rpm) / 100
        x_max = max(max_rpm * 1.1, 20)
        self.setXRange(0, x_max) #view tetap
        #update label sumbu bawah
        x_max_int = math.ceil(x_max)
        ticks = [(i, str(i)) for i in range(0, x_max_int + 1, max(1, x_max_int // 20))]
        self.getPlotItem().getAxis('bottom').setTicks([ticks])
        #untuk pembaruan data pada sumbu y kiri
        max_torque = max(self.data_torque)
        y_max = max(max_torque * 1.1, 8)
        self.setYRange(0, y_max)
        y_max_int = math.ceil(y_max)
        y_ticks = [(i, str(i)) for i in range(0, y_max_int + 1, max(1, y_max_int // 10))]
        self.getPlotItem().getAxis('left').setTicks([y_ticks])
    def reset_data(self):
        self.data_rpm = []
        self.data_torque = []
        self.data_power = []
        self._refresh_plot()
    def _on_mouse_moved(self, evt):
        if len(self.data_rpm) == 0 or len(self.data_power) == 0:
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
        if self.data_rpm:
            rpm_divided = np.array(self.data_rpm) / 100
            idx = (np.abs(rpm_divided - x)).argmin()
            # filter kalau data kosong
            if x < np.min(rpm_divided) or x > np.max(rpm_divided):
                self.hover_label.setVisible(False)
                return
            if idx < len(self.data_torque) and idx < len(self.data_power):
                torque_val = self.data_torque[idx]
                power_val = self.data_power[idx] / 1000
                rpm_val = self.data_rpm[idx]
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
                        <b>Power:</b> {int(self.data_power [idx])} → {power_val:.2f} kW
                    </div>
                    """
                )
                self.hover_label.setPos(x, y)
                self.hover_label.setVisible(True)
            else:
                self.hover_label.setVisible(False)
                self.vline.setVisible(False)
                self.hline.setVisible(False)
               

