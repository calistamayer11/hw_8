class HashMap:
    # def __init__(self, capacity):
    #     self.capacity = capacity
    #     self.slots = [None] * self.capacity
    #     self.data = [None] * self.capacity

    def __init__(self, size=8, load_factor=0.75):
        self.load_factor = load_factor
        self.size = size
        self.num_elements = 0
        self.hashMap = [[] for _ in range(size)]

    # def put(self, key, value):
    #     hash_value = hash(key) % self.capacity
    #     while self.slots[hash_value] is not None and self.slots[hash_value] != key:
    #         hash_value = (hash_value + 1) % self.capacity
    #     self.slots[hash_value] = key
    #     self.data[hash_value] = value

    def put(self, key, value):
        if self.num_elements >= self.size * self.load_factor:
            self._rehash()

        index = hash(key) % self.size

        while len(self.hashMap[index]) != 0 and self.hashMap[index][0][0] != key:
            index = (index + 1) % self.size

        if len(self.hashMap[index]) == 0:
            self.hashMap[index].append((key, value))
            self.num_elements += 1
        else:
            self.hashMap[index].clear()
            self.hashMap[index].append((key, value))

    def __repr__(self):
        # return [i for i in self.hashMap].join(", ")
        return ", ".join([", ".join(i) for i in self.hashMap])

    # def get(self, key):
    #     hash_value = hash(key) % self.capacity
    #     while self.slots[hash_value] is not None:
    #         if self.slots[hash_value] == key:
    #             return self.data[hash_value]
    #         hash_value = (hash_value + 1) % self.capacity
    #     return None

    def get(self, key):
        index = hash(key) % self.size
        start_index = index
        while len(self.hashMap[index]) != 0:
            if self.hashMap[index][0][0] == key:
                return self.hashMap[index][0][1]
            index = (index + 1) % self.size
        return None

    def remove(self, key):
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
        index = (start + 1) % self.size
        while len(self.hashMap[index]) != 0:
            next_index = (index + 1) % self.size
            if hash(self.hashMap[index][0][0]) % self.size != index:
                self.hashMap[start].append(self.hashMap[index][0])
                self.hashMap[index].clear()
                start = index
            index = next_index

    def _rehash(self):
        tempSize = self.size
        self.size += 2
        refHashMap = self.hashMap.copy()
        self.hashMap = [[] for _ in range(self.size)]
        for i in range(tempSize):
            if len(refHashMap[i]) == 0:
                continue
            keyValuePair = refHashMap[i][0]
            self.insert(keyValuePair[0], keyValuePair[1])

    # def size(self):
    #     count = 0
    #     for i in range(self.capacity):
    #         if self.slots[i] is not None:
    #             count += 1
    #     return count

    # def previous_block_hash(self):
    #     for i in range(self.capacity - 1, -1, -1):
    #         if self.slots[i] is not None:
    #             return self.data[i]
    #     return None


if __name__ == "__main__":
    map1 = HashMap()
