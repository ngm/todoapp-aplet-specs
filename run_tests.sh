#!/bin/bash

export APP_DIR=/home/neil/Code/todoapp-aplet/
cp eclipse/configs/$PRODUCT.config $APP_DIR/todo.config
export FEATURES=$(sed 's?\(.*\)?-g \1 ?' eclipse/configs/$PRODUCT.config | tr -d '\r\n')
export NOTFEATURES=$(comm -13 <(sort eclipse/configs/$PRODUCT.config) <(sort eclipse/configs/optionals.config) | sed 's?\(.*\)?-g Not\1 ?' | tr -d '\r\n')
php vendor/bin/codecept run acceptance $FEATURES $NOTFEATURES --debug --json --html --xml
# copying report file for product
cp tests/_output/report.json tests/_output/reports/report$PRODUCT.json
cp tests/_output/report.xml tests/_output/reports/report$PRODUCT.xml
cp tests/_output/report.html tests/_output/reports/report$PRODUCT.html
