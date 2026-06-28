class PrefixTree:

    # arr - store it alphabetically - sorting?
    def __init__(self):
        self.prefixes = []

    def insert(self, word: str) -> None:
        self.prefixes.append(word)
        self.prefixes.sort()

    def search(self, word: str) -> bool:
        if word in self.prefixes:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        index = 0
        for i in range(len(prefix)):
            if index < len(self.prefixes):
                print(index)
                while index < len(self.prefixes) and len(prefix) <= len(self.prefixes[index]) and prefix[i] != self.prefixes[index][i]:
                    index += 1
            else:
                return False

        return True
        