#go to folder

cd /media/psbv/sqlbackup/movies/movies_db_backup

#backup movies db

python3 backup.py singlerun localhost movies_php4dvd root swordFish@379 . noarchive fasle

#git add

git add .

# commit

git commit -m "new db backup"

# push

git push https://charan379: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@github.com/charan379/movies_db_backup.git --all

