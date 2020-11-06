"""
此处存放核心业务逻辑代码
"""
from db import db_hanlder

login_user = None


# 注册功能
def register():
    print("注册功能执行中")
    while True:
        user_name = input("请输入用户名 (输入q退出): ").strip()
        if user_name == 'q':
            break

        # 1)先校验用户是否存在
        # 涉及数据操作: 查看数据
        # 传入当前用户名,查看当前用户是否存在
        user_data = db_hanlder.select(user_name)

        # 2)若不存在,让用户重新输入
        if user_data:
            print("当前用户已存在,请重新输入")
            continue

        user_pwd = input("请输入密码: ").strip()
        re_user_pwd = input("请再次输入密码: ").strip()

        # 3)检验两次密码是否一致
        if user_pwd == re_user_pwd:
            # 4)将当前用户写入文件中
            db_hanlder.save(user_name, user_pwd)
            print("{} 用户注册成功".format(user_name))
            break
        else:
            print("两次密码不一致,请重新输入")


# 登陆功能
def login():
    print("登录功能执行中")
    while True:
        user_name = input("请输入用户名 (输入q退出): ").strip()

        # 1)先校验用户是否存在
        user_data = db_hanlder.select(user_name)

        # 2)若不存在,让用户重新输入
        if not user_data:
            print("当前用户不存在,请重新输入")
            continue

        user_pwd = input("请输入密码: ").strip()

        # 3)检验密码是否正确
        if user_pwd == user_data[1]:

            # 4)登陆成功后记录登陆状态
            global login_user
            login_user = user_name

            print("{} 用户登录成功".format(user_name))
            break
        else:
            print("密码错误, 登陆失败")


# 充值功能
def charge():
    print("充值功能执行中")


# 阅读小说功能
def read_novel():
    print("阅读小说功能执行中")


# 创建函数字典
fun_dic = {
    '0': register,
    '1': login,
    '2': charge,
    '3': read_novel
}


# 启动函数
def run():
    while True:
        print("""
        ===== 小说阅读器欢迎您 =====
                0、账号注册
                1、账号登录
                2、充值功能
                3、阅读小说
                q、退出
        =====       end      =====
        """)
        choice = input("请输入功能编号: ").strip()
        if choice == 'q':
            print("退出小说阅读软件")
            break

        # 判断用户输入的编号是否在函数字典中
        if choice not in fun_dic:
            print("当前编号有误, 请重新输入")
            continue
        fun_dic[choice]()
