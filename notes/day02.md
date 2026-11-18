# Day02 · 条件分支 / 循环

日期：2026-11-18　对应练习：`day02.py`（30 题）

## 一、分支

```python
if score >= 90:
    print("A")
elif score >= 80:     # 上面不成立才轮到这
    print("B")
else:
    print("C")
```

`if / elif / else` **自上而下匹配，命中就跳出**。

> 区间判断的顺序很重要：先写 `>=90` 再写 `>=80`。如果反过来，100 分会被判成 B。

## 二、三元表达式

```python
print("奇数" if num % 2 else "偶数")
```

`A if 条件 else B`：条件成立取 A，否则取 B。

## 三、布尔运算

| 运算符 | 含义 |
|---|---|
| `and` | 都真才真 |
| `or` | 一个真就真 |
| `not` | 取反 |

Python 支持链式比较：

```python
if 18 <= age <= 35:   # 等价于 age >= 18 and age <= 35
```

## 四、for 循环与 range

```python
for i in range(5):        # 0 1 2 3 4
for i in range(1, 6):     # 1 2 3 4 5      不含 6
for i in range(1, 10, 2): # 1 3 5 7 9      步长 2
for i in range(5, 0, -1): # 5 4 3 2 1      倒序
```

**`range` 的结束值永远不包含。** 这是最常错的点。

## 五、while 循环

```python
n = 1
while n <= 5:
    print(n)
    n += 1        # ← 忘了这行就死循环
```

条件为真就一直重复。**循环体里必须有让条件趋近于假的操作**。

## 六、break 与 continue

| | 作用 |
|---|---|
| `break` | 立刻跳出**整个**循环 |
| `continue` | 跳过**本次**剩余代码，进入下一轮 |

## 七、for-else（重要）

`else` 不是"循环结束后执行"，而是：

> **循环没有被 `break` 打断、正常跑完时，才执行 `else`。**

```python
for i in range(2, n):
    if n % i == 0:
        print(False)   # 找到因数，不是素数
        break
else:
    print(True)        # 一次都没 break，才是素数
```

这是 for-else 唯一真正合适的场景：**找东西，找到了就 break，没找到才走 else**。

普通循环不需要 else，把代码写在循环外面（不缩进）就行：

```python
for i in range(1, 11):
    print(i)
print("循环结束")     # 不缩进 = 循环结束后执行
```

## 八、遍历技巧

```python
fruits = ["苹果", "香蕉"]

for f in fruits:                      # 只要元素
for i, f in enumerate(fruits, 1):     # 下标从 1 开始 + 元素
for a, b in zip([1,2], ["x","y"]):    # 两个列表按位置配对
```

## 九、嵌套循环与字符串重复

```python
for i in range(1, 6):        # 外层：行
    for j in range(1, i+1):  # 内层：列
        print("*", end="")
    print()                  # 每行结束换行

"*" * i        # 重复 i 次
```

## 十、我的错题（真实踩过）

1. **三元表达式两个分支写反** — `"奇数" if num % 2 == 0` 条件成立时 num 是偶数，却输出了"奇数"。
2. **三角形判定用 `or`** — 应全部用 `and`。用 `or` 时 `1,2,10` 也会被判成能构成三角形。
3. **素数判断逻辑反了** — 写成"有一个除不尽就判素数"，`25`、`9` 全被误判成素数。正确是"找到能整除的就不是素数"。
4. **把 `for ... else` 当成"循环后执行"** — 连用 6 次全错。普通循环不要 else。
5. **每句 print 前多两个空格** — 输出和期望对不齐，自己看半天以为错了。
6. **`if not is_weekend == True:`** — 能跑但绕，直接写 `if not is_weekend:`。
7. **`sum` 当变量名** — 覆盖内置函数，后患无穷。

## 十一、自测

- [ ] 说出 `range(1, 6)` 和 `range(1, 10, 2)` 分别产生什么
- [ ] `break` 和 `continue` 的区别，各举一例
- [ ] for-else 什么时候执行、什么时候不执行
- [ ] 为什么区间判断要先写严格条件
- [ ] `18 <= age <= 35` 这种写法是否合法
