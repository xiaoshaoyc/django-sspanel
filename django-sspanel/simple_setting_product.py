import base64
# DEBUG设置
DEBUG = False

# 域名设置
ALLOWED_HOSTS = [
    'freedom.xiaoshao.me'
]

# mysql 设置
DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_SS',
        'USER': 'django_SS',
        'PASSWORD': 'syc712232',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True,
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        },
    }
}

# 是否开启邮件功能
USE_SMTP = False
# 邮件服务设置：
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# 是否开启ssl/tls
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False

# 我使用163邮箱作为smtp服务器
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'USER'
EMAIL_HOST_PASSWORD = 'PASS'
DEFAULT_FROM_EMAIL = 'Ehco<ADDRESS>'

# SS面板设置：
MB = 1024 * 1024
GB = 1024 * 1024 * 1024
DEFAULT_TRAFFIC = 5 * GB
START_PORT = 2000

# 默认加密混淆协议
DEFAULT_METHOD = 'aes-128-ctr'
DEFAULT_PROTOCOL = 'auth_chain_a'
DEFAULT_OBFS = 'http_simple'

# 签到流量设置
MIN_CHECKIN_TRAFFIC = 10 * MB
MAX_CHECKIN_TRAFFIC = 200 * MB

# 是否启用支付宝系统
USE_ALIPAY = False
# 支付订单提示信息 修改请保留 {} 用于动态生成金额
ALIPAY_TRADE_INFO = '光环科技的{}元充值码'

# 是否开启91pay 第三方接口
# 91PAY 、ALIPAY只能开启一项
# 需要授权请联系：
# https://t.me/gh012363  或者QQ群538609570
USE_91PAY = False
# 自己的支付宝账号
ALIPAY_NUM = 'xx'

# 网站title
TITLE = 'Aperture Science'
SUBTITLE = '光环科技'

# 用户邀请返利比例
INVITE_PERCENT = 0.2
# 用户能生成的邀请码数量
INVITE_NUM = 5

# 网站邀请界面提示语
INVITEINFO = '邀请码实时更新，如果用完了就等一会'

# 网站域名设置（请正确填写，不然订阅功能会失效：
HOST = 'locahost'


# 管理员账号
USERNAME = 'xiaoshaoyc'
# 管理员ss端口
PORT = 1025
# 管理员私有token，用于后端接口调用
TOKEN = base64.b64encode(
    bytes('{}+{}'.format(USERNAME, PORT), 'utf8')).decode()
