names = ["Arya", "Samson", "Dora", "Tim", "Ollivander"]

#min(len(name)) for name in names)

print ( max(names) )
print (max(len(name) for name in names))
print ( max(names, key=lambda n:len(n)) )

songs = [
  {"title": "happy birthday", "playcount": 1},
  {"title": "Old Town Road", "playcount": 99},
  {"title": "YMCA", "playcount": 502},
  {"title": "Toxic", "playcount": 30},
]

print (min(songs, key=lambda s: s['playcount']))
print (max(songs, key=lambda s: s['playcount']))

print (min(songs, key=lambda s: s['playcount'])['title'])
print (max(songs, key=lambda s: s['playcount'])['title'])