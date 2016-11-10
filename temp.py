def FC(a):
    b = a*9/5 + 32
    return b
def CF(a):
    b = 5*(a-32)/9
    return b
op = int(raw_input('Entre com 1 se que Fahrenheit para Celsius ou 2 se quiser Celsius para Fahrenheit:'))
temp = int(raw_input('Entre com a temperatura:'))
if op == 1:
    print FC(temp)
elif op ==2:
    print CF(temp)
