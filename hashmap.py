class HashMap:
    def __init__(self, size=8, load_factor=0.75):
        self.load_factor = load_factor
        self.size = size
        self.num_elements = 0
        self.hashMap = [[] for _ in range(size)]

    def __contains__(self, key):
        """Returns True if the key is in the HashMap, False otherwise."""
        for i in range(self.size):
            if len(self.hashMap[i]) == 0 or self.hashMap[i][0][0] != key:
                continue
            else:
                return True
        return False

    def put(self, key, value):
        """Inserts a key-value pair into the HashMap."""
        print(self.num_elements)
        print(self.size)
        if self.num_elements >= self.size * self.load_factor:
            self._rehash()

        index = hash(key) % self.size

        while len(self.hashMap[index]) != 0 and self.hashMap[index][0][0] != key:
            index = (index + 1) % self.size

        if len(self.hashMap[index]) == 0:
            self.hashMap[index].append((key, value))
            self.num_elements += 1
        else:
            old_val = self.hashMap[index][0][1]
            self.hashMap[index].clear()
            self.hashMap[index].append((key, old_val + value))

    def __repr__(self):
        """Returns a string representation of the HashMap."""
        return str(self.hashMap)

    def get(self, key):
        """Returns the value associated with the given key."""
        index = hash(key) % self.size
        while len(self.hashMap[index]) != 0:
            if self.hashMap[index][0][0] == key:
                return self.hashMap[index][0][1]
            index = (index + 1) % self.size
        return None

    def remove(self, key):
        """Removes the key-value pair associated with the given key."""
        if self.get(key) == None:
            return None

        index = hash(key) % self.size
        while len(self.hashMap[index]) != 0:
            if self.hashMap[index][0][0] == key:
                break
            index = (index + 1) % self.size

        self.hashMap[index].clear()
        self.num_elements -= 1
        self._rearrange(index)

    def _rearrange(self, start):
        """Rearranges the elements of the HashMap."""
        index = (start + 1) % self.size
        while len(self.hashMap[index]) != 0:
            next_index = (index + 1) % self.size
            if hash(self.hashMap[index][0][0]) % self.size != index:
                self.hashMap[start].append(self.hashMap[index][0])
                self.hashMap[index].clear()
                start = index
            index = next_index

    def _rehash(self):
        """Rehashes the HashMap."""
        tempSize = self.size
        self.size *= 2
        refHashMap = self.hashMap.copy()
        self.hashMap = [[] for _ in range(self.size)]
        self.num_elements = 0
        for i in range(tempSize):
            if len(refHashMap[i]) == 0:
                continue
            keyValuePair = refHashMap[i][0]
            self.put(keyValuePair[0], keyValuePair[1])


if __name__ == "__main__":
    map1 = HashMap()

    map1.put(12, 12)
    print(map1)
    map1.put(5, 12)
    print(map1)
    map1.put(4, 12)
    print(map1)
    map1.remove(12)
    print(map1)
    for i in range(16):
        map1.put(i, 0)
        print(map1)
    print(map1)
