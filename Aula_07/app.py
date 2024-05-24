# Função deverá ser declarada no inicio do codigo
def fazer_big_mac(nome):
    print(f'Ser(a) {nome} seu pedido ja esta pronto')
    print('Favor retira-lo')                                # Toda continuação da função deverá estar identada para ser
                                                             # reconhecida

def fazer_batata(tamanho):
    print(f'Batata no tamanho {tamanho}')

def preparar_refrigerante(tipo,tamanho):
    print(f'Tipo {tipo} de {tamanho}')

# fazer_big_mac('Jose Armando')
# fazer_batata('grande')
# preparar_refrigerante('Guarana','700 ml')

def fazer_combo_big_mac(nome,tamanho_batata,tipo_refri,tamanho_refri):
    fazer_big_mac(nome)
    fazer_batata(tamanho_batata)
    preparar_refrigerante(tipo_refri,tamanho_refri)

# fazer_combo_big_mac('Jose Armando','Media','Guarana','700 ml')

def maior_valor(lista_valores):
    lista_valores.sort()
    lista_valores.reverse()
    return lista_valores[0]


vlr_maior = maior_valor([10,333,60.24,50,78,88,67890])
print(vlr_maior)