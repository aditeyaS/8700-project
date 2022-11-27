class LeaderboardDB():
    __instance = None
    __db = None

    @staticmethod
    def getInstance():
        if LeaderboardDB.__instance == None:
            LeaderboardDB()
        return LeaderboardDB.__instance

    def __init__(self):
        if LeaderboardDB.__instance != None:
            raise Exception("Singleton class")
        else:
            LeaderboardDB.__instance = self

    def write_score(self, username, score):
        self.__db = open("db/leaderboard_db", "r")
        score_list = self.__db.readlines()
        score_not_present = True

        for idx, _score in enumerate(score_list):
            _username, _ = _score.rsplit(' ', 1)
            if _username == username:
                score_not_present = False
                score_list[idx] = f"{username} {score}\n"
                break
        if score_not_present:
            score_list.append(f"{username} {score}\n")
        self.__db = open("db/leaderboard_db", "w")
        self.__db.writelines(score_list)
        self.__db.close()

    def read_score(self):
        self.__db = open("db/leaderboard_db", "r")
        score_list = self.__db.readlines()
        new_score_list = []
        for score in score_list:
            username, high_score = score.rsplit(' ', 1)
            new_score_list.append([username, int(high_score)])
        new_score_list.sort(key=lambda score: score[1], reverse=True)
        self.__db.close()
        return new_score_list[:5]