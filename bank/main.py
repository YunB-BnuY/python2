
# 项目入口
# hello world
# 项思醒是女海王

from view import View
from bank import Bank


# 主函数: 运行入口
def main():

    # 欢迎界面
    pass
    View.welcome_view()
    # 登录
    ret = View.login()
    if not ret:
        print('=> 登录失败!')
        return

    # 实现功能
    my_bank = Bank()

    while True:
        # 进入主界面
        View.main_view()

        # 先输入数字,实现对应的功能
        n = input('请输入要操作的功能对应的编号:')
        if n == '1':
            my_bank.create_user()

        elif n == '2':
            my_bank.search_money()

        elif n == '3':
            my_bank.save_money()

        elif n == '4':
            my_bank.get_money()

        elif n == '5':
            my_bank.transform_money()

        elif n == '6':
            my_bank.modify_password()

        elif n == '7':
            my_bank.lock_card()

        elif n == '8':
            my_bank.unlock_card()

        elif n == '9':
            my_bank.makeup_card()

        elif n == '0':
            my_bank.delete_user()

        elif n == 'q':
            # 退出银行系统
            print('=> 感谢您的使用, 下次再来!')
            break
        else:
            print('=>输入有误,请重新输入...')


if __name__ == '__main__':
    main()
