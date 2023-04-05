class HashMap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.slots = [None] * self.capacity
        self.data = [None] * self.capacity

    def put(self, key, value):
        hash_value = hash(key) % self.capacity
        while self.slots[hash_value] is not None and self.slots[hash_value] != key:
            hash_value = (hash_value + 1) % self.capacity
        self.slots[hash_value] = key
        self.data[hash_value] = value

    def get(self, key):
        hash_value = hash(key) % self.capacity
        while self.slots[hash_value] is not None:
            if self.slots[hash_value] == key:
                return self.data[hash_value]
            hash_value = (hash_value + 1) % self.capacity
        return None

    def size(self):
        count = 0
        for i in range(self.capacity):
            if self.slots[i] is not None:
                count += 1
        return count

    def previous_block_hash(self):
        for i in range(self.capacity - 1, -1, -1):
            if self.slots[i] is not None:
                return self.data[i]
        return None
