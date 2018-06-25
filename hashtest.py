from hashlib import sha256

x = 5
y = 0

# Keep incrementing until the last digit ends with a 0.. which would yield 5 * 21
while sha256(f'{x*y}'.encode()).hexdigest()[-1] != "0":
    y += 1


def create_hash(x, y):
    return sha256(f'{x*y}'.encode()).hexdigest()


print (f'The solution for y = {y} and hash is:  {create_hash(x, y)}')


