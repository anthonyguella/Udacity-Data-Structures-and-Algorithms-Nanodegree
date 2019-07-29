import sys
import heapq

class Huffman_Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __gt__(self, other):
        if not other:
            return -1
        if not isinstance(other, Huffman_Node):
            return -1
        return self.freq > other.freq

class Huffman_Coding:

    def encode(self, text):
        if text == "":
            return "", None
        frequency_dict = self.make_frequency_dict(text)
        min_heap = self.min_heapify_dict(frequency_dict)
        merged_heap = self.merge_nodes(min_heap)
        tree = heapq.heappop(merged_heap)
        codes = self.make_codes(tree)
        encoded_text = self.get_encoded_text(text, codes)
        return encoded_text, tree

    def decode(self, encoded_text, tree):
        decoded_string = ""

        if encoded_text == "":
            return decoded_string

        current_node = tree

        for char in encoded_text:
            if char == '0':
                current_node = current_node.left
            else:
                current_node = current_node.right
            if current_node.char is not None:
                decoded_string += current_node.char
                current_node = tree
        return decoded_string  

    def make_frequency_dict(self, text):
        frequency = {}
        for char in text:
            if not char in frequency:
                frequency[char] = 0
            frequency[char] += 1
        return frequency

    def min_heapify_dict(self, frequency):
        heap = []
        for key in frequency:
            node = Huffman_Node(key, frequency[key])
            heapq.heappush(heap, node)
        return heap

    def merge_nodes(self, heap):
        if len(heap) == 1:
            node = heapq.heappop(heap)
            new_node = Huffman_Node(None, node.freq)
            new_node.left = node
            heapq.heappush(heap, new_node)
        while len(heap) > 1:
            node1 = heapq.heappop(heap)
            node2 = heapq.heappop(heap)

            new_node = Huffman_Node(None, node1.freq + node2.freq)
            new_node.left = node1
            new_node.right = node2

            heapq.heappush(heap, new_node)
        return heap

    def make_codes(self, tree):
        if tree.left is None and tree.right is None:
            return {tree.char:'0'}
        return self.make_codes_recursive(tree, "")

    def make_codes_recursive(self, root, current_code):
        codes = {}

        if root is None:
            return {}

        if root.char is not None:
            codes[root.char] = current_code
        
        codes.update(self.make_codes_recursive(root.left, current_code + "0"))
        codes.update(self.make_codes_recursive(root.right, current_code + "1"))
        return codes

    def get_encoded_text(self, text, codes):
        encoded_text = ""
        for char in text:
            encoded_text += codes[char]
        return encoded_text

if __name__ == "__main__":
    huffman_coding = Huffman_Coding()

    print("**** Test 1 ****\nRegular Sentence\n")
    test_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(test_sentence)))
    print ("The content of the data is: {}\n".format(test_sentence))

    encoded_data, tree = huffman_coding.encode(test_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_coding.decode(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


    print("**** Test 2 ****\nSingle Character\n")
    test_sentence = "a"

    print ("The size of the data is: {}\n".format(sys.getsizeof(test_sentence)))
    print ("The content of the data is: {}\n".format(test_sentence))

    encoded_data, tree = huffman_coding.encode(test_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_coding.decode(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


    print("**** Test 3 ****\nSingle Character Repeated\n")
    test_sentence = "aaaaaaa"

    print ("The size of the data is: {}\n".format(sys.getsizeof(test_sentence)))
    print ("The content of the data is: {}\n".format(test_sentence))

    encoded_data, tree = huffman_coding.encode(test_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_coding.decode(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


    print("**** Test 4 ****\nSame Letter, Different Case\n")
    test_sentence = "aaAAbbBB"

    print ("The size of the data is: {}\n".format(sys.getsizeof(test_sentence)))
    print ("The content of the data is: {}\n".format(test_sentence))

    encoded_data, tree = huffman_coding.encode(test_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_coding.decode(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    print ("The size of the data is: {}\n".format(sys.getsizeof(test_sentence)))
    print ("The content of the data is: {}\n".format(test_sentence))

    encoded_data, tree = huffman_coding.encode(test_sentence)

    decoded_data = huffman_coding.decode(encoded_data, tree)