import pytesseract
lang = "eng"#英文 中文：chi_sim
img = "image/01.jpg"#定义图片路径变量
pytesseract.pytesseract.tesseract_cmd=r"D:\Tesseract-OCR\tesseract.exe"
pytesseract.image_to_string(img,lang)#识别文字（图片：img 语言：lang）
