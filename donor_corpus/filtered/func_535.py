def create_celery():
    from celery import Celery
    celery = Celery(__name__, backend=Config.CELERY_RESULT_BACKEND, broker=Config.CELERY_BROKER_URL)
    return celery