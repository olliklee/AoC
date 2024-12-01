import re

def parse(text):
    sections = text.split("\n\n")
    seeds, maps = [int(n) for n in re.findall(r"\d+", sections[0])], []
    for section in sections[1:]:
        maps.append([])
        for l in section.split("\n")[1:]:
            maps[-1].append(tuple(int(i) for i in l.split()))
    return seeds, maps

# ir = "initial range" for this recursive (start, end) tuple where end is inclusive
# maps = list of mappings still to be processed
def best(initial_rng, maps):
    # if we've done the final mapping, just return the lowest value
    if not maps:
        return initial_rng[0]

    for dest, start, rng in maps[0]:
        # range is entirely inside a mapping
        print(".", end="")
        if start <= initial_rng[0] < start + rng and start <= initial_rng[1] < start + rng:
            r1 = (dest + initial_rng[0] - start, dest + initial_rng[1] - start)
            return best(r1, maps[1:])

        # range starts inside a mapping but ends outside
        elif start <= initial_rng[0] < start + rng and start + rng < initial_rng[1]:
            r1 = (dest + initial_rng[0] - start, dest + rng)
            r2 = (start + rng, initial_rng[1])
            return min(best(r1, maps[1:]), best(r2, maps))

        # range starts below a mapping but ends inside mapping
        elif initial_rng[0] < start and start <= initial_rng[1] < start + rng:
            r1 = (initial_rng[0], start - 1)
            r2 = (dest, dest + initial_rng[1] - start)
            return min(best(r1, maps), best(r2, maps[1:]))

        # range begins below and ends above a mapping
        elif initial_rng[0] < start and initial_rng[1] > start + rng:
            r1 = (initial_rng[0], start - 1)
            r2 = (dest, dest + rng)
            r3 = (start + rng, initial_rng[1])
            return min(best(r1, maps), best(r2, maps[1:]), best(r3, maps))

    # No maps matched this range. Preserve values and move on.
    return best(initial_rng, maps[1:])

# seeds, maps = parse(open("Day05_input_.txt").read())
seeds, maps = parse(open("Day05_input.txt").read())

# part 1, just create a "range" for each seed. It works out the same
sol1 = [(i, i) for i in seeds]
print(min((best(ir, maps) for ir in sol1)))

# part 2, note the -1 for the second number since we use inclusive ranges
sol2 = [(seeds[2 * i], seeds[2 * i] + seeds[2 * i + 1] - 1) for i in range(len(seeds) // 2)]
print(min((best(ir, maps) for ir in sol2)))
