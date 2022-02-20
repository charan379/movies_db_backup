
#go to folder

cd /media/psbv/sqlbackup/movies/movies_db_backup

#backup movies db

python3 bcmail.py singlerun localhost movies_php4dvd root swordFish@379 . noarchive true

rm -r local*
