Summary:	Supermicro Update Manager (for UEFI BIOS)
Name:		supermicro-update-manager
# sum version
Version:	1.7.0
Release:	1
License:	Unknown
Group:		Base
Source0:	ftp://ftp.supermicro.com:/utility/SuperDoctor_5/Linux/SD5_5.5.0_build.784_linux.zip
# Source0-md5:	cdd7684f7065462b9ab73d971257501b
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
%setup -qc
install -d prep; cd prep
unzip ../*.bin || :
unzip \$IA_PROJECT_DIR\$/build/SuperDoctor5-linux.zip


%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sbindir},%{_libdir}/%{name}}
cp -a prep/BIOS/sum/{ExternalData,sum} $RPM_BUILD_ROOT%{_libdir}/%{name}
chmod 755 $RPM_BUILD_ROOT%{_libdir}/%{name}/sum

cat << 'EOF' > $RPM_BUILD_ROOT%{_sbindir}/sum
#!/bin/sh
cd %{_libdir}/%{name} || exit 1
exec ./sum $@
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc prep/BIOS/sum/ReleaseNote.txt
%attr(755,root,root) %{_sbindir}/sum
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/ExternalData
%attr(755,root,root) %{_libdir}/%{name}/sum

