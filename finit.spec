%define snapshot 0
%define __release 2
%if %{snapshot}
%define snapshot_date 20080917
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

%description
Finit is an init(8) replacement aimed to enhance boot time, especially for
small and/or slow machines. It is a reimplementation of the Eeepc "fastinit"
program based on its system calls with "gaps filled with frog DNA".

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
%attr(0644,root,root) %{_sysconfdir}/finit.conf
/sbin/finit-mdv
%{_sbindir}/services.sh
