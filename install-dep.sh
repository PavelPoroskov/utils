function ins() {
    echo "installing $1"
    echo "***** installing $1" >> txt.txt
    npm i "$1" >> txt.txt
}

function insD() {
    echo "installing dev $1"
    echo "***** installing dev $1" >> txt.txt
    npm i -D "$1" >> txt.txt 
}

# ins @fortawesome/fontawesome-svg-core


# insD @types/node

