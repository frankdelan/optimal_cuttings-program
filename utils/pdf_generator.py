import os
import sys

from PySide6.QtWidgets import QMessageBox
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import datetime


def generate_pdf(data, path):
    try:
        pdf_filename = set_filename(path)
        base_path = getattr(sys, '_MEIPASS', '.')
        font_name = "Courier"
        font_path = f"{base_path}/{font_name}.ttf"
        pdfmetrics.registerFont(TTFont(font_name, font_path))

        c = canvas.Canvas(pdf_filename, pagesize=(letter[1], letter[0]))

        fill_pdf(c, data, font_name, pdf_filename)

    except Exception as e:
        show_info_dialog(f"Произошла ошибка: {str(e)}")


def show_info_dialog(message):
    msg_box = QMessageBox()
    msg_box.setWindowTitle('Информация')
    msg_box.setText(message)
    msg_box.exec()


def check_space(c: canvas, y: int, line_height: int, base_vert_indent: int):
    if y - line_height < letter[0] * 0.03:
        c.showPage()
        y = base_vert_indent
    else:
        y -= line_height
    return y


def set_filename(path):
    desktop_path = os.path.expanduser("~\Desktop")
    if path:
        pdf_filename = f"{path}/{datetime.now().date()}.pdf"
    else:
        pdf_filename = f"{desktop_path}\{datetime.now().date()}.pdf"
    return pdf_filename


def fill_pdf(c, data, font_name, pdf_filename):
    base_hor_indent = letter[1] * 0.03
    base_vert_indent = letter[0] * 0.95
    x, y = base_hor_indent, base_vert_indent
    line_height = 20
    gap = 40
    for item in data:
        c.setFont(font_name, 12)
        if y - line_height < letter[0] * 0.03:
            c.showPage()
            y = base_vert_indent
        c.drawString(x, y, f"Остаток = {item[1]}")
        y = check_space(c, y, line_height, base_vert_indent)
        c.setFont(font_name, 12)
        for segment in item[0]:
            if x + gap > letter[1] * 0.95:
                x = base_hor_indent
                y = check_space(c, y, line_height, base_vert_indent)
                c.setFont(font_name, 12)
                c.drawString(x, y, f"[{segment}]")
            else:
                c.drawString(x, y, f"[{segment}]")
                x += gap
        x = base_hor_indent
        y -= 5
        c.drawString(x, y, "___________________")
        y = check_space(c, y, line_height, base_vert_indent)
    c.save()
    show_info_dialog(f"PDF-файл успешно создан: {pdf_filename}")
