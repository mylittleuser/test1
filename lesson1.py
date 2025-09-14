import random
vac_password = '+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
len_password = input("Введите длину пароля: ")
user_password= ""

for a in range(1, int(len_password)+1):
   
   user_password = user_password+vac_password[random.randint(0, len(vac_password)-1)]
print("Сгенерированный пароль:", user_password)
