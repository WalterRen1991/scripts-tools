#!/bin/bash

args="$*"

function usage()
{
    echo "Usage:
    `basename $0` options
    (-m Mac addr
     -n Net segment)"
}

while getopts ":m:n:h" Option; do
    case $Option in
        m)
        mac_addr=$OPTARG
        ;;
        n)
        net_segment=$OPTARG
        ;;
        h)
        usage
        ;;
    esac
done

shift $(($OPTIND - 1))


