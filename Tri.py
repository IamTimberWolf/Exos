# consigne trier une liste d'entier dans l'ordre croissant

liste = [12, 21, 9, 15, 3, 32]

def tri(a):
    n = len(a)

    for i in range(n):
        for j in range(0,n-i-1):
            if a[j] >= a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

tri(liste)
print(liste)