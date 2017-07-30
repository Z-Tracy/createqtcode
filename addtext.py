#-*- coding: utf-8 -*-

from PIL import Image,ImageFont,ImageDraw,ImageFont
import qrcode

def addText():
    ttfont = ImageFont.truetype("msyh.ttc",23)
    im = Image.open('1.png')
    draw = ImageDraw.Draw(im)
    draw.text((138,300), 'CLG000352', fill=(255, 255, 255), font=ttfont)
    im.show()

def addImage():
    im=Image.open('dk.png')
    # im=im.rotate(20)
    im1=Image.open('ios_qr_code.png')
    # (w,h) = im1.size()
    # w = w*2
    # h =h*2
    # im1.thumbnail((709,709))
    im1=im1.resize((303,300)) # 1的尺寸
    # im1=im1.resize((250,250))
    im.paste(im1,(317,306))
    im.show()
    im.save('1.png')

def creQrcode():
    # img = qrcode.make("www.zhuanzhuan.com")
    # img.save("test.png")
    ipa = "http://www.dangkr.com/mobile/goods.php?u=56&id=352"
    qr = qrcode.QRCode(version=1,
                       error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=8,
                       border=1,
                       )
    qr.add_data(ipa)
    qr.make(fit=True)
    img = qr.make_image()
    img.save('ios_qr_code.png')

creQrcode()
addImage()
addText()

