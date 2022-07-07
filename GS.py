g = 10
m = int(input('zadaj hmotnosť predmetu v kg:'))
def gravitacna_sila(m):
    F = m * g
    return F

print(f'Veľkosť gravitačnej sily pri hmotnosti telesa {m} kg je {gravitacna_sila(m)} N')