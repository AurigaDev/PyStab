

class PEModule:
    def __init__(self, pe_file, arch):
        self.pe_file = pe_file
        self.arch = arch
        
    def get_export_symbols(self):
        return set()
    
    def get_unresolved_symbols(self):
        return set()
    
    def get_entry_point(self):
        return 0