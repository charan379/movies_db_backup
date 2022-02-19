#go to folder

cd /media/psbv/sqlbackup/movies/movies_db_backup

#backup movies db

python3 backup.py singlerun localhost movies_php4dvd root swordFish@379 . noarchive fasle

#git add

git add .

# commit

git commit -m date

# push

git push https://charan379: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@github.com/charan379/movies_db_backup.git --all
