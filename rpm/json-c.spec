Name:       json-c

Summary:    A JSON implementation in C
Version:    0.13.1
Release:    0
Group:      Multimedia/PulseAudio
License:    MIT
URL:        http://oss.metaparadigm.com/json-c/
Source0:    http://oss.metaparadigm.com/json-c/%{name}-%{version}.tar.gz

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
JSON-C implements a reference counting object model that allows you to
easily construct JSON objects in C, output them as JSON formatted strings
and parse JSON formatted strings back into the C representation of JSON
objects.


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{name}-%{version}/%{name}

%build
%configure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/json-c/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
