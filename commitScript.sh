#!/bin/bash
cd "$(dirname "$0")"

cat "  Keepin' the streak alive  " >> streak.txt
git add *
git commit -m "Kept the streak alive"
git push origin master

