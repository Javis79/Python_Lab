class AhoCorasick:
    def __init__(self, words):
        self.trie = {}
        self.output = {}
        self.fail = {}
        self._build_trie(words)

    def _build_trie(self, words):
        for word in words:
            node = self.trie
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['$'] = word

        self.fail = {}
        self.output = {}
        queue = []

        for char, node in self.trie.items():
            if char != '$':
                self.fail[id(node)] = self.trie
                queue.append((node, char))

        while queue:
            current_node, parent_char = queue.pop(0)
            for char, next_node in current_node.items():
                if char == '$':
                    continue
                fail_node = self.fail.get(id(current_node))
                while fail_node and char not in fail_node:
                    fail_node = self.fail.get(id(fail_node))
                self.fail[id(next_node)] = fail_node[char] if fail_node and char in fail_node else self.trie
                if '$' in self.fail[id(next_node)]:
                    self.output[id(next_node)] = self.output.get(id(next_node), []) + [self.fail[id(next_node)]['$']]
                queue.append((next_node, char))

    def search(self, text):
        result = []
        node = self.trie

        for i, char in enumerate(text):
            while node and char not in node:
                node = self.fail.get(id(node))
            if not node:
                node = self.trie
                continue
            node = node[char]

            if '$' in node:
                result.append((i - len(node['$']) + 1, node['$']))
            for word in self.output.get(id(node), []):
                result.append((i - len(word) + 1, word))

        return result

#Przykład użycia
if __name__ == "__main__":
    words = ["ja", "an", "anna", "nap"]
    text = "ajanapansanna"

    ac = AhoCorasick(words)
    matches = ac.search(text)

    for start_index, word in matches:
        print(f"Znaleziono '{word}' na pozycji {start_index}")
