# Speed, Distance, Time calculator-Ismail AlAdl-1.1

# Setting Varibles
D = 0
S = 0
T = 0

# Import library
from tkinter import *
import tkinter.messagebox as box

# Creating Window
window = Tk()
window.title( 'DST 1.1')

frame = Frame( window )
entry = Entry( frame )

def dialog():
    box.showinfo( ' Greetings','Welcome' + entry.get())

    
# Input

btn = Button( frame, text = 'Enter Speed', command=dialog)
btn = Button( frame, text = 'Enter Distance', command=dialog)
btn = Button( frame, text = 'Enter Time', command=dialog)



print( ' Input Distance (Miles) - if unknown input 0')
D = int(input ())
print( ' Input Speed (M/H) - if unknow input 0')
S = int(input ())
print( ' Input Time (Min)  - if unknow  input 0')
T = int(input ())

# Calculation
if D == 0:
    D = (T / 60) * S
   

if T == 0:
    T = D / S
   

if S == 0:
    S = D / (T / 60)
    


# Output
print ('\nDistance:\t' ,D, ' Miles')
print ('Time:      \t' ,T, 'Minutes')
print ('Speed:     \t' ,S, ' M/H')

