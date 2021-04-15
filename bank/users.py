
# 用户

class User:
    def __init__(self, name, phone, idcard, card):
        self.name = name  # 用户名
        self.phone = phone  # 电话
        self.idcard = idcard  # 身份证号
        self.card = card  # 银行卡对象

    def __repr__(self):
        return f'姓名:{self.name} 电话:{self.phone} 身份证:{self.idcard} 银行卡:({self.card})'