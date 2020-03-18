for linje in open('aarsnedbor.csv'):
    maks = 0
    regn_per_dag = linje.split()
    for regn_tekst in regn_per_dag:
        regn = float(regn_tekst)
        if regn>maks:
            maks = regn
    print(maks)
