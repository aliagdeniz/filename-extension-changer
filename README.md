# filename-extension-changer
Filename Extension Changer can be used for changing all files' extension in a directory. Just not all files, You can adjust file types to be changed. There are 4 options. These are add, replace, show and search.

Usage:
-----
    $ python filename-extension-changer.py <option> <argument1> <argument2> ...

    --add		<directory> <which file type> <to which type>
    --replace	<directory> <which file type> <to which type>
    --show		<directory>
    --search	<directory> <which file type>

Options:
-------
    --add		adds new filename extension to the and of filename.
    --replace	deletes current filename extension and adds new extension.
    --show		shows all files under the given directory.
    --search	searches based on given type.

Installation:
-------------
    $ git clone https://github.com/aliagdeniz/filename-extension-changer
    $ cd filename-extension-changer
    $ python filename-extension-changer.py

License:
--------
GNU GPLv2

Bug Report:
-----------
Issue it here: https://github.com/aliagdeniz/filename-extension-changer/issues
