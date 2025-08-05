# 更新日志

## 0.4.1版本

### 变化

- 各内置项目模板`feffery-utils-components`依赖版本规则更新至`>=0.3.2`，以优化部分情况下顶端进度条显示异常的问题，涉及项目变动：
  - [041b787](https://github.com/CNFeffery/magic-dash/commit/041b78770b95eb7478ad9afbf6249313664468ae)
  - [fa3242f](https://github.com/CNFeffery/magic-dash/commit/fa3242fd2d1f522b07158032d4328e325074b08f)

### 优化

- 针对内置模板`magic-dash-pro`数据库初始化命令`python -m models.init_db`进行优化
  - [59df478](https://github.com/CNFeffery/magic-dash/commit/59df4784c680425e6706a8892f87cc67c32d13b2)
  - [bf58493](https://github.com/CNFeffery/magic-dash/commit/bf58493aa4c5f3a44f86377099ed4e48a8be88f9)

---

## 0.4.0版本

### 变化

- 内置各模板环境依赖`requirements.txt`更新，现已全面升级并兼容`Dash 3.x`版本，具体见：
  - [simple-tool](./magic_dash/templates/simple-tool/requirements.txt)
  - [magic-dash](./magic_dash/templates/magic-dash/requirements.txt)
  - [magic-dash-pro](./magic_dash/templates/magic-dash-pro/requirements.txt)

### 新增

- `magic-dash`、`magic-dash-pro`模板新增**url参数提取**功能示范页面，对应`views/core_pages/url_params_page.py`：

<p align="center">
    <img src="./imgs/changelog/0.4.0/url参数提取示例演示.png"></img>
</p>

- `magic-dash-pro`模板新增**系统管理-日志管理-登录日志**功能页面，主要逻辑对应`models/logs.py`、`views/core_pages/login_logs.py`、`callbacks/core_pages_c/login_logs_c.py`：

<p align="center">
    <img src="./imgs/changelog/0.4.0/系统管理-日志管理-登录日志演示.png"></img>
</p>

---

## 0.3.3版本

### 修复

- `magic-dash-pro`模板修复了上个版本中`configs/base_config.py`的`duplicate_login_check_interval`配置项数值设定错误问题

---

## 0.3.2版本

### 新增

- `magic-dash-pro`模板新增**PostgreSQL**、**MySQL**数据库支持

  具体配置见`configs/database_config.py`中的相关参数

---

## 0.3.1版本

### 新增

- `magic-dash-pro`模板新增全屏自定义水印功能：

  对应`configs/base_config.py`中的参数`enable_fullscreen_watermark`、`fullscreen_watermark_generator`，可基于当前用户信息，进行全屏水印的自定义，示例配置：

```python
# 是否开启全屏额外水印功能
enable_fullscreen_watermark: bool = True

# 当开启了全屏额外水印功能时，用于动态处理实际水印内容输出
fullscreen_watermark_generator: Callable = (
    lambda current_user: current_user.user_name + "水印测试"
)
```

<p align="center">
    <img src="./imgs/changelog/0.3.1/全屏水印演示.png"></img>
</p>

- `magic-dash`、`magic-dash-pro`模板标签页模式下，右键菜单新增刷新页面功能：

<p align="center">
    <img src="./imgs/changelog/0.3.1/右键菜单刷新页面演示.gif"></img>
</p>

- `magic-dash`、`magic-dash-pro`模板，页首新增全屏切换按钮：

<p align="center">
    <img src="./imgs/changelog/0.3.1/页首全屏切换演示.png"></img>
</p>

- `magic-dash`、`magic-dash-pro`模板，页首新增页面重载按钮：

<p align="center">
    <img src="./imgs/changelog/0.3.1/页首页面重载演示.png"></img>
</p>

- 内置各模板基于[feffery-dash-utils](https://github.com/CNFeffery/feffery-dash-utils)中的工具函数`check_python_version()`、`check_dependencies_version()`，对`Python`版本以及关键依赖库版本进行运行时强制检查，具体见各模板中的`app.py`开头相关代码

### 优化

- `magic-dash-pro`模板，针对`flask-login`用户加载函数涉及到的数据库查询操作进行优化，避免静态资源获取等非核心网络请求，触发完整的数据库查询操作额外增加计算开销

### 变化

- 内置各模板环境依赖`requirements.txt`更新，具体见：
  - [simple-tool](./magic_dash/templates/simple-tool/requirements.txt)
  - [magic-dash](./magic_dash/templates/magic-dash/requirements.txt)
  - [magic-dash-pro](./magic_dash/templates/magic-dash-pro/requirements.txt)
