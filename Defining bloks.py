# Degfining block - I.Aladl - 1.0

global_var=1
def my_vars():
    print( 'Global Varible:' , global_var)
    laocal_var=2
    print('Local varible:' ,local_var)
    global inner_var
    inner_var=3
my_vars()
print( 'Coereced Global:' , inner_var)
