#!/usr/bin/env bash

apt-get update
apt-get install -y git-core
rm -rf /var/www
ln -fs /vagrant /var/www
