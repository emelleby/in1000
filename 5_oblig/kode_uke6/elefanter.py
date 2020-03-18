ut_fil = open("dikt.txt","w")
ut_fil.write("1 elefant kom marsjerende ..\n")
for antall in range(2,10000):
    ut_fil.write(str(antall) + " elefanter kom marsjerende ..\n")
ut_fil.close()
