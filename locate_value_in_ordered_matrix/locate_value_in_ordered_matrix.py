#!/usr/bin/env python3

import argparse

def findInMatrix(matrix, queryValue):
    for rownbr in range(len(matrix)):
        #print( "Debug:", matrix[rownbr], rownbr )
        if( queryValue < matrix[rownbr][0] and 0 == rownbr ):
            print("The query value:",queryValue," is not present in the matrix.")
            return
        elif(queryValue < matrix[rownbr][0]):
            # find item in previous row
            #print( "Debug: queryValue, matrix[rownbr][0]:", queryValue, matrix[rownbr][0] )
            findInRow(matrix[rownbr-1],queryValue,rownbr-1)
        elif(rownbr == (len(matrix)-1) ):
            # find in current row
            findInRow(matrix[rownbr],queryValue,rownbr)



def findInRow( row, qValue, refRow ):
    #print( "Debug: row, qValue, refRow:", row, qValue, refRow )
    for cellnbr in range(len(row)):
        if( row[cellnbr] == qValue ):
            print( "Found value:", qValue, "at location: [", refRow, ",", cellnbr, "]." )
            return
    print( "Did NOT find value:", qValue, "in the given matrix." )


def main():

    # get command line parameters
    parser = argparse.ArgumentParser()

    parser.add_argument('-m', action='store',
                        dest='matrix_string',
                        help='The string to be searched,')

    parser.add_argument('-n', action='store',
                        dest='queryValue',
                        help='The length of the substring for counting,')

    # --version
    parser.add_argument('--version', action='version',
                        version='%(prog)s 1.0')

    results = parser.parse_args()

    queryValue = int(results.queryValue)
    inputstr = results.matrix_string
    input_ary = inputstr.split(';')
    matrix = []
    for row_str in input_ary :
        row_int_ary = []
        row_ary = row_str.split(',')
        for row_elm in row_ary:
            row_int_ary.append(int(row_elm))
        #print( "Debug:",  row_ary )
        #print( "Debug:",  row_int_ary )
        matrix.append(row_int_ary)
    #print( "Debug:",  matrix )
    #print( "Debug:",  [ [1,2,3], [4,5,6], [7,8,9] ])
   
    #return

    #matrix = [ [1,2,3], [4,5,6], [7,8,9] ]
    findInMatrix( matrix, queryValue )
   
    # The BigO of the written solution is O(n).
    # More specifically, iteration over the rows in the matrix is O(n) and then when the specific row is found where the
    # query value would be if present, the one row is also iterated over which is O(n).
    # This would give O(n) + O(n) => O(2n) which amortizes to O(n).
   

main()

