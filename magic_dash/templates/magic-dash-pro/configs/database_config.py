from typing import Literal


class DatabaseConfig:
    """数据库配置参数"""

    # 应用基础数据库类型
    # 当使用postgresql类型时，请使用`pip install psycopg2-binary`安装必要依赖
    database_type: Literal["sqlite", "postgresql"] = "sqlite"

    # 当database_type为'postgresql'时，对应的数据库连接配置参数，使用时请根据实际情况修改
    postgresql_config = {
        "host": "127.0.0.1",
        "port": 5432,
        "user": "postgres",
        "password": "admin123",
        "database": "magic_dash_pro",
    }
