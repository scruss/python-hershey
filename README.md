python-hershey
==============

Some crude Python code to parse the Hershey vector fonts. Also
included is the complete font set encoded as JSON, should you just
want to use the data.

Caveats
-------

While the Hershey fonts were pretty nifty for 1967, they have some
problems:

1. They don't use any standard encoding
2. They don't use modern font conventions, so aligning, parsing and
   setting Hershey text is a little complex
3. Y-coordinates are positive *downwards*.

