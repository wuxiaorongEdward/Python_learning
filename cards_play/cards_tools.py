cards_list = []


def cards_menu():

    """打印菜单选项"""
    print("*" * 50)
    print("1、 新增名片")
    print("2、 显示所有名片")
    print("3、 查询名片")
    print("")
    print("0、  退出【名片管理系统】")
    print("*" * 50)


def new_card():

    """新增名片"""
    print("新增名片")
    # 添加名片元素  name phone qq email
    name_str = input("请输入姓名 ： ")
    phone_str = input("请输入电话 ： ")
    qq_str = input("请输入QQ ： ")
    email_str = input("请输入邮箱 ： ")
    # 添加到名片列表中
    card_dict = {
        "name" : name_str,
        "phone": phone_str,
        "qq" : qq_str,
        "email": email_str
    }
    cards_list.append(card_dict)
    print("+" * 50)
    print(" %s 的名片添加成功 ！" % name_str)
    print("+" * 50)


def show_all():

    """显示所有名片"""
    if len(cards_list) == 0:
        print("当前名片系统中没有名片，请先添加名片")
        return
    print("姓名\t\t\t电话\t\t\tQQ号\t\t\t邮箱")
    print("=" * 50)
    for card in cards_list:
        print("%-10s\t\t%-10s\t\t%-10s\t\t%-10s" % (card["name"],
                                                card["phone"],
                                                card["qq"],
                                                card["email"]))
    print("=" * 50)


def search_card():

    """查询名片"""
    find_name = input("请输入要查询的名字：")
    print("姓名\t\t\t电话\t\t\tQQ号\t\t\t邮箱")
    print("-" * 50)
    for card_dict in cards_list:
        if card_dict["name"] == find_name:
            print("%-10s\t\t%-10s\t\t%-10s\t\t%-10s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))
            # TODO 针对查询到的名片的操作
            deal_card(card_dict)
            break
    else:
        print("你查询的名片不存在 ！")
    print("-" * 50)


def deal_card(card_dict):

    """处理查询到的名片"""
    action_str = input("请输入接下来的操作 [1] 修改 [2] 删除 [0] 返回上一级菜单 ： " )
    if action_str == "1":
        card_dict["name"] = update_card(card_dict["name"], "姓名[不修改则按回车键] ： ")
        card_dict["phone"] = update_card(card_dict["phone"], "电话[不修改则按回车键] ： ")
        card_dict["qq"] = update_card(card_dict["qq"], "QQ[不修改则按回车键] ： ")
        card_dict["email"] = update_card(card_dict["email"], "邮箱[不修改则按回车键] ： ")
        print("修改成功 ！")
    elif action_str == "2":
        cards_list.remove(card_dict)
        print("删除成功 ！")


def update_card(dict_value, tip_message):
    input_str = input(tip_message)
    if len(input_str) > 0:
        return input_str
    else:
        return dict_value



