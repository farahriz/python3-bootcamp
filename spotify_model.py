playlist = {
    "title": "Bus Ride",
    "author": "Amanda",
    "songs": [
        {"title": "Kill This Love", "artist": "BLACKPINK", "duration": 2.5},
        {"title": "Boy with Luv", "artist": "BTS feat. Halsey", "duration": 4},
        {"title": "Way Back Home", "artist": "Shaun", "duration": 3.25},
    ]
}

total_length = 0
for song in playlist['songs']:
    total_length += song['duration']

print(str(total_length)+"minutes of playtime")