#!/bin/bash
mysql.server start
cd Desktop/Registro\ de\ jornada/CRT/
open -a /Applications/Firefox.app -g http://localhost:8000
python3 manage.py runserver
