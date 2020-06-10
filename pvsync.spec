Summary: pvsync to help move nfs file to new pv
Name: pvsync
Version: 1.0.0
Release: 1%{?dist}
Source0: pvsync-1.0.0.tar.gz
License: GPL
Group: liangguohun 
URL: https://github.com/liangguohun/pvsync
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Packager: liangguohun

%define userpath /usr/sbin/

%description
This is a software to help move nfs file to new pv in k8s

%prep
%setup -c

%post
echo Install Success

%build

%install
install -d $RPM_BUILD_ROOT%{userpath}
cp -a %{name}* $RPM_BUILD_ROOT%{userpath}

%clean
#rm -rf $RPM_BUILD_ROOT
#rm -rf $RPM_BUILD_DIR/%{name}-%{version}

%files
%defattr(-,root,root,-)
%{userpath}/pvsync

%preun
rm -rf %{_sbindir}/pvsync
rm -rf /etc/pvsync/pvctl.conf
