import heapq

class Node:
    def __init__(self, freq, char, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right
        self.huff = ''
    def __lt__(self, nxt):
        return self.freq < nxt.freq

def print_codes(node, code=''):
    new_code = code + str(node.huff)
    if node.left:
        print_codes(node.left, new_code)
    if node.right:
        print_codes(node.right, new_code)
    if not node.left and not node.right:
        print(f"{node.char} -> {new_code}")

# ---------- Main ----------
n = int(input("Enter number of characters: "))
chars, freq = [], []
for i in range(n):
    c = input("Enter character: ")
    f = int(input("Enter frequency: "))
    chars.append(c)
    freq.append(f)

nodes = [Node(freq[i], chars[i]) for i in range(n)]
heapq.heapify(nodes)

while len(nodes) > 1:
    l = heapq.heappop(nodes)
    r = heapq.heappop(nodes)
    l.huff, r.huff = 0, 1
    new = Node(l.freq + r.freq, l.char + r.char, l, r)
    heapq.heappush(nodes, new)

print("\nHuffman Codes:")
print_codes(nodes[0])
