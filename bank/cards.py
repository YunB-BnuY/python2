
# 银行卡
class Card:
    def __init__(self, cardid, passwd, money, islock=False):
        self.cardid = cardid  # 卡号
        self.passwd = passwd  # 密码
        self.money = money  # 余额
        self.islock = islock  # 是否锁住

    def __repr__(self):
        return f'卡号:{self.cardid} 密码:{self.passwd} 余额:{self.money} 锁住:{self.islock}'