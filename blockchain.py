import hashlib


class Transaction:
    def __init__(self, from_user, to_user, amount):
        self.from_user = from_user
        self.to_user = to_user
        self.amount = amount


class Block:
    transactions = []

    def __init__(self, previous_hash, transactions=None):
        self.transactions = transactions
        self.previous_hash = previous_hash
        # nonce starts at 0 and is incremented until it meets certain difficulty level, determined by cryptocurrency protocol
        self.nonce = 0
        self.hash = self.generate_hash()

    # not sure yet if I need this str implementation
    # def __str__(self):
    #     return f"Block Hash: {self.hash}\nTransactions: {len(self.transactions)}\nPrevious Hash: {self.previous_hash}\n"

    def generate_hash(self):
        block_contents = (
            str(self.transactions) + str(self.previous_hash) + str(self.nonce)
        )
        # SHA-256 hashing algorithm: cryptographic hash function
        # encode method is used to convert from Unicode to bytes, hexdigest() method is called to return str of hexadecimal digits
        block_hash = hashlib.sha256(block_contents.encode()).hexdigest()
        return block_hash

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        self.hash = self.generate_hash()

    def previous_block_hash(self):
        return self.previous_hash


class Ledger:
    def __init__(self):
        pass

    # def has_funds(self, user, amount):
    #     if user not in self._hashmap:
    #         return False
    #     balance = self._hashmap.get(user)
    #     return balance >= amount

    def deposit(self, user, amount):
        pass


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
