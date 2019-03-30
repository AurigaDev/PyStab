import logging
import sys

from loader.pe.pe_module import PEModule
from enum import Enum

class TargetOS(Enum):
    WINDOWS = 1
    LINUX = 2
    UNKNOWN = 3
    
def create_program(arch):
    """ Initailize program with architecture object
          Input -
            arch (Architecture obj) - physical architecture program runs on
                                      encapsulates all specifics of analysis 
          Output -
            program_instance (Program obj) - Project interface handle
    """
    program_instance = Program(arch)
    return program_instance


class Program:
    program_instance = None
    
    #############################################################
    #                       Accessors
    #############################################################
    
    def getProgram(self):
        return self.program_instance;
    
    def get_statement_couunt(self):
        return len(self.statement_map.keys())
    
    def get_assembly_couunt(self):
        return len(self.assembly_map.keys())

    def get_harness(self):
        return self.harness

    def get_target_os(self):
        return self._target_os

    def get_arch(self):
        return self.arch

    def get_cfg(self):
        return self.cfg

    def get_start(self):
        return self.exported_symbols.keys()

    def get_symbols(self):
        return self.start

    def get_main_module(self):
        """ Returns handle to main module of program
          Input - 
            None
          Output -
            main_module (ExecutableImage obj) - hanle to module with entry point
        """
        return self.main_module
    #############################################################
    #                       Core Logic
    #############################################################

    def __init__(self, arch):
        """ Instance method that initalizes a program object, constructor
          Input -
            self (Program(self)) - handle to class for instance method
            arch (Architecture obj) - physical architecture program runs on
                                      encapsulates all specifics of analysis 
          Output -
            None
        """
        self.arch = arch

        # must define target_os module unknown
        self.target_os = TargetOS.UNKNOWN
        
        # list of executable images
        self.modules = []

        # assembly map is sorted dictionary, TODO::switch to sorted dict
        self.assembly_map = {}

        # map from rtl label to rtl statement, default size 2000
        self.statement_map = {}

        # map from text to export symbol obj
        self.exported_symbols = {}

        # set of unresolved symbols objects
        self.unresolve_symbols = set()

        # set of rtl_labels
        self.unresolve_branches = set()

    def remove_decoration(s):
        """ processes out @ portion of symbol name
          Input -
            s (String) - input symbol name to process
          Output -
            s (String) - subset of s that remove character at beginning and strips after @
        """
        if len(s) > 0 and (s[0] == '@' or s[0] == '_'):
            s = s[1:]
        
        i = s.index('@')
        if i >= 0:
            s = s[:i]
        return s

    def resolve_symbols(self):
        """ Resolves symbols between loaded modules
            TODO:: Determine if this needs to be reset to unresolved_symbols
          Input - 
            None
          Output - 
            None
        """
        unresolved_symbol_lst = list(self.unresolved_symbols)

        for unres_iter in unresolved_symbol_lst:
            symbol = self.exported_symbols[remove_decoration(unres_iter)]

            if symbol is not None:
                logging.debug('Resolving symbol %s'%unres_iter.get_name())
                unres_iter.resolve(symbol.get_addr())
    
    def load_module(self, module_file):
        module = None

        try:
            # TODO::Define Windows object file class
            module = PEModule(module_file, get_arch())
            _target_os = target_os.WINDOWS
        except:
            try:
                # TODO::Define object file class
                module = ObjectFile(moduleFile, get_arch())
            except:
                # TODO::Define raw module class
                module = RawModule(module_file, get_arch())
        
        for existing_module in self.modules:
            if existing_module.get_max_addr().get_value() >= module.get_min_addr().get_value() \
            and existing_module.get_min_addr().get_value() < module.get_max_addr().get_value():
                raise Exception("Virtual Address of Modules Overlap!")
        
        self.modules.append(module)
        self.unresolve_symbols.add_all(module.get_unresolved_symbols())

        for symbol in module.get_export_symbols():
            self.exported_symbols.add(remove_decoration(symbol.get_name()))
    
        self.resolve_symbols()
        return module

    def is_stub(self, abs_addr):
        """ TODO::Understand what this function is doing and weather this is instance or not
        """
        return abs_addr.get_value() >= stub_provider.STUB_BASE

    def is_import(self, abs_addr):
        if is_stub(abs_addr):
            return True
        module = get_module(abs_addr)
        if module is None:
            return False
        return module.is_import_area(abs_addr)
    
    def install_stubs(self):
        if isinstance(self.main_module, AbstractCOFFModule):
            # TODO:: Define AbstractCOFFModule
            self.stub_library = Win32StubLibrary(self.arch)
        elif isinstance(self.main_module, ELFModule):
            # TODO:: Define ELFModule
            self.stub_library = LinuxStubLibrary(self.arch)
        else:
            logging.error("undefined arch for stubs")
            sys.exit()
        
        unresolved_symbol_lst = list(self.unresolved_symbols)
        for unres_iter in unresolved_symbol_lst:
            address = stubLibary.resolve_symbol(unres_iter.get_from_library(), unres_iter.get_name())
            if address is not None:
                unres_iter.resolve(address)
                # TODO::Determine if this is possible to remove element from set
                self.unresolved_symbols.remove(unres_iter)
        
        if not len(self.unresolve_symbols) == 0:
            logging.warning("Unresolved Symbols Remaining: ", self.unresolve_symbols)

    def install_harness(self, harness):
        """ Install a harness that sets up the symbolic environment before alling main
            and provides reeturn point with termiantion statement
          Input - 
            harness (harness obj) - the harness object to install
          Output - 
            None
        """
        self.harness = harness
        harness.install(self)

    def set_start(self, label):
        """ Set the program entry point to the given label
          Input - 
            label (RTLLabel obj) - label of the entry point
          Output - 
            None
        """
        self.start = label

    def set_entry_address(self, entry_address):
        """ Set the entyr point to the given address
          Input -
            entry_address (absolute address obj) - the new entry address
          Output - 
            None
        """
        # TODO:: Define RTLLabel
        self.set_start(RTLLabel(entry_address))

    def get_module(self, abs_addr):
        """ Get the module that contains the specified virtual address at runtime
          Input -
            abs_addr (AbsoluteAddress Obj) - a virtual address
          Output - 
            module (ExecutableImage obj) - the module to which the virtual address belongs
        """
        for module in self.modules:
            if module.get_file_pointer(abs_addr) >= 0:
                return module
        return None

    def get_statment(self, label):
        if label not in self.statement_map:
            address = label.get_addr()
            instr = get_instruction(address)

            if instr is None:
                # TODO:: Define RTLHalt
                half = RTLHalt()
                half.set_label(label)

                put_statement(halt)

                logging.error("ERROR: Replacing unknown instruction with HALT.")
                if options.debug.get_value():
                    raise Exception("Disassembly failed at ", address)
            else:
                try:
                    seq = arch.get_rtl_equivalent(address, instr)
                    for rtlstatement in seq:
                        put_statement(rtlstatement)
                except:
                    logging.error("Error during translation of instruction to IL")
                    # TODO:: Define RTLSkip
                    skip = RTLSkip()
                    skip.set_label(label)
                    skip.set_net_label(RTLLabel(AbsoluteAddress(address.get_value()+1)))
                    put_statement(skip)
                if label not in self.statement_map:
                    raise Exception("Disassembly did not produce label:", label)
        return self.statement_map[label]            

    def contains_label(self, label):
        return label in self.statement_map

    def load_main_module(self, module_file):
        """ loads module containing main function, called last for symbol resolution
          Input - 
            module_file (file descriptor) - file to be loaded
          Output -
            module (executable image object) - exectuable image obj of loaded module
        """
        module = load_module(module_file)
        self.main_module = module
        # must define executable image entry point, TODO::define stub ExectuableImage
        set_entry_address = module.get_entry_point()
        install_stubs()
        return module

    """
        TODO:: Implement the following functions
        pcout instruction
        get instruction string
        get symbol for
        get address for symbol
        symbol finder
        get unresolved branches
        set unresolved branches
        get asssembly map
        get used variables
        set cfa
        count indirect branches

    """