def recursive_function(i):
    if i == 100:
        return
    print("recursive~~")
    recursive_function(i+1)

def factorial(i):
    if i == 0:
        return 1
    return i * factorial(i-1)

print(factorial(5))
#recursive_function(0)