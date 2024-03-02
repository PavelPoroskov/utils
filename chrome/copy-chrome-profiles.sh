#!/bin/bash

CHROME_ROOT="$HOME/.config/google-chrome"
ARCHIVE_ROOT="$HOME/bookmarks-$HOSTNAME-$USER-$(date +%Y-%d-%m-%H%M)"
mkdir -p "$ARCHIVE_ROOT"

function doProfile {
  profileFolder=$1
  echo "do profile $profileFolder"
  
  mkdir -p "$ARCHIVE_ROOT/$profileFolder"
  cp "$CHROME_ROOT/$profileFolder/Preferences" "$ARCHIVE_ROOT/$profileFolder/Preferences"
  cp "$CHROME_ROOT/$profileFolder/Bookmarks" "$ARCHIVE_ROOT/$profileFolder/Bookmarks"

  mkdir -p "$ARCHIVE_ROOT/$profileFolder/Sessions"
  cp "$CHROME_ROOT/$profileFolder/Sessions/Tabs_"* "$ARCHIVE_ROOT/$profileFolder/Sessions/"
}

doProfile 'Default'

for ((i=1;i<=100;i++)); 
do 
  profileFolder="Profile $i"

  if [[ -f "$CHROME_ROOT/$profileFolder/Preferences" ]]; then
    doProfile "$profileFolder"
  fi
done
