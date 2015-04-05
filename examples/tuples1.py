mytuple=("ahmet","veli",23,45)
print( type(mytuple) )

# Output : 
# < class 'tuple'>

########################################
# Parantez kullanmadan da bir tuple tanimlayabiliriz.
mytuple2 = "ahmet","veli",23,45

########################################
# tuple() fonksiyonunu kullanarak da bir tuple elde edebiliriz.

# tuple fonksiyonuna string argument vererek : 
print( tuple("abcdefghij") )
# Output :
# ('a', 'b', 'c', 'd', 'e', 'f', 'g','h')

# tuple fonksiyonuna list argument vererek : 
tuple(["ahmet","veli",23,45])
# Output :
# ('a', 'b', 'c', 'd', 'e', 'f', 'g','h')

########################################
my_string = 'A'  # string
my_list = ['Ahmet'] # list
mytuple = ('Ahmet',) # tuple  # bu ikisini karistirma
my_string = ('Ahmet') # string # bu ikisini karistirma

########################################
my_tuple = ('elma','armut','erik')
print( mytuple[0] )  # elma
print( mytuple[-1] ) # erik
print( mytuple[:2] ) # ('elma','armut')

########################################
# tuple'lar immutable'dir, yani degistirilemez, modify edilemez.
mytuple = ('elma','armut','erik')
mytuple[0] = 'karpuz'
# ERROR occurs because of attempting to modify immutable variable.

########################################
# iki demeti birlestirmek icin, ayni demet'i tekrar tanimlayabiliriz.
demet = ('ahmet','mehmet')
demet = demet + ('selin',)  # virgul'u sakin unutma.

########################################
# Sadece ayni tur veriler birlestirilebilir : 
demet = demet + 'selin'
#  ERROR!!!

demet = demet + ('selin') 
#  ERROR!!!

########################################
# Bir demeti tekrar tanimlayarak, sanki o demet uzerinde degisiklik yapmis
# etkisi elde edebiliriz. Ama veriler uzerinde sureklii degisiklik yapacaksak
# listeleri tercih etmeliyiz

# Listeler ve tuple'larin farki nedir?
# List : mutable(modifiable)
# Tuple : immutable(immodifiable)
# Tuple'lar uzerinde islem yapmak, listelerden daha hizlidir.

########################################
# Programlarin ayar(config) dosyalarinda, yaygin olarak kullanilan veri tipi
# tuple'lardir. Ornegin Python tabanli bir framework olan Django'nun
# settings.py isimli ayar dosyasinda, pek cok deger bir tuple olarak saklanir.
# Mesela bir Django projesinde, web sayfalarinin template'lerini hangi dizin
# altinda saklayacagimizi su ayar belirler :

# TEMPLATE_DIRS = ('/home/projects/djprojects/blog/templates',)

# Burada, TEMPLATE dosyalarinin hangi dizinde yer alacagini bir demet icinde 
# gosteriyoruz. Bu demet icine birden fazla dizin adi yazabilirdik, hala da yazabiliriz.
# Ama biz tum TEMPLATE dosyalarini tek bir dizin altinda tutmayi tercih ettigimiz icin
# tek elemanli bir demet tanimlamisiz. Bu arada, daha once de soyledigimiz gibi,
# demetlerle ilgili en sik yapacaginiz hata, tek elemanli bir demet tanimlamaya
# calisirken aslinda yanlislikla, bir karakter dizisi tanimlamak olacaktir.
# Ornegin yukaridaki TEMPLATE_DIRS degiskenini soyle yazsaydik:

# TEMPLATE_DIRS = ('/home/projects/djprojects/blog/templates')

# Aslinda bir demet degil, alelade bir karakter dizisi tanimlamis olurduk...