
<div align="center">
 <img alt="logo" height="300px" src="img\lunna.png">
</div>



<h1 align="center">Image Manipulation</h1>
<h1 align="center">图片处理代码整合</h1>


## 项目目录结构

```
Image_Manipulation/
│
├── README.md             # 项目说明文档
├── img/                  # 图像文件目录
│   └── lunna.png         # 示例图像文件
├── test.py               # 图像显示测试脚本
├── photo_folder.py       # 批量分批保存图片工具
├── photo_remove.py       # 批量删除指定类型文件工具
└── photo_rename.py       # 批量重命名图像文件工具
```

## 文件说明

### test.py
测试用例

### photo_folder.py
批量处理图像保存到指定目录，按照分类名字存储到不同子文件夹中。

### photo_remove.py
批量删除指定目录下的特定类型文件（默认为.jpg文件），并统计删除的文件数量。

### photo_rename.py
批量重命名指定目录下的图像文件，支持.jpg和.png格式，按照指定格式重新命名。

## 使用说明
各脚本可独立运行，使用前可能需要根据实际需求修改文件路径等配置。

