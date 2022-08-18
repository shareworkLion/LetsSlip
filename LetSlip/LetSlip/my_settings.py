from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
mySECRET_KEY = 'django-insecure-l22buoa!=vhp01h)%@57$9he^mn&v#q*0yu3r*55of0!uzcfy$'

myDATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'letsslipdb',
        'USER': 'letsslip',
        'PASSWORD': 'LetsSlip1234!',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}