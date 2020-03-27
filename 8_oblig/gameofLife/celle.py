class Celle:
    # Konstruktør​
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
        if self._alive:
            return True
        return False
        
    def hentStatusTegn(self):
        if self.erLevende():
            return "O"
        return "."