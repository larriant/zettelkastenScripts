cd ~/Dropbox/Zettelkasten
if [[ `git status --porcelain` ]]; then
  # Changes
  git add -A
  git commit -m "Update"
else
  # No changes
fi
