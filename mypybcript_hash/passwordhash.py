import bcrypt

password = b'secretpassword55'
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password, salt)

print(f'{"plain text password:" : >25} {password}')
print(f'{"salt:" : >25} {salt}')
print(f'{"hashed password:" : >25} {hashed}')

print(f'{"in memory password match:" : >25} {bcrypt.checkpw(password, hashed)}')

# ************************************************************************************
incorrectLoginPassword = b'testing001'
loginPassword = b'secretpassword55'

savedHash =  b'$2b$12$vUeu8Z1RmxWNKALv6vtAauKMUxU.9w7QhSSPjX7s0OdHvY16yL0Hu'
print(f'{"persisted password match:" : >25} {bcrypt.checkpw(incorrectLoginPassword, savedHash)}')

secondHash = b'$2b$12$F8x.zvqS/Kh6TqevzF02K.VL5usI1TvufML6Ucg1k.8JIruju6Drq'
print(f'{"persisted password match:" : >25} {bcrypt.checkpw(loginPassword, secondHash)}')
# ************************************************************************************

