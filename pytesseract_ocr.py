import pytesseract
import cv2

class OCR:
    def __init__(self,image):
        self.image=image
    def image_reading(self):
        original_image=cv2.imread(self.image)
        gray_image=cv2.cvtColor(original_image,cv2.COLOR_BGR2GRAY)
        return gray_image
    def image_preprocessing(self):
        gray_image=self.image_reading()
        ret,thresh=cv2.threshold(gray_image,128,255,cv2.THRESH_BINARY)
        cv2.imshow("thresh",thresh)
        cv2.waitKey(0)
        return thresh
    def ocr_reading(self):
        thresh=self.image_preprocessing()
        text=pytesseract.image_to_string(thresh)
        print(text)

if __name__=="__main__":
    image=("/home/khundmeer/Documents/image1.png")
ocr=OCR(image)
ocr.ocr_reading()

