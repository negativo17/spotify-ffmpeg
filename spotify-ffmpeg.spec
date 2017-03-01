# Remove bundled libraries from requirements/provides
%global         __requires_exclude ^(libav.*\\.so\\..*|libpostproc\\.so\\..*|libswresample\\.so\\..*)$
%global         __provides_exclude ^(lib.*\\.so.*)$

Name:           spotify-ffmpeg
Version:        0.10.16
Release:        3%{?dist}
Summary:        Spotify compatibility package - FFMpeg
License:        GPL
URL:            http://ffmpeg.org

Source0:        https://ffmpeg.org/releases/ffmpeg-%{version}.tar.bz2

ExclusiveArch:  x86_64 %{ix86}

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
    --disable-static \
    --disable-stripping \
    --disable-swscale \
    --enable-gpl \
    --enable-runtime-cpudetect \
    --enable-shared \
    --enable-version3 \
    --libdir='%{_libdir}' \
    --prefix='%{_prefix}' \
    --shlibdir='%{_libdir}/spotify-client' \

%make_build

%install
%make_install
rm -fr %{buildroot}%{_includedir} \
    %{buildroot}%{_libdir}/pkgconfig \
    %{buildroot}%{_libdir}/spotify-client/*.so

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license LICENSE
%{_libdir}/spotify-client/*.so.*

%changelog
* Wed Mar 01 2017 Simone Caronni <negativo17@gmail.com> - 0.10.16-3
- Move all libraries to Spotify private location.
- Update description, summary.
- Update requirements, remove documentation.

* Tue Feb 21 2017 Simone Caronni <negativo17@gmail.com> - 0.10.16-2
- Move all libraries in the system path, for those Spotify dynamically loads
  them but not from the runpath directory. Sigh.

* Tue Feb 14 2017 Simone Caronni <negativo17@gmail.com> - 0.10.16-1
- First build.
