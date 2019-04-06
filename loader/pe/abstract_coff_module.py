import logging as logger
from executable_image import ExecutableImage
class AbstractCOFFModule(ExecutableImage):
    def __init__(self):
        self.binary_file_handler = None
        self.coff_header = None
        self.section_headers = None
        self.disassembler = None
        """ Need to define BinaryFileInputBuffer
            COFF_Header
            SectionHeader
            Disassembler
        """
        
    def get_file_pointer(self,va):
        fp = self.get_file_pointer_from_rva(va - self.get_base_address())
        if fp >= 0:
            return fp
        else:
           return -1
       
    def is_code_area(self,va):
        section = self.get_section_number(va)
        if section < 0 :
            return false
        else:
            return is_code_section(section)
    
    def get_file_pointer_from_rva(self,rva):
        sct = self.get_section_number_by_rva(rva)
        if sct < 0:
            return -1
        if rva - self.get_section_header(sct).virtual_address > self.get_section_header(sct).size_of_raw_data:
            return (rva - self.get_section_header(sct).virtual_address) + self.get_section_header(sct).pointer_to_raw_data

    def get_section_number(self,input):
        if isinstance(input,AbsoluteAddress()):
            return self.get_section_number_by_rva(va - self.get_base_address())
        else:
            for i in range(self.get_number_of_sections()):
                if self.get_section_header(i).pointer_to_raw_data <= input and self.get_section_header(i).pointer_to_raw_data + self.get_section_header(i).size_of_raw_data > input:
                    return i
            return -1;

    def get_section_number_rva(rva):
        raise Exception("function not defined")
        
    def get_virtual_address(self,fp):
        rva = self.get_rva_from_file_pointer(fp)
        if rva >= 0:
            return AbsoluteAddress(rva + self.get_base_address())
        else:
            return None
        
    def get_max_address(self):
        high_address = 0;
        for i in range(self.get_number_of_sections()):
            high_address = max(self.get_section_header(i).virtual_address + 
					self.get_section_header(i).size_of_raw_data, high_address)
            high_address += self.get_base_address()
            return AbsoluteAddress(high_address)
    
    def get_min_address(self):
        low_address = 2**32
        for i in range(self.get_number_of_sections()):
            low_address = min(self.get_section_header(i).virtual_address, low_address)
        low_address += self.get_base_address()
        return AbsoluteAddress(low_address)
    
    def get_section_header(self,index):
        return self.section_headers[index]
    
    def is_code_section(self,section):
        return self.get_section_header(section).is_code_section()
    
    def get_base_address():
         raise Exception("function not defined")
         
    def read_memory_location(self,m):
        if instanceof(RTLNumber)!= m.get_address():
            return None
        va = AbsoluteAddress(m.get_address())
        fp = self.get_file_pointer(va)
        if self.get_section_number(fp) >= 0:
            assert m.get_bit_width() % 8 == 0, "Non-byte-aligned memory reference!"
            val = 0
            bytes = m.get_bit_width()/8
            self.binary_file_handler.seek(fp)
            for i in range(bytes-1):
                val = val | binary_file_handler.read(1) << (i*8)
                
            val = val | (int(binary_file_handler.read(1)) << (bytes-1) * 8)
            return ExpressionFactory.createNumber(val, m.getBitWidth())
        logger.debug("No value can be read from image for address " + m);
        

    def get_byte_array():
        return binary_file_handler.get_byte_array()
    
    # Skipping Iterators
    

    def get_disassembler(self):
        if self.disassembler == None:
            self.disassembler = X86Disassembler(self.binary_file_handler)
        return self.disassembler
    
    def is_import_area(self,va):
        section = self.get_section_number(va)
        if section < 0 :
            return false
        else:
            # implement this
            return false
        
    
    
    
        
        
           
           