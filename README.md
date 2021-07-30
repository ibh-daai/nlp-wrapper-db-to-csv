# NLP Wrapper (Database to CSV)
Generic scripts to wrap around NLP algorithms like chexpert/chexbert to enable reading/writing from/to a database vs. CSV files

# Usage
Simple, you run `nlp-db2csv.py` BEFORE the NLP algorithm's `label.py` to dump some reports from the Database to CSV, then run `nlp-csv2db.py` AFTER to read the CSV output and store it into the database. Below is example of how you put it altogether:
```
conda activate chexbert
python3 nlp-db2csv.py
python3 label.py -d input.csv -o . -c chexbert.pth
python3 nlp-csv2db.py
```
If you have a lot of reports, you can wrap the whole thing in a BASH script loop like so:
```
i=1
while [ $i -le 100 ]
do
   echo "================ LOOP $i times"
   python3 nlp-db2csv.py
   python3 label.py -d input.csv -o . -c chexbert.pth
   python3 nlp-csv2db.py
   ((i++))
done
```
Change the 100 on line 2 to match the number of iterations you need to make.
