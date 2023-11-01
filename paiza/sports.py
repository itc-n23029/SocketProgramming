sport = input()

sports_dict = {
    'baseball': 9,
    'soccer': 11,
    'rugby': 15,
    'basketball': 5,
    'volleyball': 6
}

if sport in sports_dict:
    print(sports_dict[sport])
