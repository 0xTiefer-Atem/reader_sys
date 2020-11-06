"""
此处存放核心业务逻辑代码
"""
import os

# 获取项目根目录
BASE_PATH = os.path.dirname(os.path.dirname(__file__))

# 获取db目录路径
DB_PATH = os.path.join(BASE_PATH, 'db')

# 查看数据
def select(user_name):
    # db.txt的根目录
    db_path = os.path.join(DB_PATH, 'db.txt')
    with open(db_path, mode='rt', encoding='utf-8') as account_file:
        # 判断接收过来的用户名是否存在db.txt文件中
        if user_name in account_file.read():
            pass


# 注册功能
def register():
    print("注册功能执行中")
    while True:
        user_name = input("请输入用户名: ").strip()

        # 1)先校验用户是否存在
        # 涉及数据操作: 查看数据
        # 传入当前用户名,查看当前用户是否存在
        select(user_name)

        user_pwd = input("请输入密码: ").strip()
        re_user_pwd = input("请再次输入密码: ").strip()

        # 2)检验两次密码是否一致
        if user_pwd == re_user_pwd:
            print("{} 用户注册成功".format(user_name))
            break
        else:
            print("两次密码不一致,请重新输入")


# 登陆功能
def login():
    print("登录功能执行中")


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
