from hashlib import sha256

x = 5
y = 0

# Keep incrementing until the last 4 digits ends with a 0000.. which would yield 5 * 54455
while sha256(f'{x*y}'.encode()).hexdigest()[:5] != "00000":
    y += 1


def create_hash(x, y):
    return sha256(f'{x*y}'.encode()).hexdigest()


print (f'The solution for y = {y} and hash is:  {create_hash(x, y)}')


