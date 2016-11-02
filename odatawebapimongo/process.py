import os
import csv
import json
import subprocess
from filecmp import dircmp
#from pymongo import MongoClient
from time import strftime
from subprocess import check_output


collectionname = 'FRN_' + strftime("%Y-%m-%d")
#lient = MongoClient()

#db = client['CentralEd']
#collection = db[collectionname]
#dcmp = dircmp('D:/src/centraled/james/2016-09-28/data','D:/src/centraled/james/2016-10-18/data') 
#print_diff_files(dcmp) 


filelist = os.listdir('D:/src/centraled/james/data/2')
documents = []

for file in filelist:
    if str(file).find('.tsv') > 0:
       # subprocess.call('mongoimport','--db CentralEd', '--file D:/src/centraled/james/data/' + file,  '--headerline','--type tsv','--collection ' + collectionname)
      # check_output('mongoimport --file D:/src/centraled/james/data/2/' + file + ' --ignoreBlanks --headerline --type tsv --db CentralEd --collection applications --host localhost --port 27017', shell=True)
      check_output('mongoimport --file D:/src/centraled/james/data/2/' + file + ' --ignoreBlanks --headerline --type tsv --db eratedemo --collection applications --host ds044989.mlab.com --port 44989 --username eratedemo --password eratedemo', shell=True)
    
        #os.system('mongoimport --db CentralEd --file D:/src/centraled/james/data/' + file + ' --headerline --type tsv --collection ' + collectionname)
        #with open('data/' + file, 'r') as f:
            #reader = csv.DictReader(f, delimiter='\t')
            #for row in reader:
               # x = json.dumps(row, ensure_ascii=False)
                #collection.insert(row)


def print_diff_files(dcmp):
    for name in dcmp.diff_files:
        print "diff_file %s found in %s and %s" % (name, dcmp.left,
              dcmp.right)
    for sub_dcmp in dcmp.subdirs.values():
        print_diff_files(sub_dcmp)

