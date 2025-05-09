# Sprint 3a
#1) x dəyişəni verilmişdir. Əgər x > 0 olarsa "müsbət", x < 0 olarsa "mənfi", bərabərdirsə "sıfır" çap etsin.
x = int(input("x: "))
if x > 0:
    print("musbet")
elif x < 0:
    print("menfi")
else:
    print("sifir")
#2) n rəqəmi cütdürsə "cüt", təkdirsə "tək" çap etsin.
n = int(input("n: "))
if n % 2 == 0:
    print("cut")
else:
    print("tek")
#3) a, b, c rəqəmləri verilmişdir. Ən böyük rəqəmi çap etsin.
a, b, c = 5, 10, 8
print("en boyuk:", max(a, b, c))
#4) day dəyişəni 1-7 arası rəqəmdir. Müvafiq həftə gününü (1 = "Bazar ertəsi", ..., 7 = "Bazar") çap etsin, əks halda "Yanlış gün" yazsın.
day = int(input("gun: "))
if day == 1:
    print("bazar ertesi")
elif day == 2:
    print("cersenbe axsami")
elif day == 3:
    print("cersenbe")
elif day == 4:
    print("cume axsami")
elif day == 5:
    print("cume")
elif day == 6:
    print("senbe")
elif day == 7:
    print("bazar")
else:
    print("sehv gun")
#5) temp dəyişəni temperaturdur. Əgər temp < 0 olarsa "soyuq", 0-20 arası olarsa "normal", 20-dən böyükdürsə "isti" çap etsin.
temp = int(input("Temperatur: "))
if temp < 0:
    print("soyuq")
elif temp >= 0 and temp <= 20:
    print("normal")
else:
    print("isti")
#6) password adlı string verilmişdir. Əgər uzunluğu 8-dən kiçikdirsə "qısa", 8-12 arasıdırsa "orta", 12-dən böyükdürsə "uzun" çap etsin.
password = input("kod: ")
if len(password) < 8:
    print("qısa")
elif len(password) <= 12:
    print("orta")
else:
    print("uzun")
#7) x rəqəmi həm 3-ə, həm də 5-ə bölünürsə "3 və 5", yalnız 3-ə bölünürsə "3", yalnız 5-ə bölünürsə "5", heç birinə bölünmür
x = int(input("x: "))
if x % 3 == 0 and x % 5 == 0:
    print("3 və 5")
elif x % 3 == 0:
    print("3")
elif x % 5 == 0:
    print("5")
else:
    print("hec biri")
#8) 0-dan 20-yə qədər cüt rəqəmləri çap etsin.
for i in range(21):
    if i % 2 == 0:
        print(i)
#9) "Bağda ərik var idi …" stringinin hər elementini for ilə ayrı-ayrılıqda çap edin.
a = "bagda erik var idi …"
for char in a:
    print(char)
#10) 1-dən 10-a qədər rəqəmləri çap edin, amma 3 xaric.
for i in range(1, 11):
    if i == 3:
        continue
    print(i)
#11) 1-dən başlayaraq ilk 5-ə bölünən rəqəmi tapın və while ilə çap edin (break istifadə edin).
i = 1
while True:
    if i % 5 == 0:
        print(i)
        break
    i += 1
#12) (1, 3, 5, 7, 9) listində/vectorunda 5-i tapın və indeksini çap edin (break istifadə edin).
b = [1, 3, 5, 7, 9]
for i in range(len(b)):
    if b[i] == 5:
        print(i)
        break
#sprint 3b
#1) salam adlı funksiya yaradın ki, heç bir arqument almadan sadəcə "Salam, Dünya!" çap etsin.
def salam():
    print("Salam, Dünya!")
#2) kub_hesabla adlı funksiya yaradın ki, bir rəqəm (n) qəbul etsin və onun kubunu qaytarsın.
def kub_hesabla(n):
    return n**3
#3) birlesdir adlı funksiya yaradın ki, iki söz qəbul etsin və onları boşluqla birləşdirib qaytarsın.
def birlesdir(s1, s2):
    return s1 + " " + s2
#4) cap_et adlı funksiya yaradın ki, bir listi arqument olaraq alsın və listin hər elementini for ilə çap etsin
def cap_et(list):
    for i in list:
        print(i)
#5) toplam adlı funksiya yaradın ki, istənilən sayda rəqəmi (*args) qəbul edib onların cəmini qaytarsın.
def toplam(*args):
    return sum(args)
#6) ortalama adlı funksiya yaradın ki, istənilən sayda rəqəmi (*args) qəbul edib onların ortalamasını qaytarsın (əgər heç bir rəqəm yoxdursa, "Rəqəm yoxdur" qaytarsın).
def ortalama(*args):
        if not args:
         return "reqem yoxdur"
        else:
         return sum(ededler) / len(ededler)
#7) adlar_rəqəmlər adlı funksiya yaradın ki, istənilən sayda ad və rəqəm cütünü (**kwargs) qəbul edib hər cütü çap etsin (məsələn, "ad: bir, rəqəm: 1").
def adlar_rəqəmlər(**kwargs):
    for ad, reqem in kwargs.items():
        print("ad:", ad, ", rəqəm:", reqem)
#8) tip_yoxla adlı funksiya yaradın ki, bir dəyər qəbul edib onun tipini yoxlasın: "mətn", "rəqəm", "başqa" çap etsin.
def tip_yoxla(deyer):
    if type(deyer) == str:
        print("mətn")
    elif type(deyer) == int or type(deyer) == float:
        print("rəqəm")
    else:
        print("başqa")
#9) yas_kateqoriya adlı funksiya yaradın ki, input()/readline() ilə yaş soruşsun, 18-dən aşağıysa "Gənc", yuxarıdrsa "Yetkin" çap etsin.
def yas_kateqoriya():
    yas = int(input("yas: "))
    if yas < 18:
        print("genc")
    else:
        print("yetkin")
#10) soz_uzunluq adlı funksiya yaradın ki, input()/readline() ilə istifadəçidən söz alsın və onun uzunluğunu çap etsin.
def soz_uzunluq():
    soz = input("soz: ")
    print("uzunluq:", len(soz))
 #sprint 4a

#1) İstifadəçidən iki rəqəm və bir əməliyyat (toplama, çıxma, vurma, bölmə) daxil etməsini tələb edən funksiya yazın. Mümkün xətaları (ValueError, TypeError və s.) idarə edin və müvafiq mesajlar çıxarın. Sonda da "Hesablama bitdi" mesajı çap olunsun.
def kalkulyator():
    try:
        a = float(input("1-ci reqem: "))
        b = float(input("2-ci reqem: "))
        emel = input("emeliyyat (+, -, *, /): ")
        if emel == "+":
            print(a + b)
        elif emel == "-":
            print(a - b)
        elif emel == "*":
            print(a * b)
        elif emel == "/":
            print(a / b)
        else:
            print("yalnis emeliyyat")
    except ValueError:
        print("reqem daxil edin")
    except ZeroDivisionError:
        print("0-a bolme olmaz")
    except Exception as e:
        print("xeta basverdi:", e)
    finally:
        print("hesablama bitdi")
#2) 1-dən 50-yə qədər olan rəqəmlərdən yalnız 11ə qalıqsız bölünənlərini list olaraq qaytarın.
bolunenler = []
for i in range(1, 51):
    if i % 11 == 0:
        bolunenler.append(i)
print(bolunenler)
#3) Verilmiş sözlər siyahısından (["kitab", "qələm", "defter", "silgi"]) hər sözün ilk hərfini list olaraq qaytarın.
a = ["kitab", "qelem", "defter", "silgi"]
b = []
for s in a:
    b.append(s[0])
print(b)
#4) Şəhər adları (["Bakı", "Gəncə", "Sumqayıt"]) və kodları ([12, 22, 18]) siyahılarından {şəhər: kod} dictionary olaraq qaytarın.
seherler = ["Bakı", "Gəncə", "Sumqayıt"]
kodlar = [12, 22, 18]
cedvel = {}
for i in range(len(şəhərlər)):
    cedvel[seherler[i]] = kodlar[i]
print(cedvel)
#5) Kilometri milə çevirən (mil = km * 0.621371) lambda funksiyası yazın və 5 fərqli dəyər üçün yoxlayın.
km_to_mil = lambda km: km * 0.621371
print(km_to_mil(1))
print(km_to_mil(5))
print(km_to_mil(10))
print(km_to_mil(15))
print(km_to_mil(20))
#6) [100, 200, 300, 400] qiymətlərinə 18% vergi əlavə etmək üçün map() və lambda istifadə edin.
k = [100, 200, 300, 400]
n = list(map(lambda x: x * 1.18, k))
print(n)
#7) [3, 7, 12] və [2, 4, 6] siyahılarının elementlərini ikiqat artırmaq və sonra cəmləmək üçün map() istifadə edin.
a = [3, 7, 12]
b = [2, 4, 6]
n = list(map(lambda x, y: x * 2 + y * 2, a, b))
print(n)
#8) [150, 80, 220, 45] siyahısından ən kiçik qiyməti reduce() ilə tapın.
from functools import reduce
a = [150, 80, 220, 45]
minimum = reduce(lambda x, y: x if x < y else y, a)
print(minimum)
