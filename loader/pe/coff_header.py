import struct

class COFF_Header:
  IMAGE_FILE_MACHINE_UNKNOWN = 0x0 # The contents of this field are assumed to be applicable to any machine type
  IMAGE_FILE_MACHINE_AM33 = 0x1d3 # Matsushita AM33
  IMAGE_FILE_MACHINE_AMD64 = 0x8664 # x64
  IMAGE_FILE_MACHINE_ARM = 0x1c0 # ARM little endian
  IMAGE_FILE_MACHINE_EBC = 0xebc # EFI byte code
  IMAGE_FILE_MACHINE_I386 = 0x14c # Intel 386 or later processors and compatible processors
  IMAGE_FILE_MACHINE_IA64 = 0x200 # Intel Itanium processor family
  IMAGE_FILE_MACHINE_M32R = 0x9041 # Mitsubishi M32R little endian
  IMAGE_FILE_MACHINE_MIPS16 = 0x266 # MIPS16
  IMAGE_FILE_MACHINE_MIPSFPU = 0x366 # MIPS with FPU
  IMAGE_FILE_MACHINE_MIPSFPU16 = 0x466 # MIPS16 with FPU
  IMAGE_FILE_MACHINE_POWERPC = 0x1f0 # Power PC little endian
  IMAGE_FILE_MACHINE_POWERPCFP = 0x1f1 # Power PC with floating point support
  IMAGE_FILE_MACHINE_R4000 = 0x166 # MIPS little endian
  IMAGE_FILE_MACHINE_SH3 = 0x1a2 # Hitachi SH3
  IMAGE_FILE_MACHINE_SH3DSP = 0x1a3 # Hitachi SH3 DSP
  IMAGE_FILE_MACHINE_SH4 = 0x1a6 # Hitachi SH4
  IMAGE_FILE_MACHINE_SH5 = 0x1a8 # Hitachi SH5
  IMAGE_FILE_MACHINE_THUMB = 0x1c2 # Thumb
  IMAGE_FILE_MACHINE_WCEMIPSV2 = 0x169 # MIPS little endian WCE v2
  
  # Constants for 'Characteristics' field ########################
  IMAGE_FILE_RELOCS_STRIPPED = 0x0001
  IMAGE_FILE_EXECUTABLE_IMAGE = 0x0002
  IMAGE_FILE_LINE_NUMS_STRIPPED = 0x0004
  IMAGE_FILE_LOCAL_SYMS_STRIPPED = 0x0008
  IMAGE_FILE_AGGRESIVE_WS_TRIM = 0x0010
  IMAGE_FILE_LARGE_ADDRESS_AWARE = 0x0020
  IMAGE_FILE_BYTES_REVERSED_LO = 0x0080
  IMAGE_FILE_32BIT_MACHINE = 0x0100
  IMAGE_FILE_DEBUG_STRIPPED = 0x0200
  IMAGE_FILE_REMOVABLE_RUN_FROM_SWAP = 0x0400
  IMAGE_FILE_NET_RUN_FROM_SWAP = 0x0800
  IMAGE_FILE_SYSTEM = 0x1000
  IMAGE_FILE_DLL = 0x2000
  IMAGE_FILE_UP_SYSTEM_ONLY = 0x4000
  IMAGE_FILE_BYTES_REVERSED_HI = 0x8000

  def get_number_of_sections(self):
    return self.number_of_sections

  def is_dll_file(self):
    return not ((self.characteristics & COFF_Header.IMAGE_FILE_DLL) == 0)
    
  def is_x86(self):
    print(self.machine)
    return self.machine == COFF_Header.IMAGE_FILE_MACHINE_I386

  def get_pointer_to_symbol_table(self):
    return self.pointer_to_symbol_table

  def get_number_of_symbols(self):
    return number_of_symbols  

  def __init__(self, binary_file_handle):
    self.magic = binary_file_handle.read(4)
    self.machine = struct.unpack("h",binary_file_handle.read(2))[0]
    self.number_of_sections = struct.unpack("h",binary_file_handle.read(2))[0]
    self.time_date_stamp = struct.unpack("i", binary_file_handle.read(4))[0]
    self.pointer_to_symbol_table = struct.unpack("i", binary_file_handle.read(4))[0]
    self.number_of_symbols = struct.unpack("i", binary_file_handle.read(4))[0]
    self.size_of_optional_header = struct.unpack("h", binary_file_handle.read(2))[0]
    self.characteristics = struct.unpack("h", binary_file_handle.read(2))[0]
    
    if not self.is_x86():
      """
      logging.debug("COFF Header:{")
      logging.debug(" Machine = 0x%s"%(hex(self.machine)))
      logging.debug(" Number of sections = %d"%get_number_of_sections())
      logging.debug(" TimeDateStamp = 0x%s"%(hex(self.time_date_stamp)))
      logging.debug(" PointerToSymbolTable = 0x%s"%(hex(self.pointer_to_symbol_table)))
      logging.debug(" NumberOfSymbols = %d"%self.number_of_symbols)
      logging.debug(" SizeOfOptionalHeader = %d"%self.size_of_optional_header)
      logging.debug(" Characteristics = %s"%(str(self.characteristics)))
      logging.debug("}")
      """
      # BinaryParseException
      raise Exception("Non-x86 COFF files currently not supported")


    
