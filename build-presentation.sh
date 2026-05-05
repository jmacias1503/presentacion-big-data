#!/bin/sh

cat slides/*.md | hercule --stdin | CHROME_PATH="/usr/bin/brave-browser" marp --stdin --base . --pdf -o presentacion.pdf
