class Celle:
    """
    class Celle har en attributt _alive som angir status
    """
    def __init__(self):
        self._alive = False

    def __str__(self):
        return f"Status er {self._alive}"
        
    # Endre status​ 
    def settDoed(self):
        self._alive = False

    def settLevende(self):
        self._alive = True
        
    # Hente status​
    def erLevende(self):
        """ Returnerer status på celles _alive attributt. """
        if self._alive:
            return True
        return False
        
    def hentStatusTegn(self):
        """ Returnerer '0' hvis levende - else '.' """
        if self.erLevende():
            return "O"
        return "."