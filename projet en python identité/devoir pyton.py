#le programme demande de taper les dates de naissance 
date_naissancex=int(input("saisir l'année de naissance de Modou: "))
date_naissancey=int(input("saisir l'année de naissance de Badara: "))
age=2022 - date_naissancex
#le programme vous donne leurs ages
print("Moudou est agé de:",age)
if age<18:
#le programme vous dit si ils sont majeurs ou mineurs et si ils peuvent etre electeurs
    print("Modou vous etes mineur vous ne pouvez pas etre electeur")
elif age==18:
    print("Modou vous etes majeur vous  pouvez etre electeur")
elif age>18:
    print("Modou vous etes majeur vous  pouvez  etre electeur")
age=2022 - date_naissancey
print("Badara est agé de:",age)
if age<18:
     print("Badara vous etes mineur vous ne pouvez pas etre electeur")
elif age==18:
     print("Badara vous etes majeur vous  pouvez etre electeur")
elif age>18:
     print("Badara vous etes majeur vous  pouvez  etre electeur")
#le programme vous dit qu'ils sont des jumaux si ils ont la même date de naissance   
if date_naissancex==date_naissancey:
     print("Modou et Badara sont des jumaux")
elif date_naissancex>date_naissancey:
     print("Modou est le petit frere de Badara")
elif date_naissancex<date_naissancey:
     print("Modou est le grand frere de Badara")
else:
    print("quitter le programme")    

