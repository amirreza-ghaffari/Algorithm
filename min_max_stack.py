# Time: O(1)
# Space: O(N) --> Store 3 list containing last value, last min  and last max

class MinMaxStack:

    def __init__(self):
        self.min_max = []
        self.stack = []

    def peek(self):
        return self.stack[-1]

    def pop(self):
        self.min_max.pop()
        return self.stack.pop()

    def push(self, value):
        self.stack.append(value)
        temp = {'min': value, 'max': value}
        if len(self.min_max) > 0:
            if value > self.min_max[-1]['min']:
               temp['min'] = self.min_max[-1]['min']
            elif value < self.min_max[-1]['max']:
                temp['max'] = self.min_max[-1]['max']
        self.min_max.append(temp)

    def get_min(self):
        return self.min_max[-1]['min']

    def get_max(self):
        return self.min_max[-1]['max']






