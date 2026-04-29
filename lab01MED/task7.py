def run():
    # Работа со списком
    songs_list = [
        ['World in My Eyes', 4.86],
        ['Sweetest Perfection', 4.43],
        ['Personal Jesus', 4.56],
        ['Halo', 4.9],
        ['Waiting for the Night', 6.07],
        ['Enjoy the Silence', 4.20],
        ['Policy of Truth', 4.76],
        ['Blue Dress', 4.29],
        ['Clean', 5.83],
    ]
    
    time = 0
    for song in songs_list:
        if song[0] == 'Halo' or song[0] == 'Enjoy the Silence' or song[0] == 'Clean':
            time += song[1]
    print("Три песни звучат", round(time, 2), "минут")
    
    # Работа со словарём
    songs_dict = {
        'World in My Eyes': 4.76,
        'Sweetest Perfection': 4.43,
        'Personal Jesus': 4.56,
        'Halo': 4.30,
        'Waiting for the Night': 6.07,
        'Enjoy the Silence': 4.6,
        'Policy of Truth': 4.88,
        'Blue Dress': 4.18,
        'Clean': 5.68,
    }
    
    time = 0
    time_all = 0
    for song in songs_dict:
        if song == 'Sweetest Perfection' or song == 'Policy of Truth' or song == 'Blue Dress':
            time += songs_dict[song]
        time_all += songs_dict[song]
    
    print('Три песни звучат', round(time, 2), 'минут')
    print('Остальные песни звучат', round(time_all - time, 2), 'минут')

