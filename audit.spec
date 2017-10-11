#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : audit
Version  : 2.8
Release  : 10
URL      : https://people.redhat.com/sgrubb/audit/audit-2.8.tar.gz
Source0  : https://people.redhat.com/sgrubb/audit/audit-2.8.tar.gz
Summary  : User space tools for 2.6 kernel auditing
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ LGPL-2.1 LGPL-2.1+
Requires: audit-bin
Requires: audit-legacypython
Requires: audit-python3
Requires: audit-lib
Requires: audit-doc
Requires: audit-python
BuildRequires : go
BuildRequires : libcap-ng-dev
BuildRequires : openldap-dev
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : swig

%description
The audit package contains the user space utilities for
storing and searching the audit records generated by
the audit subsystem in the Linux 2.6 and later kernels.

%package bin
Summary: bin components for the audit package.
Group: Binaries

%description bin
bin components for the audit package.


%package dev
Summary: dev components for the audit package.
Group: Development
Requires: audit-lib
Requires: audit-bin
Provides: audit-devel

%description dev
dev components for the audit package.


%package doc
Summary: doc components for the audit package.
Group: Documentation

%description doc
doc components for the audit package.


%package legacypython
Summary: legacypython components for the audit package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the audit package.


%package lib
Summary: lib components for the audit package.
Group: Libraries

%description lib
lib components for the audit package.


%package python
Summary: python components for the audit package.
Group: Default
Requires: audit-legacypython
Requires: audit-python3

%description python
python components for the audit package.


%package python3
Summary: python3 components for the audit package.
Group: Default
Requires: python3-core

%description python3
python3 components for the audit package.


%prep
%setup -q -n audit-2.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507727538
%configure --disable-static
make V=1

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 check

%install
export SOURCE_DATE_EPOCH=1507727538
rm -rf %{buildroot}
%make_install
## make_install_append content
chmod a+x %{buildroot}/usr/bin/augenrules
chmod a+x %{buildroot}/usr/bin/audispd
## make_install_append end

%files
%defattr(-,root,root,-)
/usr/lib/golang/src/pkg/redhat.com/audit/audit.go

%files bin
%defattr(-,root,root,-)
/usr/bin/audisp-remote
/usr/bin/audispd
/usr/bin/audispd-zos-remote
/usr/bin/auditctl
/usr/bin/auditd
/usr/bin/augenrules
/usr/bin/aulast
/usr/bin/aulastlog
/usr/bin/aureport
/usr/bin/ausearch
/usr/bin/ausyscall
/usr/bin/autrace
/usr/bin/auvirt

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libaudit.so
/usr/lib64/libauparse.so
/usr/lib64/pkgconfig/audit.pc
/usr/lib64/pkgconfig/auparse.pc
/usr/share/aclocal/*.m4

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
%doc /usr/share/man/man5/*
%doc /usr/share/man/man7/*
%doc /usr/share/man/man8/*

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libaudit.so.1
/usr/lib64/libaudit.so.1.0.0
/usr/lib64/libauparse.so.0
/usr/lib64/libauparse.so.0.0.0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
