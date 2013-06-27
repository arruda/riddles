#!/bin/bash

i18n(){
    echo "atualizando .mo"
    cd riddles
    django-admin.py makemessages -a
    django-admin.py compilemessages
    cd -
}

i18n_criar(){
    echo "atualizando .mo"
    cd riddles
    django-admin.py makemessages -l pt_BR
    cd -
}


COMANDO=$1
$COMANDO
