import os

def pcd_path(*comps):
    return os.path.join(os.path.dirname(__file__), *comps)
