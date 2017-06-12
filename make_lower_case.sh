filename='train_label.txt'
echo Start
while read p; do
    echo ${p,,} >> img_label_lwr.txt
done < $filename
echo Done
