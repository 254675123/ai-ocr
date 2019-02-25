
#导入PdfFileReader和PdfFileWriter
from PyPDF4 import PdfFileReader, PdfFileWriter

#PythonMagick,单页PDF转图片
from PythonMagick import Image

def readPdf_page_by_page(filepath):
    #获取一个pdf对象
    pdf_input = PdfFileReader(open(filepath, 'rb'))
    #获取pdf页数
    page_count = pdf_input.getNumPages()
    #获取pdf第n页的内容
    for n in range(page_count):

        im = Image()
        #im.density("300")
        im.read(filepath + '[' + str(1) + ']')
        im.magick("jpg")
        im.write(filepath + str(n+1)+".jpg")


def readPdf_test_read_write():
    #获取一个pdf对象
    pdf_input = PdfFileReader(open(r'd:/data/pdf-scan/普通生物学（清晰PDF版）.pdf', 'rb'))
    #获取pdf页数
    page_count = pdf_input.getNumPages()
    #获取pdf第四页的内容
    page = pdf_input.getPage(3)
    #page.extractText()
    #page['/Contents']
    #获取一个pdfWriter对象
    pdf_output = PdfFileWriter()
    # 将一个 PageObject 加入到 PdfFileWriter 中
    pdf_output.addPage(page)
    #把新pdf保存
    pdf_output.write(open(r'd:/data/pdf-scan/n.pdf','wb'))


# 转换pdf为图片
# 代码暂时不可用
filepath = 'D:/data/pdf-scan/普通生物学（清晰PDF版）.pdf'
readPdf_page_by_page(filepath)