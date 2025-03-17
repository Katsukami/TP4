import os
os.system("git bisect start 57e1d49bd2025daf5fc34a3840512c6a6aa73229 6a82add9801de043a8ffc51b5a02d695238a3c01")
os.system("git bisect run python manage.py test")
