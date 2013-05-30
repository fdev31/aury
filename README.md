# AURy - AUR python packages upgrade automation

## What's this ?

Aury is an automatic Python packages upgrader for AUR (archlinux) users.

In short it will:

- get the list of packages you own
- if they follow the standard python packages naming convention:
    - check if there is an upgrade on PyPi
    - edit the PKGBUILD:
        - pkgver
        - pkgrel
        - md5sums
        - url
    - build the package to test if it's fine
    - upload it using ``burp``

### Sample output

    % aury
    Warming up
    Connecting...
    Processing:
    * a8
    * etm
    * Ghost.py
    * hovercraft
    * httpshell
    - insight3d (skipping: not a standard python package)
    [...]
    Processed 34 packages (45 found, 9 rolling packages, 2 non-python).
    %


## Installing

### Archlinux

    % yaourt -Sy aury-git

### Other linux

    % easy_install -U aury

## Configuration

Let *aury* fail once

    % aury

Then edit the ``~/.config/aury/config`` file to suit your AUR website login.
It should list your AUR python package one by one. You may need to list some
package names in the configuration file under ``lowercase`` entry since AUR
only accepts lowercase names.

### Sample "real life" config

    {
    "user": "fab31",
    "lowercase": ["Ghost.py", "pyPdf", "Paste", "ZConfig", "pyScss", "Moar"]
    }


## Running

Most things are now automated, you just have to fix failures related to the package itself.
So, most of the time, run ``aury`` and you'r done (you may have to fill the "lowercase" attribute of the configuration in case a new package needs it.

### When something fails

Most of the time, it's because the packager changed the compression format, this could be handled automatically in future...
But today, you must go to ``~/.config/aury/<package name>``, edit the ``PKGBUILD`` file and run ``makepkg -s`` or ``makepkg -si`` to check if it works.
Then, run ``aury`` again, still with no arguments, to apply your fix and upload the package.

## Bugs

None known, but I can only test on my packages...

## Future

Today I'm quite happy with the result because it's very simple, but maybe some day...

- Detect a compression format change in the package URL ?
- Detect change in dependencies list and upgrade PKGBUILD accordingly
- Test "rolling" packages (-git, -hg, etc...) as well and report them as failed  [enabled using ``-a`` argument ?]

