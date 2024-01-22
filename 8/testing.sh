echo Gen wersja2.py
perl -p -e "s/# Wersja2 //" wersja1.py > wersja2.py

steps=10000000
echo Test wersja1.py $steps $steps
/usr/bin/time -v python3 wersja1.py $steps $steps 2>&1 1>/dev/null | grep  -E "wall|Max"
echo -------------------------

echo Test wersja2.py $steps $steps
/usr/bin/time -v python3 wersja2.py $steps $steps 2>&1 1>/dev/null | grep  -E "wall|Max"
echo -------------------------

# Faktycznie jest roznica :)