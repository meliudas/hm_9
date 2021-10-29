# a = [1, 2, 3, 4, 5]
#     b = 0
#     for i in a:
#         b = b + i
#         print(b)
#

# obshaya_summa_za_gody = 0
#
# def bank(a, years):
#     years = years + 1
#     for i in range(1, years):
#         obshaya_summa_za_god = a * 0,1 + a
#         a = obshaya_summa_za_god
#     return a
print("Введи в меня деньги")
a =float(input())

print("Сколько лет будешь хранить?")
years = int(input())

def bank(a, years):
    i=0
    while i<years:
        a=a+a*0.1
        i=i+1
    return a

if __name__ == '__main__':
    print(bank(a, years))

