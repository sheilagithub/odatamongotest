import os
import csv
import json
import re
import subprocess
from filecmp import dircmp
from pymongo import MongoClient
from time import strftime
from subprocess import check_output


collectionname = 'applications'
client = MongoClient("mongodb://eratedemo:eratedemo@ds044989.mlab.com:44989/eratedemo")

db = client['eratedemo']
collection = db[collectionname]
#dcmp = dircmp('D:/src/centraled/james/data/2') 
#print_diff_files(dcmp) 


filelist = os.listdir('D:/src/centraled/james/data/2')
documents = []

for file in filelist:
    if str(file).find('.tsv') > 0:
       # subprocess.call('mongoimport','--db CentralEd', '--file D:/src/centraled/james/data/' + file,  '--headerline','--type tsv','--collection ' + collectionname)
      # check_output('mongoimport --file D:/src/centraled/james/data/2/' + file + ' --ignoreBlanks --headerline --type tsv --db CentralEd --collection applications --host localhost --port 27017', shell=True)
      #check_output('mongoimport --file D:/src/centraled/james/data/2/' + file + ' --ignoreBlanks --headerline --type tsv --db eratedemo --collection applications --host ds044989.mlab.com --port 44989 --username eratedemo --password eratedemo', shell=True)
    
       # os.system('mongoimport --db CentralEd --file D:/src/centraled/james/data/' + file + ' --headerline --type tsv --collection ' + collectionname)
        with open('D:/src/centraled/james/data/2/' + file, 'r') as f:
            documents=[]
            reader = csv.DictReader(f, delimiter='\t')
            for row in reader:
                row["_date"] = re.search('(\d{4}-\d{2}-\d{2})', file).group(1)
                x = json.dumps(row, ensure_ascii=False)
                documents.append(row)
               # collection.insert(row)
    collection.insert_many(documents)

def print_diff_files(dcmp):
    for name in dcmp.diff_files:
        print "diff_file %s found in %s and %s" % (name, dcmp.left,
              dcmp.right)
    for sub_dcmp in dcmp.subdirs.values():
        print_diff_files(sub_dcmp)

