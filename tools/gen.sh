> a.db
while read -r line
do
    dagzet $line | sqlite3 a.db
done < dz/dzfiles.txt

while read -r line
do
    echo $line
    ../dzbrowse/import_code.py $line | sqlite3 a.db
done < code/codefiles.txt

../dzbrowse/batchlogs.py logs/logfiles

../dzbrowse/gentagnodes.py a.db

python3 ../dzbrowse/generate.py a.db
