#.bash

cd ~
CHROME_ARCHIVE="config-google-chrome--$(date +%F-%a).tar.gz"
nohup tar --exclude=**/CacheStorage/* -zcvf "$CHROME_ARCHIVE" ~/.config/google-chrome > /dev/null 2>&1 &
