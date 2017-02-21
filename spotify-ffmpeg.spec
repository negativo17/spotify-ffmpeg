Name:           spotify-ffmpeg
Version:        0.10.16
Release:        2%{?dist}
Summary:        Complete solution to record, convert and stream audio and video

License:        GPL
URL:            http://ffmpeg.org
Source0:        https://ffmpeg.org/releases/ffmpeg-%{version}.tar.bz2

ExclusiveArch:  x86_64 %{ix86}

BuildRequires:  yasm
Requires:       spotify-client

%description
asd

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
    --shlibdir='%{_libdir}' \

%make_build

%install
%make_install
rm -fr %{buildroot}%{_includedir} \
    %{buildroot}%{_libdir}/pkgconfig \
    %{buildroot}%{_libdir}/*.so

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license LICENSE
%doc README RELEASE MAINTAINERS CREDITS Changelog
%{_libdir}/*.so.*

%changelog
* Tue Feb 21 2017 Simone Caronni <negativo17@gmail.com> - 0.10.16-2
- Move all libraries in the system path, for those Spotify dynamically loads
  them but not from the runpath directory. Sigh.

* Tue Feb 14 2017 Simone Caronni <negativo17@gmail.com> - 0.10.16-1
- First build.
