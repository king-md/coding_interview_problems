#!/usr/bin/env python3

import argparse

def main():

    # get command line parameters
    parser = argparse.ArgumentParser()

    parser.add_argument('-s', action='store',
                        dest='search_string',
                        help='The string to be searched,')

    parser.add_argument('-n', action='store',
                        dest='substring_length',
                        help='The length of the substring for counting,')

    # --version
    parser.add_argument('--version', action='version',
                        version='%(prog)s 1.0')

    results = parser.parse_args()

    n = int(results.substring_length)
    inputstr = results.search_string
    mylist = {}

    if(len(inputstr) >= n ):
        #process the string
        for i in range(len(inputstr)-n+1):
            #print( "DEBUG:",inputstr[i:i+(n)])
            if( inputstr[i:i+(n)] in mylist):
                 mylist[inputstr[i:i+(n)]] +=1
                 #print( "DEBUG::",mylist[inputstr[i:i+(n)]])
            else:
                 mylist[inputstr[i:i+(n)]] =1
                 #print( "DEBUG:.",mylist[inputstr[i:i+(n)]])
        high=0
        ndx=-1
        for j,v in mylist.items():
            if(v > high):
                high = v
                ndx = j
        print("The most common substring of size ",n," in the string ",inputstr," is:",ndx)

    else:
        #return NULL (or equivilent)
        print("Input is shorter than requested match length.")

   

main()

