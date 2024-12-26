> a.db
while read -r line
do
    dagzet $line | sqlite3 a.db
done < dz/dzfiles.txt

while read -r line
do
    mnolth lua tools/logparse.lua $line | sqlite3 a.db
done < logs/logfiles

python3 ../dzbrowse/generate.py a.db
