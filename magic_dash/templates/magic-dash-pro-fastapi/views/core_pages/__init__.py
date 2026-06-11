import re
from dash import html, dcc
import feffery_antd_components as fac
import feffery_utils_components as fuc
from feffery_dash_utils.style_utils import style

from server import current_user
from configs import RouterConfig, LayoutConfig, AuthConfig
from views.core_pages import independent_page_demo, independent_wildcard_page_demo
from components import (
    core_side_menu,
    core_header,
    personal_info,
    user_manage,
    department_manage,
    version_changelog_modal,
)

# 令绑定的回调函数子模块生效
import callbacks.core_pages_c  # noqa: F401


def render(current_user_access_rule: str, current_pathname: str = None):
    """渲染核心页面骨架

    Args:
        current_user_access_rule (str): 当前用户页面可访问性规则
        current_pathname (str, optional): 当前页面pathname. Defaults to None.
    """

    # 判断是否需要独立渲染
    if current_pathname in RouterConfig.independent_core_pathnames:
        # 返回不同地址规则对应页面内容
        if current_pathname == "/core/independent-page/demo":
            return independent_page_demo.render()

    # 判断是否需要独立通配渲染
    elif any(
        pattern.match(current_pathname)
        for pattern in RouterConfig.independent_core_pathnames
        if isinstance(pattern, re.Pattern)
    ):
        # 获取命中当前地址的第一个通配规则
        match_pattern = None
        for pattern in RouterConfig.independent_core_pathnames:
            if isinstance(pattern, re.Pattern):
                if pattern.match(current_pathname):
                    # 更新命中的通配规则
                    match_pattern = pattern
                    break
        # 返回不同地址通配规则对应页面内容
        if match_pattern == RouterConfig.wildcard_patterns["独立通配页面演示"]:
            return independent_wildcard_page_demo.render(pathname=current_pathname)

    return html.Div(
        [
            # 核心页面常量参数数据
            dcc.Store(
                id="core-page-config",
                data=dict(
                    core_side_width=LayoutConfig.core_side_width,
                    core_layout_type=LayoutConfig.core_layout_type,
                    core_header_style=LayoutConfig.core_header_style,
                ),
            ),
            # 核心页面独立路由监听
            dcc.Location(id="core-url"),
            # 核心页面pathname静默更新
            dcc.Location(id="core-silently-update-pathname", refresh="callback-nav"),
            # ctrl+k快捷键监听
            fuc.FefferyKeyPress(id="core-ctrl-k-key-press", keys="ctrl.k"),
            # 全屏化切换
            fuc.FefferyFullscreen(
                id="core-fullscreen",
            ),
            # 注入个人信息模态框
            personal_info.render(),
            # 若当前用户角色为系统管理员
            *(
                # 注入用户管理抽屉
                [
                    user_manage.render(),
                    department_manage.render(),
                ]
                if current_user.user_role == AuthConfig.admin_role
                else []
            ),
            # 版本更新日志通知
            version_changelog_modal.render(),
            # 页首
            core_header.render(current_user_access_rule=current_user_access_rule),
            # 主题区域
            fac.AntdRow(
                [
                    # 侧边栏
                    fac.AntdCol(
                        core_side_menu.render(
                            current_user_access_rule=current_user_access_rule
                        ),
                        flex="none",
                    ),
                    # 内容区域
                    fac.AntdCol(
                        # 根据页面呈现类型，渲染具有相同id的页面挂载目标组件
                        (
                            # 单页面形式
                            fac.AntdSkeleton(
                                html.Div(
                                    id="core-container",
                                    style=style(padding="36px 42px"),
                                ),
                                listenPropsMode="include",
                                includeProps=["core-container.children"],
                                active=True,
                                style=style(padding="36px 42px"),
                            )
                            if LayoutConfig.core_layout_type == "single"
                            # 多标签页形式
                            else fac.Fragment(
                                [
                                    # 多标签页形式，session生命周期内标签页key值缓存
                                    dcc.Store(
                                        id="core-container-tab-item-keys-cache",
                                        storage_type="session",
                                    ),
                                    fac.AntdTabs(
                                        id="core-container",
                                        items=[],
                                        type="editable-card",
                                        size="small",
                                        style=style(padding="6px 12px"),
                                    ),
                                ]
                            )
                        ),
                        flex="auto",
                    ),
                ],
                wrap=False,
            ),
        ]
    )
