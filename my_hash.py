

size=100
sequence=[None for _ in range(size)]

def my_hash(string):
    length=0
    for c in string:
        length +=ord(c)
        
    return length%size
    
def insert(string):
    hash = my_hash(string)
    if sequence[hash]:
        return None
    sequence[hash]=string
    return hash
    
    
string = 'one'
hash=insert(string)
if hash:
    print("'{}' at position: {}".format(string,hash))
    
else:
    print('already occupied')
    
print(sequence[hash])
