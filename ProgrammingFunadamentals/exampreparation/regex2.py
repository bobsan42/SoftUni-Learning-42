import re
# names = input()
names = 'Bethany Taylor, Oliver miller, sophia Johnson, SARah Wilson, John Smith, Sam	    Smith'

regex = "\\b[A-Z][a-z]+ [A-Z][a-z]+\\b"
matches = re.findall(regex, names)
print(", ".join(matches))
