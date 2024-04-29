def find_permutation(str, pattern):

    curr_str = ""

    for end in range(len(str)):
        curr_str = curr_str + str[end]

        if len(curr_str) == len(pattern):
            if sorted(curr_str) == sorted(pattern):
                return True
            else:
                curr_str = curr_str[1:]

    return False

print(find_permutation("aaacb", "abc"))