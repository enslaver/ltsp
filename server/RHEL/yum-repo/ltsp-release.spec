Name:		ltsp-release
Version:	5
Release:	9
Summary:	RPM Package containing LTSP repository and GPG key

Group:		User Interface/Desktops
License:	GPLv3
URL:		http://www.ltsp.org
Source0:	ltsp-release-5.tar.gz

BuildArch: noarch

%description
Installs yum repository for the Linux Terminal Server Project and GPG key

%prep
%setup -q


%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/
cp -p ltsp.repo $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/
cp -p RPM-GPG-KEY-ltsp $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/

%clean
rm -rf $RPM_BUILD_ROOT

%post
rpm --import %{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-ltsp || :

%files
%defattr(-, root, root, 0755)
%pubkey RPM-GPG-KEY-ltsp
%dir %{_sysconfdir}/yum.repos.d/
%config %{_sysconfdir}/yum.repos.d/ltsp.repo
%dir %{_sysconfdir}/pki/rpm-gpg/
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-ltsp

%doc



%changelog

