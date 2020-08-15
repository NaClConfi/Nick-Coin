

class Block:
    def __init__(self, timestamp, last_hash,hash_,data,difficulty=3,nonce=0):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash_ = hash_
        self.data = data
        self.difficulty = difficulty
        self.nonce = nonce
        
    @staticmethod
    def genesis():
        return Block("0", "Waffle House Hashbrowns", "Are The Best Hashbrowns", [{()}])    

    def __str__(self):
        return f"Timestamp: {self.timestamp} Last_Hash: {self.last_hash} Hash: {self.hash_} Data: {self.data}"

