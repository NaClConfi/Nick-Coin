from block import Block


class Blockchain:
    def __init__(self):
        self.chain = [Block.genesis()]
        self.blockindex = 1
        self.reward = 10

    def appendblock2chain(self,thablock):
        self.chain.append(thablock)
        print("A block with a timestamp of",thablock.timestamp,"has been appended")
        self.blockindex +=1
    
    
    def __str__(self):
        print("This is each block in the chain, soon to be revised:")
        for block in self.chain:
            print(f"Block # {self.blockindex}: {block.__str__()}")
            
    

