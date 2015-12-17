#!/usr/bin/python
import csv
import glob
import os

datafile_dir = './data'
datafile_list = glob.glob(os.path.join(datafile_dir, '*.csv'))

for file_name in datafile_list: 
  with open(file_name) as csv_fd:
    csv_rows = csv.reader(csv_fd)
    print "File = %s has %i lines" % (file_name, sum(1 for row in csv_rows))
