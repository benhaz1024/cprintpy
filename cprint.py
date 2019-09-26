class cprint(object):
#color mean
# R  red
# G  green
# B  blue
# P  purple
# C  cyan
# H  highlight

    c_start = { 'R'  : '\033[31m', \
                'G'  : '\033[32m', \
                'Y'  : '\033[33m', \
                'B'  : '\033[34m', \
                'P'  : '\033[35m', \
                'C'  : '\033[36m', \
                'HR' : '\033[1m\033[31m', \
                'HG' : '\033[1m\033[32m', \
                'HY' : '\033[1m\033[33m', \
                'HB' : '\033[1m\033[34m', \
                'HP' : '\033[1m\033[35m', \
                'HC' : '\033[1m\033[36m'}
    c_end = '\033[0m'
    

    def __init__(self, color, c_str):
        self.color = color
        print(self.c_start[self.color] + str(c_str) + self.c_end)

