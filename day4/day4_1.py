import re


def is_passport_valid(passport, required_fields, validator):
    return (required_fields - set(validator.findall(passport))) == set()


if __name__ == '__main__':
    with open('input', 'r') as f:
        passports = [line.replace('\n', ' ').strip() for line in f.read().split('\n\n')]

    required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    validator = re.compile('|'.join(f'(?<=^|(?<= )){field}(?=:)' for field in required_fields))
    print(sum(is_passport_valid(passport, required_fields, validator) for passport in passports))
