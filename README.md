# health app

## 依赖
1. Django>=1.9.10

## 安装
使用 pip 安装

```
pip install git+https://github.com/zhwei820/health.git
```

添加requirements.txt
```
git+https://github.com/zhwei820/health.git
```

## 配置

```
# django install app

INSTALLED_APPS += ['health']


# urls.py 添加 url
urlpatterns += [
    url(r'^health/', include('health.urls')),
]
```
