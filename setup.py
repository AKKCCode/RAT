from cx_Freeze import setup, Executable

setup(
    name="proc",
    version="1.0",
    description="proc",
    executables=[Executable("proc.py")],
)
