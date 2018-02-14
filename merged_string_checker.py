# At a job interview, you are challenged to write an algorithm to check if a given
# string, s, can be formed from two other strings, part1 and part2.
#
# The restriction is that the characters in part1 and part2 are in the same order as in s.
#
# The interviewer gives you the following example and tells you to figure out the
# rest from the given test cases.
#
# 'codewars' is a merge from 'cdw' and 'oears':
#
#     s:  c o d e w a r s   = codewars
# part1:  c   d   w         = cdw
# part2:    o   e   a r s   = oears

def is_merge(s, part1, part2):
    lst = list(s)
    p1 = list(part1)
    p2 = list(part2)
    for l1 in lst[::-1]:
        for l2 in p1[::-1]:
            if l1 == l2:
                lst.pop()
        if lst == p2:
            return True













if __name__ == '__main__':
    pass
