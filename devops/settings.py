"""
Django settings for devops project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from devops.password import dbpassword

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ik1o7f_6q7&bk#w7_#e=v57dws89wnnc=c12q5td@7fvqq+=y4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', ]


# Application definition

INSTALLED_APPS = [
    'import_export',
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'data.apps.DataConfig',
    'app.apps.AppConfig',
    'trade.apps.TradeConfig',
    'quant.apps.QuantConfig',
    # 'hisconsole.apps.HisconsoleConfig',
    # 'channels',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'devops.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'devops.wsgi.application'
# ASGI_APPLICATION = "devops.asgi.application"

# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels_redis.core.RedisChannelLayer',
#         'CONFIG': {
#             "hosts": [('127.0.0.1', 6379)],
#         },
#     },
# }

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
     'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'django',    #你的数据库名称
            'USER': 'django',   #你的数据库用户名
            'PASSWORD': dbpassword, #你的数据库密码
            'HOST': '8.129.115.98', #你的数据库主机，留空默认为localhost
            # 'HOST': '192.168.31.85',  # 你的数据库主机，留空默认为localhost
            'PORT': 3306, # 端口
     }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
# 设置上传目录
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]


# 指定simpleui默认的主题,指定一个文件名，相对路径就从simpleui的theme目录读取
# SIMPLEUI_DEFAULT_THEME = 'admin.lte.css'

# 设置simpleui 点击首页图标跳转的地址
# SIMPLEUI_INDEX = 'https://www.88cto.com'

# 首页显示服务器、python、django、simpleui相关信息
SIMPLEUI_HOME_INFO = True

# 首页显示快速操作
SIMPLEUI_HOME_QUICK = True

# 首页显示最近动作
SIMPLEUI_HOME_ACTION = True

# 自定义SIMPLEUI的Logo
# SIMPLEUI_LOGO = 'https://avatars2.githubusercontent.com/u/13655483?s=60&v=4'

# 登录页粒子动画，默认开启，False关闭
SIMPLEUI_LOGIN_PARTICLES = False

# 让simpleui 不要收集相关信息
SIMPLEUI_ANALYSIS = True

# 自定义simpleui 菜单
SIMPLEUI_CONFIG = {
    # 在自定义菜单的基础上保留系统模块
    # 'system_keep': True,
    # 'menu_display': [ 'Devops','数据爬取', '量化投资', '跨境电商'],      # 开启排序和过滤功能, 不填此字段为默认排序和全部显示, 空列表[] 为全部不显示.
    'menus_temp': [
        {
            'name': '跨境电商',
            'icon': 'fa fa-bicycle',
            'models': [
                {
                    'name': 'amz520',
                    'url': 'https://www.amz520.com/',
                    'icon': 'far fa-surprise'
                },
                {
                'name': '站长站',
                'url': 'https://data.chinaz.com/',
                'icon': 'fab fa-github'
            }
            ]
        },
        {
        'app': 'investment',
        'name': '量化投资',
        'icon': 'fas fa-camera',
        'models': [{
            'name': '股票市场',
            'icon': 'fa fa-user',
            'url': 'http://8.129.115.98:9002/'
        }]
    }]
}

# 是否显示默认图标，默认=True
SIMPLEUI_DEFAULT_ICON = True

# 图标设置，图标参考：
SIMPLEUI_ICON = {
    'Devops': 'fab fa-apple',
    '跨境电商': 'fa fa-bicycle',
    '量化投资': 'fa fa-camera',
    'Sitemap': 'fab fa-github'
}

# 指定simpleui 是否以脱机模式加载静态资源，为True的时候将默认从本地读取所有资源，即使没有联网一样可以。适合内网项目
# 不填该项或者为False的时候，默认从第三方的cdn获取

SIMPLEUI_STATIC_OFFLINE = True

# 设置上传目录
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# 设置前缀
MEDIA_URL = '/media/'