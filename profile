# ~/.profile: executed by the command interpreter for login shells.

mkdir -p /tmp/$USER

if [ -h ~/TEMP ]; then
  unlink ~/TEMP
fi
ln -s /tmp/$USER ~/TEMP

if ! grep -q file:///home/$USER/TEMP  ~/.config/gtk-3.0/bookmarks; then
  echo file:///home/$USER/TEMP >> ~/.config/gtk-3.0/bookmarks
fi


SAVE_DIR="/home/$USER/afolder/_save/$(date +%Y-%m)-01"
mkdir -p $SAVE_DIR

if [ -h ~/SAVE ]; then
  unlink ~/SAVE
fi
ln -s $SAVE_DIR ~/SAVE

if ! grep -q file:///home/$USER/SAVE  ~/.config/gtk-3.0/bookmarks; then
  echo file:///home/$USER/SAVE >> ~/.config/gtk-3.0/bookmarks
fi

if ! grep -q file:///home/$USER/SAVE  ~/.config/gtk-3.0/bookmarks; then
  echo file:///home/$USER/SAVE >> ~/.config/gtk-3.0/bookmarks
fi
