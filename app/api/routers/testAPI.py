from fastapi import APIRouter
from fastapi.params import Body
from celery import Celery
import os

CELERY_BROKER_ADDRESS = str(os.environ['CELERY_BROKER_ADDRESS'])
CELERY_BACKEND_ADDRESS = str(os.environ['CELERY_BACKEND_ADDRESS'])

router = APIRouter(
    prefix="/test",
    tags=['Test'],
)

celery = Celery(
    'app-test',
    broker=CELERY_BROKER_ADDRESS,
    backend=CELERY_BACKEND_ADDRESS,
)

celery.conf.task_routes = {'test.*': {'queue': 'test'}}


@router.post("/run_task")
async def run_task(params: dict = Body(...)):
    try:
        res1 = celery.send_task(
            'test.run', kwargs=params.get('task1'))
        res2 = celery.send_task(
            'test.run', kwargs=params.get('task2'))
        return {"info": "Task started", "task_id": [str(res1), str(res2)]}
    except Exception as e:
        return {"info": e}
