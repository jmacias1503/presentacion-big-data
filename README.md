# Presentación de gráfica de barras/histogramas

Proyecto que explora la visualización de datos de Netflix usando gráficas de barras e histogramas con tres bibliotecas de Python: Matplotlib, Plotly y Seaborn.

## Estructura del proyecto

```
.
├── setup.py                  # Configura el entorno virtual e instala dependencias
├── requirements.txt          # Dependencias de Python
├── package.json              # Scripts npm/pnpm para generar gráficas y presentación
├── netflix_titles.csv        # Dataset de títulos de Netflix
├── grafica-de-barras.ipynb   # Notebook de Jupyter con ejemplos
├── ejemplo-matplotlib.py     # Ejemplo con Matplotlib
├── ejemplo-plotly.py         # Ejemplo con Plotly
├── ejemplo-seaborn.py        # Ejemplo con Seaborn
├── graphics/                 # Gráficas generadas
│   ├── matplotlib.png
│   ├── plotly.png
│   ├── seaborn.png
│   └── graphics.png          # Composición de las tres anteriores
├── slides/                   # Diapositivas en Markdown para Marp
│   ├── 00-header.md
│   ├── 01-titles.md
│   ├── 02-por-que-barras.md
│   ├── 03-barras-o-histogramas.md
│   ├── 04-datos-a-mostrar.md
│   ├── 05-matplotlib.md
│   ├── 06-plotly.md
│   ├── 07-seaborn.md
│   └── 99-ending.md
├── venv/                     # Entorno virtual de Python
└── presentacion.pdf          # Presentación en PDF generada
```

## Dependencias

- **Python 3** con las bibliotecas enlistadas en `requirements.txt`
- **Node.js** (pnpm) para Marp CLI y Hercule

## Instalación

```bash
# Entorno virtual de Python
python3 setup.py
source venv/bin/activate

# Dependencias de Node.js (presentación)
pnpm install
```

## Uso

| Comando | Descripción |
|---------|-------------|
| `pnpm run build` | Genera las gráficas con los tres scripts de Python |
| `pnpm run aggregate` | Combina las tres gráficas en una sola imagen |
| `pnpm run present` | Compila las diapositivas y genera `presentacion.pdf` |
| `jupyter notebook` | Abre el notebook interactivo |
