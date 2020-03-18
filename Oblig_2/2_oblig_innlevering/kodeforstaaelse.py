#!usr/bin/env python3

# 1. Lovlig er vel koden, men den er litt overkomplisert og vil gi feilmelding og er vel derfor ugyldig.
# 2. I siste linje vil vi få feil siden b er int og "Hei" er str.

a = input ( "Tast inn et heltall! " )
b = int ( a )
if b < 10 :
    print ( b + " Hei!" )