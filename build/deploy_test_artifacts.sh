#!/bin/bash
export SSHPASS=$DEPLOY_PASS
mkdir tests/_output/reports
sshpass -e scp -o StrictHostKeyChecking=no $DEPLOY_USER@$DEPLOY_HOST:report*.html tests/_output/reports/
python3 scripts/fm_augment.py eclipse/model.xml BDDFeatures/ tests/_output/reports/ tests/_output/

git config --global user.email "$GIT_EMAIL"
git config --global user.name "$GIT_USERNAME"
git config credential.helper "store --file=.git/credentials"
echo "https://${GITHUB_TOKEN}:@github.com" > .git/credentials
git config --replace-all remote.origin.fetch +refs/heads/*:refs/remotes/origin/*
git fetch origin
git checkout --track origin/gh-pages

cp tests/_output/reports/report*.html .
cp tests/_output/reports/feature_model.svg .
git add report*.html
git add feature_model.svg
git commit -m "Checkin test reports from travis after CI run"
git push
