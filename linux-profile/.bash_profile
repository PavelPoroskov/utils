
if [ ! -d ~/.tmp ]; then
  mkdir -p ~/.tmp
fi

rm -rf ~/.tmp/*

if ! grep -q file:///home/$USER/.tmp  ~/.config/gtk-3.0/bookmarks; then
  echo file:///home/$USER/.tmp TMP >> ~/.config/gtk-3.0/bookmarks
fi

if ! grep -q file:///home/$USER/Pictures/Screenshots  ~/.config/gtk-3.0/bookmarks; then
  echo file:///home/$USER/Pictures/Screenshots >> ~/.config/gtk-3.0/bookmarks
fi

# SAVE_DIR="/home/$USER/afolder/_save/$(date +%Y-%m)-01"
# mkdir -p $SAVE_DIR

# if [ -h ~/SAVE ]; then
#   unlink ~/SAVE
# fi
# ln -s $SAVE_DIR ~/SAVE

# if ! grep -q file:///home/$USER/SAVE  ~/.config/gtk-3.0/bookmarks; then
#   echo file:///home/$USER/SAVE >> ~/.config/gtk-3.0/bookmarks
# fi