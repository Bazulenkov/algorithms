#%%
with open('input.txt') as f:
    days = f.readline().rstrip()
    stock = f.readline().split()
stock = list(map(int, stock))
# %%
stock.append(0)
share = False
wallet = 0
for i in range(len(stock)-1):
    if stock[i] > stock[i+1] and share == True: # Если цена сегодня больше, чем завтра, то продаем
        wallet += stock[i]
        share = False
    elif stock[i] < stock[i+1] and share == False: # Если цена сегодня меньше, чем завтра, то покупать
        wallet -= stock[i]
        share = True
print(wallet)

# %%
