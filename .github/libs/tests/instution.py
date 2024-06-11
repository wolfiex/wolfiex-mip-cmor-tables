import os, json, sys, glob

def valid(jsn):
    path = os.path.dirname(jsn['@id']).split(':')[-1]
    toplevel = os.popen('git rev-parse --show-toplevel').read().strip()
    loc = f"{toplevel}/JSONLD/{path}/"
    
    files