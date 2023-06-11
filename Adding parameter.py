# Adding parameters - I.Aladl - 1.0

def echo( user , lang , sys):
    print(' User:', user,'Langguage:',lang,'Platform:',sys)
echo('Mike' , 'Python' , 'Windows')
echo(lang='Python' , sys='Mac OS', user = 'Anne')
def mirror( user = 'Carole' , lang = 'Python'):
    print('\nUser:' , user ,'Language:" , lang)
mirror()
mirror( lang = 'Java')
mirror( user = ' Tony')
mirror(' Susan' , 'C++')
