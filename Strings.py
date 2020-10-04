string = 'Hello world'

print(string.upper())
print(string.lower())
print(string.title())

print(string[-1])
print(string[0:4])
print(string[5:])
print(string[::2])
print(string[::-1])
print(len(string))
#split in array
string_list = string.split()
print(string_list)
print('*'.join(string_list))

print(f"'i' in 'hola' is {'i' in 'hola'}")
print(f"'i' in 'wien' is {'i' in 'wien'}")

print(f'isinstance(10, int) is {isinstance(10, int)}')
print(f'isinstance(10.0, int) is {isinstance(10.0, int)}')

print(f"'Welkomme'.isupper() is {'Welkomme'.isupper()}")
print(f"'Munchen092'.isalnum() is {'Munchen092'.isalnum()}")
print(f"'Munchen092'.isalpha() is {'Munchen092'.isalpha()}")

# Number int
print(f"'5.9'.isnumeric() is {'5.9'.isnumeric()}")
print(f"'3000'.isnumeric() is {'3000'.isnumeric()}")
