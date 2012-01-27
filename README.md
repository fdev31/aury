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

# Running

The tool is currently Work In Progress, later more things will be automated.
Today's workflow consists in:

- running  ``aury`` command without any argument (the configuration file must be filled correctly, it's JSON)
- reading the traces, you will know if some package needs an update with a trace like ``python-paste (1.7.5.0 => 1.7.5.1)``
- going to your ``~/.config/aury/`` folder to edit ``version.txt`` files under package folders to update the content of the ``PKGBUILD`` file
- installing the package (``makepkg -si``) and running some tests to check everything is ok
- push manually using ``makepkg --source`` and ``burp``

# Future

- ``PKGBUILD`` file will automatically be updated
- User will be interactively prompted to push the file to servers

