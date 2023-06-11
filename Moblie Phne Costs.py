# Moblie Phone Costs - I.AlAdl - 1.0

# Data

name=input('Please input your name ')
mpn=input('Please input your moblie number ')
mins=int(input('Please input the number of minutes used this month '))
text=int(input('Please input the number of text used this month '))



# Operations

cmins = mins * 0.10
ctext = text * 0.05
#ctotal = round(float ((ctext + cmins)/ 100),2)
ctotal = ctext + cmins
ctotalvat = ctotal * 1.2


# Display

print('Customer name ', name)
print('Customers moblie number ',mpn)
print('Minutes used ',mins)
print('Cost of minutes ','£',cmins)
print('Number of texts ',text)
print('Cost of texts ','£',ctext)
print('Total cost without VAT ','£',ctotal)
print('Total cost with VAT ','£',ctotalvat)
