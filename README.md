# TODOLIST APP

> 2022/10/12

### 使用開發工具

- vscode 1.72.0
- python 3.8.8
- django 4.1.2

### 指令

- cmd: django-admin startproject todolist .
- cmd: python manage.py runserver

- 新增 app
- cmd: pyhton manage.py startapp user
- setting.py [INSTALLED_APPS]
    - 'user.apps.UserConfig'
    - 語言和時間變更
        - LANGUAGE_CODE = 'zh-Hant'
        - TIME_ZONE = 'Asia/Taipei'

- 進行資料庫同步
    - cmd: python manage.py migrate

- 後台新增超級管理者
    - python manage.py createsuperuser
    - 127.0.0.1:8000/admin

- .gitignore
    - https://github.com/jpadilla/django-project-template/blob/master/.gitignore