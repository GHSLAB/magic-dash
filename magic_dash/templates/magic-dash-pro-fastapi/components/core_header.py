import re
from dash import html, dcc
import feffery_antd_components as fac
from feffery_dash_utils.style_utils import style

from server import current_user
from configs import BaseConfig, RouterConfig, LayoutConfig, AuthConfig


def get_page_search_options(current_user_access_rule: str):
    """生成页面搜索下拉选项"""

    options = [{"label": "首页", "value": RouterConfig.index_pathname}]

    for pathname, title in RouterConfig.menu_pathnames.items():
        # 忽略已添加的首页
        if pathname in [RouterConfig.index_pathname, "/"]:
            pass

        # 忽略正则表达式通配页面
        elif isinstance(pathname, re.Pattern):
            pass

        elif (
            # 公开页面全部放行
            pathname in RouterConfig.public_pathnames
            or current_user_access_rule["type"] == "all"
        ):
            options.append(
                {
                    "label": title,
                    "value": f"{pathname}|{title}",
                }
            )

        elif current_user_access_rule["type"] == "include":
            if pathname in current_user_access_rule.get("keys", []):
                options.append(
                    {
                        "label": title,
                        "value": f"{pathname}|{title}",
                    }
                )

        elif current_user_access_rule["type"] == "exclude":
            if pathname not in current_user_access_rule.get("keys", []):
                options.append(
                    {
                        "label": title,
                        "value": f"{pathname}|{title}",
                    }
                )

    return options


def _render_logo_title():
    """渲染logo+标题+版本（无侧边折叠按钮）"""

    return fac.AntdFlex(
        [
            dcc.Link(
                fac.AntdSpace(
                    [
                        # logo
                        html.Img(
                            src=BaseConfig.app_logo,
                            height=32,
                            style=style(display="block"),
                        ),
                        fac.AntdSpace(
                            [
                                # 标题
                                fac.AntdText(
                                    BaseConfig.app_title,
                                    strong=True,
                                    style=style(fontSize=20),
                                ),
                                fac.AntdText(
                                    BaseConfig.app_version,
                                    className="global-help-text",
                                    style=style(fontSize=12),
                                ),
                            ],
                            align="baseline",
                            size=3,
                            id="core-header-title",
                        ),
                    ]
                ),
                href="/",
            ),
        ],
        id="core-header-side",
        justify="space-between",
        align="center",
    )


def _render_page_search(current_user_access_rule: str):
    """渲染页面搜索框"""

    return fac.AntdSpace(
        [
            fac.AntdSelect(
                id="core-page-search",
                placeholder="输入关键词搜索页面",
                options=get_page_search_options(current_user_access_rule),
                variant="filled",
                style=style(width=250),
            ),
            fac.AntdText(
                [
                    fac.AntdText(
                        "Ctrl",
                        keyboard=True,
                        className="global-help-text",
                    ),
                    fac.AntdText(
                        "K",
                        keyboard=True,
                        className="global-help-text",
                    ),
                ]
            ),
        ],
        size=5,
        style=style(
            **(
                {}
                if LayoutConfig.show_core_page_search
                else {"visibility": "hidden"}
            )
        ),
    )


def _render_function_icons_and_user_info():
    """渲染功能图标与用户信息"""

    return fac.AntdSpace(
        [
            # 页面全屏化切换
            fac.AntdTooltip(
                fac.AntdButton(
                    id="core-full-screen-toggle-button",
                    icon=fac.AntdIcon(
                        id="core-full-screen-toggle-button-icon",
                        icon="antd-full-screen",
                        className="global-help-text",
                    ),
                    type="text",
                ),
                title="全屏切换",
            ),
            # 页面重载
            fac.AntdTooltip(
                fac.AntdButton(
                    id="core-reload-button",
                    icon=fac.AntdIcon(
                        icon="antd-reload",
                        className="global-help-text",
                    ),
                    type="text",
                    # 省略回调函数的编写
                    clickExecuteJsString='dash_clientside.set_props("global-reload", { reload: true })',
                ),
                title="页面重载",
            ),
            # 示例功能图标
            fac.AntdTooltip(
                fac.AntdButton(
                    icon=fac.AntdIcon(
                        icon="antd-setting",
                        className="global-help-text",
                    ),
                    type="text",
                ),
                title="示例功能图标",
            ),
            # 示例功能图标
            fac.AntdTooltip(
                fac.AntdButton(
                    icon=fac.AntdIcon(
                        icon="antd-bell",
                        className="global-help-text",
                    ),
                    type="text",
                ),
                title="示例功能图标",
            ),
            # 示例功能图标
            fac.AntdTooltip(
                fac.AntdButton(
                    icon=fac.AntdIcon(
                        icon="antd-question-circle",
                        className="global-help-text",
                    ),
                    type="text",
                ),
                title="示例功能图标",
            ),
            # 自定义分隔符
            html.Div(
                style=style(
                    width=0,
                    height=42,
                    borderLeft="1px solid #e1e5ee",
                    margin="0 12px",
                )
            ),
            # 用户头像
            fac.AntdAvatar(
                mode="text",
                text=current_user.user_name[0].upper(),
                size=36,
                style=style(background="#cdcdcd"),
            ),
            # 用户名+角色
            fac.AntdFlex(
                [
                    fac.AntdText(
                        current_user.user_name.capitalize(),
                        strong=True,
                    ),
                    fac.AntdText(
                        "角色：{}".format(
                            AuthConfig.roles.get(current_user.user_role)["description"]
                        ),
                        className="global-help-text",
                        style=style(fontSize=12),
                    ),
                ],
                vertical=True,
            ),
            # 用户管理菜单
            fac.AntdDropdown(
                fac.AntdButton(
                    icon=fac.AntdIcon(
                        icon="antd-more",
                        className="global-help-text",
                    ),
                    type="text",
                ),
                id="core-pages-header-user-dropdown",
                menuItems=[
                    {
                        "title": "个人信息",
                        "key": "个人信息",
                    },
                    # 若当前用户角色为系统管理员
                    *(
                        [
                            {
                                "title": "用户管理",
                                "key": "用户管理",
                            },
                            {
                                "title": "部门管理",
                                "key": "部门管理",
                            },
                        ]
                        if (current_user.user_role == AuthConfig.admin_role)
                        else []
                    ),
                    {"isDivider": True},
                    {
                        "title": "退出登录",
                        "href": "/logout",
                    },
                ],
                trigger="click",
            ),
        ]
    )


def render_default(current_user_access_rule: str):
    """渲染默认页首（左右两列：左为logo+标题+折叠按钮，宽度对齐侧边栏；右为搜索+功能图标+用户信息）"""

    return fac.AntdRow(
        [
            # logo+标题+版本+侧边折叠按钮
            fac.AntdCol(
                fac.AntdFlex(
                    [
                        dcc.Link(
                            fac.AntdSpace(
                                [
                                    # logo
                                    html.Img(
                                        src=BaseConfig.app_logo,
                                        height=32,
                                        style=style(display="block"),
                                    ),
                                    fac.AntdSpace(
                                        [
                                            # 标题
                                            fac.AntdText(
                                                BaseConfig.app_title,
                                                strong=True,
                                                style=style(fontSize=20),
                                            ),
                                            fac.AntdText(
                                                BaseConfig.app_version,
                                                className="global-help-text",
                                                style=style(fontSize=12),
                                            ),
                                        ],
                                        align="baseline",
                                        size=3,
                                        id="core-header-title",
                                    ),
                                ]
                            ),
                            href="/",
                        ),
                        # 侧边折叠按钮
                        fac.AntdButton(
                            fac.AntdIcon(
                                id="core-side-menu-collapse-button-icon",
                                icon="antd-menu-fold",
                                className="global-help-text",
                            ),
                            id="core-side-menu-collapse-button",
                            type="text",
                            size="small",
                        ),
                    ],
                    id="core-header-side",
                    justify="space-between",
                    align="center",
                    style=style(
                        width=LayoutConfig.core_side_width,
                        height="100%",
                        paddingLeft=20,
                        paddingRight=20,
                        borderRight="1px solid #dae0ea",
                        boxSizing="border-box",
                    ),
                ),
                flex="none",
            ),
            # 页面搜索+功能图标+用户信息
            fac.AntdCol(
                fac.AntdFlex(
                    [
                        _render_page_search(current_user_access_rule),
                        _render_function_icons_and_user_info(),
                    ],
                    justify="space-between",
                    align="center",
                    style=style(
                        height="100%",
                        paddingLeft=20,
                        paddingRight=20,
                    ),
                ),
                flex="auto",
            ),
        ],
        wrap=False,
        align="middle",
        style=style(
            height=72,
            borderBottom="1px solid #dae0ea",
            position="sticky",
            top=0,
            zIndex=1000,
            background="#fff",
        ),
    )


def render_full(current_user_access_rule: str):
    """渲染页首（贯穿全宽，logo+标题靠左，页面搜索靠右并与功能图标、用户信息合并）"""

    return fac.AntdFlex(
        [
            # 左侧：logo+标题+版本（不受侧边栏折叠影响）
            _render_logo_title(),
            # 右侧：页面搜索+功能图标+用户信息
            fac.AntdFlex(
                [
                    _render_page_search(current_user_access_rule),
                    _render_function_icons_and_user_info(),
                ],
                align="center",
                gap=15,
            ),
        ],
        justify="space-between",
        align="center",
        style=style(
            height=72,
            paddingLeft=20,
            paddingRight=20,
            borderBottom="1px solid #dae0ea",
            boxSizing="border-box",
            position="sticky",
            top=0,
            zIndex=1000,
            background="#fff",
        ),
    )


def render(current_user_access_rule: str):
    """渲染核心页面页首

    Args:
        current_user_access_rule (str): 当前用户页面可访问性规则
    """

    if LayoutConfig.core_header_style == "full":
        return render_full(current_user_access_rule)

    return render_default(current_user_access_rule)