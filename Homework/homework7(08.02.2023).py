import re

# HASH colors (#FFFFFF)

sample = '#1239AF'
pattern = re.compile(r'#[0-9A-F]{6}', re.IGNORECASE)

matches = pattern.finditer(sample)

for match in matches:
    print(match)

# NUMBERS


sample1 = '345-12312+123123+12312-21312*2133-123 123123 21312'
pattern1 = re.compile(r'(\d+)[^+\d]|(\d+$)', re.IGNORECASE)

matches1 = pattern1.finditer(sample1)

for match1 in matches1:
    print(match1.group(1) or match1.group(2))
print()
print()
# TIME


sample2 = '14:20, 30:13, 13:90, 123:23, 21:213, 123:123, 43:32'
pattern2 = re.compile(r'\b([01][0-9]|2[0-3]):([0-5][0-9])\b')
matches2 = pattern2.finditer(sample2)

for match2 in matches2:
    print(match2)
print()
print()
# People

with open('people.txt', 'r', encoding='UTF8') as file:
    data = file.read()

name_pattern = re.compile(r'[A-Za-z]+ [A-Za-z]+\n')
address_pattern = re.compile(r'\d{3} [0-9A-Za-z]+ St.\., [A-Za-z\' -]+ [A-Z]{2} \d{5}')
matches3 = name_pattern.findall(data)

print(len(matches3))

matches3 = address_pattern.findall(data)
for match3 in matches3:
    print(match3)

print()
print()

#A-Za-z0-9

sample4 = 'aasdasd213123ASDASDasd'

pattern4 = re.compile(r'[^A-Za-z0-9]')
matches4 = pattern.findall(sample4)

if matches4:
    print(False)
else:
    print(True)

if not matches4:
    print(True)
else:
    print(False)


print()
print()


# ISIKUKOOD
sample = '38803160272'
pattern5 = re.compile(r'[1-8][0-9]{2}(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])\d{4}')
matches5 = pattern5.finditer(sample)

for match5 in matches5:
    print(match5)