A= int(input("Enter the age of A"))
B= int(input("Enter the age of B"))
C= int(input("Enter the age of C"))
if A>B and B>C:
    print("A is oldest and C is youngest")
elif B>A and A>C:
    print("B is oldest and C is youngest")
elif C>A and A>B:
    print("C is oldest and B is youngest")
elif A>C and C>B:
    print("A is oldest and B is youngest")
elif B>C and C>A:
    print("B is oldest and A is youngest")
elif C>B and B>A:
    print("C is oldest and A is youngest")
elif A==B and B==C:
    print(" All are same age")
elif A==B and A>C:
    print(" A and B oldest and C is youngest")
elif B==C and B>A:
    print(" C and B oldest and A is youngest")
elif C==A and C>B:
    print(" A and C oldest and B is youngest")
elif A==B and A<C:
    print(" C oldest and A & B is youngest")
elif B==C and B<A:
    print(" A oldest and B&C is youngest")
elif C==A and C<B:
    print(" B oldest and A& B is youngest")
else:
    print("invalid")
