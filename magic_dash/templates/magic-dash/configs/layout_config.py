from typing import Literal


class LayoutConfig:
    """页面布局相关配置参数"""

    # 核心页面侧边栏像素宽度
    core_side_width: int = 350

    # 核心页面呈现类型，可选项有'single'（单页面形式）、'tabs'（多标签页形式）
    core_layout_type: Literal["single", "tabs"] = "single"

    # 是否在页首中显示页面搜索框
    show_core_page_search: bool = True
