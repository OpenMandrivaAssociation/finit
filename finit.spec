%define snapshot 0
%define __release 7
%if %{snapshot}
%define snapshot_date 20090414
%define _release 0.%{snapshot_date}.%{__release}
%else
%define _release %{__release}
%endif

Name:		finit
Version:	0.6
Release:	%mkrel %{_release}
Summary:	Fast /sbin/init replacement
License:	MIT
Group:		System/Base
URL:		http://helllabs.org/git/eeepc.git
# Tarball provided by Claudio
Source0: 	finit-%{version}%{?snapshot_date:-pre}%{?snapshot_date}.tar.bz2
Source1: 	finit.conf
Source2: 	services.sh
BuildRequires:	glibc-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}
Suggests:	finit-config

%description
Finit is an init(8) replacement aimed to enhance boot time, especially for
small and/or slow machines. It is a reimplementation of the Eeepc "fastinit"
program based on its system calls with "gaps filled with frog DNA".

%package config-default
Summary:	Default configuration for finit
Group:		System/Base
Provides:	finit-config

%description config-default
This package contains the default configuration for finit.

%prep
%setup -q -n finit-%{version}%{?snapshot_date:-pre}

%build
%make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/{sbin,%{_sbindir},%{_sysconfdir}}
cp finit-mdv %{buildroot}/sbin
cp %{_sourcedir}/finit.conf %{buildroot}%{_sysconfdir}
cp %{_sourcedir}/services.sh %{buildroot}%{_sbindir}

%files
%defattr(0755,root,root,0755)
/sbin/finit-mdv

%files config-default
%attr(0644,root,root) %{_sysconfdir}/finit.conf
%{_sbindir}/services.sh


%changelog
* Tue Apr 14 2009 Caio Begotti <caio1982@mandriva.org> 0.6-7mdv2010.0
+ Revision: 367163
- no need to keep those as they have been merged upstream and a new version will be released soon

* Mon Apr 06 2009 Caio Begotti <caio1982@mandriva.org> 0.6-6mdv2009.1
+ Revision: 364478
- bumping
- fix the makefile to build it clean on deborah
- updating finit's tarball and version after claudio merged new patches upstream

* Thu Oct 02 2008 Olivier Blin <oblin@mandriva.com> 0.6-4mdv2009.0
+ Revision: 290924
- add startx command support (from git)

* Wed Oct 01 2008 Olivier Blin <oblin@mandriva.com> 0.6-3mdv2009.0
+ Revision: 290467
- split out config in a finit-config-default package

* Tue Sep 30 2008 Olivier Blin <oblin@mandriva.com> 0.6-2mdv2009.0
+ Revision: 289920
- initial finit package (from gdium project)
- create finit

