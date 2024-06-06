import qrcode
import random
num = random.randint(1000,9999)
file = input("Enter the url or Any message : ")
gen = qrcode.make(file)
gen.save("qrimg"+str(num)+".jpg")
