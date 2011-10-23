#-*- coding: utf-8 -*-
"""
main start script for the "dploi-server" command
"""
from django.core import management

def main(settings_file='dploi_server.settings'):
    try:
        mod = __import__(settings_file)
        components = settings_file.split('.')
        for comp in components[1:]:
            mod = getattr(mod, comp)

    except ImportError, e:
        import sys
        sys.stderr.write("Error loading the settings module '%s': %s"
                            % (settings_file, e))
        return sys.exit(1)

    management.setup_environ(mod, settings_file)
    utility = management.ManagementUtility()
    utility.execute()
