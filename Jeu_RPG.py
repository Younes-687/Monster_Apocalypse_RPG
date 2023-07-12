def start():

  
    print("Appuyez sur start")
    start = input()
    
    while "start" != start and start!="close" :
      
        print("Appuyez Sur start Pour Entrer Dans Le Jeu Ou Close Pour Quitter")
        start = input()
    if start == "close":
        print("Vous Avez Quitté Le Jeu")
          
    if start=="start":
       Main_menu()
       
def Main_menu():
  
 Exit=False
 while Exit== False:
     print("MAIN MENU :")
     print("1. Create New Game")
     print("2. Load Saved Game")
     print("3. About")
     print("4. Exit")
     choice=input()
     
     while choice!="1" and choice!="2" and choice!="3" and choice!="4":
        

        print("Cliquez Sur 1,2 Ou 3 Pour Continuer Ou 4 Pour Sortir Du Menu")
        choice=input()
          
     if choice == "1" :
      
       new_game()
       
     elif choice == "2" :
       
       print("Cette option n'est pas encore existante")
     
     elif choice == "3" :
       
       about() 
     
     else :
       
       Exit=True
       start()

def about():
 
 exit=False

 while exit==False:
       print("1. Description Du Jeu")
       print("2. Commandes De Jeu")
       print("3. Map")
       print("4. Exit")
       about=input()
     


       while about!="1" and about !="2" and about!="3" and about!="4":
           print("Cliquez Sur 1,2 Ou 3 Pour Continuer Ou 4 Pour Retourner Au Menu")
           about=input()
       if about=="1":
          print("////////")
          print("Monster apocalypse a été crée en Janvier 2023 par Younes Abdallaoui, en utilisant les bases des algorithmes en Python.")
          print("////////")
          print("Dans un monde plein de créatures monstrueuses, votre mission est de tuer les trois éternels, Gagrigore à longue barbe en premier lieu, Dexter le clown tueur en deuxième et enfin, l’imbattable Zombie Bigfoot.")
          print("Tout au long du trajet, faites attention à ne pas tomber dans les trous creusés par les monstres, cela réduira vos points de vie, mais ne vous inquiétez pas, vous pouvez aussi retrouver des pansements sur votre chemin pour réaugmenter celles ci.")
          print("Au début de la partie, vous aurez un couteau que vous pourrez utiliser en infinité, un arc avec une seule flèche et deux cordes. En vous déplaçant, vous pourrez trouver d’autres flèches et cordes ainsi que la fameuse bombe de l’enfer que vous retrouverez dans votre inventaire en cas de besoin.")
          print("Les armes vous aiderons a combattre les monstres. Gagrigore à longue barbe est le monstre du niveau 1, sa force d’attaque est estimée entre 3 et 8. Dexter le clown tueur est le monstre du niveau 2, sa force d’attaque est estimée entre 5 et 12.")
          print(" Le Zombie Bigfoot est le monstre du dernier niveau, sa force d’attaque est estimée entre 10 et 15. La map de Monster Apocalypse est constituée de quarante neuf carrés où vous pourrez vous déplacez librement vers le nord, le sud, l’est et l’ouest.")
          print("Lors de votre aventure, toutes rencontres avec l’un des monstres sera aléatoire, de même sont placés les trous, les pansements et les armes dans ce jeu. Votre départ sera au centre de la map, et vous n’avait pas le droit  de dépasser les bordures de cette dernière.")
          print(" NB: Vous pourrez trouver plusieurs surprises sur le même carré !")
          print(" NB: Les Troues Ne Disparaissent Pas Faites Attention De Ne Pas Retourner Au Point Ou Le troue Se Situe")
          print(" NB: Si Vous N'avez Plus De Cordes Et Que Vous Tombez Dans Un Trou Vous Perdez La Partie")
          print("Pour Gagner Il Faut Battre Les 3 Monstres")
          print("Si Vous Trouvez Une Corde ou Un Panssement Ceux Là Va Être Récuperé Automatiquement Dans Votre Inventaire")
          print("////////")



          print("Cliquez Sur e Pour Revenir Au Menu Principal")
          retour_menu=input()
          while retour_menu!="e":
             print("Cliquez Sur e Pour Revenir Au En Menu Principal")
             retour_menu=input()
             exit=False
       if about=="2":
          print("Commandes De Jeu :")
          print("Pour commencer le jeu, Tapez ( start )")
          print("Pour accéder à votre inventaire, cliquez sur ( i )")
          print("Pour vous déplacez vers le nord, cliquez sur ( n )")
          print("Pour vous déplacez vers le sud, cliquez sur ( s )")
          print("Pour vous déplacez vers l’est, cliquez sur ( e )")
          print("Pour vous déplacez vers l’ouest, cliquez sur ( o )")
          print("Pour sortir d’un trou, cliquez sur ( j ) ( si vous avez une corde )")
          print("Pour commencer un combat, cliquez sur ( c )")
          print("Pour quitter le jeu, tapez ( exit )")
          print("Pour arrêter le programme, il faut d’abord quitter le jeu, cliquez sur 4 sur le menu (exit) et tapez ( close )")
          print("////////")



          print("Cliquez Sur e Pour Revenir Au Menu Principal")
          retour_menu=input()
          while retour_menu!="e":
             print("Cliquez Sur e Pour Revenir Au En Menu Principal")
             retour_menu=input()
             exit=False
       if about=="3":
          print("Map:")
          print("////////")
          print("                 ")
          print("        ^        ")
          print("        |Axe y   ")
          print("_________________")
          print("| * * * * * * * | 3")
          print("| * * * * * * * | 2")
          print("| * * * * * * * | 1")
          print("| * * * X * * * | 0 --->")
          print("| * * * * * * * |-1 Axe x")
          print("| * * * * * * * |-2")
          print("| * * * * * * * |-3")
          print("_________________")
          print(" -3-2-1 0 1 2 3")
          print("////////")
          print("Au Début De La Partie Vous Allez Vous Trouvez Sur le Point X(0,0)")
          print("Si Vous Avancez Vers L'est Par Exemple Vous Allez Sur Le point x=1 y=0 (1,0)")
          print("Si Vous Allez Vers L'ouest Vous Allez Sur Le Point x=-1 y=0 (-1,0)")
          print("Si Vous Allez Vers Le Nord Vous Allez Sur Le Point x0 y=1 (0,1)")
          print("Si Vous Allez Vers Le Sud Vous Allez Sur Le Point x0 y=-1 (0,-1)")
          print("Et Ainsi De Suite..")
          print("////////")
          print("Cliquez Sur e Pour Revenir Au Menu Principal")
          retour_menu=input()
          while retour_menu!="e":
             print("Cliquez Sur e Pour Revenir Au En Menu Principal")
             retour_menu=input()
             exit=False
       else:
          exit=True
          Main_menu

def ask_name():
  # demander le nom
  print("Entrez Votre Nom :")
  name = input()
  print("Bonjour",name,", Votre Ville se détruit par trois monstres affreux, leurs but est d’effacer l’humanité sur Monster Apocalypse pour que cette ville se transforme à un monde monstrueux qui leurs appartient.")
  print("Vous Êtes Le Seul Espoir De Monster Apocalypse! Récupérez Toutes Armes Que Vous Trouveriez Sur Votre Trajet, Faites Attention Au Pièges Des Monstres Et à Vos Points De Vie également.")
  print("Soyez Toujours Prêts Aux Combats. N’oubliez Pas Vous Êtes L’hero De Cette Ville, Faites Votre Meilleur Pour La Sauver !!")
  print("/////")
  print("Cliquez Sur N'importe Quel Touche Pour Commencer")

from random import randint
def new_game():
 x=0
 y=0
 #HP joueur
 hp_joueur=100
 #Inventaire
 corde=2
 fleches=3
 bombe_de_lenfer=0
 ask_name()
 ordre=input()
 monstre=1
 
 #Carractéristique Map par rapport à l'axe des X et l'axe des Y
 a = randint(-3,3)
 b = randint(-3,3)
 while (a==0 and b==0) or (a==0 and b==1)or(a==0 and b==-1) or (a==1 and b==0) or (a==-1 and b==0):
   a=randint(-3,3)
   b=randint(-3,3)
 c = randint(-3,3)
 d = randint(-3,3)


 while (c==a and d==b) or (c==0 and d==0) or (c==0 and d==1)or(c==0 and d==-1) or (c==1 and d==0) or (c==-1 and d==0) :
       c = randint(-3,3)
       d = randint(-3,3)
 e = randint(-3,3)
 f = randint(-3,3)

 while (e==c and f==d) or (e==0 and f==0) or (e==0 and f==1) or (e==0 and f==-1) or (e==1 and f==0) or (e==-1 and f==0) :
       e = randint(-3,3)
       f = randint(-3,3)

 px1=randint(-3,3)
 py1=randint(-3,3)

 while (px1==e and py1==f) or (px1==0 and py1==0):
   px1=randint(-3,3)
   py1=randint(-3,3)
 
 px2=randint(-3,3)
 py2=randint(-3,3)
 while (px2==px1 and py2==py1) or (px2==0 and py2==0):
   px2=randint(-3,3)
   py2=randint(-3,3)
 
 px3=randint(-3,3)
 py3=randint(-3,3)
 while (px3==px2 and py3==py2) or (px3==0 and py3==0):
   px3=randint(-3,3)
   py3=randint(-3,3)

 px3=randint(-3,3)
 py3=randint(-3,3)
 while (px3==px2 and py3==py2) or (px3==0 and py3==0):
   px3=randint(-3,3)
   py3=randint(-3,3)

 px4=randint(-3,3)
 py4=randint(-3,3)
 while (px4==px3 and py4==py3) or (px4==0 and py4==0):
   px4=randint(-3,3)
   py4=randint(-3,3)
 
 px5=randint(-3,3)
 py5=randint(-3,3)
 while (px5==px4 and py5==py4) or (px5==0 and py5==0):
   px5=randint(-3,3)
   py5=randint(-3,3)

 px6=randint(-3,3)
 py6=randint(-3,3)
 while (px6==px5 and py6==py5) or (px6==0 and py6==0):
   px6=randint(-3,3)
   py6=randint(-3,3)

 px7=randint(-3,3)
 py7=randint(-3,3)
 while (px7==px6 and py7==py6) or (px7==0 and py7==0):
   px7=randint(-3,3)
   py7=randint(-3,3)

 trx1=randint(-3,3)
 try1=randint(-3,3)
 while (trx1==px7 and try1==py7) or (trx1==0 and try1==0) or (trx1==0 and try1==1)or(trx1==0 and try1==-1) or (trx1==1 and try1==0) or (trx1==-1 and try1==0):
   trx1=randint(-3,3)
   try1=randint(-3,3)

 trx2=randint(-3,3)
 try2=randint(-3,3)
 while (trx2==trx1 and try2==try1) or (trx2==0 and try2==0) or (trx2==0 and try2==1)or(trx2==0 and try2==-1) or (trx2==1 and try2==0) or (trx2==-1 and try2==0):
   trx2=randint(-3,3)
   try2=randint(-3,3)   

 trx3=randint(-3,3)
 try3=randint(-3,3)
 while (trx3==trx2 and try3==try2) or (trx3==0 and try3==0) or (trx3==0 and try3==1)or(trx3==0 and try3==-1) or (trx3==1 and try3==0) or (trx3==-1 and try3==0):
   trx3=randint(-3,3)
   try3=randint(-3,3)

 trx4=randint(-3,3)
 try4=randint(-3,3)
 while (trx4==trx3 and try4==try3) or (trx4==0 and try4==0) or (trx4==0 and try4==1)or(trx4==0 and try4==-1) or (trx4==1 and try4==0) or (trx4==-1 and try4==0):
   trx4=randint(-3,3)
   try4=randint(-3,3) 

 cx1=randint(-3,3)
 cy1=randint(-3,3)
 while (cx1==trx4 and cy1==try4) or (cx1==0 and cy1==0):
   cx1=randint(-3,3)
   cy1=randint(-3,3)

 cx2=randint(-3,3)
 cy2=randint(-3,3)
 while (cx2==cx1 and cy2==cy1) or (cx2==0 and cy2==0):
   cx2=randint(-3,3)
   cy2=randint(-3,3)   

 cx3=randint(-3,3)
 cy3=randint(-3,3)
 while (cx3==cx2 and cy3==cy2) or (cx3==0 and cy3==0):
   cx3=randint(-3,3)
   cy3=randint(-3,3)

 cx4=randint(-3,3)
 cy4=randint(-3,3)
 while (cx4==cx3 and cy4==cy3) or (cx4==0 and cy4==0):
   cx4=randint(-3,3)
   cy4=randint(-3,3)

 cx5=randint(-3,3)
 cy5=randint(-3,3)
 while (cx5==cx4 and cy5==cy4) or (cx5==0 and cy5==0):
   cx5=randint(-3,3)
   cy5=randint(-3,3)

 bx1=randint(-3,3)
 by1=randint(-3,3)
 while (bx1==cx5 and by1==cy5) or (bx1==0 and by1==0) or (bx1==0 and by1==1) or (bx1==0 and by1==-1) or (bx1==1 and by1==0) or (bx1==-1 and by1==0):
   bx1=randint(-3,3)
   by1=randint(-3,3)

 bx2=randint(-3,3)
 by2=randint(-3,3)
 while (bx2==bx1 and by2==by1) or (bx2==0 and by2==0) or (bx2==0 and by2==1) or (bx2==0 and by2==-1) or (bx2==1 and by2==0) or (bx2==-1 and by2==0):
   bx2=randint(-3,3)
   by2=randint(-3,3)

 fx1=randint(-3,3)
 fy1=randint(-3,3)
 while (fx1==bx2 and fy1==by2) or (fx1==0 and fy1==0) :
   fx1=randint(-3,3)
   fy1=randint(-3,3)

 fx2=randint(-3,3)
 fy2=randint(-3,3)
 while (fx2==fx1 and fy2==fy1) or (fx2==0 and fy2==0) :
   fx2=randint(-3,3)
   fy2=randint(-3,3)

 fx3=randint(-3,3)
 fy3=randint(-3,3)
 while (fx3==fx2 and fy3==fy2) or (fx3==0 and fy3==0) :
   fx3=randint(-3,3)
   fy3=randint(-3,3)


 while ordre!="exit" and hp_joueur>0 and monstre!=False:
    
    #instruction_(avancer vers le nord)
    if ordre== "n" and y<3:
      y=y+1
    elif ordre=="n" and y>=3:
      print("Vous Ne Pouvez Plus Avancer") 


    #instruction_(avancer vers le sud)
    if ordre=="s" and y>-3:
      y=y-1
    elif ordre=="s" and y<=-3:
      print("Vous Ne Pouvez Plus Avancer")


    #instrution_(avancer vers l'est)
    if ordre== "e" and x<3:
      x=x+1
    elif ordre=="e" and x>=3 :
      print("Vous Ne Pouvez Plus Avancer")


    #instruction_(avancer vers l'ouest)
    if ordre=="o" and x>-3:
       x=x-1
    elif ordre=="o" and x<=-3:
       print("Vous Ne Pouvez Plus Avancer")
    #Afficher_Map à chaque fois que le joueur bouge
    print("Map: Vous Êtes Au Point x=",x," y=",y)
    #Consulter_l'inventaire

    if ordre=="i":
      print("Inventaire:")
      print("Cordes :",corde)
      print("Flêches :",fleches)
      print("Bombes De L'Enfer :",bombe_de_lenfer)
    #instruction_Trous

    if (x==trx1 and y==try1) or (x==trx2 and y==try2) or (x==trx3 and y==try3) or (x==trx4 and y==try4):
       print("Aïee! Vous Êtes Tombé Dans Un Trou Que Les Monstres Vous Ont Préparés...")
       if corde>0:
         degats=randint(2,5)
         hp_joueur= hp_joueur-degats
         print("Vos HP Ont Diminué De",degats,"HP, Vous Avez Maintenant",hp_joueur,"HP")
         print("Utilisez Une Corde Pour Sortir Du Trou")
         print("Cliquez Sur j Pour Utiliser La Corde")
         trou=input()
         while trou!="j":
            print("Cliquez Sur j Pour Utiliser La Corde")
            trou=input()
         if trou=="j":
           corde=corde-1
           print("Ouff!! Vous Êtes Sorti Du Trou")
           print("Attention! Vous N'avez Plus que",corde,"Cordes")
       else : 
          hp_joueur=0
          print("Oh! Il Parait Que Vous N'avez Plus De Corde Pour Sortir Du Trou")
          print("Vous Avez échoué !")
          
    #instruction_recuperation_bombe de l'enfer

    if (x==bx1 and y==by1) or (x==bx2 and y==by2):
      print("YEESS ! Vous Avez Trouvé Une Bombe De L'Enfer")
      print("Vous Pourrez L'Utiliser Lors De Vos Combats")
      bombe_de_lenfer=bombe_de_lenfer+1
      if x==bx1 and y==by1:
        bx1=4
        by1=4
      if x==bx2 and y==by2:
        bx2=4
        by2=4
    #instruction_recuperation_fleches

    if (x==fx1 and y==fy1) or (x==fx2 and y==fy2) or (x==fx3 and y==fy3):
       print("Vous Venez de Trouver Une Flêche !!! Vous Pouvez Vous En Servir Pour Votre Arc")
       fleches=fleches+1
       print("Vous Avez",fleches,"Flêches Dans Votre Inventaire")
       
       if x==fx1 and y==fy1:
         fx1=4
         fy1=4
       if x==fx2 and y==fy2:
         fx2=4
         fy2=4
       if x==fx3 and y==fy3:
         fx3=4
         fy3=4
    #instruction_recuperation_cordes
    if (x==cx1 and y==cy1) or (x==cx2 and y==cy2) or (x==cx3 and y==cy3) or (x==cx4 and y==cy4) or (x==cx5 and y==cy5):
       corde=corde+1
       print("Vous Venez de Trouver Une Corde !!! Vous Vous en Servirez Pour Sortir Des Trous Que Les Monstres Vous Ont Préparés")
       print("Vous Avez",corde,"Cordes Dans Votre Inventaire")
       if x==cx1 and y==cy1:
          cx1=4
          cy1=4
       if x==cx2 and y==cy2:
          cx2=4
          cy2=4
       if x==cx3 and y==cy3:
          cx3=4
          cy3=4
       if x==cx4 and y==cy4:
          cx4=4
          cy4=4
       if x==cx5 and y==cy5:
          cx5=4
          cy5=4
    

    #instruction_pensements
    if (x==px1 and y==py1) or (x==px2 and y==py2) or (x==px3 and y==py3) or (x==px4 and y==py4) or (x==px5 and y==py5):

       hp_joueur=hp_joueur+10
       print("Hourraa! Vous Avez Trouvez Un Penssement,")
       print("Vos Points De Vie Ont Augmenté de 10HP, Vous Avez Maintenant",hp_joueur,"HP")
       if x==px1 and y==py1:
          px1=4
          py1=4
       if x==px2 and y==py2:
          px2=4
          py2=4
       if x==px3 and y==py3:
          px3=4
          py3=4
       if x==px4 and y==py4:
          px4=4
          py4=4
       if x==px5 and y==py5:
          px5=4
          py5=4


    if (x==px6 and y==py6) or (x==px7 and y==py7):

       hp_joueur=hp_joueur+20
       print("Hourraa! Vous Avez Trouvez Un Penssement,")
       print("Vos Points De Vie Ont Augmenté de 20HP, Vous Avez Maintenant",hp_joueur,"HP")      
       if x==px6 and y==py6:
         px6=4
         py6=4
       if x==px7 and y==py7:
         px7=4
         py7=4

    #instruction_combat_Monstre_Niveau1
    if (( x==a and y==b) or (x==c and y==d) or (x==e and y==f)) and monstre==1 :
                
          hp_monstre1=100
          print("VOUS ÊTES ATTAQUÉ Par Gagrigore À Longue Barbe !!!")
          print("Clique Sur c Pour Combattre...")
          combat=input()
          while combat!="c":
             print("Clique Sur c Pour Combattre...")
             combat=input()
          

          while hp_monstre1>0 and hp_joueur>0:

            degats=randint(3,8)
            hp_joueur=hp_joueur-degats
             
            if hp_joueur>0: 
                 
               if fleches>0 and bombe_de_lenfer>0:  
                 print("Aïe.. GAGRIGORE À LONGUE BARBE Vous A Causé",degats,"De Dégats, Vous Avez Maintenant",hp_joueur,"HP")
                 print("1. Attaquer Avec Le Couteau")
                 print("2. Attaquer Avec L'Arc")
                 print("3. Attaquer Avec La BOMBE DE L'ENFER")
                 combat=input()

                 while combat!="1" and combat!="2" and combat!="3":
                    
                       print("Cliquez Sur 1 Ou 2 Ou 3 Pour Continuer...")
                       combat=input()
                    
                 if combat=="1":
                    degats=randint(10,20)
                    hp_monstre1=hp_monstre1-degats
                    print("Vous Avez Attaqué GAGRIGORE À LONGUE BARBE Avec Le Couteau! Vous lui Avez Causé",degats,"De Dégats, Il A Maintenant",hp_monstre1,"HP")
                 if combat=="2":
                    degats=randint(25,35)
                    hp_monstre1=hp_monstre1-degats
                    fleches=fleches-1
                    print("Vous Avez Attaqué GAGRIGORE À LONGUE BARBE Avec L'Arc! Vous lui Avez Causé",degats,"De Dégats, Il A Maintenant",hp_monstre1,"HP")
                 if combat=="3":
                    degats=randint(40,60)
                    hp_monstre1=hp_monstre1-degats
                    bombe_de_lenfer=bombe_de_lenfer-1
                    print("Vous Avez Attaqué GAGRIGORE À LONGUE BARBE Avec La BOMBE DE L'ENFER! Vous lui Avez Causé",degats,"De Dégats, Il A Maintenant",hp_monstre1,"HP")
                 if hp_monstre1<=0:
                    print("BIEN JOUÉ ! Vous Avez Gagné Votre Combat Contre GAGRIGORE À LONGUE BARBE")
  
               elif fleches>0 and bombe_de_lenfer<=0 :
                   print("Aïe.. GAGRIGORE À LONGUE BARBE Vous A Causé",degats,"De Dégats, Vous Avez Maintenant",hp_joueur,"HP")
                   print("1. Attaquer Avec Le Couteau")
                   print("2. Attaquer Avec L'Arc")
                   combat=input()
                   
                   while combat!="1" and combat!="2" :
                      
                         print("Cliquez Sur 1 Ou 2 Pour Continuer...")
                         combat=input()
                    
                   if combat=="1":
                        degats=randint(10,20)
                        hp_monstre1=hp_monstre1-degats
                        print("Vous Avez Attaqué GAGRIGORE À LONGUE BARBE Avec Le Couteau! Vous lui Avez Causé",degats,"De Dégats, Il A Maintenant",hp_monstre1,"HP")
                   if combat=="2":
                        degats=randint(25,35)
                        hp_monstre1=hp_monstre1-degats
                        fleches=fleches-1
                        print("Vous Avez Attaqué GAGRIGORE À LONGUE BARBE Avec L'Arc! Vous lui Avez Causé",degats,"De Dégats, Il A Maintenant",hp_monstre1,"HP")
                   if hp_monstre1<=0:
                    print("BIEN JOUÉ ! Vous Avez Gagné Votre Combat Contre GAGRIGORE À LONGUE BARBE")
               elif fleches<=0 and bombe_de_lenfer>0:
                   print("Aïe.. GAGRIGORE À LONGUE BARBE Vous A Causé",degats,"De Dégats, Vous Avez Maintenant",hp_joueur,"HP")
                   print("1. Attaquer Avec Le Couteau")
                   print("2. Attaquer Avec La BOMBE DE L'ENFER")
                   combat=input()

                   while combat!="1" and combat!="2" :
                      
                         print("Cliquez Sur 1 Ou 2 Pour Continuer...")
                         combat=input()
                    
                   if combat=="1":
                        degats=randint(10,20)
                        hp_monstre1=hp_monstre1-degats
                        print("Vous Avez Attaqué GAGRIGORE À LONGUE BARBE Avec Le Couteau! Vous lui Avez Causé",degats,"De Dégats, Il A Maintenant",hp_monstre1,"HP")
                   if combat=="2":
                        degats=randint(40,60)
                        hp_monstre1=hp_monstre1-degats
                        bombe_de_lenfer=bombe_de_lenfer-1
                        print("Vous Avez Attaqué GAGRIGORE À LONGUE BARBE Avec La BOMBE DE L'ENFER! Vous lui Avez Causé",degats,"De Dégats, Il A Maintenant",hp_monstre1,"HP")
                   if hp_monstre1<=0:
                    print("BIEN JOUÉ ! Vous Avez Gagné Votre Combat Contre GAGRIGORE À LONGUE BARBE")
               else:
                   print("Aïe.. GAGRIGORE À LONGUE BARBE Vous A Causé",degats,"De Dégats, Vous Avez Maintenant",hp_joueur,"HP")
                   print("1. Attaquer Avec Le Couteau")
                   
                   combat=input()

                   while combat!="1" :
                      
                         print("Cliquez Sur 1 Pour Continuer...")
                         combat=input()

                    
                   
                   degats=randint(10,20)
                   hp_monstre1=hp_monstre1-degats
                   print("Vous Avez Attaqué GAGRIGORE À LONGUE BARBE Avec Le Couteau! Vous lui Avez Causé",degats,"De Dégats, Il A Maintenant",hp_monstre1,"HP")
                   if hp_monstre1<=0:
                     print("BIEN JOUÉ ! Vous Avez Gagné Votre Combat Contre GAGRIGORE À LONGUE BARBE")

            else:
                  print("Aïe.. GAGRIGORE À LONGUE BARBE Vous A Causé",degats,"De Dégats, Vous Avez Maintenant 0 HP")
                  print(hp_joueur)
                  print("Vous Avez Échoué !") 
                  print("Cliquez Sur N'Importe Quel Bouton Pour Aller Vers Le Menu..")  

          if x==a and y==b :   
            monstre=2
            a=4
            b=4
              
          if x==c and y==d:

            monstre=2
            c=4
            d=4

          if x==e and y==f :
                    
            monstre=2
            e=4
            f=4

    if (( x==a and y==b) or (x==c and y==d) or (x==e and y==f)) and monstre==2 :
      
        
          hp_monstre1=100
          print("VOUS ÊTES ATTAQUÉ Par DEXTER Le Clown Tueur !!!")
          print("Clique Sur c Pour Combattre...")
          combat=input()
          while combat!="c":
             print("Clique Sur c Pour Combattre...")
             combat=input()
          

          while hp_monstre1>0 and hp_joueur>0:

            degats=randint(5,12)
            hp_joueur=hp_joueur-degats
             
            if hp_joueur>0: 
                 
               if fleches>0 and bombe_de_lenfer>0:  
                 print("Aïe.. DEXTER Le Clown Tueur Vous A Causé",degats,"De Dégats, Vous Avez Maintenant",hp_joueur,"HP")
                 print("1. Attaquer Avec Le Couteau")
                 print("2. Attaquer Avec L'Arc")
                 print("3. Attaquer Avec La BOMBE DE L'ENFER")
                 combat=input()

                 while combat!="1" and combat!="2" and combat!="3":
                    
                       print("Cliquez Sur 1 Ou 2 Ou 3 Pour Continuer...")
                       combat=input()
                    
                 if combat=="1":
                    degats=randint(10,20)
                    hp_monstre1=hp_monstre1-degats
                    print("Vous Avez Attaqué DEXTER Le Clown Tueur Avec Le Couteau! Vous lui Avez Causé",degats,"De Dégats, Il A Maintenant",hp_monstre1,"HP")
                 if combat=="2":
                    degats=randint(25,35)
                    hp_monstre1=hp_monstre1-degats
                    fleches=fleches-1
                    print("Vous Avez Attaqué DEXTER Le Clown Tueur Avec L'Arc! Vous lui Avez Causé",degats,"De Dégats, Il A Maintenant",hp_monstre1,"HP")
                 if combat=="3":
                    degats=randint(40,60)
                    hp_monstre1=hp_monstre1-degats
                    bombe_de_lenfer=bombe_de_lenfer-1
                    print("Vous Avez Attaqué DEXTER Le Clown Tueur Avec La BOMBE DE L'ENFER! Vous lui Avez Causé",degats,"De Dégats, Il A Maintenant",hp_monstre1,"HP")
                 if hp_monstre1<=0:
                    print("BIEN JOUÉ ! Vous Avez Gagné Votre Combat Contre DEXTER Le Clown Tueur")
  
               elif fleches>0 and bombe_de_lenfer<=0 :
                   print("Aïe.. DEXTER Le Clown Tueur Vous A Causé",degats,"De Dégats, Vous Avez Maintenant",hp_joueur,"HP")
                   print("1. Attaquer Avec Le Couteau")
                   print("2. Attaquer Avec L'Arc")
                   combat=input()
                   
                   while combat!="1" and combat!="2" :
                      
                         print("Cliquez Sur 1 Ou 2 Pour Continuer...")
                         combat=input()
                    
                   if combat=="1":
                        degats=randint(10,20)
                        hp_monstre1=hp_monstre1-degats
                        print("Vous Avez Attaqué DEXTER Le Clown Tueur Avec Le Couteau! Vous lui Avez Causé",degats,"De Dégats, Il A Maintenant",hp_monstre1,"HP")
                   if combat=="2":
                        degats=randint(25,35)
                        hp_monstre1=hp_monstre1-degats
                        fleches=fleches-1
                        print("Vous Avez Attaqué DEXTER Le Clown Tueur Avec L'Arc! Vous lui Avez Causé",degats,"De Dégats, Il A Maintenant",hp_monstre1,"HP")
                   if hp_monstre1<=0:
                    print("BIEN JOUÉ ! Vous Avez Gagné Votre Combat Contre DEXTER Le Clown Tueur")
               elif fleches<=0 and bombe_de_lenfer>0:
                   print("Aïe.. DEXTER Le Clown Tueur Vous A Causé",degats,"De Dégats, Vous Avez Maintenant",hp_joueur,"HP")
                   print("1. Attaquer Avec Le Couteau")
                   print("2. Attaquer Avec La BOMBE DE L'ENFER")
                   combat=input()

                   while combat!="1" and combat!="2" :
                      
                         print("Cliquez Sur 1 Ou 2 Pour Continuer...")
                         combat=input()
                    
                   if combat=="1":
                        degats=randint(10,20)
                        hp_monstre1=hp_monstre1-degats
                        print("Vous Avez Attaqué DEXTER Le Clown Tueur Avec Le Couteau! Vous lui Avez Causé",degats,"De Dégats, Il A Maintenant",hp_monstre1,"HP")
                   if combat=="2":
                        degats=randint(40,60)
                        hp_monstre1=hp_monstre1-degats
                        bombe_de_lenfer=bombe_de_lenfer-1
                        print("Vous Avez Attaqué DEXTER Le Clown Tueur Avec La BOMBE DE L'ENFER! Vous lui Avez Causé",degats,"De Dégats, Il A Maintenant",hp_monstre1,"HP")
                   if hp_monstre1<=0:
                    print("BIEN JOUÉ ! Vous Avez Gagné Votre Combat Contre DEXTER Le Clown Tueur")
               else:
                   print("Aïe.. DEXTER Le Clown Tueur Vous A Causé",degats,"De Dégats, Vous Avez Maintenant",hp_joueur,"HP")
                   print("1. Attaquer Avec Le Couteau")
                   
                   combat=input()

                   while combat!="1" :
                      
                         print("Cliquez Sur 1 Pour Continuer...")
                         combat=input()

                    
                   
                   degats=randint(10,20)
                   hp_monstre1=hp_monstre1-degats
                   print("Vous Avez Attaqué DEXTER Le Clown Tueur Avec Le Couteau! Vous lui Avez Causé",degats,"De Dégats, Il A Maintenant",hp_monstre1,"HP")
                   if hp_monstre1<=0:
                     print("BIEN JOUÉ ! Vous Avez Gagné Votre Combat Contre DEXTER Le Clown Tueur")

            else:
                  print("Aïe.. DEXTER Le Clown Tueur Vous A Causé",degats,"De Dégats, Vous Avez Maintenant 0 HP")
                  print(hp_joueur)
                  print("Vous Avez Échoué !") 
                  print("Cliquez Sur N'Importe Quel Bouton Pour Aller Vers Le Menu..") 

          if x==a and y==b: 
               monstre=3
               a=4
               b=4

          if x==c and y==d:
               monstre=3
               c=4
               d=4

          if x==e and y==f:
               monstre=3
               e=4
               f=4 


    if (( x==a and y==b) or (x==c and y==d) or (x==e and y==f)) and monstre==3 :
      
       
        
          hp_monstre1=100
          print("VOUS ÊTES ATTAQUÉ Par Zombie Bigfoot !!!")
          print("Clique Sur c Pour Combattre...")
          combat=input()
          while combat!="c":
             print("Clique Sur c Pour Combattre...")
             combat=input()
          

          while hp_monstre1>0 and hp_joueur>0:

            degats=randint(10,15)
            hp_joueur=hp_joueur-degats
             
            if hp_joueur>0: 
                 
               if fleches>0 and bombe_de_lenfer>0:  
                 print("Aïe.. Zombie Bigfoot Vous A Causé",degats,"De Dégats, Vous Avez Maintenant",hp_joueur,"HP")
                 print("1. Attaquer Avec Le Couteau")
                 print("2. Attaquer Avec L'Arc")
                 print("3. Attaquer Avec La BOMBE DE L'ENFER")
                 combat=input()

                 while combat!="1" and combat!="2" and combat!="3":
                    
                       print("Cliquez Sur 1 Ou 2 Ou 3 Pour Continuer...")
                       combat=input()
                    
                 if combat=="1":
                    degats=randint(10,20)
                    hp_monstre1=hp_monstre1-degats
                    print("Vous Avez Attaqué Zombie Bigfoot Avec Le Couteau! Vous lui Avez Causé",degats,"De Dégats, Il A Maintenant",hp_monstre1,"HP")
                 if combat=="2":
                    degats=randint(25,35)
                    hp_monstre1=hp_monstre1-degats
                    fleches=fleches-1
                    print("Vous Avez Attaqué Zombie Bigfoot Avec L'Arc! Vous lui Avez Causé",degats,"De Dégats, Il A Maintenant",hp_monstre1,"HP")
                 if combat=="3":
                    degats=randint(40,60)
                    hp_monstre1=hp_monstre1-degats
                    bombe_de_lenfer=bombe_de_lenfer-1
                    print("Vous Avez Attaqué Zombie Bigfoot Avec La BOMBE DE L'ENFER! Vous lui Avez Causé",degats,"De Dégats, Il A Maintenant",hp_monstre1,"HP")
                 if hp_monstre1<=0:
                    print("BIEN JOUÉ ! Vous Avez Gagné Votre Combat Contre DEXTER Le Clown Tueur")
  
               elif fleches>0 and bombe_de_lenfer<=0 :
                   print("Aïe.. Zombie Bigfoot Vous A Causé",degats,"De Dégats, Vous Avez Maintenant",hp_joueur,"HP")
                   print("1. Attaquer Avec Le Couteau")
                   print("2. Attaquer Avec L'Arc")
                   combat=input()
                   
                   while combat!="1" and combat!="2" :
                      
                         print("Cliquez Sur 1 Ou 2 Pour Continuer...")
                         combat=input()
                    
                   if combat=="1":
                        degats=randint(10,20)
                        hp_monstre1=hp_monstre1-degats
                        print("Vous Avez Attaqué Zombie Bigfoot Avec Le Couteau! Vous lui Avez Causé",degats,"De Dégats, Il A Maintenant",hp_monstre1,"HP")
                   if combat=="2":
                        degats=randint(25,35)
                        hp_monstre1=hp_monstre1-degats
                        fleches=fleches-1
                        print("Vous Avez Attaqué Zombie Bigfoot Avec L'Arc! Vous lui Avez Causé",degats,"De Dégats, Il A Maintenant",hp_monstre1,"HP")
                   if hp_monstre1<=0:
                    print("BIEN JOUÉ ! Vous Avez Gagné Votre Combat Contre Zombie Bigfoot")
               elif fleches<=0 and bombe_de_lenfer>0:
                   print("Aïe.. Zombie Bigfoot Vous A Causé",degats,"De Dégats, Vous Avez Maintenant",hp_joueur,"HP")
                   print("1. Attaquer Avec Le Couteau")
                   print("2. Attaquer Avec La BOMBE DE L'ENFER")
                   combat=input()

                   while combat!="1" and combat!="2" :
                      
                         print("Cliquez Sur 1 Ou 2 Pour Continuer...")
                         combat=input()
                    
                   if combat=="1":
                        degats=randint(10,20)
                        hp_monstre1=hp_monstre1-degats
                        print("Vous Avez Attaqué Zombie Bigfoot Avec Le Couteau! Vous lui Avez Causé",degats,"De Dégats, Il A Maintenant",hp_monstre1,"HP")
                   if combat=="2":
                        degats=randint(40,60)
                        hp_monstre1=hp_monstre1-degats
                        bombe_de_lenfer=bombe_de_lenfer-1
                        print("Vous Avez Attaqué Zombie Bigfoot Avec La BOMBE DE L'ENFER! Vous lui Avez Causé",degats,"De Dégats, Il A Maintenant",hp_monstre1,"HP")
                   if hp_monstre1<=0:
                    print("BIEN JOUÉ ! Vous Avez Gagné Votre Combat Contre Zombie Bigfoot")
               else:
                   print("Aïe.. Zombie Bigfoot Vous A Causé",degats,"De Dégats, Vous Avez Maintenant",hp_joueur,"HP")
                   print("1. Attaquer Avec Le Couteau")
                   
                   combat=input()

                   while combat!="1" :
                      
                         print("Cliquez Sur 1 Pour Continuer...")
                         combat=input()

                    
                   
                   degats=randint(10,20)
                   hp_monstre1=hp_monstre1-degats
                   print("Vous Avez Attaqué Zombie Bigfoot Avec Le Couteau! Vous lui Avez Causé",degats,"De Dégats, Il A Maintenant",hp_monstre1,"HP")
                   if hp_monstre1<=0:
                     print("BIEN JOUÉ ! Vous Avez Gagné Votre Combat Contre Zombie Bigfoot")

            else:
                  print("Aïe.. Zombie Bigfoot Vous A Causé",degats,"De Dégats, Vous Avez Maintenant 0 HP")
                  print(hp_joueur)
                  print("Vous Avez Échoué !") 
                  print("Cliquez Sur N'Importe Quel Bouton Pour Aller Vers Le Menu..")

          if x==a and y==b:
               monstre=False
               a=4
               b=4

          if x==c and y==d:
               monstre=False
               c=4
               d=4

          if x==e and y==f:
               monstre=False
               e=4
               f=4   
    if monstre==False:
          print("Félicitation !! Vous Avez Gagné La Partie.. Vous Avez Battu Tous Les Monstres Du Jeu")
          print("Cliquez Sur N'importe Quel Touche Pour Aller Vers Le Menu")
    
    ordre=input()
start()
