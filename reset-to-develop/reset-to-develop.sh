#!/usr/bin/env sh

RED='\033[0;31m'
NC='\033[0m' # No Color

header() {
    echo ----------------------------------------------
    echo
    printf "${RED}$(pwd)${NC}\n"
}

handle_choice() {
    CHOICE=$(gum choose Stash Commit "Open Terminal")
    case "$CHOICE" in
    "Stash")
        git stash
        git checkout develop
        ;;
    "Commit")
        git commit -am "Intermediate commit"
        git checkout develop
        ;;
    "Open Terminal")
        bash
        ;;
    esac
}

main() {
    REPOS=$(fd --hidden -td ".git" | sd ".git/" "")
    for repo in $REPOS; do
        pushd $repo >/dev/null
        header
        git checkout develop
        STATUS=$?
        if [ $STATUS -ne 0 ]; then
            git status
            handle_choice
        fi
        popd >/dev/null
    done
}

main
