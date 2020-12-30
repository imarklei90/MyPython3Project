# Demo：使用函数实现增删改查操作

def show_menus():
    print('-----用户信息管理-----')
    print('1. 添加信息')
    print('2. 删除信息')
    print('3. 修改信息')
    print('4. 查找信息')
    print('5. 显示所有信息')
    print('6. 退出系统')


# 全局变量存储信息
infos = []


# 添加信息
def add_info():
    # 根据名称查找是否存在
    name = input('输入需要添加的名称:')
    age = input('输入需要添加的年龄:')
    # 如果存在则不需要添加，否则需要添加信息
    global infos
    for info in infos:
        if name == info['name']:
            print('用户名存在')
            break
    else:
        print('不存在，可以添加信息')
        user = {}
        user['name'] = name
        user['age'] = age

        infos.append(user)
    print(infos)


# 查找信息
def find_user():
    # 根据名称查找信息
    name = input('请输出需要查找的姓名：')
    for info in infos:
        if name == info['name']:
            print(info)
            break
    else:
        print('查找的用户不存在')


# 删除信息
def del_info():
    # 根据名称删除信息
    name = input('输入需要删除的名称: ')

    # 先查找是否存在，存在则删除，否则给出提示信息
    for info in infos:
        if name == info['name']:
            infos.remove(info)
            print('删除成功')
            break
    else:
        print('要删除的用户不存在')

    print('当前用户列表:%s' % infos)


# 修改信息
def update_info():
    # 根据名称修改信息
    name = input('输入需要修改的名称：')
    for info in infos:
        if name == info['name']:
            info['name'] = name
            info['age'] = input(f'输入需要修改的{name}对应的age：')
            # info['gender'] = input(f'输入需要修改的{name}对应的gender：')
            break
    else:
        print('需要更新的用户不存在')


# 列出所有的用户
def list_users():
    # 查找所有的用户
    for info in infos:
        print(f"名称: {info['name']}, 年龄: {info['age']}")


while True:
    # 显示操作菜单
    show_menus()
    user_input = input('请选择需要执行的操作:')

    if user_input == '1':
        add_info()
    elif user_input == '2':
        del_info()
    elif user_input == '3':
        update_info()
    elif user_input == '4':
        find_user()
    elif user_input == '5':
        list_users()
    elif user_input == '6':
        break
