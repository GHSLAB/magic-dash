from typing import List


class BaseConfig:
    """应用基础配置参数"""

    # 应用基础标题
    app_title: str = "Magic Dash"

    # 应用版本
    app_version: str = "dev"

    # 是否启用版本更新日志通知功能，每次的新版本更新日志将在用户点击“已阅”按钮后不再重复展示
    enable_version_changelog_modal: bool = False

    # 设置版本更新日志通知对应的markdown文件所在目录，目录下文件名格式应为“版本号.md”
    version_changelog_markdown_folder: str = "changelogs"

    # 浏览器最低版本限制规则
    min_browser_versions: List[dict] = [
        {"browser": "Chrome", "version": 88},
        {"browser": "Firefox", "version": 78},
        {"browser": "Edge", "version": 100},
    ]

    # 是否基于min_browser_versions开启严格的浏览器类型限制
    # 不在min_browser_versions规则内的浏览器将被直接拦截
    strict_browser_type_check: bool = False
