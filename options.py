from optparse import OptionParser
''' 
parser = OptionParser()
parser.add_option("-f", "--file", default=False, dest="filename",
                  help="write report to FILE", metavar="FILE")
parser.add_option("-q", "--quiet",
                  action="store_false", default=False, dest="verbose", default=True,
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
    parser.remove_option('-h')
    parser.add_option("--help", action="help", help="Prints this help message.")
    parser.add_option("-m", "--mainFilename", default=False, dest="mainFilename",help="write report to FILE", metavar="FILE")
    parser.add_option("-w", "--wdm", action="store_true", default=False, dest="wdm", help="WDM mode, export main function as DriverMain.")
    parser.add_option("-a","--all-edges", action="store_true", default=False, dest="allEdges", help="Generate a true over-approximation and add edges to all possible addresses when over-approximating a jump (very slow!).")
    parser.add_option("-s", action="store_true", default=False, dest="dumpStates", help="Output all reached states after analysis.")
    parser.add_option("-t", "--toplocs", action="store_true", default=False, dest="outputLocationsWithMostStates", help="Output the 10 locations with the highest state count.")
    parser.add_option("-f", "--failFast", action="store_true", default=False, dest="failFast", help="Stop when unsound assumptions are necessary to continue.")
    parser.add_option("-d", "--debug", action="store_true", default=False, dest="debug", help="Stop on failed assertions or weak updates to the complete stack or all store regions.")
    parser.add_option("-e", "--error-trace", action="store_true", default=False, dest="errorTrace", help="Build an abstract error trace for failed assertions and debug stops.")
    parser.add_option("-b", "--background", action="store_true", default=False, dest="background", help="Background mode, i.e., disable shutdown hook on enter.")
    parser.add_option("-g", "--graphML", action="store_true", default=False, dest="graphML", help="Produce graphML output instead of GraphViz .dot files.")
    parser.add_option("-n", "--no-graphs", action="store_true", default=False, dest="noGraphs", help="Do not generate output graphs")
    parser.add_option("-h", "--heuristicEntryPoints", action="store_true", default=False, dest="heuristicEntryPoints", help="Use heuristics to determine additional procedures and add pseudo-calls to include them in disassembly.")
    parser.add_option("-i", "--ignore-weak-updates", action="store_true", default=False, dest="ignoreWeakUpdates", help="Do not perform weak store updates (unsound).")
    parser.add_option("--backward", action="store_true", default=False, dest="backward", help="Perform secondary cpa as a backward analysis.")
    parser.add_option("--asm-trace", "--asmTrace", action="store_true", default=False, dest="asmTrace", help="Output any error trace as a list of assembly instructions instead of IL statements.")
    parser.add_option("--bot-heap", action="store_true", default=False, dest="initHeapToBot", help="Initialize heap cells to BOT to force strong updates.")
    parser.add_option("--summarize-rep", action="store_true", default=False, dest="summarizeRep", help="Use summarizing transformer for string instructions.")
    parser.add_option("--basicblocks", action="store_true", default=False, dest="basicBlocks", help="Build CFA from basic-blocks instead of single statements.")

    return parser.parse_args()