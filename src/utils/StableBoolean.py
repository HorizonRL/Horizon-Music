class StableBoolean:
    def __init__(self, true_threshold=1, false_threshold=1, val=False):
        self.true_threshold = true_threshold
        self.false_threshold = false_threshold
        self.out_val = val

        self.counter = 0

    def update(self, value):
        if self.out_val:
            if value:
                self.counter = 0
            
            else:
                self.counter += 1
                if self.counter >= self.false_threshold:
                    self.out_val = False
                    self.counter = 0

        else:
            if not value:
                self.counter = 0
            
            else:
                self.counter += 1
                if self.counter >= self.true_threshold:
                    self.out_val = True
                    self.counter = 0
