from SCons.Script import Import

Import("env")

board_config = env.BoardConfig()

env.Append(
    CCFLAGS=[
        "-O2",
        "-Wall",  # show warnings
        "-march=%s" % board_config.get("build.march"),
        "-mabi=%s" % board_config.get("build.mabi"),
        "-mcmodel=%s" % board_config.get("build.mcmodel")
    ],

    LINKFLAGS=[
        "-O2",
        "-nostartfiles",
        "-march=%s" % board_config.get("build.march"),
        "-mabi=%s" % board_config.get("build.mabi"),
        "-mcmodel=%s" % board_config.get("build.mcmodel"),
        "-Wl,--wrap=malloc",
        "-Wl,--wrap=free",
        "-Wl,--wrap=open",
        "-Wl,--wrap=lseek",
        "-Wl,--wrap=read",
        "-Wl,--wrap=write",
        "-Wl,--wrap=fstat",
        "-Wl,--wrap=stat",
        "-Wl,--wrap=close",
        "-Wl,--wrap=link",
        "-Wl,--wrap=unlink",
        "-Wl,--wrap=execve",
        "-Wl,--wrap=fork",
        "-Wl,--wrap=getpid",
        "-Wl,--wrap=kill",
        "-Wl,--wrap=wait",
        "-Wl,--wrap=isatty",
        "-Wl,--wrap=times",
        "-Wl,--wrap=sbrk",
        "-Wl,--wrap=_exit",
        "-Wl,--wrap=puts",
        "-Wl,--wrap=_malloc",
        "-Wl,--wrap=_free",
        "-Wl,--wrap=_open",
        "-Wl,--wrap=_lseek",
        "-Wl,--wrap=_read",
        "-Wl,--wrap=_write",
        "-Wl,--wrap=_fstat",
        "-Wl,--wrap=_stat",
        "-Wl,--wrap=_close",
        "-Wl,--wrap=_link",
        "-Wl,--wrap=_unlink",
        "-Wl,--wrap=_execve",
        "-Wl,--wrap=_fork",
        "-Wl,--wrap=_getpid",
        "-Wl,--wrap=_kill",
        "-Wl,--wrap=_wait",
        "-Wl,--wrap=_isatty",
        "-Wl,--wrap=_times",
        "-Wl,--wrap=_sbrk",
        "-Wl,--wrap=__exit",
        "-Wl,--wrap=_puts",
    ],

    LIBS=["c"],
)

# copy CCFLAGS to ASFLAGS (-x assembler-with-cpp mode)
env.Append(ASFLAGS=env.get("CCFLAGS", [])[:])
