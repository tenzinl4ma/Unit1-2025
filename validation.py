### This is the validation library where you can import classes like color and its foreground,background and other style

class color:
    reset = '\033[39m'
    class fg:
        black   = '\033[30m'
        red     = '\033[31m'
        green   = '\033[32m'
        yellow  = '\033[33m'
        blue    = '\033[34m'
        magenta = '\033[35m'
        cyan    = '\033[36m'
        white   = '\033[37m'
    class bg:
        black   = '\033[40m'
        red     = '\033[41m'
        green   = '\033[42m'
        yellow  = '\033[43m'
        blue    = '\033[44m'
        magenta = '\033[45m'
        cyan    = '\033[46m'
        white   = '\033[47m'
    class style:
        bright    = '\033[1m'
        dim       = '\033[2m'
        normal    = '\033[22m'
        reset_all = '\033[0m'

# Number validation functions
class numbervalidation:
    @staticmethod
    def positivenum(number):
        return number > 0

    @staticmethod
    def integernum(number):
        return isinstance(number, int)
