"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xga7qabm&0h-b0+^_ju70(5a*m_sf_v$f#w_t5j=j)b50$f1ra'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com','localhost','[::1]']
"""
왜 이런 걸 하는건지: 이 설정은 Django 웹 애플리케이션의 보안을 위한 것입니다. Django는 ALLOWED_HOSTS 설정을 통해 웹 요청이 유효한 호스트에서 오는 것인지 확인합니다.
DEBUG가 True이고 ALLOWED_HOSTS가 비어 있으면, Django는 자동으로 localhost, 127.0.0.1, 그리고 [::1] (IPv6 주소)를 유효한 호스트로 간주합니다. 이는 개발 환경에서 유용합니다.
그러나 애플리케이션을 실제 서버에 배포할 때는 DEBUG를 False로 설정하고, ALLOWED_HOSTS에 실제 서버의 도메인 이름을 추가해야 합니다. 이렇게 하지 않으면 Django는 서버에서 오는 웹 요청을 거부합니다.
예를 들어, PythonAnywhere에서 애플리케이션을 호스팅하는 경우, ALLOWED_HOSTS 설정은 다음과 같이 변경해야 합니다:

ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']
이렇게 하면 127.0.0.1 (로컬호스트)와 pythonanywhere.com 도메인에서 오는 요청을 Django가 수락합니다. .pythonanywhere.com 앞의 점(.)은 PythonAnywhere의 모든 서브도메인도 수락한다는 것을 의미합니다.
즉, 이 설정은 Django 애플리케이션의 보안을 강화하고, 웹 요청이 유효한 소스에서만 오는지 확인하는 역할을 합니다. 이는 웹 사이트를 보호하고, 악의적인 사용자가 웹 사이트를 공격하는 것을 방지하는 중요한 단계입니다.
"""

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog', # blog 앱을 추가해줍니다.
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ko'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static' #정적 파일 경로 추가

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
