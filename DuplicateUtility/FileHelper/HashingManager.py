import hashlib

class Hashing(object):
    pass

    def hashFile(self, file):
        blockSize = 65536
        hasher = hashlib.sha1()
        with open(file, 'rb') as f:
            buffer = f.read(blockSize)
            while len(buffer) > 0:
                hasher.update(buffer)
                buffer = f.read(blockSize)
        return hasher.hexdigest()