python-hershey
==============

Some simple Python code to parse the Hershey vector fonts. Also
included is the complete font set encoded as JSON, should you just
want to use the data.

The Python code creates an array of dictionaries (hashes), for example:

    glyph = {
        'bbox': [[-4,-5],[4,4]], # glyph bounding box (derived)
		'charcode': 1,           # Hershey (NOT ASCII) character code
		'left':  -5,             # left bearing X coordinate
		'right':  5,             # right bearing X coordinate
		# glyph vectors: a list of lists of lists, or an array of
        #                lines of points
		'lines': [[[0,-5],[-4,4]],[[0,-5],[4,4]],[[-2,1],[2,1]]]
    }

The above example has three lines, each with two points, each with an
X and a Y coordinate. If you plot the lines, you will get an *upside
down* capital letter A. These data use obsolete machine coordinates
instead of the familiar Cartesian convention.

## Caveats ##

While the Hershey fonts were pretty nifty for 1967, they have some
problems:

1. They don't use any standard encoding
2. They don't use modern font conventions, so aligning, parsing and
   setting Hershey text is a little complex
3. Y-coordinates are positive *downwards*, so everything's upside down. (Or right way up, if you use SVG.)

## Requirements ##

* Python 2.7.x

## Contents ##

* hershey-occidental.dat --- the original Usenet
  [Hershey](http://cd.textfiles.com/sourcecode/usenet/compsrcs/unix/volume04/hershey/)
  western font data, reformatted without linebreaks (using Kamal
  Mostafa's
  [hershey-jhf-fix-linebreaks.py](https://github.com/kamalmostafa/hershey-fonts/blob/master/tools/hershey-jhf-fix-linebreaks.py
  "hershey-jhf-fix-linebreaks.py")), and with a minor error in the
  side bearing of character #3010 corrected.
* hershey-oriental.dat --- the original Usenet Hershey Japanese font
  data, reformatted as above, verbatim.
* hershey-occidental.json --- the Hershey western data as JSON;
  essentially the output of `hersheyparse.py` run over `hershey-occidental.dat`
* hershey-oriental.json --- the Hershey Japanese data as JSON.
* hersheyparse.py --- simple Python parser for reformatted Hershey
  font files.
* turtle-hershey-example.py --- tiny demo that uses Python's turtle
  module to say hello.

## Licence ##

For the work created or modified by me (Stewart C. Russell, aka
scruss), dual-licensed CC0 / WTFPL (srsly). Time and link rot haven't
been kind to the Hershey fonts since they were first published in
1967, and then republished to mod.sources sometime in the
1980s. References to US Government publications documenting the fonts
are mostly dead: tapes of the data are no longer available, and the
best we have is Jim Hurt et al's efforts from Usenet.

It asks that the following be kept in any distribution derived from
the work of the Usenet Font Consortium:

    USE RESTRICTION:
        This distribution of the Hershey Fonts may be used by anyone for
        any purpose, commercial or otherwise, providing that:
                1. The following acknowledgements must be distributed with
                        the font data:
                        - The Hershey Fonts were originally created by Dr.
                                A. V. Hershey while working at the U. S.
                                National Bureau of Standards.
                        - The format of the Font data in this distribution
                                was originally created by
                                        James Hurt
                                        Cognition, Inc.
                                        900 Technology Park Drive
                                        Billerica, MA 01821
                                        (mit-eddie!ci-dandelion!hurt)
                2. The font data in this distribution may be converted into
                        any other format *EXCEPT* the format distributed by
                        the U.S. NTIS (which organization holds the rights
                        to the distribution and use of the font data in that
                        particular format). Not that anybody would really
                        *want* to use their format... each point is described
                        in eight bytes as "xxx yyy:", where xxx and yyy are
                        the coordinate values as ASCII numbers.

More details at
[Hershey fonts for Ghostscript](http://www.ghostscript.com/doc/current/Hershey.htm
"Hershey fonts for Ghostscript"), where the data are described as being
in the public domain. 

## Other resources ##

* I have compiled a document containing all of the outlines of the
  Hershey fonts as PDF, available here:
  [Forgive me, A V Hershey ...](http://scruss.com/blog/2014/05/02/forgive-me-a-v-hershey/
  "Forgive me, A V Hershey ..."). It is under a CC0/WTFPL licence, and
  can be used for anything.
  
* Archive.org hosts Wolcott & Hilsenrath's [A contribution to computer typesetting techniques : tables of coordinates for Hershey's repertory of occidental type fonts and graphic symbols](https://archive.org/details/contributiontoco424wolc)

* (PDF page images of Wolcott & Hilsenrath's *“A contribution to
  computer typesetting techniques : tables of coordinates for
  Hershey's repertory of occidental type fonts and graphic symbols”* (1976)
  are available at the Hathi Trust, again marked as public domain:
  [Catalog Record: A contribution to computer typesetting... | Hathi Trust Digital Library](http://catalog.hathitrust.org/Record/006865721
  "Catalog Record: A contribution to computer typesetting... | Hathi
  Trust Digital Library"))

* Allen V. Hershey's *Calligraphy for Computers* (US Naval Weapons
  Laboratory, 1967-08-01, NWL Report No. 2101, NTIS accession number
  AD-662 398) is still available for US $25 for a PDF copy from NTIS:
  [Calligraphy for Computers.](http://www.ntis.gov/search/product.aspx?ABBR=AD662398
  "Calligraphy for Computers."). It is of some historical interest.

* *Calligraphy for Computers* is also available for free on Archive.org: [Calligraphy for Computers - Hershey, A V](https://archive.org/details/hershey-calligraphy_for_computers "Calligraphy for Computers - Hershey, A V"). Thanks to Frank Grießhammer [@kioskfonts](https://twitter.com/kioskfonts/status/632015080981327872) for pointing me to the record/download link on [dtic.mil](http://oai.dtic.mil/oai/oai?verb=getRecord&amp;metadataPrefix=html&amp;identifier=AD0662398).

* The file [plhershey-unicode.csv](http://sourceforge.net/p/plplot/code/HEAD/tree/trunk/fonts/plhershey-unicode.csv
  "plhershey-unicode.csv") from the PLplot project purports to be a
  Hershey to Unicode mapping table. It's not very useful.

* [plotutils](http://www.gnu.org/software/plotutils/ "plotutils") has an updated table of glyphs embedded in its source code.

Stewart C. Russell, Toronto - scruss.com - 2014-06-01
