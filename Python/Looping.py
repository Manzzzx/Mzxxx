# x = 0
# y = 20

# for cuy in range(x,y + 1):
#     print(cuy)  <----- untuk looping 0 - 20

x = 0
y = 20

for cuy in range(x,y + 1):
    if cuy%2:
        print('ganjil: ' + str(cuy))
    else:
        print('genap: ' + str(cuy) + '\n') #<---------looping dengan memisahkan ganjil dan genap
