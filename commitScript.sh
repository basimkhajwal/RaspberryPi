#!/bin/bash
cd "$(dirname "$0")"

echo "  Keepin' the streak alive  " >> streak.txt
git add *
git commit -m "Kept the streak alive"
