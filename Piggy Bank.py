# Piggy bank

needed = float(input("How much money do you need "))
piggybank= float(input("How much money do you have "))

if needed < piggybank:
    print(" We have enough")
else:
    print(" Sorry we need £", needed - piggybank)
