#!/usr/bin/env zsh

run_sol () {
    local prog="$1"
    make $prog
    diff <( ./$prog < "in" ) "out" -s
    rm -v $prog
}
