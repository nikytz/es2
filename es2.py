tupla_vendite = (
                (("RepartoA","Informatica"),("Prodotto A", ("contanti",1000))),
                (("RepartoA","Informatica"),("Prodotto B", ("carta di credito",1500))),
                (("RepartoA","Informatica"),("Prodotto C", ("carta di credito",1200))),
                (("RepartoA","Informatica"),("Prodotto D", ("contanti",200))),
                (("RepartoA","Informatica"),("Prodotto E", ("contanti",800))),
                (("RepartoA","Informatica"),("Prodotto F", ("N/D",200))),
                (("RepartoB","Elettronica"),("Prodotto A", ("contanti",1500))),
                (("RepartoB","Elettronica"),("Prodotto B", ("carta di credito",900)))
                )
def media_globale(tupla_vendite):
    somma=0
    conta=0
    for(reparto,materia),(prodotto,(metodo,soldi))in tupla_vendite:
      somma+=soldi
      conta+=1
    return somma/conta
print(f"la media globale è di: {media_globale(tupla_vendite)}")

nuovaMateria=input("inserisci la materia: ")
nuovoMetodo=input("inserisci il metodo di pagamento: ")
def media(tupla_vendite, nuovaMateria, nuovoMetodo):
    somma=0
    conta=0
    for(reparto,materia),(prodotto,(metodo,soldi))in tupla_vendite:
      if (nuovaMateria==materia)and(nuovoMetodo==metodo):
        somma+=soldi
        conta+=1
    return somma/conta
print(media(tupla_vendite,nuovaMateria, nuovoMetodo))

def venditaMax(tupla_vendite):
    max=0
    prodottoMax=[]
    for(reparto,materia),(prodotto,(metodo,soldi))in tupla_vendite:
      if soldi>max:
        max=soldi
    for(reparto,materia),(prodotto,(metodo,soldi))in tupla_vendite:
      if soldi==max:
        prodottoMax.append((prodotto,soldi))
    return (max, prodottoMax)
print(f"la vendita massima è di: {venditaMax(tupla_vendite)}")

def venditaMinima(tupla_vendite):
  min=100000
  for(reparto,materia),(prodotto,(metodo,soldi))in tupla_vendite:
    if reparto=="RepartoA" and soldi<min:
      min=soldi
  return min
print(f"la vendita minima del reparto A è di: {venditaMinima(tupla_vendite)}")

def venditaPer(tupla_vendite):
  sommaA=0
  sommaB=0
  conta=0
  sommaTot=0
  repartoVendita=[]
  for(reparto,materia),(prodotto,(metodo,soldi))in tupla_vendite:
    if reparto=="RepartoA":
      sommaA+=soldi
      conta+=1
  for(reparto,materia),(prodotto,(metodo,soldi))in tupla_vendite:
    if reparto=="RepartoB":
      sommaB+=soldi
      conta+=1
  for(reparto,materia),(prodotto,(metodo,soldi))in tupla_vendite:
    if reparto=="RepartoB":
      sommaB+=soldi
      conta+=1
  for(reparto,materia),(prodotto,(metodo,soldi))in tupla_vendite:
    sommaTot+=soldi
    conta+=1
  percentualeA=sommaA/sommaTot*100
  percentualeB=sommaB/sommaTot*100
  return (percentualeA,percentualeB)

pA,pB=venditaPer(tupla_vendite)
print(f"la percentuale di vendita del reparto A è di: {pA} e quello del reparto B è di {pB}")
    
