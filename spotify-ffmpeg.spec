# Remove bundled libraries from requirements/provides
%global         __requires_exclude ^(libav.*\\.so\\..*)$
%global         __provides_exclude ^(lib.*\\.so.*)$

%global         _lto_cflags %{nil}

Name:           spotify-ffmpeg
Version:        3.4.9
Release:        1%{?dist}
Summary:        Spotify compatibility package - FFMpeg
License:        GPL
URL:            http://ffmpeg.org

Source0:        https://ffmpeg.org/releases/ffmpeg-%{version}.tar.bz2

ExclusiveArch:  x86_64 %{ix86}

BuildRequires:  gcc
BuildRequires:  yasm

Requires:       spotify-client%{?_isa}

%description
This package is meant for compatibility purposes with Spotify which requires old
versions of specific libraries in a non-standard path.

%prep
%autosetup -n ffmpeg-%{version}

%build
./configure \
    --disable-avdevice \
    --disable-avfilter \
    --disable-ffmpeg \
    --disable-ffplay \
    --disable-ffprobe \
    --disable-ffserver \
    --disable-indevs \
    --disable-outdevs \
    --disable-postproc \
    --disable-static \
    --disable-stripping \
    --disable-swresample \
    --disable-swscale \
    --enable-gpl \
    --enable-shared \
    --enable-version3 \
    --libdir='%{_libdir}' \
    --optflags="%{optflags}" \
    --prefix='%{_prefix}' \
    --shlibdir='%{_libdir}/spotify-client'

%make_build

%install
%make_install
rm -fr %{buildroot}%{_includedir} \
    %{buildroot}%{_libdir}/pkgconfig \
    %{buildroot}%{_libdir}/spotify-client/*.so \
    %{buildroot}%{_datadir}/ffmpeg

%files
%license COPYING.GPLv3
%{_libdir}/spotify-client/*.so.*

%changelog
* Thu Mar 10 2022 Simone Caronni <negativo17@gmail.com> - 3.4.9-1
- Update to 3.4.9.

* Fri Apr 09 2021 Simone Caronni <negativo17@gmail.com> - 3.4.8-1
- Update to 3.4.8.

* Sun Nov 01 2020 Simone Caronni <negativo17@gmail.com> - 3.4.6-3
- Fix build on Fedora 33+.

* Wed Jul 24 2019 Simone Caronni <negativo17@gmail.com> - 3.4.6-2
- Disable swresample and postproc.

* Sat Apr 13 2019 Simone Caronni <negativo17@gmail.com> - 3.4.6-1
- Update to 3.4.6.

* Wed Mar 01 2017 Simone Caronni <negativo17@gmail.com> - 0.10.16-3
- Move all libraries to Spotify private location.
- Update description, summary.
- Update requirements, remove documentation.

* Tue Feb 21 2017 Simone Caronni <negativo17@gmail.com> - 0.10.16-2
- Move all libraries in the system path, for those Spotify dynamically loads
  them but not from the runpath directory. Sigh.

* Tue Feb 14 2017 Simone Caronni <negativo17@gmail.com> - 0.10.16-1
- First build.
