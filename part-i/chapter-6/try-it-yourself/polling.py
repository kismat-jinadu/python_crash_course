favourite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
participants=['kate','jen','sarah','edward','chris', 'jake','phil','tony']
for name in participants:
    if name in favourite_languages.keys():
        print(f"Hi {name.title()}.")
        print(f"\tThank you for responding.")
    if name not in favourite_languages.keys():
        print(f"Hi {name.title()}.")
        print(f"\tPlease take the poll.")
