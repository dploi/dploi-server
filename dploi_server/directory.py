# This is heavily inspired by the django admin sites.py

class AlreadyRegistered(Exception):
    pass

class NotRegistered(Exception):
    pass

class ServiceDirectory(object):
    def __init__(self):
        self._service_registry = []
        self._service_instance_registry = []

    def register(self, service, service_instance):
        if service in self._service_registry:
            raise AlreadyRegistered('The model %s is already registered' % service.__name__)
        self._service_registry.append(service)
        if service_instance in self._service_instance_registry:
            raise AlreadyRegistered('The model %s is already registered' % service_instance.__name__)
        self._service_instance_registry.append(service_instance)
#
#    def unregister(self, model_or_iterable):
#        for model in model_or_iterable:
#            if model not in self._registry:
#                raise NotRegistered('The model %s is not registered' % model.__name__)
#            del self._registry[model]

service_dir = ServiceDirectory()
service_admin_dir = ServiceDirectory()