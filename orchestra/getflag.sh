#to view the entire file content
cat orchestra.txt
#this script is used to get the flag from the file(unix/linux command)
string orchestra.txt | grep "Asthra"
#another method
string orchestra.txt | grep -i "Asthra"



#to view the entire file content in windows
type orchestra.txt
#this script is used to get the flag from the file(windows command)
findstr /i "asthra" orchestra.txt