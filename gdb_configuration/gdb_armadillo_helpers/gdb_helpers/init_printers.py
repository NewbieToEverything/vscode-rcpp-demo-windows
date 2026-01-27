# init_printers.py
import gdb
# load pretty printers for std::complex and Armadillo types
try:
    import gdb_std_complex_printer
except ImportError as e:
    print(f"[GDB] Failed to load std::complex printer: {e}")
try:
    import gdb_armadillo_printers
except ImportError as e:
    print(f"[GDB] Failed to load Armadillo printers: {e}")

# Set GDB to print all elements in containers，
# will not affect VSCode VARIABLES view，but the -exec print command DEBUG CONSOLE
gdb.execute("set print elements unlimited")