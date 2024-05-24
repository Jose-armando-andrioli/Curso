# tenho_sede = True
# if tenho_sede:
#     print("Bebo Agua")



# tenho_frio = True
# if tenho_frio:
#     print("Vestir Casado")
# else:
#     print("Vestir Camiseta")

tenho_sede=True
tenho_fome=False
estou_em_dieta = False

# if tenho_sede or tenho_fome:
#     print("Vou na Cozinha")
# else:
#     print("Fico assistindo NetFlicks")


if tenho_sede and tenho_fome:
    print("Fazer Sanduiche e coca")
elif tenho_sede and not (tenho_fome):
    if estou_em_dieta:
        print("Tomar agua")
    else:
        print("Tomar uma coquinha")
elif  not (tenho_sede) and tenho_fome:
    print("Fazer um sanduiche")
else:
    print("Fico assistindo NetFlicks")