#!/usr/bin/python
# turtle-hershey-example - a trivial demo to say hello
# scruss - 2014-05-06 - dual WTFPL (srsly)

from string import split
import turtle


def char2val(c):  # data is stored as signed bytes relative to ASCII R
    return ord(c) - ord('R')


def hersheyparse(dat):
    """ reads a line of Hershey font text """

    if int(dat[5:8]) - 1 < 2:  # fail if there impossibly few vertices
        return None
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
               # indicative number of vertices in columns 6-9
               # left side bearing encoded in column 9
               # right side bearing encoded in column 10
        'charcode': int(dat[0:5]),
        'vertices': int(dat[5:8]) - 1,
        'left': char2val(dat[8]),
        'right': char2val(dat[9]),
        'lines': lines,
        }
    return glyph


# a hash for the four chars we're going to use: they're cursive

glyphs = {
    'h': '  658 29M\MVOSRNSLTITGSFQGPIOMNSM[ RM[NXOVQSSRURVSVUUXUZV[W[YZZY\V',
    'e': '  655 17NXOYQXRWSUSSRRQROSNUNXOZQ[S[UZVYXV',
    'l': '  662 18OWOVQSTNULVIVGUFSGRIQMPTPZQ[R[TZUYWV',
    'o': '  665 23LZRRPRNSMTLVLXMZO[Q[SZTYUWUUTSRRQSQURWTXWXYWZV',
    }

x_scale = 3
y_scale = -3  # remember: Y is +ve *down* for Hershey ...
x = 0
y = 0
turtle.penup()
turtle.pensize(3)
turtle.goto(x, y)
for c in list('hello'):
    glyph = hersheyparse(glyphs[c])
    x_origin = x
    y_origin = y
    for line in glyph['lines']:
        first = 1
        for pt in line:
            if first == 1:
                first = 0
                turtle.goto(x_origin + x_scale * (pt[0] - glyph['left'
                            ]), y_origin + y_scale * pt[1])
                turtle.pendown()
            else:
                turtle.goto(x_origin + x_scale * (pt[0] - glyph['left'
                            ]), y_origin + y_scale * pt[1])
        turtle.penup()

        # don't forget to move to (right sidebearing, 0) at end of draw

        x = x_origin + x_scale * (glyph['right'] - glyph['left'])
        y = y_origin

turtle.done()
