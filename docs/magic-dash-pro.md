# `magic-dash-pro`

多页面+用户登录应用模板。

## 1 创建方式

```bash
magic-dash create --name magic-dash-pro
```

## 2 应用初始化启动

- 安装项目依赖库

```bash
pip install -r requirements.txt
```

- 用户信息数据库初始化

```bash
python -m models.init_db
```

- 启动应用

```bash
python app.py
```

- 访问应用

应用默认地址：http://127.0.0.1:8050

- 自带管理员账号信息

```
用户名：admin
密码：admin123
```

## 3 项目目录结构

```bash
magic-dash-pro
 ┣ assets # 静态资源目录
 ┃ ┣ css # 样式文件目录
 ┃ ┣ imgs # 图片文件目录
 ┃ ┣ js # 浏览器回调函数目录
 ┃ ┗ favicon.ico # 网页图标
 ┣ callbacks # 回调函数模块
 ┣ components # 自定义组件模块
 ┣ configs # 配置参数模块
 ┣ models # 数据库模型模块
 ┣ utils # 工具函数模块
 ┣ views # 页面模块
 ┣ magic_dash_pro.db # 数据库文件（初始化后自动生成）
 ┣ server.py # 应用初始化模块
 ┣ app.py # 应用主文件
 ┗ requirements.txt # 项目依赖信息
```

## 4 主要功能配置说明

### 4.1 浏览器版本检测&限制

> `BaseConfig.min_browser_versions`

针对用户浏览器最低版本检测功能，配置所依赖的相关浏览器类型及最低版本信息，默认值：

```python
[
    {"browser": "Chrome", "version": 88},
    {"browser": "Firefox", "version": 78},
    {"browser": "Edge", "version": 100},
]
```

> `BaseConfig.strict_browser_type_check`

针对用户浏览器最低版本检测功能，配置是否开启严格的浏览器类型限制，默认值：`False`，设置为`True`后，将依据`min_browser_versions`参数，直接拦截不在所列举范围内的浏览器类型。
