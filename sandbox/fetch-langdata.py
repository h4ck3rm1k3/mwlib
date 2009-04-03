#! /usr/bin/env python

from mwlib import lang, mwapidb

def main():
    languages = list(lang.languages)
    languages.sort()
    langdata = {}
    for l in languages:
        w=mwapidb.APIHelper("http://%s.wikipedia.org/w" % l)
        res = w.query(meta='siteinfo', siprop='general|namespaces|namespacealiases|magicwords')
        if res is not None:
            langdata[l] = res["query"]
    import pprint
    pprint.pprint(langdata, open("langdata.py", "wb"))
    

if __name__=="__main__":
    main()
    
