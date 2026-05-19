#!/bin/sh

echo "Generando graficas"
python3 ejemplo-matplotlib.py
python3 ejemplo-plotly.py
python3 ejemplo-seaborn.py
echo "Creando presentacion"
cat slides/*.md | hercule --stdin | CHROME_PATH="/usr/bin/brave-browser" marp --stdin --base . --pdf -o presentacion.pdf

convert matplotlib.png plotly.png seaborn.png -append graphics.png
