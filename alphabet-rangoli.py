#APHABET RANGOLI
import string
def just_letters(size,line):
 sonuc=""
 #harf ve satır sırasına göre harf yazıdırma
 #liste ici fonkisyon ile istediğmiz indexleri belirleyerek ascii fonksiyonunda bulduk
 listem=[string.ascii_lowercase[x]  for x in reversed(range(size-line,size)) ]#size 5 iken 3. satır ise [e,d,c] olur
 
 y=list(reversed(listem))
 all_=listem+y#simetri halini olusturmak icin tersiyle topladık
 all_.pop(len(all_)//2)#orta da ana terim tek oldugu icin ortadaki 1 terimi sildik
 #"-" ve harfleri birlestirmek

 #1.YOL
 for x in range(4*line-3):
   if x%2!=0:
     sonuc +="-"
   else:
      #harfleri döngüye sokmadan sıra sıra yazdırma taktiği

      sonuc +=all_[0]#ilk elemanı koyduk
      all_.pop(0)#sonra ilk elemanı sildik
      #böylece diğer döngüde ilk eleman bi sonraki olur ve böyle tüm elemanlar yazılana kadar devam eder
 #2.YOL(Daha kısa)
 #join parametrede aldıgı degerleri sırayla ice serpiştirir,bi o bi bu şeklinde
 sonuc="-".join(all_)   
 return sonuc#size 5 iken 3.satırın sonucu "e-d-c-d-e" budur

def print_rangoli(size):
 length=4*size-3#her satırın toplam uzunlugunu hesapladık
 baslangic=(length-1)//2#sag-sol "-" kısmının başlangıc eleman sayısı
 for x in range(size):#size 5 ise 4,3,2,1,0 olur
    print("-"*(baslangic)+just_letters(size,x+1)+"-"*(baslangic))
    baslangic -= 2#merkeze kadar,her satırda 2şer azaldıgı icin bunu bunu yazdık
 counter=1#merkez kısmından sonra "-" kısımları arta arta gideceği icin bi counter olusturduk
 for x in reversed(range(size-1)):#size 5 ise 3,2,1,0 olur
    print("-"*(counter*2)+just_letters(size,x+1)+"-"*(counter*2))
    counter+=1