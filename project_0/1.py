from collections import OrderedDict

def check(temps):
    temps.sort(key=lambda x: x[1], reverse=True)
    od = OrderedDict(temps)
    od = str(od)
    print(od)

temps = [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5)]

print(check(temps))

def check2(temps):
    temps.sort(key=lambda x: x[1], reverse=False)
    od = OrderedDict(temps)
    od = str(od)
    print(od)


print(check2(temps))