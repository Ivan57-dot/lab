def run():
    fam_h = [
        ['сестра', 140],
        ['брат', 155],
        ['я', 174],
        ['мама', 170],
        ['отец', 180]
    ]
    
    for member in fam_h:
        if member[0] == 'отец':
            print("Рост отца -", member[1], "см")
    
    count = 0
    for member in fam_h:
        count += member[1]
    print("Общий рост моей семьи -", count, "см")
