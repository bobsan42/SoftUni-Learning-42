import re
pattern = "\\b(?P<day>\\d{2})([-.\\/])(?P<month>[A-Z][a-z]{2})\\2(?P<year>\\d{4})\\b"
# text = input()
text="13/Jul/1928, 10-Nov-1934, 25.Dec.1937"
matches = re.finditer(pattern, text)
for match in matches:
    print(f"Day: {match.group('day')}, Month: {match.group('month')}, Year: {match.group('year')}")
