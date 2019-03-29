import logging as logger
import stats_tracker 
import options
import sys
sys.path.append('ssl')
import Architecture
import time
import program


version = '0.8.4-devl'
activeAlgorithm = None
mainThread = None


def logBanner():
    logger.error('30') # Will fix later
    logger.error("   Jakstab " + version)
    logger.error("   Copyright 2007-2015  Johannes Kinder  <jk@jakstab.org>");
    logger.error('')
    logger.error("   Jakstab comes with ABSOLUTELY NO WARRANTY. This is free software,")
    logger.error("   and you are welcome to redistribute it under certain conditions.")
    logger.error("   Refer to LICENSE for details.")
    logger.error('30')  # Will fix later

def main():
    logger.basicConfig (level=logger.DEBUG)
    logBanner()
    
    # mainThread = Thread.currentThread()
    st = stats_tracker.StatsTracker()
    stats = st.getInstance()
    
    opts = options.parseOptions()
    try:
        arch = Architecture.Architecture(opts.sslFilename) 
    except OSError as e:
        logger.critical('Unable to open SSL file!',e)
        return
    except:
        logger.critical('Error parsing SSL file!',e)
        return
    
    overallStartTime = time.time()
    _program = program.create_program(arch)

if __name__ == "__main__":
    main()

