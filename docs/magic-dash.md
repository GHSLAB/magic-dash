# `magic-dash`

基础多页面应用模板。

## 1 创建方式

```bash
magic-dash create --name magic-dash
```

## 2 应用初始化启动

- 安装项目依赖库

```bash
pip install -r requirements.txt
```

- 启动应用

```bash
python app.py
```

- 访问应用

应用默认地址：http://127.0.0.1:8050

## 3 项目目录结构

```bash
magic-dash
 ┣ assets # 静态资源目录
 ┃ ┣ css # 样式文件目录
 ┃ ┣ imgs # 图片文件目录
 ┃ ┣ js # 浏览器回调函数目录
 ┃ ┗ favicon.ico # 网页图标
 ┣ callbacks # 回调函数模块
 ┣ components # 自定义组件模块
 ┣ configs # 配置参数模块
 ┣ utils # 工具函数模块
 ┣ views # 页面模块
 ┣ server.py # 应用初始化模块
 ┣ app.py # 应用主文件
 ┗ requirements.txt # 项目依赖信息
```
