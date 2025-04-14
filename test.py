from PIL import Image  # 导入 Python Imaging Library (PIL) 中的 Image 模块，用于处理图像

# 使用 Image.open() 打开指定路径的图像文件，并将其赋值给变量 a
a = Image.open("img\lunna.png")

a.show()  # 调用 show() 方法显示图像（会弹出一个窗口）

# 打印图像的格式（例如 PNG、JPEG 等）
print("图像的格式为:", a.format)

# 打印图像的尺寸（宽度和高度，以像素为单位，返回一个元组，例如 (512, 512)）
print("图像的尺寸为:", a.size)

# 打印图像的模式（表示图像的颜色类型，例如 RGB 表示彩色图像，L 表示灰度图像）
print("图像的颜色类型为:", a.mode)