import cards_tools


while True:

    # 菜单选项
    # 打印欢迎
    print("欢迎使用名片系统 V 1.0 ")
    cards_tools.cards_menu()
    choice = input("请选择一个功能 : ")
    print("你的选择是 【%s】" % choice)

    # 1 新增名片 2 显示所有 3 查询名片名片 0 退出名片查询系统
    if choice in ["1", "2", "3"]:
        if choice == "1":
            cards_tools.new_card()
        elif choice == "2":
            cards_tools.show_all()
        else :
            cards_tools.search_card()
    elif choice == "0":
        print("欢迎再次使用【名片管理系统】")
        break
    else:
        print("你输入的选项错误，请重新选择！")
