#  RTR105   
##  Datormācības kursa elektroniskā klade   
    
###  8.Stunda    
 
   8.Stunda      
###  7.Stunda(history_20181017.txt)
```
      1  VirtualBox --startvm XP
    2  quartus
    3  git clone https://github.com/rbogdanovs/RTR105
    4  ls -l
    5  cd RTR105
    6  firefox &
    7  idle &
    8  ls -l
    9  ls -lt
   10  history
       11  history > history_20181017.txt
    7.Stunda
```

###  6.Stunda
    dgr_20181010_9_55.py
    test_20181010_1.py
    test_20181010_2.py
   6.Stunda

###  5.Stunda(history_20181003a.txt)
   5.Stunda

###  4.Stunda(history_20180926.txt)
   4.Stunda

###  3.Stunda(history_20180919.txt    
  mkdir MapeMapee fails = piešķiršanas operācijas zīme (pa labi komanda piešķir kreisajam failam) cat-pārskatīt sarakstu nano-mans_skripts.sh (veidojam mapi) echo $PATH -(komandu saraksts) Path = piešķiršanas operāciju zīme rwx-111(7) rwx- 110(6) rwx- 100(4) ar skriptu var izveidot mapi instrukcijas 0/1 >   OS fails rakstīts cilvēkam saprotama valodā- tas nogādā interpratoram un -tas (OS)   
    Lai izveidotu skriptu, kas izpilda vairākas komandas vienlaicīgi, izpilda šādas darbības:   
   1)Izveido teksta failu - nano mans_skripts.sh   
   2)Raksta ceļu un programmēšanas valodu ar kuru tiek izpildīts skripts - *#!bin/bash   
   3)Ieraksta komandas. piem. mkdir Mape...   
   4)PATH=$PATH:~ - paplašina adresi komandu meklēšanai   
   5)Saglabā failu   
   6)Lai atļautu palaist skriptu, nepieciešams modificēt faila atļaujas - *chmod 764 mans_skripts.sh   
   7)Palaiž skriptu mans_skripts.sh   
   chmod 764 git-upload     
   echo $PATH   
   ./mans_skripts.sh     
   ~/mans_skripts.sh       
    3.stunda   
       
###  2.Stunda(history_20180912.txt)
   cd - pārvietošanās mapju sistēmā
   . - cd . nonākt tekošajā direktorijā (palikt uz vietas)
   .. - cd .. nonākt par mapi uz augšu mapju direktorijā
   / - cd / saknes apgabala apzīmejums (root) (augstākā direktorija)
   /home/user / ~ / cd - atgriezties sākuma direktorijā
   mkdir - izveidot mapi
   rmdir - dzēst mapi
   rm -r - dzēst mapi ar visām apakšmapēm
   echo (teksts) - parādīt tekstu
   echo -e (teksts)\n(teksts) - teksts pa rindkopām (\n)
   cat (fails)
   more (fails)
   less (fails) - faila lasīšana
   echo (teksts) > fails.txt - izveidot failu ar (tekstu)
   echo (teksts) >> fails.txt - papildina failu ar (tekstu)
   nano (fails) - atver tekstu redaktorā
   chmod 540 fails.txt - maina darbību atļaujas failam (540 pēc binārajiem cipariem RWX RWX RWX - 101 100 000)
   cp fails1.txt fails2.txt - failu kopēšana (1. fails - faila nosaukums pēc kopēšanas)
    mv fails1.txt Music/ - faila pārvietošana uz Music/ direktoriju
   fails - zvaigznītes apzīmē filtrē visus failus, kam nosaukumā fails
   rm - dzēst failu
   rm -f - dzēst failu, ja ir liegta piekļuve (rwx)
            2.stunda    

###  1.Stunda(history_20180905.txt)
  Ctrl+Alt+T  - Termināļā ieslēgšasna  
  Ctrl+L   - Termināļā attīrīšana  
  Firefox &   - Atvērt internetu  
  Ctrl+Alt+F(1-7) - pārvietošanās uz citām OS vidēm
  Burts(i)+TAB(2x)    - komandu saraksts (ar noteikto burtu) 
  Q - saraksta aizvēršana
  OS  - operētājsistēma  
  u   -   
  uname  - OS nosaukums   
  uname -a   - OS apraksts  
  echo - izmantotā kodu valoda
  echo $0 - izmantotās kodu valodas detalizētāks apraksts
  whoami - lietotājs
  who - lietotāja pieslēguma vide un laiks
  pwd - lokācija failu sistēmā
  pwds - 
  man command - komandas apraksts
  man uname   - sīkāka informācija par doto komandu
  ls - galveno failu un mapju saraksts
  ls -l - galveno failu un mapju detalizēts apraksts
  ls -al - visu failu, mapju detalizēts apraksts
     1.stunda  
