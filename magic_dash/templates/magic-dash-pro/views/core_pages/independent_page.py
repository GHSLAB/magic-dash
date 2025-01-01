from dash import html
import feffery_antd_components as fac
from feffery_dash_utils.style_utils import style


def render():
    """子页面：独立页面渲染入口页简单示例"""

    return fac.AntdSpace(
        [
            fac.AntdBreadcrumb(
                items=[{"title": "主要页面"}, {"title": "独立页面渲染入口页"}]
            ),
            fac.AntdAlert(
                type="info",
                showIcon=True,
                message="这里是独立页面渲染入口页演示示例",
                description=fac.AntdText(
                    [
                        "点击",
                        html.A(
                            "此处", href="/core/independent-page/demo", target="_blank"
                        ),
                        "打开示例独立显示页面。",
                    ]
                ),
            ),
        ],
        direction="vertical",
        style=style(width="100%"),
    )
