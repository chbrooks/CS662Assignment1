
import cPickle as pickle
### read in data and metadata from a UCI-formatted file and return the following data structures:
### A dict that maps attribute names to possible values 
### A list containing all data instances, with each instance stored as a tuple.
### for example, readData("breast-cancer") should read from breast-cancer.data and breast-cancer.names
def readData(filehandle) :


### Compute ZeroR - that is, the most common data classification without 
### examining any of the attributes. Return the most common classification.
def computeZeroR(attributes, data) :


### Usage: readARFF {--pfile=outfile} infile
### If --pfile=outfile, pickle and store the results in outfile. Otherwise, 
### print them to standard out. Your code should also call computeZeroR and 
### print out the classification, precision and accuracy.

if__name__ == '__main__' :
