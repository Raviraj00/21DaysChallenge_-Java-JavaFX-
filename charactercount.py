import pprint
message = 'It was a bright cold day in August, and the clock was ticking 7pm'
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)