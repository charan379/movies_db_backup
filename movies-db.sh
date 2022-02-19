#go to folder

cd /media/psbv/sqlbackup/movies/movies_db_backup

#backup movies db

python3 backup.py singlerun localhost movies_php4dvd root swordFish@379 . noarchive fasle

#git add

git add .

# commit

git commit -m "new db backup"

# push
git push --all

