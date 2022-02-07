h_letters = []

for letter in 'human':
    h_letters.append(letter)

print(h_letters)
h_letters2 = [ letter for letter in 'human' ]
print( h_letters2)

letters = list(map(lambda x: x, 'human'))
print(letters)
