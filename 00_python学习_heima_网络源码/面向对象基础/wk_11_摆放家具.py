class HouseItem:

    def __init__(self, name, area):

        self.name = name
        self.area = area

    def __str__(self):

        return "[%s] 占地 %.2f" % (self.name, self.area)


class House:

    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area

        # 剩余面积
        self.free_area = area

        # 家具名称列表
        self.item_list = []

    def __str__(self):
        return ("户型: %s\n总面积: %.2f[剩余: %.2f]\n家具: %s"
                % (self.house_type, self.area,
                   self.free_area, self.item_list))

    def add_item(self, item):

        print("要添加 %s" % item)
        # 1. 判断家具的面积
        if item.area > self.free_area:
            print("%s 的面积太大了, 无法添加" % item.name)
            return
        # 2. 将家具的名称添加到列表中
        self.item_list.append(item.name)
        # 3. 计算剩余面积
        self.free_area -= item.area


# 创建家具
bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)


print(bed)
print(chest)
print(table)

# 创建房子
my_home = House("三室两厅", 130)

my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)
print(my_home)

# 打印结果
# [席梦思] 占地 4.00
# [衣柜] 占地 2.00
# [餐桌] 占地 1.50
# 要添加 [席梦思] 占地 4.00
# 要添加 [衣柜] 占地 2.00
# 要添加 [餐桌] 占地 1.50
# 户型: 三室两厅
# 总面积: 130.00[剩余: 122.50]
# 家具: ['席梦思', '衣柜', '餐桌']
