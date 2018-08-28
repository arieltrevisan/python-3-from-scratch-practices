import logging as log
import os
import errno


def del_file(file_name: str):
    try:
        os.remove(file_name)
    except OSError as e:
        if e.errno != errno.ENOENT:
            raise


fn = "test.log"
del_file(fn)

# filename=fn,
log.basicConfig(level=log.DEBUG,
                format="%(asctime)s %(levelname)s T%(thread)s P%(process)s \"%(message)s\"",
                datefmt="%Y-%m-%d %H:%M:%S")

log.debug("Debug msg")
log.info("Info msg")
log.warning("Warning msg")
log.error("Error msg")
log.critical("Critical msg")
