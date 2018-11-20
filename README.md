# 审核平台站内信后端组件

## 依赖
1. Django>=1.9.10
2. djangorestframework>=3.5.3

## 安装
使用 pip 安装

```
pip install git+http://gitlab.intra.knownsec.com/weixin/notify.git
```

添加requirements.txt
```
git+http://gitlab.intra.knownsec.com/weixin/notify.git
```

## 配置

```
# django install app

INSTALLED_APPS += ['notify']


# 站内信
# 用户模型
STAFF_MODEL = 'toutiao.models.StaffProfile'
# 常用筛选模型
COMMON_FILTER_MODEL = 'toutiao.apps.common_filter.models.CommonFilter'
# 站内信模块
NOTIFY_BUSINESS_TYPE_CHOICES = (
    ('default', u'默认'),
)
# 站内信分类
NOTIFY_TYPE_CHOICES = (
    ('system', u'系统消息'),
)
# (可选字段) 站内信管理权限字段, 不设置则后端不判断用户权限
NOTIFY_AUTH = 'check_notify_list'

# urls.py 添加 url
urlpatterns += [
    url(r'^notify/', include('notify.urls')),
]
```
