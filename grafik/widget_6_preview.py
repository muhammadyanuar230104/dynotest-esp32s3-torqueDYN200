import math
import pyqtgraph as pg
import numpy as np
from pyqtgraph import PlotWidget as PGPlotWidget
from PySide6.QtCore import QTimer
 
class Widget6PowerOnly(PGPlotWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setBackground('w')
        self.showGrid(x=True, y=True)
        # Judul dan label sumbu
        self.setTitle("Grafik Power (kW) vs RPM", color='k', size='14pt')
        self.setLabel('bottom', 'RPM (x100)', color='k')
        self.setLabel('left', 'Power (kW)', color='b')
        #default view range
        self.setXRange(0, 20)
        self.getPlotItem().vb.setLimits(xMin=0)
        self.setLimits(xMin=0, xMax=1000)
        self.setYRange(0, 1)
        self.getPlotItem().vb.setLimits(yMin=0)
        self.setLimits(xMin=0, yMax=1000)
        # Text label untuk nilai maksimum
        self.max_label = pg.TextItem("", anchor=(0, 0), color='k')
        self.addItem(self.max_label)
        # Garis power (biru)
        self.power_curve = self.plot(pen=pg.mkPen('b', width=2), name='Power')
        # Data
        self.rpm_data = []
        self.power_data_watt = []
        # Timer untuk refresh otomatis
        self.timer = QTimer()
        self.timer.timeout.connect(self._refresh_plot)
        self.timer.start(50)
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
    def append_data(self, rpm: int, power_watt: int):
        try:
            self.rpm_data.append(rpm)
            self.power_data_watt.append(power_watt)

            self.rpm_data = self.rpm_data[-10000:]
            self.power_data_watt = self.power_data_watt[-10000:]
            self._update_axis_limits()           
        except Exception as e:
            print("[append_data error]", e)
    def _refresh_plot(self):
        if not self.rpm_data:
            return
        #convert rpm and power
        rpm_scaled = [r / 100 for r in self.rpm_data]
        power_kw = [p / 1000 for p in self.power_data_watt]
        #update curve
        self.power_curve.setData(rpm_scaled, power_kw)

        try:
            max_power_watt = max(self.power_data_watt)
            index = self.power_data_watt.index(max_power_watt)
            max_power_kw = max_power_watt / 1000
            rpm = self.rpm_data[index]

            self.max_label.setText(
                f"Max Power = {max_power_kw:.2f} kW at RPM = {rpm}")
            self.max_label.setPos(
                self.getViewBox().viewRange()[0][0] + 1,
                self.getViewBox().viewRange()[1][1] - 0.01,
            )
        except Exception as e:
            print("[max label error]", e)
    def _update_axis_limits(self):
        if not self.rpm_data:
            return
        #calculate max values for x and y axis
        max_rpm = max(self.rpm_data) / 100
        x_max = max(max_rpm * 1.1, 20)
        self.setXRange(0, x_max)
        x_max_int = math.ceil(x_max)
        #calculate untuk power
        max_power_kw = max(self.power_data_watt) / 1000
        y_max = max(max_power_kw * 1.1, 1)
        self.setYRange(0, y_max)
        #calculate and update ticks
        x_ticks = [(i, str(i)) for i in range(0, x_max_int + 1, max(1, x_max_int // 20))]
        if y_max <= 1:
            y_ticks = [(i / 10, f"{i / 10:.1f}") for i in range(0, 11)] #interval 0.1
        else:
            step = round(y_max / 10, 1)
            y_max_rounded = math.ceil(y_max / step) * step
            y_ticks = [(round(i * step, 1), f"{round(i * step, 1):.1f}") 
               for i in range(0, int(y_max_rounded / step) + 1)]
            
            #y_max_int = math.ceil(y_max)
            #y_ticks = [(i, str(i)) for i in range(0, y_max_int + 1, max(1, y_max_int // 10))]
        #plot grafik
        self.getPlotItem().getAxis('left').setTicks([y_ticks])
        self.getPlotItem().getAxis('bottom').setTicks([x_ticks])
    def reset_data(self):
        self.rpm_data.clear()
        self.power_data_watt.clear()
        self._refresh_plot()
    def _on_mouse_moved(self, evt):
        if len(self.rpm_data) == 0 or len(self.power_data_watt) == 0:
            return 
        pos = evt[0]
        if not self.sceneBoundingRect().contains(pos):
            self.hover_label.setVisible(False)
            self.vline.setVisible(False)
            self.hline.setVisible(False)
            return
        mouse_point = self.getPlotItem().vb.mapSceneToView(pos)
        x = mouse_point.x()
        y = mouse_point.y()
        view_x_range, view_y_range = self.getPlotItem().vb.viewRange()
        #cek apakah mouse berada dalam rentang tampilan
        if not (view_x_range[0] <= x <= view_x_range[1]) or not (view_y_range[0] <= y <= view_y_range[1]):
            self.hover_label.setVisible(False)
            self.vline.setVisible(False)
            self.hline.setVisible(False)
            return
        self.vline.setVisible(True)
        self.hline.setVisible(True)
        self.vline.setPos(x)
        self.hline.setPos(y)
        #cari index terdekat berdasarkan posisi x (rpm)
        if self.rpm_data:
            rpm_scaled = np.array(self.rpm_data) / 100
            idx = (np.abs(rpm_scaled - x)).argmin()
            #filter kalau data kosong
            if x < np.min(rpm_scaled) or x > np.max(rpm_scaled):
                self.hover_label.setVisible(False)
                self.vline.setVisible(False)
                self.hline.setVisible(False)
                return
            if idx < len(self.rpm_data) and idx < len(self.power_data_watt):
                power_val = self.power_data_watt[idx] / 1000
                rpm_val = self.rpm_data[idx]
                #update label hover
                self.hover_label.setText(f"Power: {power_val:.2f} kW\nRPM: {rpm_val}")
                self.hover_label.setPos(x, y)
                self.hover_label.setVisible(True)
                #gunakan html untuk menampilkan label hover
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
                        <b>RPM:</b> {rpm_val} <br>
                        <b>Power:</b> {power_val:.2f} kW
                    </div>
                    """
                )
                self.hover_label.setPos(x,y)
                self.hover_label.setVisible(True)
            else:
                self.hover_label.setVisible(False)
                self.vline.setVisible(False)
                self.hline.setVisible(False)
