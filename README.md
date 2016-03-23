The Yewno Journals assignment
=============================

How To Run Me
-------------

This assumes you have a docker environment already set up.

1. `build.sh`
2. docker-compose up
3. `load_data.sh` [<endpoint_ip>]
4. go wild with `curl`, probably

What I Should've Done But Didn't... And Why
-------------------------------------------

The assignment asked to treat this as a *feature request*.

Under these circumstances I would normally negotiate the spec if I feel it is
inadequate, but alas that would probably mean nothing would get done till
Wednesday, and that day is mostly packed for me. :D

This demo is fully functional but there is a couple of potential issues:

* Autocomplete is going to be slow as molasses.  This is because searches are
  case-insensitive regexes.  It would be better to store lowercase titles and
  do substring matches with a functioning index.  Of course then one probably
  would need not bother with an entirely extraneous `redis` database.
* There is no way to distinguish journals with identical titles whatsoever as
  that is the only field.  Maybe another field like publication date would help.
* The `haproxy` configuration has warnings.

In an ideal world I would've had more comments and unit tests!
