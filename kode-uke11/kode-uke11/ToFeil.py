
def differanse(tall1, tall2):
    # Differanse er minus, ikke pluss: logisk feil
    return tall1 + tall2

def hovedprogram():
    x = float(input("Tast inn forste tall: "))
    y = float(input("Tast inn andre tall: "))

    diff = differanse(x, y)
    # I print-setningen mangler det komma: syntaksfeil
    print("Differansen mellom" x "og" y "er" diff)

hovedprogram()
