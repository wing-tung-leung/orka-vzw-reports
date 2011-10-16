#!/bin/bash
#
# Eerst afschriften aanvragen, en daarna export van uitgaves naar CSV.
# Anders geen transactie-nummer.
#
# Nog te doen: data aanpassen, kolommen verschuiven met cut & paste,
# interesten en huur gemeente markeren, ..
# 
# ====================================================================

INPUT=export.csv

cat "$INPUT" | sed -e '1,13d' |  # headers weggooien
	sed 's/\&#199;/C/g' | # replace encoded c cedile, cause ; problem
	cut -d\; -f2,4,6,9,11|  # split columns based on ;
	sed 's/CELIS ROZA/Petanque/1' |
	sed 's/VAN DER BEEUREN PATRIK/Petanque/1' |
	sed 's/VAN THIELEN CAROLINA/Kaarters/1' |
	sed 's/VERHOEVEN JULIETTE/Kaarters/1' |
	sed 's/VAN CAMP LUTGARDE/Kaarters/1' |
	sed 's/SEGERS ANGELA/Kaarters/1' |
	sed 's/MELIS - VOS/Donderdagspelers/1' |
	sed 's/GEMEENTE RANST/Huur gemeente/1' |
	sed 's/"CORNAND FRAN.*OIS"/Swa:/1' |
	sed 's/CORNAND FRANCOIS/Swa:/1' |
	sed "s/D'HOOGE LUCIAAN/Luc:/1" |
	sed 's/HOFKENS CECILIA/Luc:/1' |
	sed 's/LEUNG-ENNEKENS/Tung:/1' |
	sed 's/VAN PELT-MAMPAEY/Walter:/1' |
	sed 's/BECKERS - SLABBINCK/Hugo:/1' |
	sed 's/Oelegemse Drankendiscount/Drankendiscount/1' |
	sed 's/Electrabel N.V./Electrabel/1' |
	tac

