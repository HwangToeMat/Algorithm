class Node():
    def __init__(self, value):
        self.value = value
        self.fin = False
        self.next = dict()


class Trie():
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head

        for word in string:
            if word not in curr_node.next:
                curr_node.next[word] = Node(word)
            curr_node = curr_node.next[word]

        curr_node.fin = string

    def auto_complete(self, string):
        curr_node = self.head

        result = []

        for word in string:
            if word not in curr_node.next:
                return "추천 검색어가 없습니다."
            else:
                curr_node = curr_node.next[word]

        if curr_node.fin:
            result.append(curr_node.fin)

        stack = list(curr_node.next.values())

        while stack:
            v = stack.pop()

            if v.fin:
                result.append(v.fin)
            stack.extend(list(v.next.values()))

        return result

    def show_list(self):
        curr_node = self.head
        stack = list(curr_node.next.values())
        result = []

        while stack:
            v = stack.pop()

            if v.fin:
                result.append(v.fin)
            stack.extend(list(v.next.values()))
        return result
