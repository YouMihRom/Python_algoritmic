import heapq
from collections import Counter, namedtuple


class Node(namedtuple('Node', ['left', 'right'])):
    def walk(self, code, prefix):# prefix - префикс узла, накапливающийся по мере спуска по дереву
        self.left.walk(code, prefix + '0')# левый потомок
        self.right.walk(code, prefix + '1')# правый потомок


class Leaf(namedtuple('Leaf', ['simbol'])):
    def walk(self, code, prefix):
        code[self.simbol] = prefix or '0'


def huffman_encode(start_str):
    que = []# Очередь, состоит из частоты использования элемента(freq) и его значения
    for simbol, freq in Counter(start_str).items():
        que.append((freq, len(que), Leaf(simbol)))

    heapq.heapify(que)# построение очереди с приоритетом

    count = len(que)
    while len(que) > 1:
        freq1, _count1, left = heapq.heappop(que)
        freq2, _count2, right = heapq.heappop(que)
        heapq.heappush(que, (freq1 + freq2, count, Node(left, right)))
        count += 1

    code = {}
    if que:
        [(_freq, _count, root)] = que
        root.walk(code, '')
    return code


def main():
    start_str = input('Введите кодируемую строку: ')
    sim_code = huffman_encode(start_str)
    encoded = ''.join(sim_code[simb] for simb in start_str)
    print(f'В строке {len(sim_code)} различных символов')
    for ch in sorted(sim_code):
        print('{}: {}:'.format(ch, sim_code[ch]))
    print(f'Закодированная строка: {encoded}')


main()
