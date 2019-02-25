import os

from PyPDF4 import PdfFileReader, PdfFileWriter
from tempfile import NamedTemporaryFile
from PythonMagick import Image

reader = PdfFileReader(open("D:/data/pdf-scan/普通生物学（清晰PDF版）.pdf", "rb"))
for page_num in range(reader.getNumPages()):
    writer = PdfFileWriter()
    writer.addPage(reader.getPage(page_num))
    temp = NamedTemporaryFile(prefix=str(page_num), suffix=".pdf", delete=False)
    writer.write(temp)
    print(temp.name)
    tempname = temp.name
    temp.close()
    im = Image(tempname)
    im.quality(100)  # 0-100 full compression
    # 不保持比例
    #im.sample('298x412!')
    # 保持比例
    im.sample('1788x2526')
    #im.density("3000") # DPI, for better quality
    # im.read(tempname)
    im.write("D:/data/pdf-scan/temp-pdf/{}.jpeg".format(page_num))

    os.remove(tempname)
