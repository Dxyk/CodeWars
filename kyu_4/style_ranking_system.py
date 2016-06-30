class User:
    """
    a Codewars style ranking system

    attributes:
    @rank: user rank, from -8 to 8 without 0
    @progress: rank progress, from 0 to 100 and rank up when reach 100

    """

    def __init__(self):
        """
        initialize a user
        :return: None
        :rtype: None
        """
        self.rank = -8
        self.progress = 0

    def inc_progress(self, act_rank):
        """
        increase the rank progress of the user when the user completes an act
        :param act_rank: the rank of the act
        :type act_rank: int
        :return: none
        :rtype: None
        """
        if act_rank >= 9 or act_rank <= -9 or act_rank == 0:
            raise ValueError
        if self.rank == act_rank:
            self.progress += 3
        elif (self.rank - 1 == 0 and act_rank == -1) \
                or self.rank - 1 == act_rank:
            self.progress += 1
        elif self.rank < act_rank:
            if self.rank < 0 < act_rank:
                self.progress += 10 * ((act_rank - self.rank - 1) ** 2)
            else:
                self.progress += 10 * ((act_rank - self.rank) ** 2)
        # else:
        #     pass

        if self.rank < 0 <= self.progress // 100 + self.rank:
            self.rank += self.progress // 100 + 1
        else:
            self.rank += self.progress // 100
        self.progress %= 100
        if self.rank >= 8:
            self.rank = 8
            self.progress = 0
