> a.db
dagzet files.dz | sqlite3 a.db
./dzbrowse/logparse.py ../../logs/ripgrep.log | sqlite3 a.db
dzbrowse/gentagnodes.py a.db
dzbrowse/import_code.py ../../code/ripgrep/crates/core/main.rs codestudy/ripgrep/crates/core/main.rs | sqlite3 a.db

./dzbrowse/generate.py a.db
