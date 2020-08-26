## 1. Creating Directories ##

/home/dq$ mkdir dir2 dir3 dir5

## 2. Deleting Directories ##

/home/dq$ rmdir dir2 dir3 dir5

## 3. Failing to Delete Directories ##

/home/dq$ rmdir prize_winners

## 4. Copying Files ##

/home/dq/prize_winners$ cp .mike mike

## 5. Hidden Dangers of Copying Files ##

/home/dq/prize_winners$ cp -i east coasts

## 6. Copying Directories ##

/home/dq$ cp -R prize_winners brats

## 7. Deleting Directories and Files ##

/home/dq$ rm -R prize_winners

## 8. Moving and Renaming Directories and Files ##

/home/dq/brats/prize_winners$ mv .mike Mike