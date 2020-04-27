score = input("Enter Score: ")

s=float(score)

if s<0.0 :

    print("error")

elif s>1.0 :

    print("error")

elif s>=0.9 :

	grade='A'

    print(grade)

elif s>=0.8 :

	grade='B'

    print(grade)

elif s>=0.7 :

	grade='C'

    print(grade)

elif s>=0.6 :

	grade='D'

    print(grade)

elif s<0.6 :

	grade='F'

    print(grade)

else :

    print("you had entered a wrong input")
