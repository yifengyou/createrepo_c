Name:           balicek-iso88591
Version:        1.1.1
Release:        1
License:        GPL
Summary:        Balicek s "�������"
Group:          System Environment/Shells
Url:            http://fake_bash_shell.com/
#Source:         %{name}-%{version}.tar.gz

Provides: Balicek
Requires: �������

%description
divny o: � "�������" divny u: �

#%prep
#%setup -q

%build
echo OK

%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files

%changelog
* Tue Apr 17 2012 Tom�s Mlcoch <tmlcoch@redhat.com> - 1.1.1-1
- Nejak� comment "�������"
