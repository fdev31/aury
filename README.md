# Installing

## Archlinux

    % yaourt -Sy aury-git

## Other linux

    % easy_install -U aury

# Configuration

Let *aury* fail once

    % aury

Then edit the ``~/.config/aury/config`` file to suit your AUR website login.
It should list your AUR python package one by one. You may need to list some
package names in the configuration file under ``lowercase`` entry since AUR
only accepts lowercase names.

## Sample "real life" config

    {
    "user": "fab31",
    "lowercase": ["Ghost.py", "pyPdf", "Paste", "ZConfig", "pyScss", "Moar"]
    }


# Running

Most things are now automated, you just have to fix failures related to the package itself.
So, most of the time, run ``aury`` and you'r done (you may have to fill the "lowercase" attribute of the configuration in case a new package needs it.

## When something fails

Most of the time, it's because the packager changed the compression format, this could be handled automatically in future...
But today, you must go to ``~/.config/aury/<package name>``, edit the ``PKGBUILD`` file and run ``makepkg -s`` or ``makepkg -si`` to check if it works.
Then, run ``aury`` again, still with no arguments, to apply your fix and upload the package.

# Bugs

None known, but I can only test on my packages...

# Future

Today I'm quite happy with the result, it automates all the packages I own on AUR, but:

- Detect a compression format change in the package URL ?


