#!/bin/bash

export APP_DIR=/home/neil/Code/todoapp-aplet/
cp eclipse/configs/$PRODUCT.config $APP_DIR/todo.config
export FEATURES=$(sed 's?\(.*\)?-g \1 ?' eclipse/configs/$PRODUCT.config | tr -d '\r\n')
export NOTFEATURES=$(comm -13 <(sort eclipse/configs/$PRODUCT.config) <(sort eclipse/configs/optionals.config) | sed 's?\(.*\)?-g Not\1 ?' | tr -d '\r\n')
php vendor/bin/codecept run acceptance $FEATURES $NOTFEATURES
