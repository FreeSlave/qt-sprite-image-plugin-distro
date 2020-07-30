Name:           qt-sprite-image-plugin
Version:        1.0
Release:        1%{?dist}
Summary:        Qt5 image format plugin for Half-Life and Quake sprites

License:        LGPLv2
URL:            https://github.com/FreeSlave/%{name}
Source0:        https://github.com/FreeSlave/%{name}/archive/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++ cmake qt5-qtbase-devel extra-cmake-modules

%description
qt-sprite-image-plugin is Qt5 image format plugin
and related KDE services for Half-Life and Quake sprites.

%prep
%setup -q

%build
%cmake .
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%package -n qt5-sprite-image-plugin
Summary: qt-sprite-image-plugin shared library
%description -n qt5-sprite-image-plugin
Qt5 image format plugin for Half-Life and Quake sprites.

%package -n qt5-sprite-image-plugin-extra
Summary: KDE services for qt5-sprite-image-plugin
Requires: qhl-mimetypes
BuildArch: noarch
%description -n qt5-sprite-image-plugin-extra
KDE services plugin descriptions for qt5-sprite-image-plugin
and thumbnail service.

%files -n qt5-sprite-image-plugin
%{_libdir}/qt5/plugins/imageformats/libqspr.so

%files -n qt5-sprite-image-plugin-extra
%{_datadir}/kservices5/qimageioplugins/qspr.desktop
%{_datadir}/kservices5/qimageioplugins/spr32.desktop
%{_datadir}/kservices5/qimageioplugins/hlspr.desktop
%{_datadir}/kservices5/qsprthumbnail.desktop

%changelog
* Tue May 31 2016 Roman Chistokhodov 1.0-1
- Initial release
