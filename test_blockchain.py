import unittest
from hashmap import HashMap
from blockchain import Transaction, Block, Ledger, Blockchain


class test_blockchain(unittest.TestCase):
    def test_blockchain_instantiation(self):
        hashed_name = Block("Calista").hash
        self.assertEqual(
            hashed_name,
            "c3b469a098023c9577525564f2a99a835670ce67a3350e6fc9f6b26ba076e257",
        )

    def test_blockchain_add_transaction(self):
        b = Block("Calista")
        bc = Blockchain()
        t = Transaction("Calista", "Richard", 500)
        b.add_transaction(t)
        bc._bc_ledger.deposit("Calista", 10000)
        assert t.to_user == "Richard"
        assert t.amount == 500
        assert t.from_user == "Calista"

        block1 = Block("")
        assert block1.transactions == []
        assert block1.previous_block_hash == None

        ledger = Ledger()
        assert ledger.has_funds("Calista", 100) is False

        blockchain = Blockchain()
        assert len(blockchain._blockchain) == 1


unittest.main()
