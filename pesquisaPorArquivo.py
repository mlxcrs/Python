import os.path
import sys
import glob
def find(txt):
    resp = []
    for path in sys.path:
        mods = glob.glob('%s/*.py' % path)
        for mod in mods:
            if txt in os.path.basename(mod):
                resp.append(mod)
    return resp