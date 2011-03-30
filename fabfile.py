"""
Fabric script for easing deployment processes.

update staging and restart:         fab stage deploy
update live server and restart:     fab live deploy
update all servers and deploy:      fab full deploy
"""

from __future__ import with_statement
from fabric.api import *


def stage():
    env.hosts = ['chefathome@chefatho.me',]

def live():
    env.hosts = ['', ]

def full():
    env.hosts = ['chefathome@chefatho.me']

def reboot():
    """Reboot the server."""
    sudo("svc -h /etc/service/chefathome")

def deploy():
    """Update the code repository."""
    local("git push")
    with cd("~/chefathome/"):
        run("git pull")
    reboot()