with open("data/08.txt") as f:
    raw = f.read().splitlines()

messages = [line.split(' | ') for line in raw]
inputs = [line[0].split() for line in messages]
outputs = [line[1].split() for line in messages]

# digits 1, 4, 7, 8 have respectively unique length of 2, 4, 3, 7
# so we can easily count them
res1 = sum(len(x) in [2, 3, 4, 7] for line in outputs for x in line)
print("#1:", res1)

# sort letters
inputs = [[''.join(sorted(digit)) for digit in line] for line in inputs]
outputs = [[''.join(sorted(digit)) for digit in line] for line in outputs]


def standard_decode(digits):
    """
    standard:
     aaa
    b   c
    b   c
     ddd
    e   f
    e   f
     ggg
    """
    d = {
        "abcefg": "0", "cf": "1", "acdeg": "2", "acdfg": "3", "bcdf": "4",
        "abdfg": "5", "abdefg": "6", "acf": "7", "abcdefg": "8", "abcdfg": "9",
    }
    return int("".join(d[pattern] for pattern in digits))


def translate(digit_pattern, match_dict):
    translated = [match_dict[letter] for letter in digit_pattern]
    translated_sorted_str = "".join(sorted(translated))
    return translated_sorted_str


def translated_decode(digits, match_dict):
    new_digits = [translate(digit_pattern, match_dict) for digit_pattern in digits]
    return standard_decode(new_digits)


def find_matches(ten_digits):
    lengths = [2, 3, 4, 5, 6, 7]
    patterns_by_length = {length: [] for length in lengths}
    for digit_pattern in ten_digits:
        patterns_by_length[len(digit_pattern)].append(digit_pattern)
    for n in [2, 3, 4, 7]:
        patterns_by_length[n] = patterns_by_length[n][0]

    letters = "abcdefg"
    letter_matches = {letter: [] for letter in letters}
    known_letters = []

    # find a using 1 and 7 and f candidate
    for letter in patterns_by_length[3]:
        if letter not in patterns_by_length[2]:
            letter_matches["a"] = letter
            known_letters.append(letter)
        else:
            # letter_matches["c"].append(letter)
            letter_matches["f"].append(letter)
    assert len(known_letters) == 1, f" known: {known_letters}, match {letter_matches}"

    # find c,d,e candidates using 0,6,9 and 8
    for letter in patterns_by_length[7]:
        for pattern in patterns_by_length[6]:
            if letter not in pattern:
                letter_matches["c"].append(letter)
                letter_matches["d"].append(letter)
                letter_matches["e"].append(letter)

    # deduct f and c
    c, f = "", ""
    for letter in letter_matches["f"]:
        if letter in letter_matches["c"]:
            c = letter
        else:
            f = letter
    letter_matches["c"] = c
    letter_matches["f"] = f
    known_letters.append(c)
    known_letters.append(f)
    assert len(known_letters) == 3, f" known: {known_letters}, match {letter_matches}"

    # remove c from d, e candidates
    letter_matches["d"].remove(c)
    letter_matches["e"].remove(c)

    # find b and d using 4, and deduct e
    for letter in patterns_by_length[4]:
        if letter not in known_letters:
            if letter in letter_matches["d"]:
                letter_matches["d"] = letter
                known_letters.append(letter)
                letter_matches["e"].remove(letter)
                letter_matches["e"] = letter_matches["e"][0]
                known_letters.append(letter_matches["e"])
            else:
                letter_matches["b"] = letter
                known_letters.append(letter)
    assert len(known_letters) == 6, f" known: {known_letters}, match {letter_matches}"

    # find g using any of 9, 6, 0
    for letter in patterns_by_length[6][0]:
        if letter not in known_letters:
            letter_matches["g"] = letter
            known_letters.append(letter)
    assert len(known_letters) == 7, f" known: {known_letters}, match {letter_matches}"

    # revert matching
    return {v: k for k, v in letter_matches.items()}


res2 = sum(translated_decode(digits, find_matches(ten_digits)) for ten_digits, digits in zip(inputs, outputs))
print("#2:", res2)


def test_08():
    assert res1 == 367
    assert res2 == 974512
