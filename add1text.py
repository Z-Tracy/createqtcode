#-*- coding: utf-8 -*-

from PIL import Image,ImageFont,ImageDraw,ImageFont
import qrcode

def addText(hh,id):
    ttfont = ImageFont.truetype("msyh.ttc",23)
    im = Image.open('1.png')
    draw = ImageDraw.Draw(im)
    draw.text((138,300), '{0}'.format(hh), fill=(0, 0, 0), font=ttfont)
    # im.show()
    im.save(r'img\{0}.png'.format(id))

def addImage(hh,id):
    im=Image.open('hf.png')
    # im=im.rotate(20)
    im1=Image.open('ios_qr_code.png')
    # (w,h) = im1.size()
    # w = w*2
    # h =h*2
    # im1.thumbnail((709,709))
    im1=im1.resize((303,300)) # 1的尺寸
    # im1=im1.resize((250,250))
    im.paste(im1,(317,306))
    im.save('1.png')
    addText(hh,id)


def creQrcode(hh,id):
    # img = qrcode.make("www.zhuanzhuan.com")
    # img.save("test.png")
    ipa = "http://www.dangkr.com/mobile/goods.php?u=56&id={0}".format(id)
    qr = qrcode.QRCode(version=1,
                       error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=8,
                       border=1,
                       )
    qr.add_data(ipa)
    qr.make(fit=True)
    img = qr.make_image()
    img.save('ios_qr_code.png')
    addImage(hh,id)

# id =354

hhs = [hh.strip() for hh in open('huohao.txt', 'r')]
ids = [id.strip() for id in open('id.txt', 'r')]
# print(hhs,ids)
#
# with open('huohao.txt', 'r') as f:
#         hhs = f.read()
#         print(hhs)
# with open('id.txt', 'r') as f:
#         ids = f.read()
#         print(ids)
#
for (hh,id) in zip(hhs,ids):
    print(hh,id)
    creQrcode(hh,id)
# creQrcode(id)

