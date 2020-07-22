import cPickle as pickle
import os

### word frequencies:

### function that takes as input a string and, optionally, 
### a dictionary, and returns the dictionary populated with word frequencies.
### provide options to strip punctuation and convert to lowercase.
## 

### instr is the input string
### wf is an optional dictionary. This can be used to count over
### multiple files. If it is present, add counts to this.
### stripPunc and toLower indicate whether to strip punctuation and
### convert to lower case.
def wordfreq(instr, wf=None, stripPunc=True, toLower=True) :


### wc - takes as input the name of a directory and returns a
### dictionary mapping each word in each file in that directory and all subdirectories.
### Optional arguments include whether to strip away punctuation and whether to convert everything to lower case. 
### You should use os.walk() to traverse the directories.  
xf
def wc(dirname, stripPunc=True, toLower=True) :    

### Usage: wordfreq {--nostrip --noConvert --pfile=outfile} directory
### if --nostrip, don't strip punctuation
### if --noConvert, don't convert everything to lower case
### if --pfile=outfile, pickle the resulting dictionary and store it in outfile.
### otherwise, print it to standard out.

if __name__ == '__main__' :

