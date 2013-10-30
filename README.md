excess
======

Make XML Schemas feel more like Python

Status
------

`excess` is still in the "exploratory", pre-alpha phase.  It is being developed to support future versions of [python-cybox](https://github.com/CybOXProject/python-cybox), [python-maec](https://github.com/MAECProject/python-maec), and [python-stix](https://github.com/STIXProject/python-stix), but the intent is that it will be useful beyond just those three projects.


Why?
----

The goal of `excess` is to provide a simple, declarative way to build Python classes that implement XML Schemas. 

Sometimes (or perhaps often) you need to generate XML content that conforms to a particular XML Schema, or parse existing XML content into Python objects.  Existing tools such as [lxml](http://lxml.de/) provide a excellent way to create and access the underlying XML in a Pythonic way, but still require a good understanding of XML to use effectively and ensure error-free XML.

Additionally, `excess` will allow programmers to work with standard Python datatypes while seamlessly translating them too and from their XML equivalents, and also support serializing the objects into other data serialization formats such as JSON or YAML. 

Other tools in a related vein include:
* [generateDS](http://www.rexx.com/~dkuhlman/generateDS.html)
* [xmltodict](https://github.com/martinblech/xmltodict)
* [PyXB](http://pyxb.sourceforge.net/)
* [lxml.objectify](http://lxml.de/objectify.html)

While each of these is useful, each is either missing features that I'd like, or in some other way just doesn't mesh with the way my brain thinks about XML and Python, resulting in Python code that feels tedious or labored to me. 
