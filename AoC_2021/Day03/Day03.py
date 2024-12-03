# # #  Solutions of Advent of Code
# # #  Oliver Kleemann

from aoc_helper import *

year, day = "2021", "03"

def solve():
    binaries = load_input().split('\n')
    binaries_orignal = binaries[:]

    gamma = epsilon = ""

    bits = len(binaries[0])
    lines_count = len(binaries)
    results = [0] * bits

    # count "1" in each column
    for binary in binaries:
        for i in range(bits):
            if binary[i] == "1":
                results[i] += 1

    # determine the most and less common used bits in each column
    for result in results:
        if result > int(lines_count / 2):
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    result_a = int(gamma, 2) * int(epsilon, 2)

    ### Part 2
    for i in range(bits):
        # get most common bit
        result = [binary for binary in binaries if binary[i] == "1"]
        count_ones = len(result)

        if count_ones >= len(binaries) / 2:
            binaries = result
        else:
            binaries = [binary for binary in binaries if binary[i] == "0"]

    o_g_r = int(binaries[0], 2)


    binaries = binaries_orignal[:]
    for i in range(bits):
        # get most common bit
        result = [binary for binary in binaries if binary[i] == "0"]
        count_zeroes = len(result)

        if len(binaries) == 1:
            break
        if count_zeroes <= len(binaries) / 2:
            binaries = result
        else:
            binaries = [binary for binary in binaries if binary[i] == "1"]

    co2_s_r = int(binaries[0], 2)

    result_b = o_g_r * co2_s_r

    return result_a, result_b


### ----------- Start ------------- ###

run_puzzle(day, year, solve)
