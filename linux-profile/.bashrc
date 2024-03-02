
alias nodeupdate='nvm install $(nvm current | sed -rn "s/v([[:digit:]]+).*/\1/p") --reinstall-packages-from=$(nvm current)'
