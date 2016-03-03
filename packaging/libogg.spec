Name:           libogg
Version:        1.3.2
Release:        0
License:        BSD-2.0
Summary:        Ogg Bitstream Library
Url:            http://www.vorbis.com/
Group:          Multimedia/Audio
Source:         http://downloads.xiph.org/releases/ogg/%{name}-%{version}.tar.gz
Source2:        baselibs.conf
Source1001: 	libogg.manifest
BuildRequires:  pkg-config

%description
Libogg is a library for manipulating ogg bitstreams.  It handles both
making ogg bitstreams and getting packets from ogg bitstreams.

Ogg is the native bitstream format of the libvorbis (Ogg Vorbis audio
codec ) and the libtheora (Theora video codec)

%package devel
Summary:        Include Files and Libraries mandatory for Ogg Development
Group:          Development/Libraries
Requires:       glibc-devel
Requires:       libogg = %{version}

%description devel
This package contains all necessary include files and libraries needed
to compile and develop applications that use libogg.

%prep
%setup -q
cp %{SOURCE1001} .

%build
# Fix optimization level
sed -i s,-O20,-O3,g configure

%configure --disable-static
%__make %{?_smp_mflags}


%check
make check


%install
%make_install

%remove_docs

%post  -p /sbin/ldconfig

%postun  -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%defattr(0644,root,root,0755)
%license COPYING 
%{_libdir}/libogg.so.*

%files devel
%manifest %{name}.manifest
%defattr(0644,root,root,0755)
%{_includedir}/ogg
%{_libdir}/libogg.so
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/ogg.m4
%{_libdir}/pkgconfig/ogg.pc

