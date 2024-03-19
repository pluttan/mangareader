import os
from fpdf import FPDF


def convert_images_to_pdf(folder_path, output_pdf_path):
    pdf = FPDF()

    # Получаем список файлов в папке
    image_files = [f for f in os.listdir(
        folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Сортируем файлы по имени, чтобы сохранить порядок
    image_files.sort()

    # Обрабатываем каждый файл
    for image_file in image_files:
        if image_file.endswith(".jpg") or image_file.endswith(".png"):
            image_path = os.path.join(folder_path, image_file)
            pdf.add_page()
            # Добавляем изображение на страницу с размерами A4 (210x297 мм)
            pdf.image(image_path, 0, 0, 210, 297)

    # Сохраняем PDF-файл
    pdf.output(output_pdf_path, "F")


# Укажите путь к папке с фотографиями
folder_path = "путь_к_папке"

# Укажите путь для сохранения PDF-файла
output_pdf_path = "путь_для_сохранения_pdf.pdf"

# Вызываем функцию для конвертации фотографий в PDF
convert_images_to_pdf(folder_path, output_pdf_path)
