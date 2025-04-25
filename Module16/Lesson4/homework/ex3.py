goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
print('Текущий ассортимент:', goods)

fruit_name = input('Новый фрукт: ')
price = int(input('Цена: '))

goods.append([fruit_name, price])

for i_good in range(len(goods)):
    goods[i_good][1] += goods[i_good][1] * 8 / 100

print('Новый ассортимент с увел. ценой:', goods)
