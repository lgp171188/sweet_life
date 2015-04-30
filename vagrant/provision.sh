#!/bin/bash

set -e
set -x

cd ~vagrant/sweet_life

apt-get update

export LC_ALL="en_US.UTF-8"
locale-gen en_US.UTF-8

apt-get upgrade -y -q

apt-get install -y -q python-virtualenv libpython-dev git

VENV=/home/vagrant/.virtualenvs/sweet_life

sudo -H -u vagrant virtualenv $VENV

sudo -H -u vagrant -s -- <<EOF
source $VENV/bin/activate
cd ~/sweet_life
pip install -r requirements/requirements.txt
pip install -r requirements/dev.txt
pre-commit install -f
EOF

apt-get autoremove -y -q

echo ". $VENV/bin/activate" >> /home/vagrant/.bashrc

echo "export PATH=\$PATH:/home/vagrant/sweet_life/node_modules/.bin" >> /home/vagrant/.bashrc

cat <<EOF
********************************************************************************

VM provisioning is done

********************************************************************************
EOF
