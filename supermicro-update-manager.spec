Summary:	Supermicro Update Manager (for UEFI BIOS)
Name:		supermicro-update-manager
# sum version
Version:	2.3.0
Release:	1
License:	Unknown
Group:		Base
# https://www.supermicro.com/SwDownload/SwSelect_Free.aspx?cat=SUM
Source0:	sum_%{version}_Linux_x86_64_20190808.tar.gz
# Source0-md5:	ff46c61ac9c418905c7fe1ab397daa05
URL:		https://www.supermicro.com/solutions/SMS_SUM.cfm
BuildRequires:	unzip
ExclusiveArch:	%{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages	0

%description
The Supermicro Update Manager (SUM) can be used to manage the
BIOS/BMC/CMM/ Broadcom 3108 RAID firmware image update and
configuration update for select systems. In addition, system checks as
well as event log management are also supported. Moreover, special
applications are also provided to facilitate system management.

%prep
%setup -q -n sum_%{version}_Linux_x86_64

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sbindir},%{_libdir}/%{name}}
cp -a {ExternalData,sum} $RPM_BUILD_ROOT%{_libdir}/%{name}
chmod 755 $RPM_BUILD_ROOT%{_libdir}/%{name}/sum

cat << 'EOF' > $RPM_BUILD_ROOT%{_sbindir}/%{name}
#!/bin/sh
cd %{_libdir}/%{name} || exit 1
exec %{_libdir}/%{name}/sum $@
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ReleaseNote.txt SUM_UserGuide.pdf sumrc.sample
%attr(755,root,root) %{_sbindir}/%{name}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/ExternalData
%attr(755,root,root) %{_libdir}/%{name}/sum

