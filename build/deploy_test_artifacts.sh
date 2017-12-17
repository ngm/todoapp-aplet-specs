#!/bin/bash
git config --global user.email "$GIT_EMAIL"
git config --global user.name "$GIT_USERNAME"
git config credential.helper "store --file=.git/credentials"
echo "https://${GITHUB_TOKEN}:@github.com" > .git/credentials
git config --replace-all remote.origin.fetch +refs/heads/*:refs/remotes/origin/*
git fetch origin
git checkout --track origin/gh-pages
export SSHPASS=$DEPLOY_PASS
sshpass -e scp -o StrictHostKeyChecking=no $DEPLOY_USER@$DEPLOY_HOST:report*.html .
git add report*.html
git commit -m "Checkin test reports from travis after CI run"
git push
