pack = []
decode = []
bad_packs = 0

pack_amt = int(input('Кол-во пакетов: '))
for i_pack in range(1, pack_amt + 1):
    print('\nПакет номер', i_pack)
    for i_bit in range(1, 5):
        print(f'{i_bit} бит: ', end = '')
        num = int(input())
        pack.append(num)
    if pack.count(-1) <= 1:
        decode.extend(pack)
    else:
        print('Много ошибок в пакете.')
        bad_packs += 1
    pack = []

print('\nПолученное сообщение:', decode)
print('Кол-во ошибок в сообщении:', decode.count(-1))
print('Кол-во потерянных пакетов:', bad_packs)
