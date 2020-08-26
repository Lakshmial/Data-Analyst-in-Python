## 1. Printing User Input ##

/home/dq$ echo This is a command line interface.

## 2. Redirecting Output with > ##

/home/dq$ help echo >echo_help

## 3. Redirecting Output with >> ##

/home/dq$ grep -hi ',Math' rg_data/* >>math_dataset

## 4. Creating Empty Files ##

/home/dq$ touch empty_file1 empty_file2

## 5. Why Pipelines? ##

/home/dq$ cut -d"," -f1,2,5 math_dataset

## 6. Using Pipelines ##

/home/dq$ zen | grep "better"

## 7. The Unix Philosophy ##

/home/dq/rg_data$ sort -u * | wc -l

## 8. Trying to Redirect Errors ##

/home/dq/rg_data$ echo "This is going to disappear" >/dev/null