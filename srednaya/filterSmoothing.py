class Mid:
    def __init__(self, n=5):
        self.n = n

    @staticmethod
    def stepMid(l):
        m = 0
        for i in range(len(l)):
            m += l[i]
        return m / len(l)

    def smoothOut(self, sh):
        for i in range(self.n, len(sh) - 1):
            sh[i] = self.stepMid(sh[i:i + self.n])
        return sh
