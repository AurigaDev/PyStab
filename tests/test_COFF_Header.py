import sys
sys.path.append('loader/pe')
from coff_header import COFF_Header

def test_coff_constructor():
    f = open("/home/auriga/Projects/Auriga/samples/Angr-Samples/tests/x86/windows/TLS.exe", "rb")
    # Seek to COFF header for debugging 
    f.seek(0xf0)
    
    COFF_Header(f)


def test_coff_constructor_arm():
    f = open("/home/auriga/Projects/Auriga/samples/Angr-Samples/tests/armel/test_loops", "rb")
    # Seek to COFF header for debugging 
    f.seek(0xf0)

    COFF_Header(f)
