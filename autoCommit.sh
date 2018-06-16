cd ~/Dropbox/Zettelkasten
if [[ `git status --porcelain` ]]; then
  # Changes
  echo 'Changes'
  git add -A
  git commit -m "Update"
else
  # No changes
  echo 'No Changes'
fi
