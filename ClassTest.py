#class 정의
class Sports:
    def __init__(self,teamname):    #class를 구성하는 methods
        self.teamname = teamname 
        print(f"{self.teamname}팀에 대한 정보입니다.")
    def won(self, won):
        print(f"{self.teamname} 팀은 {won}회 승리하였습니다.")
    def loss(self, loss):
        print(f"{self.teamname} 팀은 {loss}회 패배하였습니다.")
    def draw(self, draw):
        print(f"{self.teamname} 팀은 {draw}회 비겼습니다.")

#instance 생성
SNFC = Sports(SeongnamFC)
SNFC.won(20)
SNFC.loss(5)
SNFC.draw(8)

#class inheritance
class Baseball(Sports):
    def __init__ (self, teamname):
        self.teamname = teamname
    #overriding
    def draw(self, draw):
        super().work(draw)
        print(f"{self.teamname} 팀은 {draw}회 연장전에 돌입했습니다.")        

class Soccer(Sports):
    def __init__ (self, teamname):
        self.teamname = teamname

SNFC = Soccer(SeongnamFC)
SNFC.won(20)
SNFC.loss(5)
SNFC.draw(8)

LGT = Baseball(LG_Twins)
LGT.won(40)
LGT.loss(14)
LGT.draw(19)