from app.modules.test import TestClass
from celery import Celery

import os

CELERY_BROKER_ADDRESS = str(os.environ['CELERY_BROKER_ADDRESS'])
CELERY_BACKEND_ADDRESS = str(os.environ['CELERY_BACKEND_ADDRESS'])


celery_cc = Celery(
    'app-test',
    broker=CELERY_BROKER_ADDRESS,
    backend=CELERY_BACKEND_ADDRESS,
)


@celery_cc.task(name='test.run')
def run(**params):
    try:
        result = TestClass().test(params.get('time'))
        return result
    except Exception as e:
        return {'error': e}
