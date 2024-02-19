"""
Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。

请你实现 Trie 类：

Trie() 初始化前缀树对象。
void insert(String word) 向前缀树中插入字符串 word 。
boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。


示例：

输入
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
输出
[null, null, true, false, true, null, true]
"""
from typing import Optional


class Trie:

    def __init__(self):
        self.is_end = False
        self.children = [None] * 26

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.is_end = True

    def search_prefix(self, word: str) -> Optional["Trie"]:
        node = self
        for w in word:
            ch = ord(w) - ord('a')
            if not node.children[ch]:
                return None
            node = node.children[ch]
        return node

    def search(self, word: str) -> bool:
        node = self.search_prefix(word)
        return node and node.is_end

    def startsWith(self, prefix: str) -> bool:
        return True if self.search_prefix(prefix) else False


if __name__ == '__main__':
    trie = Trie()
    trie.insert('word')
    trie.insert('apple')
    res = trie.search('wo')
    print(res)

    res = trie.startsWith('ao')
    print(res)
