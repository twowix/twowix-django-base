#### ENV CONFIG (DATABASE, SECRET_KEY, ...)
- config/common/env.json (실제 사용 시 에는 .gitignore 필수!!)

#### REQUIREMENT CONFIG
- config/common/scripts/requirements.txt

#### SETTINGS
- config/settings

#### USING PACKAGE
##### Base
- Django [FRAMEWORK]
- djangorestframework [API]
- djangorestframework-jwt [AUTH_TOKEN]
- boto3 [AWS-S3]
- django-storages [AWS-S3]
- requests [REQUEST]
- django-crontab [CRONTAB]
- pyfcm [FCM]
- psycopg2 [POSTGRESQL DRIVE]
- psycopg2-binary [POSTGRESQL DRIVE]
- termcolor [PRINT LOG COLOR]

##### Development
- django-debug-toolbar [DEBUG]


##### 사용 환경변수
- SERVER_ENV (local, develop, product)