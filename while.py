numero_del_usuario = int(input("deci un numero del 1 al 10 ameo"))
numero_a_adivinar = 11
wea = 1
while numero_del_usuario != numero_a_adivinar and wea != 5:
    numero_del_usuario = int(input("trata devuelta intento #" + str(wea)))
    wea = wea + 1
if numero_a_adivinar == numero_del_usuario:
    print("le pegaste ameo")

if wea == 5:
    print("sos terrible pelotudo")