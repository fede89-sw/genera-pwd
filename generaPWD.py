import random
import string

print("""
Questo programma genera una password.
Scegli tra password semplice (8 caratteri alfanumerici) 
o complessa(20 caratteri alfanumerici + ASCII)

- Semplice:     Premi 1
- Complessa :   Premi 2
""")
scelta=int(input(""))

def genera_pwd(scelta):
    lettere=string.ascii_letters # CONTIENE TUTTE LE LETTERE SIA MINUSCOLE CHE MAIUSCOLE
    numeri=string.digits # CONTIENE I NUMERI TRA 0 A 9
    speciali=string.punctuation # CONTIENE CARATTERI ASCII (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)
    if scelta == 1:
        tutti=lettere+numeri
        pwd="".join(random.sample(tutti,8))
        print("La password semplice creata è:",pwd)
    if scelta == 2:
        tutti=lettere+numeri+speciali
        pwd="".join(random.sample(tutti,20))
        print("La password complessa creata è:",pwd)

genera_pwd(scelta)
input("")