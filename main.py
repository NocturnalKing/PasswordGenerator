import string, random
characters = string.ascii_letters + string.digits + "@*&#$%~!?+=-_)(^}{][\/.,|"
passLen = int(input('How many characters should your password be? '))
print(''.join([characters[random.randint(0,len(characters))] for i in range(passLen+1)])) 
