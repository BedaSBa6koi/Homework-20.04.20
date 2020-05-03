appeal = input('Hello, select service office ')

dictionary = {
    'Kazakstan':'google_kazakstan.txt', 'Paris':'google_paris.txt', 'UAR':'google_uar.txt', 'Kyrgystan':'google_kyrgystan.txt',
    'San Francisco':'google_san_francisco.txt', 'Germany':'google_germany.txt', 'Moscow':'google_moscow.txt', 
    'Sweden':'google_sweden.txt'
}

extract = dictionary.get(appeal)

if appeal in dictionary:
    f = open(extract, 'w')
    f.write(input('Enter text '))
    f.close()