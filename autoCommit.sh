cd ~/Dropbox/Zettelkasten
if [[ `git status --porcelain` ]]; then
  # Changes
  git add -A
  git commit -m "Update"
  git push origin master
else
  # No changes
fi
