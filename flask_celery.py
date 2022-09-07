from celery import Celery

def make_celery(app):
    celery=Celery(app.import_name, backend=app.config['CELERY_BACKEND'],broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase=celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def call(self, args, * kwargs):
            with app.app_context():
                return TaskBase.call(self, args, * kwargs)
    celery.Task=ContextTask
    return celery