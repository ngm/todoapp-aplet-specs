#!/bin/bash

export APP_DIR=/home/neil/Code/todoapp-aplet/
mkdir tests/_output/reports
rm -rf build/lektor
cp -R ~/Code/aplet-lektor/ build/lektor/

for PRODUCT in "ProdA" "ProdB" "ProdC" "ProdD" "ProdE"
do
    cp eclipse/configs/$PRODUCT.config $APP_DIR/todo.config
    export FEATURES=$(sed 's?\(.*\)?-g \1 ?' eclipse/configs/$PRODUCT.config | tr -d '\r\n')
    export NOTFEATURES=$(comm -13 <(sort eclipse/configs/$PRODUCT.config) <(sort eclipse/configs/optionals.config) | sed 's?\(.*\)?-g Not\1 ?' | tr -d '\r\n')
    php vendor/bin/codecept run acceptance $FEATURES $NOTFEATURES --debug --json --html --xml
    # copying report file for product
    cp tests/_output/report.json tests/_output/reports/report$PRODUCT.json
    cp tests/_output/report.xml tests/_output/reports/report$PRODUCT.xml
    cp tests/_output/report.html tests/_output/reports/report$PRODUCT.html
    mkdir build/lektor/content/products/$PRODUCT
    cp build/lektor/helpers/product_contents.lr build/lektor/content/products/$PRODUCT/contents.lr
    sed -i "s/<<PRODUCT>>/$PRODUCT/g" build/lektor/content/products/$PRODUCT/contents.lr
    sed -i "s/<<PROJECT>>/SuperTodo PL/g" build/lektor/aplet.lektorproject
    cp tests/_output/report.html build/lektor/content/products/$PRODUCT/report$PRODUCT.html
done

echo ""
echo "- Generating feature model SVG..."
python3 scripts/fm_augment.py eclipse/model.xml BDDFeatures/ tests/_output/reports/ build/lektor/content/

echo "- Building site"
cd build/lektor/
lektor build -O out
