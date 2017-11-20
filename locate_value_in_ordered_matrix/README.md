# Locate Value in Ordered Matrix - 

Find the location of a given value in an ordered number matrix of size n x m.
An ordered number matrix for this problem is defined as each row ordered in the matrix having it's elementes ordered from lowest to highest, with the lowest value being in column 0.  For a given matrix of size N x M, the value in column N for each row m is less than the value in column 0 row m+1.
  Example:
```
1  2  3
4  5  6
7  8  9
```
It is assummed the values in the matrix are unique (no duplicates).

The solution should have a less than O(n^2) runtime.
Explain the solutions Big-O complexity and why.

This was given to me as an interview question on Nov 14, 2017.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

argparse - for cli arguments
Otherwise, it is a stand alone program.

### Installing

Get a copy of the coding_interview_solutions repository.

```
git clone https://github.com/king-md/coding_interview_solutions.git
```

Copy the locate_value_in_ordered_matrix.py program to the directory where you want to run it from.

```
Windows: copy src\coding_interview_solutions\locate_value_in_ordered_matrix.py C:\DESTINATION

Linux: cp -p src/coding_interview_solutions/locate_value_in_ordered_matrix.py /home/user/bin/.
```


## Test Cases

input matrix
```
1  2  3
4  5  6
7  8  9
```
input substring size "4"
expected result: (1,0)
```
./locate_value_in_ordered_matrix.py -n 4 -m '1, 2, 3; 4, 5, 6; 7, 8, 9'
```

input matrix
```
1  2  3
4  5  6
7  8  9
```
input substring size "8"
expected result: (2,1)
```
./locate_value_in_ordered_matrix.py -n 8 -m '1, 2, 3; 4, 5, 6; 7, 8, 9'
```

input matrix
```
1  2  3
4  5  6
7  8  9
```
input substring size "3"
expected result: (0,2)
```
./locate_value_in_ordered_matrix.py -n 3 -m '1, 2, 3; 4, 5, 6; 7, 8, 9'
```

input matrix
```
1  2  3
4  5  6
7  8  9
```
input substring size "10"
expected result: ()
```
./locate_value_in_ordered_matrix.py -n 10 -m '1, 2, 3; 4, 5, 6; 7, 8, 9'
```

input matrix
```
1  2  3
4  5  6
7  8  9
```
input substring size "0"
expected result: ()
```
./locate_value_in_ordered_matrix.py -n 0 -m '1, 2, 3; 4, 5, 6; 7, 8, 9'
```

input matrix
```
1  2  3
4  5  6
7  8  9
```
input substring size "-1"
expected result: ()
```
./locate_value_in_ordered_matrix.py -n -1 -m '1, 2, 3; 4, 5, 6; 7, 8, 9'
```

## Contributing

Not available at this time.

## Versioning

Not available at this time.

## Authors

* **Michael King** - *Initial work* - 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

Not available at this time.

