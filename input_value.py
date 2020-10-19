def jatek():
    num = input("Irj be egy szamot: ")

    # ez csak kipróbálás volt: print("A szam amit kaptam: {}".format(num))

    try:
        test_num = int(num)
        test_num = test_num + 1
        print('\n {}, én nyertem'.format(test_num))
    except ValueError:
        print('ez nem szám')

# jatek()

nums = input('Irj be szamokat vesszovel elvalasztva!\n')
# itt a nums változó még string
print(nums)
# a strip függvény leszedi a string elejéről és végéről a
# megadott karaktert/karaktereket (jelen esetben a vesszőt)
nums = nums.strip(',')
print(nums)
# a split függvény a stringekből listát csinál, a vessző karakter
# lesz a delimiter (elválasztó)
# a nums változó mostantól nem string típusú, hanem lista (ha nem hiszed, írasd ki)
nums = nums.split(',')
print(nums)
print(type(nums))

# keressük meg a listában lévő legnagyobb értéket! (maximum)
# itt most nincs hibakezelés (el lehet rontani, ha vki nem számokat ír be
# vagy több vesszőt tesz közé)
max_index = 0
for i, num in enumerate(nums):
    if int(nums[i]) > int(nums[max_index]):
        max_index = i

print('A legnagyobb elem: {}'.format(nums[max_index]))
print('A legnagyobb elem helye: {}'.format(max_index))

