#export.export_widget_1.py
import os
import csv
import pandas as pd
import tempfile
from datetime import datetime
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from PySide6.QtWidgets import QMessageBox, QFileDialog, QWidget
from PySide6.QtGui import QImage, QPainter
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

def export_to_pdf_3(db, widget: QWidget, parent=None):
    default_filename = f"dynotest_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    save_path = get_save_path(default_filename, parent, "PDF Files (*.pdf)")
    if not save_path:  # User canceled the dialog
        return

    snapshot_path = None  # Inisialisasi variabel
    try:
        data = db.fetch_all_data()
        # Buat snapshot
        if widget is None:
            raise ValueError("Widget tidak valid untuk diambil snapshot.")
        
        snapshot_dir = tempfile.gettempdir()
        snapshot_path = os.path.join(snapshot_dir, f"widget_snapshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
        pixmap = widget.grab()
        pixmap.save(snapshot_path)
        
        if not os.path.exists(snapshot_path):
            raise ValueError(f"Gagal membuat snapshot di path {snapshot_path}")
        
        # PDF setup
        c = canvas.Canvas(save_path, pagesize=landscape(A4))
        width, height = landscape(A4)
        
        # Add title
        c.setFont("Times-Bold", 24)
        c.drawCentredString(width / 2, height - 50, "Dynamits")
        
        # Add widget snapshot
        image_width = 500
        image_height = 300
        image_x = (width - image_width) / 2
        image_y = height - 400
        c.drawImage(snapshot_path, image_x, image_y, image_width, image_height)
        c.showPage()
        # Prepare table data
        header = [
            "Timestamp",
            "RPM",
            "RPM\nCal",
            "RPM\nCal\nFactor",
            "Torque\n(N.m)",
            "Torque\nCal (N.m)",
            "Torque\nCal\nFactor",
            "Power (W)"
        ]
        col_widths = [100, 60, 60, 80, 60, 60, 80, 60]
        row_height = 20
        rows_per_page = int(height - 100) // row_height
        # Iterate through data to create multiple pages
        for page_start in range(0, len(data), rows_per_page):
            page_end = page_start + rows_per_page
            page_data = data[page_start:page_end]
            table_data = [header] + page_data

            #hitung posisi horizontal (center)
            table_width = sum(col_widths)
            table_x = (width - table_width) / 2
            table_y = height - 50

            # Tabel
            table = Table(table_data, colWidths=col_widths)
            table.setStyle(
                TableStyle(
                    [
                        ("FONT", (0, 0), (-1, 0), "Times-Bold", 12),  # Bold header
                        ("FONT", (0, 1), (-1, -1), "Times-Roman", 10),
                        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),  # Header background
                        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                        ("GRID", (0, 0), (-1, -1), 1, colors.black),  # Grid lines
                        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                    ]
                )
            )
            table.wrapOn(c, width, height)
            table.drawOn(c, table_x, table_y - (len(page_data) + 1) * row_height)

            if page_end < len(data):
                c.showPage()
                
        # Finalize PDF
        c.save()
        show_notification(parent, f"PDF berhasil disimpan di:\n{save_path}")

    except Exception as e:
        QMessageBox.critical(parent, "Error", f"Gagal menyimpan PDF: {e}")
    finally:
        # Hapus snapshot file jika ada
        if snapshot_path and os.path.exists(snapshot_path):
            os.remove(snapshot_path)
