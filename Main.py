import logging as logger
import stats_tracker 
import options
import sys
import time
import program
import os


sys.path.append('ssl')
import Architecture

version = '0.8.4-devl'
activeAlgorithm = None
mainThread = None

def get_base_filename(file):
    base_filename = os.path.abspath(file)    
    if '.' in base_filename:
        dotindex = base_filename.rindex('.')
        if dotindex > 0:
            base_filename = base_filename[0:dotindex]
    return base_filename
            
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
    mainfile = os.path.abspath(opts.mainFilename)
    
    basefilename = None
    
    try:

        logger.warning("Parsing " + opts.mainFilename + "...") 
        _program.load_main_module(mainfile)
        
        if basefilename == None:
            basefilename = get_base_filename(mainfile)
            
    except OSError as e:
        logger.critical('File not found: ',e)
        return
        
    except IOError as e:
        logger.critical('IOException while parsing executable!',e)
        return        
        
    except Exception as e:
        logger.critical('Error during parsing',e)
        return

    logger.info('Finished parsing executable')     
    
    if opts.startAddress > 0:
        logger.log("Setting start address to 0x" + hex(opts.startAddress)) 
        
if __name__ == "__main__":
    main()

