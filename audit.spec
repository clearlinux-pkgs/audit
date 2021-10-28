#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : audit
Version  : 3.0.6
Release  : 59
URL      : https://people.redhat.com/sgrubb/audit/audit-3.0.6.tar.gz
Source0  : https://people.redhat.com/sgrubb/audit/audit-3.0.6.tar.gz
Summary  : User space tools for kernel auditing
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ LGPL-2.1 LGPL-2.1+
Requires: audit-bin = %{version}-%{release}
Requires: audit-data = %{version}-%{release}
Requires: audit-lib = %{version}-%{release}
Requires: audit-license = %{version}-%{release}
Requires: audit-man = %{version}-%{release}
Requires: audit-python = %{version}-%{release}
Requires: audit-python3 = %{version}-%{release}
Requires: audit-services = %{version}-%{release}
Requires: audisp-json
BuildRequires : audisp-json
BuildRequires : buildreq-golang
BuildRequires : libcap-ng-dev
BuildRequires : openldap-dev
BuildRequires : python3-dev
BuildRequires : swig

%description
The audit package contains the user space utilities for
storing and searching the audit records generated by
the audit subsystem in the Linux 2.6 and later kernels.

%package bin
Summary: bin components for the audit package.
Group: Binaries
Requires: audit-data = %{version}-%{release}
Requires: audit-license = %{version}-%{release}
Requires: audit-services = %{version}-%{release}

%description bin
bin components for the audit package.


%package data
Summary: data components for the audit package.
Group: Data

%description data
data components for the audit package.


%package dev
Summary: dev components for the audit package.
Group: Development
Requires: audit-lib = %{version}-%{release}
Requires: audit-bin = %{version}-%{release}
Requires: audit-data = %{version}-%{release}
Provides: audit-devel = %{version}-%{release}
Requires: audit = %{version}-%{release}

%description dev
dev components for the audit package.


%package lib
Summary: lib components for the audit package.
Group: Libraries
Requires: audit-data = %{version}-%{release}
Requires: audit-license = %{version}-%{release}

%description lib
lib components for the audit package.


%package license
Summary: license components for the audit package.
Group: Default

%description license
license components for the audit package.


%package man
Summary: man components for the audit package.
Group: Default

%description man
man components for the audit package.


%package python
Summary: python components for the audit package.
Group: Default
Requires: audit-python3 = %{version}-%{release}

%description python
python components for the audit package.


%package python3
Summary: python3 components for the audit package.
Group: Default
Requires: python3-core

%description python3
python3 components for the audit package.


%package services
Summary: services components for the audit package.
Group: Systemd services

%description services
services components for the audit package.


%prep
%setup -q -n audit-3.0.6
cd %{_builddir}/audit-3.0.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1633108178
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static --enable-systemd \
--without-python \
--with-python3
make

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check

%install
export SOURCE_DATE_EPOCH=1633108178
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/audit
cp %{_builddir}/audit-3.0.6/COPYING %{buildroot}/usr/share/package-licenses/audit/dfac199a7539a404407098a2541b9482279f690d
cp %{_builddir}/audit-3.0.6/COPYING.LIB %{buildroot}/usr/share/package-licenses/audit/3ac522f07da0f346b37b29cd73a60f79e992ffba
%make_install
## Remove excluded files
rm -f %{buildroot}/usr/libexec/initscripts/legacy-actions/auditd/condrestart
rm -f %{buildroot}/usr/libexec/initscripts/legacy-actions/auditd/reload
rm -f %{buildroot}/usr/libexec/initscripts/legacy-actions/auditd/restart
rm -f %{buildroot}/usr/libexec/initscripts/legacy-actions/auditd/resume
rm -f %{buildroot}/usr/libexec/initscripts/legacy-actions/auditd/rotate
rm -f %{buildroot}/usr/libexec/initscripts/legacy-actions/auditd/state
rm -f %{buildroot}/usr/libexec/initscripts/legacy-actions/auditd/stop
## install_append content
chmod a+x %{buildroot}/usr/bin/augenrules
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib/golang/src/pkg/redhat.com/audit/audit.go

%files bin
%defattr(-,root,root,-)
/usr/bin/audisp-remote
/usr/bin/audisp-syslog
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

%files data
%defattr(-,root,root,-)
/usr/share/audit/sample-rules/10-base-config.rules
/usr/share/audit/sample-rules/10-no-audit.rules
/usr/share/audit/sample-rules/11-loginuid.rules
/usr/share/audit/sample-rules/12-cont-fail.rules
/usr/share/audit/sample-rules/12-ignore-error.rules
/usr/share/audit/sample-rules/20-dont-audit.rules
/usr/share/audit/sample-rules/21-no32bit.rules
/usr/share/audit/sample-rules/22-ignore-chrony.rules
/usr/share/audit/sample-rules/23-ignore-filesystems.rules
/usr/share/audit/sample-rules/30-nispom.rules
/usr/share/audit/sample-rules/30-ospp-v42-1-create-failed.rules
/usr/share/audit/sample-rules/30-ospp-v42-1-create-success.rules
/usr/share/audit/sample-rules/30-ospp-v42-2-modify-failed.rules
/usr/share/audit/sample-rules/30-ospp-v42-2-modify-success.rules
/usr/share/audit/sample-rules/30-ospp-v42-3-access-failed.rules
/usr/share/audit/sample-rules/30-ospp-v42-3-access-success.rules
/usr/share/audit/sample-rules/30-ospp-v42-4-delete-failed.rules
/usr/share/audit/sample-rules/30-ospp-v42-4-delete-success.rules
/usr/share/audit/sample-rules/30-ospp-v42-5-perm-change-failed.rules
/usr/share/audit/sample-rules/30-ospp-v42-5-perm-change-success.rules
/usr/share/audit/sample-rules/30-ospp-v42-6-owner-change-failed.rules
/usr/share/audit/sample-rules/30-ospp-v42-6-owner-change-success.rules
/usr/share/audit/sample-rules/30-ospp-v42.rules
/usr/share/audit/sample-rules/30-pci-dss-v31.rules
/usr/share/audit/sample-rules/30-stig.rules
/usr/share/audit/sample-rules/31-privileged.rules
/usr/share/audit/sample-rules/32-power-abuse.rules
/usr/share/audit/sample-rules/40-local.rules
/usr/share/audit/sample-rules/41-containers.rules
/usr/share/audit/sample-rules/42-injection.rules
/usr/share/audit/sample-rules/43-module-load.rules
/usr/share/audit/sample-rules/44-installers.rules
/usr/share/audit/sample-rules/70-einval.rules
/usr/share/audit/sample-rules/71-networking.rules
/usr/share/audit/sample-rules/99-finalize.rules
/usr/share/audit/sample-rules/README-rules

%files dev
%defattr(-,root,root,-)
/usr/include/auparse-defs.h
/usr/include/auparse.h
/usr/include/libaudit.h
/usr/lib64/libaudit.so
/usr/lib64/libauparse.so
/usr/lib64/pkgconfig/audit.pc
/usr/lib64/pkgconfig/auparse.pc
/usr/share/aclocal/*.m4
/usr/share/man/man3/audit_add_rule_data.3
/usr/share/man/man3/audit_add_watch.3
/usr/share/man/man3/audit_close.3
/usr/share/man/man3/audit_delete_rule_data.3
/usr/share/man/man3/audit_detect_machine.3
/usr/share/man/man3/audit_encode_nv_string.3
/usr/share/man/man3/audit_encode_value.3
/usr/share/man/man3/audit_get_reply.3
/usr/share/man/man3/audit_get_session.3
/usr/share/man/man3/audit_getloginuid.3
/usr/share/man/man3/audit_is_enabled.3
/usr/share/man/man3/audit_log_acct_message.3
/usr/share/man/man3/audit_log_semanage_message.3
/usr/share/man/man3/audit_log_user_avc_message.3
/usr/share/man/man3/audit_log_user_comm_message.3
/usr/share/man/man3/audit_log_user_command.3
/usr/share/man/man3/audit_log_user_message.3
/usr/share/man/man3/audit_open.3
/usr/share/man/man3/audit_request_rules_list_data.3
/usr/share/man/man3/audit_request_signal_info.3
/usr/share/man/man3/audit_request_status.3
/usr/share/man/man3/audit_set_backlog_limit.3
/usr/share/man/man3/audit_set_backlog_wait_time.3
/usr/share/man/man3/audit_set_enabled.3
/usr/share/man/man3/audit_set_failure.3
/usr/share/man/man3/audit_set_pid.3
/usr/share/man/man3/audit_set_rate_limit.3
/usr/share/man/man3/audit_setloginuid.3
/usr/share/man/man3/audit_update_watch_perms.3
/usr/share/man/man3/audit_value_needs_encoding.3
/usr/share/man/man3/auparse_add_callback.3
/usr/share/man/man3/auparse_destroy.3
/usr/share/man/man3/auparse_feed.3
/usr/share/man/man3/auparse_feed_age_events.3
/usr/share/man/man3/auparse_feed_has_data.3
/usr/share/man/man3/auparse_find_field.3
/usr/share/man/man3/auparse_find_field_next.3
/usr/share/man/man3/auparse_first_field.3
/usr/share/man/man3/auparse_first_record.3
/usr/share/man/man3/auparse_flush_feed.3
/usr/share/man/man3/auparse_get_field_int.3
/usr/share/man/man3/auparse_get_field_name.3
/usr/share/man/man3/auparse_get_field_num.3
/usr/share/man/man3/auparse_get_field_str.3
/usr/share/man/man3/auparse_get_field_type.3
/usr/share/man/man3/auparse_get_filename.3
/usr/share/man/man3/auparse_get_line_number.3
/usr/share/man/man3/auparse_get_milli.3
/usr/share/man/man3/auparse_get_node.3
/usr/share/man/man3/auparse_get_num_fields.3
/usr/share/man/man3/auparse_get_num_records.3
/usr/share/man/man3/auparse_get_record_num.3
/usr/share/man/man3/auparse_get_record_text.3
/usr/share/man/man3/auparse_get_serial.3
/usr/share/man/man3/auparse_get_time.3
/usr/share/man/man3/auparse_get_timestamp.3
/usr/share/man/man3/auparse_get_type.3
/usr/share/man/man3/auparse_get_type_name.3
/usr/share/man/man3/auparse_goto_field_num.3
/usr/share/man/man3/auparse_goto_record_num.3
/usr/share/man/man3/auparse_init.3
/usr/share/man/man3/auparse_interpret_field.3
/usr/share/man/man3/auparse_new_buffer.3
/usr/share/man/man3/auparse_next_event.3
/usr/share/man/man3/auparse_next_field.3
/usr/share/man/man3/auparse_next_record.3
/usr/share/man/man3/auparse_node_compare.3
/usr/share/man/man3/auparse_normalize.3
/usr/share/man/man3/auparse_normalize_functions.3
/usr/share/man/man3/auparse_reset.3
/usr/share/man/man3/auparse_set_eoe_timeout.3
/usr/share/man/man3/auparse_set_escape_mode.3
/usr/share/man/man3/auparse_timestamp_compare.3
/usr/share/man/man3/ausearch_add_expression.3
/usr/share/man/man3/ausearch_add_interpreted_item.3
/usr/share/man/man3/ausearch_add_item.3
/usr/share/man/man3/ausearch_add_regex.3
/usr/share/man/man3/ausearch_add_timestamp_item.3
/usr/share/man/man3/ausearch_add_timestamp_item_ex.3
/usr/share/man/man3/ausearch_clear.3
/usr/share/man/man3/ausearch_next_event.3
/usr/share/man/man3/ausearch_set_stop.3
/usr/share/man/man3/get_auditfail_action.3
/usr/share/man/man3/set_aumessage_mode.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libaudit.so.1
/usr/lib64/libaudit.so.1.0.0
/usr/lib64/libauparse.so.0
/usr/lib64/libauparse.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/audit/3ac522f07da0f346b37b29cd73a60f79e992ffba
/usr/share/package-licenses/audit/dfac199a7539a404407098a2541b9482279f690d

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man5/audisp-remote.conf.5
/usr/share/man/man5/auditd-plugins.5
/usr/share/man/man5/auditd.conf.5
/usr/share/man/man5/ausearch-expression.5
/usr/share/man/man5/libaudit.conf.5
/usr/share/man/man5/zos-remote.conf.5
/usr/share/man/man7/audit.rules.7
/usr/share/man/man8/audisp-remote.8
/usr/share/man/man8/audisp-syslog.8
/usr/share/man/man8/audispd-zos-remote.8
/usr/share/man/man8/auditctl.8
/usr/share/man/man8/auditd.8
/usr/share/man/man8/augenrules.8
/usr/share/man/man8/aulast.8
/usr/share/man/man8/aulastlog.8
/usr/share/man/man8/aureport.8
/usr/share/man/man8/ausearch.8
/usr/share/man/man8/ausyscall.8
/usr/share/man/man8/autrace.8
/usr/share/man/man8/auvirt.8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/auditd.service
