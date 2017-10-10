It is an application of MapReduce in HDFS.

rawdata.txt contains sample raw data
finaldata.txt contains processed data.
First the wordcount.py reads the raw txt file and eliminates all the special characters and splits all words by ','.
Second create a .jar file using wordcount.java which implements MapReduce.

Load finaldata.txt in HDFS
Run the .jar file
