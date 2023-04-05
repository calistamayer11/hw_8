import hashlib
from hashmap import HashMap


class Transaction:
    def __init__(self, from_user, to_user, amount):
        self.from_user = from_user
        self.to_user = to_user
        self.amount = amount


class Block:
    # transactions = []

    def __init__(self, user_id, transactions=None):
        if transactions is None:
            self.transactions = []
        else:
            self.transactions = transactions
        self.previous_block_hash = None
        # nonce starts at 0 and is incremented until it meets certain difficulty level, determined by cryptocurrency protocol
        # self.nonce = 0
        self.hash = self.generate_hash()
        self.user_id = user_id

    # not sure yet if I need this str implementation
    # def __str__(self):
    #     return f"Block Hash: {self.hash}\nTransactions: {len(self.transactions)}\nPrevious Hash: {self.previous_block_hash}\n"

    def generate_hash(self):
        block_contents = (
            str(self.transactions) + str(self.previous_block_hash) + str(self.nonce)
        )
        # SHA-256 hashing algorithm: cryptographic hash function
        # encode method is used to convert from Unicode to bytes, hexdigest() method is called to return str of hexadecimal digits
        block_hash = hashlib.sha256(block_contents.encode()).hexdigest()
        return block_hash

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        self.hash = self.generate_hash()

    # def previous_block_hash(self):
    #     return self.previous_block_hash


class Ledger:
    def __init__(self):
        self._hashmap = HashMap()

    def __repr__(self):
        return f"Ledger: {self._hashmap}"

    def has_funds(self, user, amount):
        if user not in self._hashmap:
            return False
        balance = self._hashmap.get(user)
        return balance >= amount

    def deposit(self, user, amount):
        self._hashmap.put(user, amount)

    def transfer(self, user, amount):
        if self.has_funds(user, amount):
            self._hashmap.put(user, -amount)
            # self._hashmap.put(user, self._hashmap.get(user) - amount)
            # self._hashmap.put(self._ROOT_BC_USER, self._hashmap.get(self._ROOT_BC_USER) + amount)
        else:
            raise Exception("Insufficient funds")


class Blockchain:
    """Contains the chain of blocks."""

    #########################
    # Do not use these three values in any code that you write.
    _ROOT_BC_USER = "ROOT"  # Name of root user account.
    _BLOCK_REWARD = 1000  # Amoung of HuskyCoin given as a reward for mining a block
    _TOTAL_AVAILABLE_TOKENS = (
        999999  # Total balance of HuskyCoin that the ROOT user receives in block0
    )
    #########################

    def __init__(self):
        self._blockchain = list()  # Use the Python List for the chain of blocks
        self._bc_ledger = Ledger()  # The ledger of HuskyCoin balances
        # Create the initial block0 of the blockchain, also called the "genesis block"
        self._create_genesis_block()

    # This method is complete. No additional code needed.
    def _create_genesis_block(self):
        """Creates the initial block in the chain.
        This is NOT how a blockchain usually works, but it is a simple way to give the
        Root user HuskyCoin that can be subsequently given to other users"""
        trans0 = Transaction(
            self._ROOT_BC_USER, self._ROOT_BC_USER, self._TOTAL_AVAILABLE_TOKENS
        )
        block0 = Block([trans0])
        self._blockchain.append(block0)
        self._bc_ledger.deposit(self._ROOT_BC_USER, self._TOTAL_AVAILABLE_TOKENS)

    # This method is complete. No additional code needed.
    def distribute_mining_reward(self, user):
        """
        You need to give HuskyCoin to some of your users before you can transfer HuskyCoing
        between users. Use this method to give your users an initial balance of HuskyCoin.
        (In the Bitcoin network, users compete to solve a meaningless mathmatical puzzle.
        Solving the puzzle takes a tremendious amount of copmputing power and consuming a lot
        of energy. The first node to solve the puzzle is given a certain amount of Bitcoin.)
        In this assigment, you do not need to understand "mining." Just use this method to
        provide initial balances to one or more users."""
        trans = Transaction(self._ROOT_BC_USER, user, self._BLOCK_REWARD)
        block = Block([trans])
        self.add_block(block)

    # TODO - add the rest of the code for the class here
    def add_block(self, block):
        users_give = {}
        users_get = {}
        for transaction in block.transactions:

            if transaction.from_user in users_give:
                update_total = (
                    users_give.get(transaction.from_user) + transaction.amount
                )
                users_get.update({transaction.from_user: update_total})
            else:
                users_give.update({transaction.from_user: transaction.amount})

            if transaction.to_user in users_get:
                update_total = users_get.get(transaction.to_user) + transaction.amount
                users_get.update({transaction.to_user: update_total})
            else:
                users_get.update({transaction.to_user: transaction.amount})

        for key in users_give.keys():
            if self._bc_ledger.has_funds(key, users_give.get(key)) == False:
                return False

        for key in users_give.keys():
            self._bc_ledger.transfer(key, users_give.get(key))

        for key in users_get.keys():
            self._bc_ledger.deposit(key, users_get.get(key))

        previous_hash = self._blockchain[-1].hash
        block.previous_block_hash = previous_hash
        self._blockchain.append(block)

        return True

        # for key in users_give.keys():
        #     self._bc_ledger.transfer(key, users_give.get(key))
        # return True

    def validate_chain(self):
        pass


# if __name__ == "__main__":
#     block1 = Block(Transaction())  # big and lots of data
if __name__ == "__main__":
    b = Block("name")
    print(b.hash)
    print(b.hash)
    print(hash(b))
    print(b.transactions)
    t = Transaction(1, 2, 1000)
    b.add_transaction(t)
    print(b.hash)
    print(b.transactions)
    new_transaction = Transaction("Richard", "Calista", 2)
    b.add_transaction(new_transaction)
    print(b.hash)
    print(b.hash)
    print(b.transactions)
