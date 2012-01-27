#!/usr/bin/env python
# encoding: utf-8

import sys
from django.contrib.auth.models import User
from dploi_server.directory import service_dir
import re
from yaml import load, dump
from django.core.management.base import BaseCommand, CommandError
from dploi_server.models import Host

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        n = sys.argv[2]
        host = Host.objects.get(name=n)

        ## Too lazy to do it properly
        #text = re.sub('.*!ruby\/.*','', open("/var/lib/puppet/yaml/facts/" + n + '.yaml').read())
        #facts = load(text)['values']

        classes = ['dploi::enc-customer', 'dploi::admin::enc-developer'] + host.puppet_classes_list()  # obtain from DB

        # Convert list to dict with empty values
        cdict = {}
        cdict = dict((x, "") for x in classes)

        projectlist = {}
        for cls in service_dir._service_instance_registry:
            for service_instance in cls.objects.filter(service__host=host):
                projectlist[service_instance.deployment.get_default_identifier()] = {
                    'uid': service_instance.deployment.pk,
                    'state': service_instance.deployment.name,
                }
        developerslist = {}
        ssh_keys = {}
        team = []
        for user in User.objects.filter(groups__dploi_admins=host):
            ssh_key_list = user.dploi_ssh_keys.all()
            developerslist[user.get_full_name() or user.username] = {
                'username':  user.username,
                'uid':  user.pk,
                'gid': 500, # STATIC!
                'enabled': str(user.is_active).lower(),
                'keys': [sshkey.name for sshkey in ssh_key_list],
            }
            for ssh_key in ssh_key_list:
                ssh_keys[ssh_key.name] = {
                    'type': ssh_key.type,
                    'key': ssh_key.key,
                }
                team.append(ssh_key.name)

        cdict['dploi::enc-customer'] = {"projects": projectlist,  }
        cdict['dploi::admin::enc-developer'] = {"developers": developerslist,  }
        node = {
            'classes' : cdict,
            'parameters' : {
#                "my_memory" : 216,
#                "location"  : "Hamburg",    # "Hamburg",
#                "manager"   : "Jane Doe",
#                "nodename" : facts['ipaddress'],
                "ssh_keys": ssh_keys,
                "team": team,
                }
        }

        dump(node, sys.stdout,
            default_flow_style=False,
            explicit_start=True,
            indent=10 )