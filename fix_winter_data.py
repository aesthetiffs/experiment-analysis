import csv
import glob
import os
import re

# Config - change these if needful!
datafile_dir = 'data'
output_dir = 'processed_data'
extract_columns = ['cra', 'CRAsolution', 'solution_cra.keys', 'solution_cra.rt', 'cra_solved.keys', 'cra_solved.rt', 'insight_resp.keys', 'insight_resp.rt', 'date', 'frameRate', 'expName', 'participant', 'session']
# End config

datafile_list = glob.glob(os.path.join('.', datafile_dir, '*.csv'))
def csv_thingie(orig_filename, csv_writer):
  with open(orig_filename) as csv_fd:
    csv_rows = csv.DictReader(csv_fd)
    for row in csv_rows:
       csv_writer.writerow([row[col_name] for col_name in extract_columns])

for file_name in datafile_list:
   #open the files to be worked on...
    with open(file_name) as csv_fd:
        csv_rows = csv.DictReader(csv_fd)

    run_info = re.match('^([0-9]+)_', os.path.basename(file_name))
    participant = run_info.group(1)

    print "* Participant %s processing..." % (participant)
    output_filename = '%s_all.csv' % (participant)
    output_path = os.path.join('.', output_dir, output_filename)

    #save the files that were worked on...
    with open(output_path, 'wb') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(extract_columns)
        csv_thingie(file_name,csv_writer)
