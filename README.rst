============
dploi-server
============

.. warning:: dploi is still in the plannig phase. The code is not functional yet!

dploi-server manages all the information about Host, Applications and Deployments and acts as the main hub of a
dploi setup.

Installation
============

dploi-server is written in python. Using virtualenv is highly recommended!

To develop dploi-server in the current virtualenv, clone the sourcecode and then install it as a develop package::

	git clone git://github.com/dploi/dploi-server.git
	cd dploi-server
	virtualenv . --no-site-packages   # creates a virtualenv without globally installed packages
	source bin/activate  # activates the virtualenv
	python setup.py develop  # installs all the dependencies and adds the dploi-server source directory to pythonpath
	dploi-server syncdb
	dploi-server migrate
	dploi-server runserver

dploi-server is a django project. It can be run the classic django way::

	python dploi_server/manage.py runserver

or using the built in command shortcut::

	dploi-server runserver

Puppet ENC Support
==================
You can use dploi server to configure your entire puppet managed setup. But first, you need to make sure that the following items are available on all servers. You can do that by putting it in site.pp:

	node default {
			group { "customers":
				name		=> "customers",
				gid		=> 502,
				alias		=> 502,
				ensure		=> present,
				allowdupe	=> false,
			}
			group { "developers":
				name		=> "developers",
				gid		    => 500,
				alias		=> 500,
				ensure		=> present,
				allowdupe	=> false;
			}

			sudo::sudo_user{
			    "developers":
			        user => "%developers",
			        privileges => [
			            "ALL = NOPASSWD: ALL",
			        ]
			}
	}

Furthermore, this should go into /etc/puppet/puppet.conf

	[master]
	node_terminus = exec
	external_nodes = /path/to/dploi-server puppet_enc