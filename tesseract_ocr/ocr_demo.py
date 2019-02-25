from PIL import Image
import pytesseract
# 英文还可以
text = pytesseract.image_to_string(Image.open('en_1.png'),lang='eng')
print(text)

# 但中文效果差
text = pytesseract.image_to_string(Image.open('cn_1.jpg'),lang='chi_sim')
print(text)