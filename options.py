from optparse import OptionParser
''' 
parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()
'''
lineLength = 80
indention = 22

jakstabHome = None
# To do later

# Ignore Map line 53

def parseOptions():
    mainFilename = None
    moduleFilenames = []

    arguments = None

    parser = OptionParser()
    parser.add_option("-m", "--mainFilename", dest="mainFilename",help="write report to FILE", metavar="FILE")
    return parser.parse_args()