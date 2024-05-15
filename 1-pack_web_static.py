#!/usr/bin/python3
"""
This module contains the function do_pack that generates a .tgz archive
  from the contents of the web_static folder (fabric script)
"""

import os
from datetime import datetime
from fabric.api import *


def do_pack():
    """ A script that generates archive the contents of web_static folder"""
    local("sudo mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(date)
    result = local("sudo tar -cvzf {} web_static".format(file_name))
    if result.succeeded:
        return file_name
    else:
        return None
