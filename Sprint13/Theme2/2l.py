#%%
def search(remain, stack, coins):
    if remain == 0:
        result.append(stack)
        return # Успех - мы подобрали комбинацию
    for i in range(len(coins)):
        if coins[i] > remain:
            return # Неудача - следующая монетка в комбинации больше суммы остатка цели
        if len(stack) == 0 or coins[i] >= stack[-1]:
            search(remain-coins[i], stack + [coins[i]], coins[i:])

    return  # Неудача - проверили все номиналы, но успешную комбирацию не нашли


def get_comb_coins(m_summ, coins):
    """Более изящное решение."""
    if m_summ == 0:
        return 1
    if m_summ < 0 or not coins:
        return 0
    return get_comb_coins(m_summ, coins[1:]) + get_comb_coins(m_summ-coins[0], coins)

#%%
if __name__ == "__main__":
    with open("input.txt") as f:
        m = int(f.readline())
        n = int(f.readline())
        coins = list(map(int, f.readline().split()))

    coins.sort()
    target = m
    result = []
    search(target, [], coins)
    print(len(result))

    print(get_comb_coins(m, coins))
    # with open("output.txt", "w") as f:
        # f.write(str(result))

# %%
