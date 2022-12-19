import logger
line = ''
def init(data):
    global line
    line = str(data).split(', ')
    logger.in_lines(line)