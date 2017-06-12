filename='images.txt'
echo Start
while read p; do
    echo $p >> output.txt
    alpr --topn 1 $p >> output.txt
    printf '\n' >> output.txt
done < $filename
echo Done
