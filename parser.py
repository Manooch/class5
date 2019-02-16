
#1. Load a dataset from a file
#2. "organize" that file, so we can access columns *or* rows of it easily
#3. compute some "summary statistics
#4. print those summary statistics

# load a dataset
#1.a accept a arbitrary filename as argument
#1b.  load the file

from argparse import Argumentparser(description = 'A csv reader + stats make maker")
parser.add_argument('csvfile'help="path to the input csv file.')
parsed_args = parser.parser_args()
print(parsed_args)
print(parsed_args.csvfile)

my_csv_file = parsed_args.csvfile

import os 

if os.path.isfile(my_csv_file):
   print('yay,it is a real file!')
else
   print('ooops, plz give rl files')

assert op.path.isfile(my_csv)file), "please give us a real file, k thx"
print('hello')


 
# 1b. load the file
import pandas as pd

data = pd.read_csv(my_csv_file, sep ='\s+|, ', header= None)
print(data.head())

for item in dir(data)
 print(item)

print(data.shape)


#2. "organize" that file,...
# 2a. access any row "pandas access data by column"
print(data.iloc[3:4,:])
# 2b. access any column "pandas access data by row"
print(data.iloc[:3, -2:])
# 2c. access any value "pandas access specific data by loacation"

print(data.iloc[3,4])


#compute some "summary statistics"

import numpy as np

print(np.mean(data))
print(np.std(data)) 


