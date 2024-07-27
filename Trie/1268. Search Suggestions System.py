from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.products = []  # List to store products that pass through this node

class Trie:
    def __init__(self):
        self.root = TrieNode()  # Root of the Trie
    
    def insert(self, product: str):
        node = self.root
        for char in product:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            # Add the product to the node's products list
            if len(node.products) < 3:
                node.products.append(product)
            node.products.sort()
            if len(node.products) > 3:
                node.products.pop()
    
    def search(self, prefix: str) -> List[str]:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return node.products

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Sort products to ensure lexicographical order
        products.sort()
        
        # Initialize the Trie and insert all products
        trie = Trie()
        for product in products:
            trie.insert(product)
        
        # Collect results for each prefix of the search word
        result = []
        prefix = ""
        for char in searchWord:
            prefix += char
            result.append(trie.search(prefix))
        
        return result

# Example usage
solution = Solution()
products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
searchWord = "mouse"
print(solution.suggestedProducts(products, searchWord))
# Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]

products = ["havana"]
searchWord = "havana"
print(solution.suggestedProducts(products, searchWord))
# Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
