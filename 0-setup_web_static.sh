#!/usr/bin/env bash
#A script sets up your web servers for the deployment of web_static
apt-get update
apt-get -y install nginx
#sudo ufw allow 'Nginx HTTP'

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
# Create a fake HTML file for testing
echo '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' | tee /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '/^\tserver_name.*;/a \\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

service nginx restart
