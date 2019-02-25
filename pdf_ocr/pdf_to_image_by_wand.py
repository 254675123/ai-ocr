# -*- coding: utf-8 -*-
import io
import os
from wand.image import Image
# from wand.color import Color
from PyPDF4 import PdfFileReader, PdfFileWriter
# from tempfile import NamedTemporaryFile
from tencent_ocr import tencent_ocr_api
memo = {}
def getPdfReader(filename):
    reader = memo.get(filename, None)
    if reader is None:
        reader = PdfFileReader(filename, strict=False)
        memo[filename] = reader
    return reader


def pdf_to_images(input_pdf_file, output_img_file):
    # 将pdf文件转为jpg图片文件
    # ./PDF_FILE_NAME 为pdf文件路径和名称
    image_pdf = Image(filename=input_pdf_file, resolution=300)
    image_jpeg = image_pdf.convert('jpg')

    # wand已经将PDF中所有的独立页面都转成了独立的二进制图像对象。我们可以遍历这个大对象，并把它们加入到req_image序列中去。
    req_image = []
    for img in image_jpeg.sequence:
        img_page = Image(image=img)
        req_image.append(img_page.make_blob('jpg'))

    # 遍历req_image,保存为图片文件
    i = 0
    for img in req_image:
        image_file = '{}/{}.jpg'.format(output_img_file, i)
        ff = open(image_file, 'wb')
        ff.write(img)
        ff.close()
        i += 1

    return image_file

def pdf_to_image(input_pdf_file, output_img_file):
    # 将pdf文件转为jpg图片文件
    # ./PDF_FILE_NAME 为pdf文件路径和名称
    image_pdf = Image(filename=input_pdf_file, resolution=300)
    image_jpeg = image_pdf.convert('jpg')

    # wand已经将PDF中所有的独立页面都转成了独立的二进制图像对象。我们可以遍历这个大对象，并把它们加入到req_image序列中去。
    req_image = []
    for img in image_jpeg.sequence:
        img_page = Image(image=img)
        req_image.append(img_page.make_blob('jpg'))

    # 遍历req_image,保存为图片文件
    i = 0
    for img in req_image:

        ff = open(output_img_file, 'wb')
        ff.write(img)
        ff.close()
        i += 1


def split_pdf_by_page(input_pdf_filepath, output_pdf_dir):
    pdf_reader = getPdfReader(input_pdf_filepath)
    # 获取pdf页数
    page_count = pdf_reader.getNumPages()
    # 获取pdf第n页的内容
    for page_num in range(page_count):
        writer = PdfFileWriter()
        writer.addPage(pdf_reader.getPage(page_num))
        #temp = NamedTemporaryFile(prefix=str(page_num), suffix=".pdf", delete=False)
        tempname = '{}/{}.pdf'.format(output_pdf_dir, page_num)
        writer.write(open(tempname, 'wb'))

        #yield tempname





def convert_pdf_to_txt():
    # 转换pdf为图片
    input_pdf_filepath = 'D:/data/pdf-scan/Scan20190115.pdf'
    output_pdf_dir = 'D:/data/pdf-scan/temp-pdf'
    output_image_dir = 'D:/data/pdf-scan/temp-img'
    output_text_filepath = 'D:/data/pdf-scan/普通生物学（清晰PDF版）.txt'

    split_pdf_by_page(input_pdf_filepath, output_pdf_dir)
    #page_count = len(os.walk(output_pdf_dir))
    #print(page_count)
    for pdf_page_file in os.walk(output_pdf_dir):
        file_list = pdf_page_file[2]
        page_count = len(file_list)
        print(page_count)
        page_index = 0
        for page_index in range(page_count):
            page_pdf_file = '{}/{}.pdf'.format(output_pdf_dir,page_index)
            page_img_file = '{}/{}.jpg'.format(output_image_dir,page_index)

            # 开始进行pdf 到 image的转换
            print('开始第{}页pdf到image的转换'.format(page_index))
            pdf_to_image(page_pdf_file, page_img_file)
            # 开始进行图片到文本的转换
            print('开始第{}页image到text的转换'.format(page_index))
            #page_text = tencent_ocr_api.invoke_api_file(page_img_file)
            page_text = ''  # 这里先不调用上面的图片转文字，如果需要，打开上面注释即可。
            print(page_text)
            print('page {} has generated.'.format(page_index))
            page_index += 1
            saveFile(page_text, output_text_filepath)
            removeCache()


def removeCache():
    # remove prefix magick
    # C:\Users\Administrator\AppData\Local\Temp
    #catch_path = '/tmp'
    catch_path = 'C:/Users/Administrator/AppData/Local/Temp'
    for name in os.walk(catch_path):
        file_list = name[2]

        for f in file_list:
            try:

                if f.startswith('magick'):
                    os.remove('{}/{}'.format(catch_path,f))
            except Exception:
                print("无法删除，可能正在被使用。")
                continue
        break


def saveFile(data, file):
    fout = open(file, 'a')
    fout.write('\n'.join(data))
    fout.write('\n')
    fout.close()
# 这个可以用
convert_pdf_to_txt()