import re
d = {}
with open('lorem.txt') as lorem:
    for line in lorem:
        for word in re.sub(r'[^\w\s]','',line).lower().split():
            if word in d:
                d[word] += 1
            else:
                d[word] = 1

for w in sorted(d, key=d.get, reverse=True):
  print(w, d[w])