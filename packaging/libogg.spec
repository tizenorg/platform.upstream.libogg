Name:           libogg
Version:        1.3.0
Release:        0
License:        BSD-3-Clause
Summary:        Ogg Bitstream Library
Url:            http://www.vorbis.com/
Group:          System/Libraries
Source:         %{name}-%{version}.tar.bz2
Source2:        baselibs.conf
BuildRequires:  pkg-config

%description
Libogg is a library for manipulating ogg bitstreams.  It handles both
making ogg bitstreams and getting packets from ogg bitstreams.

Ogg is the native bitstream format of the libvorbis (Ogg Vorbis audio
codec ) and the libtheora (Theora video codec)

%package devel
Summary:        Include Files and Libraries mandatory for Ogg Development
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libogg = %{version}

%description devel
This package contains all necessary include files and libraries needed
to compile and develop applications that use libogg.

%prep
%setup -q

%build
# Fix optimization level
sed -i s,-O20,-O3,g configure

%configure --disable-static
make %{?_smp_mflags}


%check
make check


%install
%make_install

%post  -p /sbin/ldconfig

%postun  -p /sbin/ldconfig

%files
%defattr(0644,root,root,0755)
%doc COPYING 
%{_libdir}/libogg.so.*

%files devel
%defattr(0644,root,root,0755)
%{_includedir}/ogg
%{_libdir}/libogg.so
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/ogg.m4
%{_libdir}/pkgconfig/ogg.pc

%changelog
