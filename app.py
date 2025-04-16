import pyxel
from random import randint

class Pong:
    def __init__(self):
        self.TITLE = "PONG"
        self.WIDTH = 300
        self.HEIGHT = 200
        self.RAYON = 10
        self.FRAME_REFRESH = 15
        pyxel.init(self.WIDTH,self.HEIGHT,title=self.TITLE)
        pyxel.load("res.pyxres", False, False, False, False)
        self.score1 = 0
        self.score2 = 0
        self.largeur = 40
        self.compteur = 0
        self.pos1 = self.HEIGHT//2-self.largeur//2
        self.pos2 = self.HEIGHT//2-self.largeur//2
        self.direction = [3,3]
        self.balle = [(self.WIDTH)//2-3,randint(40,self.HEIGHT-40)]
        self.etat = 0


    def update(self):
        self.move_raq1()
        self.move_raq2()

    def move_raq1(self):
        if pyxel.btn(pyxel.KEY_A) and self.pos1 > 0:
            self.pos1 -= 2
        if pyxel.btn(pyxel.KEY_Q) and self.pos1 + self.largeur < self.HEIGHT:
            self.pos1 += 2

    def move_raq2(self):
        if pyxel.btn(pyxel.KEY_P) and self.pos2 > 0:
            self.pos2 -= 2
        if pyxel.btn(pyxel.KEY_M) and self.pos2 + self.largeur < self.HEIGHT:
            self.pos2 += 2
    
    def dessine_terrain(self):
        pyxel.cls(7)
        pyxel.rect(2,2,(self.WIDTH-8) // 2, (self.HEIGHT - 4), 0)
        pyxel.rect(self.WIDTH // 2 + 2, 2, (self.WIDTH-8) // 2, (self.HEIGHT - 4), 0)
        
    def dessine_raquettes(self):
        pyxel.rect(4, self.pos1, 6, self.largeur, 7)
        pyxel.rect(self.WIDTH - 4 - 6, self.pos2, 6, self.largeur, 7)
        
    def dessine_balle(self):
        x, y = self.balle
        pyxel.circ(x, y, self.RAYON, 7)

    def draw(self):
        self.dessine_terrain()
        self.dessine_raquettes()
        self.dessine_balle()
        
if __name__ == "__main__":
    game=Pong()
    pyxel.run(game.update,game.draw)




