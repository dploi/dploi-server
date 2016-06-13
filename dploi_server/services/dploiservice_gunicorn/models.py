from dploi_server.directory import service_dir
from dploi_server.models import BaseService, BaseServiceInstance
from django.db import models

class Gunicorn(BaseService):
    pass

class GunicornInstance(BaseServiceInstance):
    service = models.ForeignKey(Gunicorn, related_name='instances')
    workers = models.PositiveSmallIntegerField(default=3)
    max_requests = models.PositiveSmallIntegerField(default=2000)

service_dir.register(Gunicorn, GunicornInstance)
