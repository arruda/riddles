#!/usr/bin/env bash
sed -i "s/set timeout=-1/set timeout=0/g" /etc/grub.d/00_header
