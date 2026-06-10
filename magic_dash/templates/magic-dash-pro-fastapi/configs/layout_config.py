from typing import Literal


class LayoutConfig:
    """页面布局相关配置参数"""

    # 核心页面侧边栏像素宽度
    core_side_width: int = 350

    # 核心页面呈现类型，可选项有'single'（单页面形式）、'tabs'（多标签页形式）
    core_layout_type: Literal["single", "tabs"] = "single"

    # 是否在页首中显示页面搜索框
    show_core_page_search: bool = True


class LoginConfig:
    """登录页面相关配置参数"""

    # 登录页面布局风格，可选项有'center'（居中布局）、'right'（左右分割，登录框在右）
    login_page_style: Literal["center", "right"] = "center"
    # 登录卡片宽度（像素）
    login_card_width: int = 400
    # 登录页面背景内容形式，可选项有'image'（图片内容）、'video'（视频内容）
    login_content_type: Literal["image", "video"] = "image"
    # 登录页面背景图片路径，仅当login_content_type为'image'时有效
    login_bg_image: str = "./assets/imgs/login/left-side-bg.svg"
    # 登录页面背景视频路径，仅当login_content_type为'video'时有效
    login_bg_video: str = "./assets/videos/login-bg.mp4"
