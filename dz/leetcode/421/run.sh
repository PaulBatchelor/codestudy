TOP=../../..
MAIN=leetcode/421

> a.db
dagzet main.dz | sqlite3 a.db
dzbrowse/logparse.py $TOP/logs/leetcode/notes.log | sqlite3 a.db
dzbrowse/gentagnodes.py a.db
dzbrowse/import_code.py $TOP/code/$MAIN/hashset.py codestudy/$MAIN/hashset.py | sqlite3 a.db

dzbrowse/generate.py a.db
