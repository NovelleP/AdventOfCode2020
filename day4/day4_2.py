import re


def is_passport_valid(passport, required_fields, validator):
    return (required_fields - set(validator.findall(passport))) == set()


if __name__ == '__main__':
    with open('input', 'r') as f:
        passports = [line.replace('\n', ' ').strip() for line in f.read().split('\n\n')]

    required_field_to_validator = {
        'byr': '(?:(?:(?:19[2-9][0-9])|(?:200[0-2]))(?: |$))',
        'iyr': '(?:(?:(?:201[0-9])|(?:2020))(?: |$))',
        'eyr': '(?:(?:(?:202[0-9])|(?:2030))(?: |$))',
        'hgt': '(?:(?:(?:(?:(?:1[5-8][0-9])|(?:19[0-3]))cm)|(?:(?:(?:59)|(?:6[0-9])|(?:7[0-6]))in))(?: |$))',
        'hcl': '(?:#[0-9a-f]{6}(?: |$))',
        'ecl': '(?:(?:(?:amb)|(?:blu)|(?:brn)|(?:gry)|(?:grn)|(?:hzl)|(?:oth))(?: |$))',
        'pid': '(?:[0-9]{9}(?: |$))'
    }

    validator = re.compile('|'.join(f'(?:(?:(?<=^)|(?<= )){field}(?=:{validator}))'
                                    for field, validator in required_field_to_validator.items()))
    print(sum(is_passport_valid(passport, set(required_field_to_validator.keys()), validator) for passport in passports))
