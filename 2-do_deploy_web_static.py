#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py) that distributes."""
from datetime import datetime
from os.path import exists
from fabric.api import *


env.hosts = ['54.160.79.156', '34.207.64.145']  # <IP web-01>, <IP web-02>
# (using env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)


def do_deploy(archive_path):
    """The distributes an archive to my web servers"""
    if exists(archive_path) is False:
        return False  # Returns False if the file at archive_path doesnt exist
    file_name = archive_path.split('/')[-1]
    no_tgz = '/data/web_static/releases/' + "{}".format(filename.split('.')[0])
    tmp = "/tmp/" + file_name

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}/".format(no_tgz))
        run("tar -xzf {} -C {}/".format(tmp, no_tgz))
        run("rm {}".format(tmp))
        run("mv {}/web_static/* {}/".format(no_tgz, no_tgz))
        run("rm -rf {}/web_static".format(no_tgz))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(no_tgz))
        return True
    except:
        return False
