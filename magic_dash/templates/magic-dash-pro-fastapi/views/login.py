from dash import html, dcc
import feffery_antd_components as fac
import feffery_utils_components as fuc
from feffery_dash_utils.style_utils import style

from configs import BaseConfig, LoginConfig
from utils.crypto_utils import rsa_public_key

# 令绑定的回调函数子模块生效
import callbacks.login_c  # noqa: F401


def get_login_form_content():
    """构建登录表单内容"""
    return fac.AntdSpace(
        [
            html.Img(src=BaseConfig.app_logo, height=72),
            fac.AntdText(
                BaseConfig.app_title,
                className="login-title",
                style=style(fontSize=28, fontWeight="bold"),
            ),
            fac.AntdForm(
                [
                    # 存储RSA公钥（从文件读取初始值）
                    dcc.Store(id="login-rsa-pubkey", data=rsa_public_key),
                    # 存储当前项目是否启用登录密码RSA加密
                    dcc.Store(
                        id="login-rsa-crypto-enabled",
                        data=BaseConfig.enable_login_rsa_crypto,
                    ),
                    # 存储加密后的密码
                    dcc.Store(id="login-password-crypto"),
                    fac.AntdFormItem(
                        fac.AntdInput(
                            id="login-user-name",
                            placeholder="请输入用户名",
                            size="large",
                            prefix=fac.AntdIcon(
                                icon="antd-user",
                                className="global-help-text",
                            ),
                            autoComplete="off",
                        ),
                        id="login-user-name-form-item",
                        label="用户名",
                    ),
                    fac.AntdFormItem(
                        fac.AntdInput(
                            id="login-password",
                            placeholder="请输入密码",
                            size="large",
                            mode="password",
                            prefix=fac.AntdIcon(
                                icon="antd-lock",
                                className="global-help-text",
                            ),
                        ),
                        id="login-password-form-item",
                        label="密码",
                    ),
                    (
                        fac.AntdFormItem(
                            fuc.FefferySliderCaptcha(
                                id="login-slider-captcha",
                                block=True,
                                mode="slider",
                                tipText={
                                    "default": "请按住滑块，拖动到最右边",
                                    "moving": "请按住滑块，拖动到最右边",
                                    "error": "验证失败，请重新操作",
                                    "success": "验证成功",
                                },
                                style=style(width="100%"),
                            )
                        )
                        if BaseConfig.enable_login_captcha
                        else None
                    ),
                    fac.AntdCheckbox(id="login-remember-me", label="记住我"),
                    fac.AntdButton(
                        "登录",
                        id="login-button",
                        loadingChildren="校验中",
                        type="primary",
                        block=True,
                        size="large",
                        style=style(marginTop=18),
                    ),
                ],
                layout="vertical",
                style=style(width=360, maxWidth="calc(90vw - 40px)"),
            ),
        ],
        direction="vertical",
        align="center",
    )


def get_background_decorations():
    """构建背景装饰图片"""
    decorations = [
        {
            "src": "/assets/imgs/login/插图1.svg",
            "width": "25vw",
            "style": {
                "position": "absolute",
                "left": "10%",
                "top": "15%",
                "rotateZ": "-5deg",
            },
            "animate": {"y": [25, -25, 25]},
            "duration": 4.5,
        },
        {
            "src": "/assets/imgs/login/插图2.svg",
            "width": "15vw",
            "style": {
                "position": "absolute",
                "right": "20%",
                "top": "25%",
                "rotateZ": "15deg",
            },
            "animate": {"y": [-15, 15, -15]},
            "duration": 5.5,
        },
        {
            "src": "/assets/imgs/login/插图3.svg",
            "width": "12vw",
            "style": {
                "position": "absolute",
                "left": "25%",
                "bottom": "25%",
                "rotateZ": "-8deg",
            },
            "animate": {"y": [10, -10, 10]},
            "duration": 5,
        },
        {
            "src": "/assets/imgs/login/插图4.svg",
            "width": "25vw",
            "style": {
                "position": "absolute",
                "right": "15%",
                "bottom": "8%",
                "rotateZ": "5deg",
            },
            "animate": {"y": [20, -20, 20]},
            "duration": 6,
        },
    ]
    return [
        fuc.FefferyMotion(
            html.Img(src=d["src"], style=style(width=d["width"])),
            style=d["style"],
            animate=d["animate"],
            transition={
                "duration": d["duration"],
                "repeat": "infinity",
                "type": "spring",
            },
        )
        for d in decorations
    ]


def get_background_video():
    """构建背景视频内容"""
    return html.Video(
        src=LoginConfig.login_bg_video,
        autoPlay=True,
        muted=True,
        loop=True,
        style=style(
            width="100%",
            height="100%",
            position="absolute",
            objectFit="cover",
            borderTopRightRadius=12,
            borderBottomRightRadius=12,
            pointerEvents="none",
        ),
    )


def basic_login_layout():
    """左右分割布局"""
    return fac.AntdRow(
        [
            fac.AntdCol(
                (
                    get_background_decorations()
                    if LoginConfig.login_content_type == "image"
                    else [get_background_video()]
                ),
                flex="auto",
                className="login-left-side",
                style=(
                    style()
                    if LoginConfig.login_content_type == "image"
                    else style(backgroundImage="none")
                ),
            ),
            fac.AntdCol(
                fac.AntdCenter(
                    [get_login_form_content()],
                    style=style(height="calc(100% - 200px)"),
                ),
                flex="none",
                style=style(
                    width=f"calc({LoginConfig.login_card_width}px + 200px)",
                    maxWidth="100vw",
                ),
                className="login-right-side",
            ),
        ],
        wrap=False,
        style=style(height="100vh"),
    )


def center_login_layout():
    """居中卡片布局"""
    return html.Div(
        [
            *(
                get_background_decorations()
                if LoginConfig.login_content_type == "image"
                else [get_background_video()]
            ),
            fac.AntdCenter(
                fac.AntdCard(
                    get_login_form_content(),
                    style=style(
                        width=f"{LoginConfig.login_card_width}px",
                        maxWidth="90vw",
                        borderRadius=12,
                        boxShadow="0 8px 24px rgba(0, 0, 0, 0.1)",
                        border="1px solid rgba(255, 255, 255, 0.1)",
                        backgroundColor="rgba(255, 255, 255, 0.75)",
                        backdropFilter="blur(3px)",
                    ),
                    styles={
                        "header": {"display": "none"},
                        "body": style(padding="40px 20px"),
                    },
                ),
                style=style(height="100%"),
            ),
        ],
        className="login-container",
        style=style(
            height="100vh",
            position="relative",
            overflow="hidden",
            backgroundImage=(
                f'url("{LoginConfig.login_bg_image}")'
                if LoginConfig.login_content_type == "image"
                else "none"
            ),
            backgroundSize="cover",
            backgroundPosition="center",
        ),
    )


def render():
    """登录页面渲染函数"""
    return html.Div(
        id="login-layout-container",
        children=(
            center_login_layout()
            if LoginConfig.login_page_style == "center"
            else basic_login_layout()
        ),
    )
