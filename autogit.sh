echo 'Running auto git push bash!'
pwd

git status
git add -A
git commit -m 'Auto git commit'
git push -u origin
git status
echo 'bash closed!'
