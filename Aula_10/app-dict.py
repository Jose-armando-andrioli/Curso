meses = {
 "jan" : "Janeiro"
,"fev" : "Fevereiro"
,"mar" : "Março"
,"abr" : "Abril"
,"mai" : "Maio"
,"jun" : "Junho"
,"jul" : "Julho"
,"ago" : "Agosto"
,"set" : "Setembro"
,"out" : "Outubro"
,"nov" : "Novembro"
,"dez" : "Dezembro"
}

#print(meses["xxx"])   # Quando coloca o print e não tem na coleção, da erro

print(meses.get("xxx","Não existe"))  