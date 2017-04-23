#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : audit
Version  : 2.7.6
Release  : 3
URL      : https://people.redhat.com/sgrubb/audit/audit-2.7.6.tar.gz
Source0  : https://people.redhat.com/sgrubb/audit/audit-2.7.6.tar.gz
Summary  : User space tools for 2.6 kernel auditing
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ LGPL-2.1 LGPL-2.1+
Requires: audit-bin
Requires: audit-python
Requires: audit-lib
Requires: audit-doc
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


%package lib
Summary: lib components for the audit package.
Group: Libraries

%description lib
lib components for the audit package.


%package python
Summary: python components for the audit package.
Group: Default

%description python
python components for the audit package.


%prep
%setup -q -n audit-2.7.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1492961383
%configure --disable-static
make V=1

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 check

%install
export SOURCE_DATE_EPOCH=1492961383
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

%files lib
%defattr(-,root,root,-)
/usr/lib64/libaudit.so.1
/usr/lib64/libaudit.so.1.0.0
/usr/lib64/libauparse.so.0
/usr/lib64/libauparse.so.0.0.0

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
