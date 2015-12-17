#!/usr/bin/python
import csv
import glob
import os
import re

# Config - change these if needful!
datafile_dir = 'data'
output_dir = 'processed_data'
extract_columns = ['cra', 'CRAsolution', 'solution_cra.keys', 'solution_cra.rt', 'cra_solved.keys', 'cra_solved.rt', 'insight_resp.keys', 'insight_resp.rt', 'date', 'frameRate', 'expName', 'participant', 'condition']
# End config

def mangleFile(orig_filename, csv_writer):
  with open(orig_filename) as csv_fd:
    csv_rows = csv.DictReader(csv_fd)
    for row in csv_rows:
      if row[extract_columns[0]] is not "":
        csv_writer.writerow([row[col_name] for col_name in extract_columns])

  return True

datafile_list = glob.glob(os.path.join('.', datafile_dir, '*.csv'))
file_pairs = {}

# Take all the files and organize them into a dict.
for file_name in datafile_list: 
  if re.match('.*(pre|post).*', file_name) is None:
    continue

  # Operate on filename, not whole path!
  run_info = re.match('^([0-9]+)_([^_]+)_', os.path.basename(file_name))
  participant_num = run_info.group(1)
  experiment = run_info.group(2)

  if participant_num not in file_pairs:
    file_pairs[participant_num] = {'pre': None, 'post': None}

  file_pairs[participant_num][experiment] = file_name

# Now we have participant number -> pre & post filenames.
# The pre and post files are different, so load the CSV and pull out the
# relevant columns, leaving the rest of the junk columns behind.
for participant in file_pairs:
  print "* Participant %s processing..." % (participant)
  output_filename = '%s_all.csv' % (participant)
  output_path = os.path.join('.', output_dir, output_filename)

  with open(output_path, 'wb') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(extract_columns)
    
    mangleFile(file_pairs[participant]['pre'], csv_writer)
    mangleFile(file_pairs[participant]['post'], csv_writer)
