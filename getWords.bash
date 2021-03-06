# first replace '%' with 'percent' because it makes printf confused sometimes
LANG=C sed -i -e 's/%/percent/g' dict.xml

# now print a word followed by all translations separated by commas
egrep -o '''"trans">''[^\<]*<|''d:title="(.+?)"''' dict.xml | awk -F '\"|\>|\ \<|\<' '/trans/{printf ","$4}/d:title/{printf "\n"$2}' >> wordlist

# clean up file

# delete words with no translations ie. has no commas
sed -i -e '/,/!d' wordlist

# delete extra commas for translations that came out as "" for some reason, still doesn't work right though
sed -i -e 's/,{2,100}/,/g' wordlist
