import math
import pyqtgraph as pg
import numpy as np
from pyqtgraph import PlotWidget as PGPlotWidget
from PySide6.QtCore import QTimer

class Widget4HPOnly(PGPlotWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setBackground('w')
        self.showGrid(x=True, y=True)
        # Tambahkan judul       
        self.setTitle("Grafik HP vs RPM", color='k', size='14pt')
        self.setLabel('left', 'Power (HP)', color='b')
        self.setLabel('bottom', 'RPM (x100)', color='k')
        # Max power label
        self.max_label = pg.TextItem("", anchor=(0, 0), color='k')
        self.addItem(self.max_label)
        # Power curve buat nampilin grafik
        self.power_curve = self.plot(pen=pg.mkPen('b', width=2), name='HP')
        # Data
        self.data_rpm = []
        self.data_power = []
        # Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self._refresh_plot)
        self.timer.start(50)
        # Default view range
        self.setXRange(0, 20)
        self.getPlotItem().vb.setLimits(xMin=0)
        self.setLimits(xMin=0, xMax=1000)
        self.setYRange(0, 2)
        self.getPlotItem().vb.setLimits(yMin=0)
        self.setLimits(xMin=0, yMax=1000)
        #garis vertikal dan horizontl untuk hover
        self.vline = pg.InfiniteLine(angle=90, movable=False, pen=pg.mkPen('k', style=pg.QtCore.Qt.DashLine))
        self.hline = pg.InfiniteLine(angle=0, movable=False, pen=pg.mkPen('k', style=pg.QtCore.Qt.DashLine))
        self.addItem(self.vline, ignoreBounds=True)
        self.addItem(self.hline, ignoreBounds=True)
        #label untuk menunjukkan data saat hover
        self.hover_label = pg.TextItem("", anchor=(0,1), color='k')
        self.addItem(self.hover_label)
        #enable mouse hover
        self.proxy = pg.SignalProxy(self.scene().sigMouseMoved, rateLimit=60, slot=self._on_mouse_moved)
    def append_data(self, rpm: int, power: int):
        try:
            self.data_rpm.append(rpm)
            self.data_power.append(power)

            self.data_rpm = self.data_rpm[-10000:]
            self.data_power = self.data_power[-10000:]
            
            self.update_axis_limits()
        except Exception as e:
            print("[append_data error]", e)

    def _refresh_plot(self):
        if not self.data_rpm:
            return
        #konversi data
        rpm_divided = [r / 100 for r in self.data_rpm]
        power_in_hp = [(p * 1.341) / 1000 for p in self.data_power]
        #perbarui plot
        self.power_curve.setData(rpm_divided, power_in_hp)
        #update label max torque & power
        try:
            max_power = max(self.data_power)
            max_power_hp = (max_power * 1.341) / 1000
            index = self.data_power.index(max_power)
            rpm = self.data_rpm[index]
            #posisi dan nama keterangan
            self.max_label.setText(
                f"Max Power = {max_power_hp:.2f} HP at RPM = {rpm}")
            self.max_label.setPos(
                self.getViewBox().viewRange()[0][0] + 1,
                self.getViewBox().viewRange()[1][1] - 0.01)
        except Exception as e:
            print("[max label error]", e)
    def update_axis_limits(self):
        if not self.data_rpm:
            return
        #update label sumbu bawah
        max_rpm = max(self.data_rpm) / 100
        x_max = max(max_rpm * 1.1, 20)
        self.setXRange(0, x_max)
        #update label bawah
        x_max_int = math.ceil(x_max)
        ticks = [(i, str(i)) for i in range(0, x_max_int + 1, max(1, x_max_int // 20))]
        self.getPlotItem().getAxis('bottom').setTicks([ticks])
        #update label sumbu kiri
        max_power_hp = max([(p * 1.341) / 1000 for p in self.data_power])
        y_max = max(max_power_hp * 1.1, 2) 
        self.setYRange(0, y_max)
        #update label y axis
        if y_max <= 2:
            num_ticks = 10 #sesuaikan ticks
            ticks = [(i, f"{i:.1f}") for i in np.linspace(0, y_max, num_ticks)] #interval 0.1
        else:
            step = round(y_max / 10, 1)
            y_max_rounded = math.ceil(y_max / step) * step
            ticks = [(round(i * step, 1), f"{round(i * step, 1):.1f}") 
                    for i in range(0, int(y_max_rounded / step) + 1)]
            
            #y_max_int = math.ceil(y_max)
            #ticks = [(i, str(i)) for i in range(0, y_max_int + 1, max(1, y_max_int // 10))]
        self.getPlotItem().getAxis('left').setTicks([ticks])
    def reset_data(self):
        self.data_rpm.clear()
        self.data_power.clear()
        self._refresh_plot()
    def _on_mouse_moved(self, evt):
        if len(self.data_rpm) == 0 or len(self.data_power) == 0:
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
        if self.data_rpm:
            rpm_divided = np.array(self.data_rpm) / 100
            idx = (np.abs(rpm_divided - x)).argmin()
            #filter kalau data kosong
            if x < np.min(rpm_divided) or x > np.max(rpm_divided):
                self.hover_label.setVisible(False)
                self.vline.setVisible(False)
                self.hline.setVisible(False)
                return
            if idx < len(self.data_rpm) and idx < len(self.data_power):
                power_val = self.data_power[idx] * 1.341/ 1000
                rpm_val = self.data_rpm[idx]
                
                #update label hover
                self.hover_label.setText(f"Power: {power_val:.2f} HP\nRPM: {rpm_val}")
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
                        <b>Power:</b> {power_val:.2f} HP
                    </div>
                    """
                )
                self.hover_label.setPos(x,y)
                self.hover_label.setVisible(True)
            else:
                self.hover_label.setVisible(False)
                self.vline.setVisible(False)
                self.hline.setVisible(False)