# pip install aima3
from aima3.logic import expr,FolKB, fol_fc_ask

clauses = []



clauses.append(expr("Progenitor(Pedro,Joao)"))
clauses.append(expr("Progenitor(Antonia,Joao)"))
clauses.append(expr("Progenitor(Pedro,Clara)"))
clauses.append(expr("Progenitor(Antonia,Clara)"))
clauses.append(expr("Progenitor(Pedro,Francisco)"))
clauses.append(expr("Progenitor(Antonia,Francisco)"))
clauses.append(expr("Progenitor(Pedro,Ana)"))
clauses.append(expr("Progenitor(Antonia,Ana)"))

clauses.append(expr("Progenitor(Ana,Helena)"))
clauses.append(expr("Progenitor(Ana,Joana)"))

clauses.append(expr("Pessoa(Pedro)"))
clauses.append(expr("Pessoa(Antonia)"))
clauses.append(expr("Pessoa(Joao)"))
clauses.append(expr("Pessoa(Clara)"))
clauses.append(expr("Pessoa(Francisco)"))
clauses.append(expr("Pessoa(Ana)"))
clauses.append(expr("Pessoa(Helena)"))
clauses.append(expr("Pessoa(Joana)"))
clauses.append(expr("Pessoa(Mario)"))
clauses.append(expr("Pessoa(Carlos)"))
clauses.append(expr("Pessoa(Milene)"))
clauses.append(expr("Pessoa(Pietro)"))
clauses.append(expr("Pessoa(Enzo)"))
clauses.append(expr("Pessoa(Francisca)"))
clauses.append(expr("Pessoa(Antonia_2)"))

clauses.append(expr("Progenitor(Joao,Mario)"))
clauses.append(expr("Progenitor(Helena,Carlos)"))

clauses.append(expr("Progenitor(Carlos,X) ==> Pessoa(X)"))
clauses.append(expr("Progenitor(Helena,X) ==> Pessoa(X)"))
clauses.append(expr("Progenitor(Joao,X) ==> Pessoa(X)"))
clauses.append(expr("Progenitor(Ana,X) ==> Pessoa(X)"))
clauses.append(expr("Progenitor(Pedro,X) ==> Pessoa(X)"))
clauses.append(expr("Progenitor(Antonia,X) ==> Pessoa(X)"))
clauses.append(expr("Progenitor(X,Y) ==> Pessoa(Y)"))

clauses.append(expr("Progenitor(x,y) ==> Descendente(y,x)"))

clauses.append(expr("Progenitor(x,y) & Sexo(x,Masculino) ==> Pai(x,y)"))
clauses.append(expr("Progenitor(x,y) & Sexo(x,Feminino) ==> Mae(x,y)"))

clauses.append(expr("Progenitor(x,y) & Progenitor(x,z) & Sexo(y,Masculino) ==> Irmao(y,z)"))
clauses.append(expr("Progenitor(x,y) & Progenitor(x,z) & Sexo(y,Feminino) ==> Irma(y,z)"))

clauses.append(expr("Progenitor(x,y) & Progenitor(z,y) & Sexo(y,Masculino) ==> Irmao(x,z)"))
clauses.append(expr("Progenitor(x,y) & Progenitor(z,y) & Sexo(y,Feminino) ==> Irma(x,z)"))

clauses.append(expr("Progenitor(Clara,X) & Progenitor(Clara,Y) & Sexo(X,Feminino) & Sexo(Y,Feminino) ==> Irma(X,Y)"))

clauses.append(expr("Progenitor(Francisco,X) & Progenitor(Francisco,Y) & Sexo(X,Masculino) & Sexo(Y,Masculino) ==> Irmao(X,Y)"))
clauses.append(expr("Progenitor(Francisco,X) & Progenitor(Francisco,Y) & Sexo(X,Feminino) & Sexo(Y,Feminino) ==> Irma(X,Y)"))

clauses.append(expr("Progenitor(X,Carlos) & Progenitor(Y,Carlos) & Progenitor(Y,Helena) & Sexo(X,Masculino) ==> Pai(X,Carlos)"))
clauses.append(expr("Progenitor(X,Carlos) & Progenitor(Y,Carlos) & Progenitor(Y,Helena) & Sexo(X,Feminino) ==> Mae(X,Carlos)"))




Genealogia = FolKB(clauses)

perguntas = ["Sexo(x,Masculino)",
             "Sexo(Antonia,x)",
             "Irmao(x,Ana)",
             "Irma(x,Joao)",
             "Descendente(x,Antonia)",
             "Descendente(Joao,x)",
             "Pessoa(x)",
             "Mae(x,y)",
             "Pai(x,y)"]



for i in perguntas:
    resposta = fol_fc_ask(Genealogia, expr(i))
    print("%s -> %s" %(i, (list(resposta))))

