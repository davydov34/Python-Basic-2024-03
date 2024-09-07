#!/usr/bin/env bash

echo "Start migration"

#flask db init
#flask db migration
flask db upgrade

echo "Migration is done"