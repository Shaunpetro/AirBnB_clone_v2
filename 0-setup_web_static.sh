#!/usr/bin/env bash
# sets up web server for deployment
sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo echo "
<!doctype html>
<html>
<head>
<title> HTML Template example</title>
</head>
<body>
	Holberton School
</body>
</html>
" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "38 i \location /hbnb_static {\n\talies /data/web_static/current/;\n\t}\n" /etc/nginx/sites-enabled/default
sudo service nginx start
