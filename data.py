class Data:
    def __init__(self):
        self.X = []
        self.Y = []
        mapping = {
            "ISTJ-T": 1,
            "ISTJ-A": 2,
            "ISFJ-T": 3,
            "ISFJ-A": 4,
            "INFJ-T": 5,
            "INFJ-A": 6,
            "INTJ-T": 7,
            "INTJ-A": 8,
            "ISTP-T": 9,
            "ISTP-A": 10,
            "ISFP-T": 11,
            "ISFP-A": 12,
            "INFP-T": 13,
            "INFP-A": 14,
            "INTP-T": 15,
            "INTP-A": 16,
            "ESTJ-T": 17,
            "ESTJ-A": 18,
            "ESFJ-T": 19,
            "ESFJ-A": 20,
            "ENFJ-T": 21,
            "ENFJ-A": 22,
            "ENTJ-T": 23,
            "ENTJ-A": 24,
            "ESTP-T": 25,
            "ESTP-A": 26,
            "ESFP-T": 27,
            "ESFP-A": 28,
            "ENFP-T": 29,
            "ENFP-A": 30,
            "ENTP-T": 31,
            "ENTP-A": 32
        }
        self.read_data()
        self.encode_x()
        self.encode_y
        
    def read_data(self):
        with open("results.txt", "r") as file:
            l_with_all_data = file.readlines()
            l_with_all_data = [line.split(";") for line in l_with_all_data]
            self.X = [line[1::2] for line in l_with_all_data]
            self.Y = [line[-1] for line in l_with_all_data]
        
    def encode_x(self):
        for i in range(0, len(self.X)):
            for j in range(0, len(self.X[i])):
                if self.X[i][j] == "agree max":
                    self.X[i][j] = 1
                elif self.X[i][j] == "agree med":
                    self.X[i][j] = 2
                elif self.X[i][j] == "agree min":
                    self.X[i][j] = 3
                elif self.X[i][j] == "neutral":
                    self.X[i][j] = 4
                elif self.X[i][j] == "disagree min":
                    self.X[i][j] = 5
                elif self.X[i][j] == "disagree med":
                    self.X[i][j] = 6
                elif self.X[i][j] == "disagree max":
                    self.X[i][j] = 7

    def encode_y(self):
        self.Y = [pt.strip("()\n") for pt in self.Y]
        self.Y = [self.mapping[personality] for personality in self.Y]
        
    def get_data(self, size=0.8):
        train_x = self.X[:int(len(self.X)*size)]
        train_y = self.Y[:int(len(self.Y)*size)]
        test_x = self.X[int(len(self.X)*size):]
        test_y = self.Y[int(len(self.Y)*size):]
        return train_x, train_y, test_x, test_y
        
