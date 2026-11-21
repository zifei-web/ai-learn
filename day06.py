# -*- coding: utf-8 -*-
"""
Day 06 —— 周复盘 + 第一个综合小项目：命令行通讯录
日期：2026-11-22（周日，减负日）

今天不讲新知识。目标是把你前 5 天学到的所有零件，第一次组装成一个
"能真正用起来"的程序——有菜单、有状态、能增删改查。

为什么重要：
前 5 天你写的是"函数"，今天写的是"程序"。区别在于：
  函数 = 一个动作
  程序 = 一堆函数 + 状态 + 一个主循环
面试时你说"我会 Python"没人信，说"我写过一个通讯录"别人会追问细节。

项目需求
------------------------------------------------------------------
实现一个命令行通讯录，数据结构是字典：{"张三": "13800001111"}

  1. 添加联系人    重名要提示"已存在"
  2. 删除联系人    不存在要提示"查无此人"
  3. 修改电话      不存在要提示
  4. 搜索联系人    支持模糊：输"张"能搜出"张三""张伟"
  5. 显示全部      按姓名字典序排列，带序号
  6. 统计          总人数 + 按姓氏分组各几人
  0. 退出

程序骨架（菜单、主循环）我已经写好了，你只需要填 6 个函数。
------------------------------------------------------------------
"""

# ═══════════════════════════════════════════════════════════════
# 一、把下面 6 个函数实现掉
# ═══════════════════════════════════════════════════════════════


def add_contact(contacts, name, phone):
    """添加联系人。已存在则不覆盖，返回提示语。

    参数：
        contacts: 字典 {"姓名": "电话"}
        name: 姓名
        phone: 电话
    返回：
        字符串，"已添加 xxx" 或 "xxx 已存在"

    提示：用 name in contacts 判断是否存在
    """
    # TODO: 在这里写
    print("  [还没实现] add_contact")
    return ""


def delete_contact(contacts, name):
    """删除联系人。不存在返回提示语。

    返回：字符串，"已删除 xxx" 或 "查无此人：xxx"
    提示：del contacts[name] 前先判断；或用 contacts.pop(name, None)
    """
    # TODO: 在这里写
    print("  [还没实现] delete_contact")
    return ""


def update_contact(contacts, name, phone):
    """修改电话。不存在返回提示语。

    返回：字符串，"已更新 xxx" 或 "查无此人：xxx"
    """
    # TODO: 在这里写
    print("  [还没实现] update_contact")
    return ""


def find_contact(contacts, keyword):
    """模糊搜索：姓名里包含 keyword 的都算命中。

    返回：命中的 [(姓名, 电话), ...] 列表，按姓名排序
    提示：if keyword in name:  然后 sorted(结果)
    """
    # TODO: 在这里写
    print("  [还没实现] find_contact")
    return []


def list_contacts(contacts):
    """显示全部联系人，按姓名升序，带序号。

    输出示例：
        1. 李四  13900002222
        2. 张三  13800001111
    提示：sorted(contacts.items()) 按元组第一位（姓名）排序
    """
    # TODO: 在这里写
    print("  [还没实现] list_contacts")


def show_stats(contacts):
    """统计：总人数 + 按姓氏（第一个字）分组。

    输出示例：
        总人数：3
        张：2 人
        李：1 人
    提示：分组用 setdefault 或 get；输出时按姓氏排序
    """
    # TODO: 在这里写
    print("  [还没实现] show_stats")


# ═══════════════════════════════════════════════════════════════
# 二、主程序（已写好，不用改；但你要看懂它怎么调度函数）
# ═══════════════════════════════════════════════════════════════


def show_menu():
    print()
    print("=" * 30)
    print("     命令行通讯录")
    print("=" * 30)
    print("  1. 添加联系人")
    print("  2. 删除联系人")
    print("  3. 修改电话")
    print("  4. 搜索联系人")
    print("  5. 显示全部")
    print("  6. 统计")
    print("  0. 退出")
    print("=" * 30)


def main():
    contacts = {}

    while True:
        show_menu()
        choice = input("请选择操作：").strip()

        if choice == "1":
            name = input("  姓名：").strip()
            phone = input("  电话：").strip()
            print("  " + add_contact(contacts, name, phone))

        elif choice == "2":
            name = input("  要删除的姓名：").strip()
            print("  " + delete_contact(contacts, name))

        elif choice == "3":
            name = input("  姓名：").strip()
            phone = input("  新电话：").strip()
            print("  " + update_contact(contacts, name, phone))

        elif choice == "4":
            keyword = input("  搜索关键字：").strip()
            results = find_contact(contacts, keyword)
            if results:
                for i, (n, p) in enumerate(results, 1):
                    print(f"  {i}. {n}  {p}")
            else:
                print("  没有匹配的联系人")

        elif choice == "5":
            list_contacts(contacts)

        elif choice == "6":
            show_stats(contacts)

        elif choice == "0":
            print("  再见")
            break

        else:
            print("  无效选项，请重新选择")


if __name__ == "__main__":
    main()


# ═══════════════════════════════════════════════════════════════
# 三、进阶挑战（做完前面 6 个函数再来，不做也行）
# ═══════════════════════════════════════════════════════════════
#
# 挑战 1：导出 JSON
#   写一个 export_json(contacts) 函数，用 day05 学的 json.dumps
#   把通讯录打印成 JSON 字符串（ensure_ascii=False）。
#   这个能力第 7 周调大模型 API 时会天天用到。
#
# 挑战 2：按电话尾号排序
#   写一个 sort_by_tail(contacts) 函数，按电话号码最后 3 位从小到大排序。
#   提示：sorted(contacts.items(), key=lambda kv: kv[1][-3:])
#
# 挑战 3：给每个函数补上类型提示（Day03 第 20 题学的）
#   def add_contact(contacts: dict, name: str, phone: str) -> str:


# ═══════════════════════════════════════════════════════════════
# 四、周复盘：10 个自测问题（口答，不写代码）
# ═══════════════════════════════════════════════════════════════
#
# 答不上来的，回去翻对应那天的文件：
#
#  1. int("3.14") 会怎样？怎么改才能转成 3？          → day01
#  2. bool("False") 是 True 还是 False？为什么？       → day01
#  3. "a  b".split() 和 "a  b".split(" ") 结果差在哪？ → day01
#  4. for ... else 里的 else 什么时候执行？            → day02
#  5. x = nums.sort() 之后 x 是什么？                  → day04
#  6. b = a 和 c = a[:] 有什么区别？                   → day04
#  7. 函数里 print 和 return 的区别是什么？            → day03
#  8. d["k"] 和 d.get("k") 的区别？项目里该用哪个？    → day05
#  9. 列表能当字典的键吗？为什么？                     → day05
# 10. 怎么按字典的「值」降序排序？                      → day05
#
# 全部能答上，说明 W1 过关；有 3 个以上答不上，明天先花 1 小时回炉。


# ═══════════════════════════════════════════════════════════════
# 五、验收清单
# ═══════════════════════════════════════════════════════════════
# [ ] 6 个函数全部实现，没有一个 print("[还没实现]")
# [ ] 添加重名会提示"已存在"，且不会覆盖原电话
# [ ] 删除不存在的名字会提示"查无此人"
# [ ] 搜索结果为空时有提示，不为空时带序号
# [ ] 显示全部是按姓名排序的
# [ ] 统计输出的姓氏是排过序的
# [ ] 输入 0 能正常退出，不报错
# [ ] 连续添加 3 个人、删 1 个、改 1 个、搜 1 次、看统计，全流程走一遍
#
# 全流程跑通后，执行：
#   git add -A
#   git commit -m "完成 W1D6 通讯录小项目"
#   git push
