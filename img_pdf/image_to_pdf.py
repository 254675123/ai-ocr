# -*- coding: UTF-8 -*-
import os
from reportlab.lib.pagesizes import portrait
from reportlab.pdfgen import canvas
from PIL import Image
from PyPDF4 import PdfFileReader, PdfFileWriter

def mkdir(path):
    """
    创建文件夹
    :param path: 
    :return: 
    """
    path = path.strip()
    path = path.rstrip('\\')
    isExist = os.path.exists(path)
    if not isExist:
        os.mkdir(path)
        return True
    else:
        return False

def imgtopdf(input_paths, outputpath):
    """
    将单张图片转成单页的pdf
    :param input_paths: 
    :param outputpath: 
    :return: 
    """
    (maxw, maxh) = Image.open(input_paths).size
    c = canvas.Canvas(outputpath, pagesize=portrait((maxw, maxh)))
    c.drawImage(input_paths, 0, 0, maxw, maxh)
    c.showPage()
    c.save()

def image_to_pdf(image_folder, pdf_folder):
    output_pdf_dir = pdf_folder
    output_image_dir = image_folder

    # 遍历img的文件夹，获取所有的image
    page_count = 0
    for image_page_file in os.walk(output_image_dir):
        file_list = image_page_file[2]
        page_count = len(file_list)
        print(page_count)
        for page_index in range(page_count):
            page_pdf_file = '{}/{}.pdf'.format(output_pdf_dir,page_index)
            page_img_file = '{}/{}.jpg'.format(output_image_dir,page_index)

            # 开始进行pdf 到 image的转换
            print('开始第{}页image到pdf的转换'.format(page_index))
            imgtopdf(page_img_file, page_pdf_file)
            page_index += 1
    return page_count

def pdf_to_pdfs(pdf_folder, page_count):
    """
    将单页的pdf文件合并成整个文件
    :param pdf_folder: 
    :param page_count: 
    :return: 
    """
    # 创建一个pdf空白文档
    pdf_writer = PdfFileWriter()
    pdf_file_path = '{}/{}.pdf'.format(pdf_folder, 'combine')
    # 读取每页的pdf
    for page_index in range(page_count):
        page_pdf_file = '{}/{}.pdf'.format(pdf_folder, page_index)
        # 读取单页的pdf
        # 开始进行pdf 到 image的转换
        reader = PdfFileReader(page_pdf_file, strict=False)
        pdf_writer.addPage(reader.getPage(0))
        page_index += 1
    # 保存
    pdf_writer.write(open(pdf_file_path, 'wb'))


if __name__ == '__main__':
    # 指定图片的文件夹，合成的pdf会放在下面的文件夹里面
    output_image_dir = 'D:/data/pdf-scan/Scan20190115'
    output_pdf_dir = '{}/temp-pdf'.format(output_image_dir)
    mkdir(output_pdf_dir)

    page_count = image_to_pdf(output_image_dir, output_pdf_dir)
    pdf_to_pdfs(output_pdf_dir, page_count)

# 调用demo:
#imgtopdf("D:/data/pdf-scan/Scan-20190102/1.jpg", "cc.pdf")
