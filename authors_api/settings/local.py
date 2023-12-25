from .base import * # noqa
from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="TaSphqOrhSmrwV-JBMMgDSKV3nhm3Jzn_cYZMc4jbLvP8zKsbKg",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# 사이트 간 요청을 허용하는 도메인 목록읻   
CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]