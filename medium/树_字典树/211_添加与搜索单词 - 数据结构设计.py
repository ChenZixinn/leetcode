"""
请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。

实现词典类 WordDictionary ：

WordDictionary() 初始化词典对象
void addWord(word) 将 word 添加到数据结构中，之后可以对它进行匹配
bool search(word) 如果数据结构中存在字符串与 word 匹配，则返回 true ；否则，返回  false 。word 中可能包含一些 '.' ，每个 . 都可以表示任何一个字母。

"""

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def insert(self, word:str):
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            if not node.children[ch]:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEnd = True

class WordDictionary:

    def __init__(self):

        self.trieRoot = TrieNode()


    def addWord(self, word: str) -> None:
        self.trieRoot.insert(word)


    def search(self, word: str) -> bool:
        def dfs(index, node):
            if index == len(word):
                return node.isEnd
            if word[index] != '.':
                ch = ord(word[index]) - ord('a')
                if not node.children[ch]:
                    return False
                else:
                    return dfs(index+1, node.children[ch])
            else:
                for child in node.children:
                    if child is not None and dfs(index+1, child):
                        return True

            return False
        return dfs(0, self.trieRoot)

# Your WordDictionary object will be instantiated and called as such:
word = "abc"
word1 = 'acc'
obj = WordDictionary()
obj.addWord(word)
obj.addWord(word1)
param_2 = obj.search('abc')
print(param_2)