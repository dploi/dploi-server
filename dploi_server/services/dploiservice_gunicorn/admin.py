from django.contrib.admin.options import TabularInline
from dploi_server.directory import service_admin_dir
from dploi_server.services.dploiservice_gunicorn.models import Gunicorn, GunicornInstance

class GunicornInline(TabularInline):
    model = Gunicorn

class GunicornInstanceInline(TabularInline):
    model = GunicornInstance

service_admin_dir.register(GunicornInline, GunicornInstanceInline)