"""
请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
实现 LRUCache 类：
LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。



示例：

输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
"""


class DLinkedNode:
    """
    双向链表
    """
    def __init__(self,key=None,value=None,prev=None,next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()  # 缓存
        # dummy head和dummy tail
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        # 容量
        self.capacity = capacity
        # 当前数量
        self.size = 0

    def get(self, key: int) -> int:
        if not key or key not in self.cache:
            return -1
        # 获取当前的节点，把节点移动到链表的头部
        node = self.cache.get(key)
        self.move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        # 判断是否存在
        if key not in self.cache:
            # 新建一个节点，添加到链表和缓存中
            node = DLinkedNode(key, value)
            self.size += 1
            self.cache[key] = node
            self.add_to_head(node)
            # 如果超过容量
            if self.size > self.capacity:
                # 删除一个节点
                node = self.remove_tail()
                self.cache.pop(node.key)
                self.size -= 1
        else:
            # 如果存在，更新值
            node = self.cache.get(key)
            node.value = value
            # 移动到头节点
            self.move_to_head(node)

    def add_to_head(self, node):
        """
        把节点添加到头节点
        :param node:
        :return:
        """
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def move_to_head(self, node):
        """
        把节点移动到头部
        :param node:
        :return:
        """
        self.remove_node(node)
        self.add_to_head(node)

    def remove_node(self, node):
        """
        删除节点
        :param node:
        :return:
        """
        node.next.prev = node.prev
        node.prev.next = node.next

    def remove_tail(self):
        """
        删除尾部的节点
        :return:
        """
        node = self.tail.prev
        self.remove_node(node)
        return node


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)
param_1 = obj.get(1)
print(param_1)
obj.put(3,3)
param_2 = obj.get(2)
print(param_2)
obj.put(4,4)
param_3 = obj.get(1)
print(param_3)
param_4 = obj.get(3)
print(param_4)
param_5 = obj.get(4)
print(param_5)


