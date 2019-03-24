from argparse import ArgumentParser
''' 
parser = OptionParser()
parser.add_argument("-f", "--file", default=False, dest="filename",
                  help="write report to FILE", metavar="FILE")
parser.add_argument("-q", "--quiet",
                  action="store_false", default=False, dest="verbose", default=True,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()
'''
parser = ArgumentParser(add_help=False) # Keep global copy of option parser for ease of add of options

lineLength = 80
indention = 22

jakstabHome = None


# To do later

# Ignore Map line 53

def addOption(arglist, **kwargs):
    #check_choice(None, None, '-h')
    if isinstance(arglist[0], str):
        pass
    if len(arglist)>1 and isinstance(arglist[1], str):
        pass

def parseOptions():
    mainFilename = None
    moduleFilenames = []

    arguments = None

    #parser.remove_option('-h')
    
    # OptionGroup, group.add_argument, parser.add_argument_group(group)
    # Group options for more intuitive help
    parser.add_argument("-a", metavar='address', type=int, dest="startAddress", help="Start analysis at given virtual address.")
    parser.add_argument("--simplyVCFG", metavar='l', type=int, dest="simplyVCFG", help="In VPC-CFG reconstruction, simplify the reconstructed graph using (0) nothing (1) DCE (2) DCE + Expression Substitution")
    parser.add_argument("-v", metavar='level', type=int, dest="verbosity", help="Set verbosity to value. Default is 3.")
    parser.add_argument("--timeout", metavar='t', type=int, dest="timeout", help="Set timeout in seconds for the analysis.")
    parser.add_argument("--procedure", metavar='n', type=int, dest="procedure", help="Level of procedure assumptions: " +
			"0: Pessimistic: No assumptions, treat calls and returns as jumps (default). " + 
			"1: Semi-optimistic: Abstract unknown calls according to ABI contract. " + 
			"2: Optimistic: Abstract all calls to ABI contract (fastest).")
    parser.add_argument("--getprocaddress", metavar='n', type=int, dest="getprocaddress", help="How to resolve GetProcAddress: 0: Always succeed, 1: Split success/fail, 2: Merge success/fail (default)")
   
    parser.add_argument("--ssl", metavar='file', dest="sslFilename", help="Use <file> instead of pentium.ssl.")
    # Ignore cpas and SecondaryCPAs
    parser.add_argument("--procedure-graph", metavar='p', dest="procedureGraph", help="Generate intraprocedural CFG for procedure with give name (requires symbols)")
    
    parser.add_argument("--help", action="help", help="Prints this help message.")
    parser.add_argument("-m", "--mainFilename", default=False, dest="mainFilename",help="write report to FILE", metavar="FILE", required=True)
    parser.add_argument("-w", "--wdm", action="store_true", default=False, dest="wdm", help="WDM mode, export main function as DriverMain.")
    parser.add_argument("--all-edges", action="store_true", default=False, dest="allEdges", help="Generate a true over-approximation and add edges to all possible addresses when over-approximating a jump (very slow!).")
    parser.add_argument("-s", action="store_true", default=False, dest="dumpStates", help="Output all reached states after analysis.")
    parser.add_argument("-t", "--toplocs", action="store_true", default=False, dest="outputLocationsWithMostStates", help="Output the 10 locations with the highest state count.")
    parser.add_argument("-f", "--failFast", action="store_true", default=False, dest="failFast", help="Stop when unsound assumptions are necessary to continue.")
    parser.add_argument("-d", "--debug", action="store_true", default=False, dest="debug", help="Stop on failed assertions or weak updates to the complete stack or all store regions.")
    parser.add_argument("-e", "--error-trace", action="store_true", default=False, dest="errorTrace", help="Build an abstract error trace for failed assertions and debug stops.")
    parser.add_argument("-b", "--background", action="store_true", default=False, dest="background", help="Background mode, i.e., disable shutdown hook on enter.")
    parser.add_argument("-g", "--graphML", action="store_true", default=False, dest="graphML", help="Produce graphML output instead of GraphViz .dot files.")
    parser.add_argument("-n", "--no-graphs", action="store_true", default=False, dest="noGraphs", help="Do not generate output graphs")
    parser.add_argument("-h", "--heuristicEntryPoints", action="store_true", default=False, dest="heuristicEntryPoints", help="Use heuristics to determine additional procedures and add pseudo-calls to include them in disassembly.")
    parser.add_argument("-i", "--ignore-weak-updates", action="store_true", default=False, dest="ignoreWeakUpdates", help="Do not perform weak store updates (unsound).")
    parser.add_argument("--backward", action="store_true", default=False, dest="backward", help="Perform secondary cpa as a backward analysis.")
    parser.add_argument("--asm-trace", "--asmTrace", action="store_true", default=False, dest="asmTrace", help="Output any error trace as a list of assembly instructions instead of IL statements.")
    parser.add_argument("--bot-heap", action="store_true", default=False, dest="initHeapToBot", help="Initialize heap cells to BOT to force strong updates.")
    parser.add_argument("--summarize-rep", action="store_true", default=False, dest="summarizeRep", help="Use summarizing transformer for string instructions.")
    parser.add_argument("--basicblocks", action="store_true", default=False, dest="basicBlocks", help="Build CFA from basic-blocks instead of single statements.")
    #addOption(["--basicblocks"], action="store_true", default=False, dest="basicBlocks", help="Build CFA from basic-blocks instead of single statements.")
    return parser.parse_args()