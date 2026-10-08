"""
==================================================
XATIRLATMA — DƏRSDƏ ÖYRƏNDİKLƏRİMİZ
==================================================

Homework zamanı hansısa sintaksisi unutsanız,
bu hissəyə baxıb xatırlaya bilərsiniz.


1. VARIABLE YARATMAQ

Variable məlumatı saxlamaq üçün istifadə olunur.

name = "Ayxan"
age = 24
price = 15.50
is_active = True


2. ƏSAS DATA TYPE-LAR

str   -> mətn
int   -> tam ədəd
float -> onluq ədəd
bool  -> True və ya False

Nümunə:

city = "Baku"        -> str
age = 25             -> int
temperature = 21.5   -> float
is_open = True       -> bool


3. DATA TYPE-I YOXLAMAQ

type() istifadə edə bilərik.

age = 25

print(type(age))

Nəticə:

<class 'int'>


4. USER-DƏN MƏLUMAT ALMAQ

input() istifadə olunur.

name = input("Adınızı daxil edin: ")


VACİB:

input() ilə gələn məlumat həmişə str olur.

Məsələn:

age = input("Yaşınızı daxil edin: ")

User 25 yazsa belə,
age Variable-ı hələ də str olacaq.


5. TYPE CONVERSION

String-i integer-a çevirmək:

age = int(age)

və ya:

age = int(input("Yaşınızı daxil edin: "))


String-i float-a çevirmək:

price = float(input("Qiyməti daxil edin: "))


Ədədi string-ə çevirmək:

number = 100
number_text = str(number)


6. ARITHMETIC OPERATORS

+   toplama
-   çıxma
*   vurma
/   bölmə
//  tam bölmə
%   bölmədən qalan qalıq
**  qüvvət


Nümunələr:

total = 10 + 5

difference = 20 - 8

price = 12 * 3

average = 100 / 4

result = 10 // 3

remainder = 10 % 3

square = 5 ** 2


7. EXPRESSION

Bir neçə value və operator birlikdə yeni nəticə yarada bilər.

price = 25
quantity = 4

total = price * quantity


8. COMPARISON OPERATORS

>    böyükdür
<    kiçikdir
>=   böyükdür və ya bərabərdir
<=   kiçikdir və ya bərabərdir
==   bərabərdir
!=   bərabər deyil


Comparison nəticəsi True və ya False olur.

age = 20

result = age >= 18

print(result)

Nəticə:

True


Diqqət:

=   value assign etmək üçündür

==  iki value-nu müqayisə etmək üçündür


9. LOGICAL OPERATORS

and
or
not


AND

Hər iki tərəf True olmalıdır.

has_card = True
has_money = True

result = has_card and has_money

Nəticə:

True


OR

Ən azı bir tərəf True olsa kifayətdir.

has_cash = False
has_card = True

result = has_cash or has_card

Nəticə:

True


NOT

Boolean value-nu əksinə çevirir.

is_closed = False

result = not is_closed

Nəticə:

True


10. PRINT İLƏ BİRDƏN ÇOX MƏLUMAT GÖSTƏRMƏK

name = "Tural"
age = 22

print("Ad:", name)
print("Yaş:", age)


11. SADƏ ERROR-LARI XATIRLAYAQ

Əgər belə yazsaq:

age = input("Yaş: ")
next_age = age + 1

problem yaranacaq.

Çünki:

age -> str
1   -> int

Düzgün variant:

age = int(input("Yaş: "))
next_age = age + 1


Əgər belə yazsaq:

number = int("hello")

ValueError alacağıq.

Çünki "hello" integer-a çevrilə bilmir.
"""


"""
==================================================
TASK 1 — ŞƏXSİ PROFİL
==================================================

Özünüz haqqında kiçik bir profil yaradın.

Proqramda aşağıdakı məlumatlar saxlanmalıdır:

- ad
- yaş
- yaşadığınız şəhər
- boy
- hazırda tələbə olub-olmamağınız

Hər məlumat üçün uyğun Data Type seçin.

Bütün məlumatları aydın şəkildə ekrana çıxarın.

Sonda yaratdığınız Variable-ların Data Type-larını da göstərin.

Variable adlarını özünüz müəyyən edin.
"""

# Kodunuzu burada yazın:




"""
==================================================
TASK 2 — KAFE SİFARİŞİ
==================================================

Kiçik bir kafe sifariş proqramı hazırlayın.

User-dən:

- adını
- seçdiyi məhsulun qiymətini
- neçə ədəd almaq istədiyini

alın.

Sifarişin ümumi qiymətini hesablayın.

User-in daxil etdiyi rəqəmlərin hansı Data Type-da
olmalı olduğunu özünüz müəyyən edin və lazım olan
Type Conversion-ları edin.

Sonda:

- müştərinin adını
- məhsulun qiymətini
- sayını
- ümumi sifariş məbləğini

ekranda göstərin.

Variable adlarını və hesablamanı özünüz qurun.
"""

# Kodunuzu burada yazın:




"""
==================================================
TASK 3 — ƏDƏDLƏRLƏ İŞ
==================================================

User-dən bir tam ədəd alın.

Həmin ədəddən istifadə edərək aşağıdakı nəticələri tapın:

- ədədin kvadratı
- ədədin kubu
- ədədin 2-yə bölünməsindən qalan qalıq
- ədədin 5-ə tam bölünmə nəticəsi

Bütün nəticələri aydın şəkildə ekrana çıxarın.

Hansı operatorlardan istifadə etməli olduğunuzu
XATIRLATMA hissəsindən baxa bilərsiniz.

"""

# Kodunuzu burada yazın:




"""
==================================================
TASK 4 — TƏDBİRƏ GİRİŞ YOXLAMASI
==================================================

Bir tədbirə giriş üçün sadə yoxlama proqramı hazırlayın.

Proqramda aşağıdakı məlumatlar nəzərə alınmalıdır:

- şəxsin yaşı
- bileti olub-olmaması
- şəxsiyyət vəsiqəsinin olub-olmaması

Yaş məlumatını user-dən alın.

Bilet və şəxsiyyət vəsiqəsi məlumatlarını
Boolean value kimi özünüz müəyyən edin.

Tədbirə giriş üçün:

- şəxs ən azı 18 yaşında olmalıdır
- bileti olmalıdır
- şəxsiyyət sənədi olmalıdır

Comparison və Logical Operators istifadə edərək
şəxsin bütün tələblərə uyğun olub-olmadığını hesablayın.

Nəticə True və ya False şəklində göstərilməlidir.
"""

# Kodunuzu burada yazın:




"""
==================================================
FINAL TASK — SƏYAHƏT BÜDCƏSİ
==================================================

Sadə səyahət büdcəsi proqramı hazırlayın.

User-dən aşağıdakı məlumatları alın:

- adı
- gedəcəyi şəhər
- neçə gün qalacağı
- bir gecəlik hotel qiyməti
- bir günlük yemək xərci
- səyahət üçün ayırdığı ümumi büdcə

Proqram:

1. Hotel üçün ümumi xərci hesablamalıdır.

2. Yemək üçün ümumi xərci hesablamalıdır.

3. Səyahətin ümumi xərcini hesablamalıdır.

4. User-in büdcəsinin səyahət üçün kifayət edib-etmədiyini
   müəyyən etməlidir.

5. Büdcə yoxlamalarını Logical Operator ilə birləşdirib
   yekun True və ya False nəticəsi yaratmalıdır.

Sonda proqram aşağıdakı məlumatları aydın şəkildə göstərməlidir:

- şəxsin adı
- gedəcəyi şəhər
- səyahət müddəti
- hotel üçün ümumi xərc
- yemək üçün ümumi xərc
- ümumi səyahət xərci
- ayrılmış büdcə
- büdcənin kifayət edib-etməməsi
- yekun nəticə
"""

# Kodunuzu burada yazın:
