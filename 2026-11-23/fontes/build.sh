#!/bin/bash
# Renderiza as peças da semana. Uso: bash build.sh (a partir de 2026-11-23/fontes)
set -e
S=../../sistema; H=html; O=..
for p in p_aimax p_painel p_raiox; do python3 $S/render.py png $H/$p.html $O/$p.png; done
python3 $S/render.py png $H/art_capa.html $O/art_capa.png 1920 1080
python3 $S/carrossel.py $O/cbf_black-friday-metade-indecisa.pdf $H/cbf_0*.html
python3 $S/carrossel.py $O/ccpl_cpl-de-7-reais.pdf $H/ccpl_0*.html
