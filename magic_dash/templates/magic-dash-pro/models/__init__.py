from peewee import SqliteDatabase, Model
from playhouse.pool import PooledPostgresqlExtDatabase
from feffery_dash_utils.version_utils import check_dependencies_version

from configs.database_config import DatabaseConfig


def get_db():
    """根据配置参数，创建数据库连接对象"""

    if DatabaseConfig.database_type == "postgresql":
        # 必要依赖检查
        check_dependencies_version(
            rules=[
                {
                    "name": "psycopg2-binary",
                }
            ]
        )

        # 返回postgresql类型连接池对象
        return PooledPostgresqlExtDatabase(
            host=DatabaseConfig.postgresql_config["host"],
            port=DatabaseConfig.postgresql_config["port"],
            user=DatabaseConfig.postgresql_config["user"],
            password=DatabaseConfig.postgresql_config["password"],
            database=DatabaseConfig.postgresql_config["database"],
            max_connections=32,
            stale_timeout=300,
        )

    # 默认返回sqlite类型连接对象
    return SqliteDatabase("magic_dash_pro.db")


# 创建数据库连接对象
db = get_db()


class BaseModel(Model):
    """数据库表模型基类"""

    class Meta:
        # 关联数据库
        database = db
