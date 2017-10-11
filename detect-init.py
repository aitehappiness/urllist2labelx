# -*- coding: utf-8 -*-

import json, sys


def gen(url):
    flow = {
        "url": url,
        "ops": "download()",
        "type": "image",
        "label": {"detect": {"general_d": {"bbox": []}}},
        "source_url": ""
    }
    return flow


if __name__ == '__main__':
    name = sys.argv[1] if len(sys.argv) > 1 else 'in.txt'
    urllist = []
    with open(name) as content:
        line = content.readline()
        while line:
            url = line.rstrip('\n')
            urllist.append(url)
            line = content.readline()

    r = '\n'.join([json.dumps(gen(url)) for url in urllist])
    with open(name+'.json', 'w+') as f: f.write(r)