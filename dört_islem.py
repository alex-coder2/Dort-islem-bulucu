print("Yapmak istediğiniz işlemi seçiniz(toplama/çıkartma/çarpma/bölme):")
cvp = input()
if cvp == "toplama":
    while True:
     print("İlk sayıyı giriniz")
     y = int(input())
     print("İkinci sayıyı giriniz")
     x = int(input())
     z = str(y + x)
     print("Cevabınız: " + z)
     
elif cvp == "çıkartma":
    while True:
     print("İlk sayıyı giriniz")
     y = int(input())
     print("İkinci sayıyı giriniz")
     x = int(input())
     z = str(y - x)
     print("Cevabınız: " + z)     
     
elif cvp == "çarpma":
    while True:
     print("İlk sayıyı giriniz")
     y = int(input())
     print("İkinci sayıyı giriniz")
     x = int(input())
     z = str(y * x)
     print("Cevabınız: " + z)  
     
elif cvp == "bölme":
    while True:
     print("İlk sayıyı giriniz")
     y = int(input())
     print("İkinci sayıyı giriniz")
     x = int(input())
     z = str(y / x)
     print("Cevabınız: " + z)      
     
else:
    print("Geçersiz işlem")      