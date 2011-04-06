"""
Fabric script for easing deployment processes.

update staging and restart:         fab stage deploy
update live server and restart:     fab live deploy
update all servers and deploy:      fab full deploy
"""

from __future__ import with_statement
from fabric.api import *

env.user = "chefathome"
env.directory = "/home/chefathome/chefathome/cah"
env.virtualenvdir = "/home/chefathome/virtualenvs/chefathome/"
env.activate = "source %sbin/activate" % env.virtualenvdir

def stage():
    env.hosts = ['chefathome@chefatho.me',]
    env.deploy_user = "chefathome"

def live():
    env.hosts = ['', ]

def full():
    env.hosts = ['chefathome@chefatho.me']
    env.deploy_user = "chefathome"

def reboot():
    """Reboot the server."""
    sudo("svc -h /etc/service/chefathome")

def virtualenv(command):
    with cd(env.directory):
        sudo(env.activate + '&&' + command, user=env.deploy_user)

def syncdb():
    with cd(env.directory):
        virtualenv("./manage.py syncdb")

def migrate():
    with cd(env.directory):
        virtualenv("./manage.py migrate")

def deploy():
    """Update the code repository."""
    local("git push")
    with cd("~/chefathome/"):
        run("git pull")
    reboot()