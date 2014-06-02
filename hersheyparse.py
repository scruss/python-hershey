#!/usr/bin/python
# hersheyparse.py - simple Hershey Font file parser
# as an example, writes data to a JSON file
# ** NB: Requires input to be cleaned of broken lines **
# scruss - 2014-06-01 - WTFPL (srsly)

from string import split
import sys
import json


def char2val(c):  # data is stored as signed bytes relative to ASCII R
    return ord(c) - ord('R')


def hersh_bbox(lines):
    """ passed an array of lines, returns the smallest bounding box """

    # nice ways of bombing out
    if lines is None:
        return None
    if len(lines[0]) < 1:
        return None
    min_x = max_x = lines[0][0][0]
    min_y = max_y = lines[0][0][1]
    for line in lines:
        for pt in line:
            if pt[0] < min_x:
                min_x = pt[0]
            if pt[1] < min_y:
                min_y = pt[1]
            if pt[0] > max_x:
                max_x = pt[0]
            if pt[1] > max_y:
                max_y = pt[1]
    return ((min_x, min_y), (max_x, max_y))


def hersheyparse(dat):
    """ reads a line of Hershey font text """

    lines = []

    # individual lines are stored separated by <space>+R
    # starting at col 11

    for s in split(dat[10:], ' R'):

        # each line is a list of pairs of coordinates
        # NB: origin is at centre(ish) of character
        #     Y coordinates **increase** downwards

        line = map(None, *[iter(map(char2val, list(s)))] * 2)
        lines.append(line)
    glyph = {  # character code in columns 1-6; it's not ASCII
               # indicative number of vertices in columns 6-9 ** NOT USED **
               # left side bearing encoded in column 9
               # right side bearing encoded in column 10
        'charcode': int(dat[0:5]),
        'left': char2val(dat[8]),
        'right': char2val(dat[9]),
        'lines': lines,
        }
    glyph['bbox'] = hersh_bbox(glyph['lines'])
    return glyph


hershey = []
f = open(sys.argv[1], 'r')
for line in f:
    g = hersheyparse(line.rstrip())
    if g != None:
        hershey.append(g)
f.close()
print json.dumps(hershey, sort_keys=True, separators=(',', ':'))
