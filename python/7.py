#Python Program to Convert Kilometers to Miles


kilometers = float(input("Enter value in kilometers: "))


conv_fac = 0.621371


miles = kilometers * conv_fac
print('%0.2f kilometers to %0.2f miles' %(kilometers,miles))
