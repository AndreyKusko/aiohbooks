# Welcome to the aiohbooks!

this project is about async and bad choices...



http://95.213.191.108:8080/
python main_files/main.py


# Разворачивание проекта

    git clone git@github.com:AndreyKusko/aiohbooks.git

### Create a Python Virtual Environment, install requirements

    cd /root/aiohbooks/
    sudo pip install virtualenv
    virtualenv -p python3 venv
    source /root/aiohbooks/venv/bin/activate
    pip install -r requirements.txt
    

### Supervisord (battle server only)
    deactivate
    apt-get install supervisor
    service --status-all | grep super
    >>> [ + ] supervisor
.
   
sudo nano /etc/supervisor/conf.d/aiohbooks.conf

    [program:aiohbooks]
    command=/root/aiohbooks/venv/bin/python main_files/main.py
    directory=/root/aiohbooks
    autorestart=true

    supervisorctl update

### CONGRATS YOU CAN START!
