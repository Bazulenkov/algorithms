#%%
def happy_ticket(n: str, input=set()):
    input.add(n)
    s = sum([int(digit)**2 for digit in n])
    if s == 1:
        return True
    if str(s) in input:
        return False
    
    return happy_ticket(str(s), input)


if __name__ == "__main__":
    num = input()

    print(happy_ticket(num))
# %%
