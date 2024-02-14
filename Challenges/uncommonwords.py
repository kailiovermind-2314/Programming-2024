"""
句子 是一串由空格分隔的单词。每个 单词 仅由小写字母组成。
如果某个单词在其中一个句子中恰好出现一次，在另一个句子中却 没有出现 ，那么这个单词就是 不常见的 。
给你两个 句子 s1 和 s2 ，返回所有 不常用单词 的列表。返回列表中单词可以按 任意顺序 组织。
"""
s1 = "apple apple apple".split()
s2 = "banana banana".split()

wordcounter = {}
for w in s1 + s2:
  wordcounter[w] = wordcounter.get(w, 0) + 1

print([word for word in wordcounter if wordcounter[word] == min(wordcounter.values())])
