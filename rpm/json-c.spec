Name:       json-c
Summary:    JSON implementation in C
Version:    0.15
Release:    1
License:    MIT
URL:        https://github.com/json-c/json-c/wiki
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:    cmake
BuildRequires:    ninja
Requires(post):   /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
JSON-C implements a reference counting object model that allows you
to easily construct JSON objects in C, output them as JSON formatted
strings and parse JSON formatted strings back into the C representation
of JSON objects.  It aims to conform to RFC 7159.


%package devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}/%{name}

%build
%cmake \
    -DBUILD_STATIC_LIBS:BOOL=OFF \
    -DCMAKE_BUILD_TYPE:STRING=RELEASE \
    -G Ninja
%ninja_build

%install
%ninja_install

%check
LD_LIBRARY_PATH=$PWD ctest --output-on-failure --force-new-ctest-process %{?_smp_mflags}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog README*
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc
