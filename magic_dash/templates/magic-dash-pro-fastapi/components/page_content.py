import feffery_antd_components as fac

from views.core_pages import (
    index,
    page1,
    sub_menu_page1,
    sub_menu_page2,
    sub_menu_page3,
    independent_page,
    independent_wildcard_page,
    url_params_page,
    # 系统管理相关页面
    login_logs,
)


def render(pathname: str, current_url: str = None):
    """渲染pathname对应的页面内容"""

    # 路径名到页面渲染函数的映射关系
    pathname_to_page = {
        "/": index.render,
        # 主要页面
        "/core/page1": page1.render,
        # 子菜单演示
        "/core/sub-menu-page1": sub_menu_page1.render,
        "/core/sub-menu-page2": sub_menu_page2.render,
        "/core/sub-menu-page3": sub_menu_page3.render,
        # 独立页面
        "/core/independent-page": independent_page.render,
        "/core/independent-wildcard-page": independent_wildcard_page.render,
        # url参数提取页面
        "/core/url-params-page": lambda: url_params_page.render(
            current_url=current_url
        ),
        # 系统管理 - 日志管理
        "/core/login-logs": login_logs.render,
    }

    render_func = pathname_to_page.get(pathname)

    if render_func:
        return render_func()

    # 未匹配到路由时返回占位提示
    return fac.AntdAlert(
        type="warning",
        showIcon=True,
        message=f"这里是{pathname}",
        description="该页面尚未进行开发哦🤔~",
    )
