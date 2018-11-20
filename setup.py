from setuptools import setup

PACKAGE = "health"
NAME = "health app"
DESCRIPTION = "health app"
AUTHOR = "zw"
AUTHOR_EMAIL = ""
URL = ""
VERSION = '0.1.3'
PACKAGES = ['health', ]
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="BSD",
    url=URL,
    packages=PACKAGES,
    install_requires=[
        'django',
        'djangorestframework',
    ],
    zip_safe=False,
)
