import re
pattern = "(\+359-2-[0-9]{3}-[0-9]{4}|\+359 2 [0-9]{3} [0-9]{4})\\b"
# text = input()
text = "+359 2 222 2222,359-2-222-2222, +359/2/222/2222, +359-2 222 2222 +359 2-222-2222, +359-2-222-222, +359-2-222-22222 +359-2-222-2222"
matches = re.findall(pattern, text)
print(", ".join(matches))
