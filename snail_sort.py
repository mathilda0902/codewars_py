# Given an n x n array, return the array elements arranged from outermost elements
# to the middle element, traveling clockwise.
#
# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# For better understanding, please follow the numbers of the next array consecutively:
#
# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]
#
# warning: The idea is not sort the elements from the lowest value to the highest;
# the idea is to traverse the 2-d array in a clockwise snailshell pattern.
# The 0x0 (empty matrix) is represented as [[]]


def snail(array):
    d = np.array(array)
    output = []
    while d.size != 0:
        output.extend(d[0])
        d = np.delete(d, 0, 0)
        d = np.rot90(d)
    return output
