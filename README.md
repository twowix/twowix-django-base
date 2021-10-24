#### ENV CONFIG (DATABASE, SECRET_KEY, ...)
- config/common/env.json
- env format

```
{
  "development": {
    "SECRET_KEY": "12345123451234512345123451234512354123512351235123",
    "DATABASES": {
      "default": {
        "ENGINE": "",
        "NAME": "",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": ""
      }
    }
    ...
  },

  "product": {
    "SECRET_KEY": "12345123451234512345123451234512354123512351235123",
    "DATABASES": {
      "default": {
        "ENGINE": "",
        "NAME": "",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": ""
      }
    }
    ...
  }
}
```

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

---
### TODO
1. AWS - S3 Connection
2. FCM - PUSH Library
3. ...