
# k8s move backup and restore data

## suggest install like so
rpm -ivh pvsync-1.0.0-1.el7.centos.x86_64.rpm
so you can use "pvsync"  command direct:

## backup data
mv data_center/default-* /data_center_bak/

# how to use
## use to registry nfs path and backup nfs path.
"/data_center" is the new nfs mount path, "/data_center_bak" is the backup data path
./pvsync init /data_center /data_center_bak

## command tool [-num 20 ]to sync file number can choose,use to replace kubectl on data mve and create new pv
pvsync [create/apply] -num 20 -f file.yaml

if your backup pv is very big, please wait and no broke it.

# make rpm package step
## install tool
> yum  install  -y  rpm-build
## need normal user
> useradd  hunge

> tar -zcvf pvsync-1.0.0.tar.gz .

> cp pvsync-1.0.0.tar.gz ~hunge/

> su - hunge

## gernate spce file
touch pvsync.spec

donot need

BuildRequires: 

Requires: 

```
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

```

> cd ../ #  rpm package in fold RPMS and source in SRPMS

-ba: Build binary and source packages (after doing
	the %prep, %build, and %install stages).

## install rpm

> rpm -ivh pvsync-1.0.0-1.el7.centos.x86_64.rpm
