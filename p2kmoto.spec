%define	lib_name lib%{name}
%define		soname 0
%define		svnversion svn20071112
Name:		p2kmoto
Summary:	Software intended to be used with Motorola telephones based on the P2K platform
Version:	0.1.%{svnversion}
Release:	1
Url:		http://moto4lin.sourceforge.net/
Source0:	p2kmoto-%{svnversion}.tar.bz2
Patch0:		fix-no-return-in-nonvoid-function.patch
License:	GPL
Group:		Networking/File transfer
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool 
BuildRequires:	libusb-devel >= 0.1.8
Requires:	%{lib_name}%{soname} = %{version}-%{release}

%description
The moto4lin software is intended to be used with Motorola telephones based on the P2K platform.

%package -n %{lib_name}%{soname}
Summary:	Software intended to be used with Motorola telephones based on the P2K platform
Group:		System/Libraries
Provides:	%{lib_name}%{soname} = %{version}-%{release}
Provides:	%{lib_name} = %{version}-%{release}

%description -n  %{lib_name}%{soname}
The moto4lin software is intended to be used with Motorola telephones based on the P2K platform.

%package -n p2kmoto-devel
Summary:	Software intended to be used with Motorola telephones based on the P2K platform
Group:		System/Libraries
Provides:	p2kmoto-devel = %{version}-%{release}
Requires:	%{lib_name}%{soname} = %{version}-%{release}

%description -n p2kmoto-devel
The moto4lin software is intended to be used with Motorola telephones based on the P2K platform.

%prep
%setup -q -n %{name}-%{svnversion}
%patch0
ln -s %{_datadir}/automake-1.10/depcomp

%build
autoconf
export CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS"
./configure --prefix=%{_prefix} --libdir=%{_libdir}
make -j 2

%install
make DESTDIR=$RPM_BUILD_ROOT install

rm -fr %{buildroot}%{_libdir}/*.*a

%post -n  %{lib_name}%{soname} -p /sbin/ldconfig

%postun -n  %{lib_name}%{soname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/*

%files -n  %{lib_name}%{soname}
%defattr(-,root,root)
%{_libdir}/libp2kmoto.so.%{soname}
%{_libdir}/libp2kmoto.so.%{soname}.*

%files -n p2kmoto-devel
%defattr(-,root,root)
%{_libdir}/libp2kmoto.so
%{_includedir}/*

