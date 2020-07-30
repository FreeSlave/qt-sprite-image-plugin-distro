# qt-sprite-image-plugin distributions

Making [qt-sprite-image-plugin](https://github.com/FreeSlave/qt-sprite-image-plugin) packages for different distros.

## Make deb package

First make an orig archive. Assuming [qt-sprite-image-plugin](https://github.com/FreeSlave/qt-sprite-image-plugin) is cloned into the same directory as this repository is:

```
    ./make_deb_orig.sh
```

Build the package using debuild:

```
    sudo apt-get install build-essential devscripts debhelper
    (cd deb/qt-sprite-image-plugin && debuild -uc -us)
```

## Make rpm package

```
    ./make_rpm_orig.sh
```

Build using mock:

```
    sudo apt-get install mock # also can be installed on Debian
    sudo groupadd mock # if group does not exist yet
    sudo usermod -a -G mock $USER # allow starting mock as regular user

    # Re-login to system to apply changes to user groups

    CONFIGURATION=fedora-25-x86_64
    VENDOR=fc25
    VERSION="$(cat ../qt-sprite-image-plugin/version)"
    REVISION=1
    mkdir -p rpm/SRPMS rpm/RPMS
    mock --resultdir="rpm/SRPMS" -r "$CONFIGURATION" --buildsrpm --spec "rpm/SPECS/qt-sprite-image-plugin.spec" --sources "rpm/SOURCES"
    mock --resultdir="rpm/RPMS" -r "$CONFIGURATION" "rpm/SRPMS/qt-sprite-image-plugin-$VERSION-$REVISION.$VENDOR.src.rpm"
```
