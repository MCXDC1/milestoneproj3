#Mia

class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class Mapping:

    def get(self, key):
        raise NotImplementedError
    
    def put(self, key, value):
        raise NotImplementedError
    
    def __len__(self):
        raise NotImplementedError
    
    def _entryiter(self):
        raise NotImplementedError
    
    def __iter__(self):
        return (e.key for e in self._entryiter())
    
    def values(self):
        return (e.value for e in self._entryiter())
    
    def items(self):
        return ((e.key, e.value) for e in self._entryiter())
    
    def __contains__(self, key):
        try:
            self.get(key)
        except KeyError:
            return False

        return True
    
    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, value):
        self.put(key, value)

    
    

class ListMapping(Mapping):
    def __init__(self):
        self._entries = []

    def put(self, key, value):
        e = self._entry(key)
        if e is not None:
            e.value = value
        else:
            self._entries.append(Entry(key, value))

    def get(self, key):
        e = self._entry(key)
        if e is not None:
            return e.value
        else:
            raise KeyError
        
    def _entry(self, key):
        for e in self._entries:
            if e.key == key:
                return e
        return None
    
    def _entryiter(self):
        return iter(self._entries)
    
    def __len__(self):
        return len(self._entries)


class HashMapping(Mapping):

    def __init__(self, size =2):
        self._size = size
        self._buckets = [ListMapping() for i in range(self._size)]
        self._length = 0

    def _entryiter(self):
        return (e for bucket in self._buckets for e in bucket._entryiter())

    def put(self, key, value):
        bucket = self._bucket(key)
        if key not in bucket:
            self._length +=1

        bucket[key] = value

        if self._length / self._size >= .8:
            self._double()

    def get(self, key):
        bucket = self._bucket(key)
        return bucket[key]

    
    def __len__(self):
        return self._length
    
    def _bucket(self, key):
        return self._buckets[hash(key) % self._size]
    
    def _double(self):
        oldbuckets = self._buckets

        self.__init__(self._size * 2)
        for bucket in oldbuckets:
            for key, value in bucket.items():
                self[key] = value






   