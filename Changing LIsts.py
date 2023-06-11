# Changing lists-Ismail AlAdl-1.0

basket = ['Apple','Bun','Cola']
crate = ['Egg','Fig','Grape']

print('Basket List:',basket )
print('Basket Elements:' , len(basket))

basket.append('Damson')

print('Appended:', basket)
print('Lats Item Removed:',basket.pop() )
print('Basket LIst:', basket)

basket.extend( crate )
print( 'Extended:',basket)
del basket[1]
print( 'Itme Removed:',basket)
del basket[1:3]
print( 'Slice Removed:',basket)
