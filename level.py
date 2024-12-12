import platform

FILE = "./levels/1.txt"
FILE_2 = "./levels/2.txt"
BG_FILE = "./images/bg/super-mario.jpg"



class Level:
    path_level: str

    def __init__(self, path=FILE):
        self.path_level = path
        self.__lines_of_file = []
        self.platforms = []
        self.__load()
        self.__get_platform()
        self.width = len(self.__lines_of_file[0]) * platform.PLATFORM_WIDTH
        self.haght = len(self.__lines_of_file) * platform.PLATFORM_HEIGHT



    def __load(self):
        with open(self.path_level, "r") as file:
            for line in file:
                self.__lines_of_file.append(line[:-2])

    def __get_platform(self):
        x = y = 0
        for row in self.__lines_of_file:
            for column in row:
                if column == "-":
                    pf = platform.Platform(x, y)
                    self.platforms.append(pf)
                elif column == "=":
                    krp = platform.Kirpich(x, y)
                    self.platforms.append(krp)
                elif column == "_":
                    krp = platform.Ground(x, y)
                    self.platforms.append(krp)
                elif column == "*":
                    db = platform.DieBlock(x, y)
                    self.platforms.append(db)
                elif column == "P":
                    #p = platform.Finish(x, y)
                    self.platforms.append(db)


                x += platform.PLATFORM_WIDTH
            y += platform.PLATFORM_HEIGHT
            x = 0
