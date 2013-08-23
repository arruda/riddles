#!/bin/bash
COMANDO=$1

if [ -z "$PY_PATH" ]; then
    PY_PATH="python"
fi

start_django(){
    echo "iniciando django"
    $PY_PATH manage.py runserver 0.0.0.0:8000&
}

stop_django(){
    echo "parando django"
    kill -9 $(ps aux | grep "manage.py" | grep -v "grep" | awk '{print $2}')
}

start_compass(){
    echo "iniciando compass"
    compass watch riddles/compass&
}

stop_compass(){
    echo "parando compass"
    kill -9 $(ps aux | grep "compass" | grep -v "grep" | awk '{print $2}')
}

start(){
    start_compass
    start_django
}
stop(){
    stop_compass
    stop_django
}

$COMANDO
