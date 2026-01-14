import os
import csv
import pandas as pd
import pyqtgraph.exporters as pg_exporters  

from datetime import datetime
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from PySide6.QtWidgets import QMessageBox, QFileDialog, QWidget
from PySide6.QtGui import QPixmap
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from pathlib import Path

def show_notification(parent, message):
    msg = QMessageBox(parent)
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle("Export Berhasil")
    msg.setText(message)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec()

def get_save_path(default_filename, parent, file_filter):
    # Dapatkan direktori Documents pengguna
    default_dir = Path.home() / "Documents"
    if not default_dir.exists():  # Jika folder Documents tidak ada
        default_dir.mkdir(parents=True, exist_ok=True)  # Buat folder Documents
    
    # Gabungkan default directory dengan nama file default
    default_path = str(default_dir / default_filename)

    # Tampilkan dialog Save As dengan default directory
    save_path, _ = QFileDialog.getSaveFileName(
        parent,
        "Simpan File",
        default_path,
        file_filter
    )
    return save_path

def export_to_png_5(widget_5, parent):
    try:
        if widget_5 is None:
            raise ValueError("Widget tidak valid.")
        default_filename = f"widget_snapshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        save_path = get_save_path(default_filename, parent, "Image Files (*.png)")

        if not save_path:  # User canceled the dialog
            return
        
        #ambil snapshot dari widget
        pixmap = widget_5.grab()
        pixmap.save(save_path)
        QMessageBox.information(
            parent, "Sukses", f"Gambar berhasil disimpan di:\n{save_path}"
        )
    except Exception as e:
        QMessageBox.critical(
            parent, "Error", f"Gagal menyimpan gambar: {e}"
        )
        
    
  