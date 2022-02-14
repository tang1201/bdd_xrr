from PIL import Image # 图像处理相关库
import os # 系统库

path = os.getcwd() # 获取当前所在文件夹的路径
wx_img = Image.open(os.path.join(path,'tx.jpg')) # 头像路径
bdd_img = Image.open(os.path.join(path,'bdd.png')) # 冰墩墩路径
xrr_img = Image.open(os.path.join(path,'xrr.png')) # 雪容融路径

wx_rgba = wx_img.convert('RGBA') # 将头像转为 RGBA 模式的 32 位彩色图像
bdd_rgba = bdd_img.convert('RGBA') # 将冰墩墩图片转为 RGBA 模式的 32 位彩色图像
xrr_rgba = xrr_img.convert('RGBA') # 将雪容融图片转为 RGBA 模式的 32 位彩色图像

wx_x, wx_y = wx_rgba.size # 返回头像的宽高
bdd_x, bdd_y = bdd_rgba.size # 返回冰墩墩rgba图片的宽高
xrr_x, xrr_y = xrr_rgba.size # 返回雪容融rgba图片的宽高

scale = 5 # 缩放的比例值 数值越大，冰墩墩雪容融越小，这里我采用5
img_scale = max(wx_x / (scale * bdd_x), wx_y / (scale * bdd_y))
new_size = (int(bdd_x * img_scale), int(bdd_y * img_scale))
bdd = bdd_rgba.resize(new_size, resample=Image.ANTIALIAS)  # 高质量改变图像大小为new_size
# bdd.show()

img_scale = max(wx_x / (scale * xrr_x), wx_y / (scale * xrr_y))
new_size = (int(xrr_x * img_scale), int(xrr_y * img_scale))
xrr = xrr_rgba.resize(new_size, resample=Image.ANTIALIAS) # 高质量改变图像大小为new_size
# xrr.show()

bdd_x, bdd_y = bdd.size # 返回冰墩墩图片原始的宽高
wx_rgba.paste(bdd, (0, wx_y-bdd_y), bdd) # wx_rgba是大图，bdd是小图，将两张图粘在一起 左下角,坐标(0, wx_y-bdd_y) 可调 最后一个bdd使得透明起作用
#wx_rgba.show()

xrr_x, xrr_y = xrr.size # 返回雪容融图片原始的宽高
wx_rgba.paste(xrr, (wx_x-bdd_x, 0), xrr) # wx_rgba是大图，xrr是小图，将两张图粘在一起 右上角，坐标(wx_x-bdd_x, 0) 可调 最后一个xrr使得透明起作用
wx_rgba.show() # 显示绘制完成的图片

wx_rgba.save(os.path.join(path,'bdd_xrr.png'))
