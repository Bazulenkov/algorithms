#%%
def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 1
    return True 

def get_smaller_primes(n):
    smaller_primes = []
    num = 2
    while len(smaller_primes) < n:
        if is_prime(num):
            smaller_primes.append(num)
        num += 1
    return smaller_primes 

def hash_keys(array_of_strings):
    s = set()
    for string in array_of_strings:
        for c in string:
            s.add(c)
    
    len_s = len(s)
    smaller_primes = get_smaller_primes(len_s)
    
    return {s.pop(): smaller_primes[i] for i in range(len_s)}

def anagrams_group(keys):
    d = hash_keys(keys)
    ord_arr = []
    for key in keys:
        composition = 1
        for c in key:
            composition *=  d[c]
        ord_arr.append(composition)
    
    for i in range(len(ord_arr)):
        if ord_arr[i]:
            temp = []
            item = ord_arr[i]
            for j in range(i, len(ord_arr)):
                if item == ord_arr[j]:
                    temp.append(j)
                    ord_arr[j] = None
            print(*temp)

if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        array_of_strings = f.readline().split()

    anagrams_group(array_of_strings)
# %%
