
from enum import Enum

class mjFunctionCode (Enum):
    DRIVER_INIT =-3    # Not really part of MajorFunction array, but
    DRIVER_STARTIO = -2    # directly precedes it in DriverObject
    DRIVER_UNLOAD = -1
    IRP_MJ_CREATE = 0x00
    IRP_MJ_CREATE_NAMED_PIPE = 0x01
    IRP_MJ_CLOSE = 0x02
    IRP_MJ_READ = 0x03
    IRP_MJ_WRITE = 0x04
    IRP_MJ_QUERY_INFORMATION = 0x05
    IRP_MJ_SET_INFORMATION = 0x06
    IRP_MJ_QUERY_EA = 0x07
    IRP_MJ_SET_EA = 0x08
    IRP_MJ_FLUSH_BUFFERS = 0x09
    IRP_MJ_QUERY_VOLUME_INFORMATION = 0x0a
    IRP_MJ_SET_VOLUME_INFORMATION = 0x0b
    IRP_MJ_DIRECTORY_CONTROL = 0x0c
    IRP_MJ_FILE_SYSTEM_CONTROL = 0x0d
    IRP_MJ_DEVICE_CONTROL = 0x0e
    IRP_MJ_INTERNAL_DEVICE_CONTROL = 0x0f
    IRP_MJ_SHUTDOWN = 0x10
    IRP_MJ_LOCK_CONTROL = 0x11
    IRP_MJ_CLEANUP = 0x12
    IRP_MJ_CREATE_MAILSLOT = 0x13
    IRP_MJ_QUERY_SECURITY = 0x14
    IRP_MJ_SET_SECURITY = 0x15
    IRP_MJ_POWER = 0x16
    IRP_MJ_SYSTEM_CONTROL = 0x17
    IRP_MJ_DEVICE_CHANGE = 0x18
    IRP_MJ_QUERY_QUOTA = 0x19
    IRP_MJ_SET_QUOTA = 0x1a
    IRP_MJ_PNP = 0x1b
    
class Win32StubLibrary(StubProvider): 
    stubDir =  Options.jakstabHome + "/stubs/win32/"
    jakstab_internal = "jakstab.dll"
    def __init__(self, arch):
        self.code = None
        self.stub_map = {}
        self.active_stubs = {}
        self.address_map = {}
        self.imp_id = 0
        self.loaded_def_files = ''
        self.arg0 = expression_factory.create_memory_location(expression_factory.create_plus(arch.stack_pointer(), expression_factory.create_number(4, 32)), 32)
        self.arg1 = expression_factory.create_memory_location(expression_factory.create_plus(arch.stack_pointer(), expression_factory.create_number(8, 32)), 32)
        self.symFinder = None
        self.arch = arch
        # TODO::Define functions in arg0