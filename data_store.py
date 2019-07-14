class DataStore:
    def __init__(self):
        self.data_map = dict()

    def incr(self, key):
        pass
        
    def set(self, key, value):
        self.data_map[key] = value

    def get(self, key):
        if key in self.data_map.keys():
            return self.data_map[key]
        else:
            pass

    def delete(self, key):
        del self.data_map[key]
    
    def show_db(self):
        for key in self.data_map.keys():
            print('{}: {}'.format(key, self.data_map[key]))

