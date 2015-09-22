Summary: ST2 Common Libraries
Name: st2common
Version: 0.4.0
Release: 1
License: Apache
Group: Applications/Engineering
BuildArch: noarch
Source: /opt/git/st2/st2common.tar.gz
URL: https://github.com/StackStorm/st2
Vendor: StackStorm
Packager: Estee Tew <st2@stackstorm.com>
Requires:	python-devel
Requires:   	python-pip
Requires:     mongodb
Requires:     mongodb-server

%description
An automation plaform that needs a much better description than this.

%prep
%setup

%build
# Empty section.

%install

mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}%{python2_sitelib}
mkdir -p %{buildroot}/var/log/st2
mkdir -p %{buildroot}/etc/st2
mkdir -p %{buildroot}/etc/logrotate.d
mkdir -p %{buildroot}/opt/stackstorm/packs
mkdir -p %{buildroot}/opt/stackstorm/rbac
mkdir -p %{buildroot}/opt/stackstorm/rbac/roles
mkdir -p %{buildroot}/opt/stackstorm/rbac/assignments
mkdir -p %{buildroot}/usr/share/doc/st2
mkdir -p %{buildroot}/usr/share/stackstorm
cp -R contrib/default %{buildroot}/opt/stackstorm/packs/
chmod -R 770 %{buildroot}/opt/stackstorm/packs/default
cp -R contrib/core %{buildroot}/opt/stackstorm/packs/
chmod -R 770 %{buildroot}/opt/stackstorm/packs/core
cp -R contrib/packs %{buildroot}/opt/stackstorm/packs/
chmod -R 770 %{buildroot}/opt/stackstorm/packs/packs
cp -R contrib/linux %{buildroot}/opt/stackstorm/packs/
chmod -R 770 %{buildroot}/opt/stackstorm/packs/linux
cp -R contrib/examples %{buildroot}/usr/share/doc/st2/
cp -R docs/* %{buildroot}/usr/share/doc/st2/
cp -R st2common %{buildroot}/%{python2_sitelib}/
cp -R bin %{buildroot}/%{python2_sitelib}/st2common/
install st2/st2.conf %{buildroot}/etc/st2/st2.conf
install logrotate.d/st2.conf %{buildroot}/etc/logrotate.d/st2.conf
install rbac/roles/sample.yaml %{buildroot}/opt/stackstorm/rbac/roles/sample.yaml
install rbac/assignments/sample.yaml %{buildroot}/opt/stackstorm/rbac/assignments/sample.yaml
install -m755 tools/st2ctl %{buildroot}/usr/bin/st2ctl
install -m755 tools/st2-setup-tests %{buildroot}/usr/lib/python2.7/site-packages/st2common/bin/st2-setup-tests
install -m755 tools/st2-setup-examples %{buildroot}/usr/lib/python2.7/site-packages/st2common/bin/st2-setup-examples
install -m755 tools/st2-self-check %{buildroot}/usr/lib/python2.7/site-packages/st2common/bin/st2-self-check
install -m755 tools/migrate_rules_to_include_pack.py %{buildroot}/usr/lib/python2.7/site-packages/st2common/bin/migrate_rules_to_include_pack.py

%files
%{python2_sitelib}/st2common*
/usr/share/doc/st2/*
/etc/st2/*
/opt/stackstorm/*
/var/log/st2
/usr/bin/st2ctl
/etc/logrotate.d/st2.conf
