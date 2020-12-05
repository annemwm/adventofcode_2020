import re

# data setup
with open("input.txt", "r") as f:
    data = f.read()

data = [d for d in data.split("\n") if d]


# part 1
def validate_password_range(range_object, character, password):
    return password.count(character) in range_object


regex = re.compile(r'^(?P<RANGE_LOWER>\d+)-(?P<RANGE_UPPER>\d+) (?P<CHARACTER>[a-z]): '
                   r'(?P<PASSWORD>[a-z]+)\s*$', re.IGNORECASE)
total_valid = 0
for d in data:
    rule = regex.search(d)
    count = range(int(rule.group('RANGE_LOWER')), int(rule.group('RANGE_UPPER')) + 1)
    if validate_password_range(count, rule.group('CHARACTER'), rule.group('PASSWORD')):
        total_valid += 1

# print(total_valid)


# part 2
def validate_password_position(index1, index2, character, password):
    i = index1  # first index
    j = index2-1-index1
    possible_string = f'^[a-z]{{{i}}}{character}[a-z]{{{j}}}[^{character}]' \
                      f'|' \
                      f'^[a-z]{{{i}}}[^{character}][a-z]{{{j}}}{character}'
    possible_passwords = re.compile(possible_string, re.IGNORECASE)
    if possible_passwords.search(password) is not None:
        return True
    else:
        return False


total_valid = 0
for d in data:
    rule = regex.search(d)
    index1 = int(rule.group('RANGE_LOWER')) - 1
    index2 = int(rule.group('RANGE_UPPER')) - 1
    if validate_password_position(index1, index2, rule.group('CHARACTER'), rule.group('PASSWORD')):
        total_valid += 1

print(total_valid)
