import os
os.system("git bisect start 6b80294bb0ce203946adbb699023e1634e3b5289 6a82add9801de043a8ffc51b5a02d695238a3c01")
os.system("git bisect run python myscript.py test")
