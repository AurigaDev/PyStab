import logging as logger
import stats_tracker 
import options

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
    
    options.parseOptions()
    



if __name__ == "__main__":
    main()

