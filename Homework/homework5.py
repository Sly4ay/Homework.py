with open('trimushketera.txt', 'r', encoding='UTF8') as file:

    data = file.read().lower().replace('.', '').replace(',','')\
            .replace('!', '').replace('?', '').replace(';', '').replace('"', '').replace('*', '').replace('(', '')\
    .replace('-', '').replace(')', '').replace(':', '')
    words = data.split()
    unique = list(set(words))
    unique.sort() # сортируем в подярке возрастания

    with open('trimushketera_copy.txt', 'w', encoding='UTF8') as wfile:
       wfile.write(f'There are {len(words)} words. \n')
       wfile.write(f'There are {len(unique)} unique words. \n')

       for word in unique:
           wfile.write(word + '\n')