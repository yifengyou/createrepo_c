Name:           balicek-iso88592
Version:        1.1.1
Release:        1
License:        GPL
Summary:        Bal��ek s "���������"
Group:          System Environment/Shells
Url:            http://fake_bash_shell.com/
#Source:         %{name}-%{version}.tar.gz

Provides: Bal��ek
Requires: b�l�k��

%description
B�l� k�� p�l �dy n� n�.
"���������"

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
* Tue Apr 17 2012 Tom� Ml�och <tmlcoch@redhat.com> - 1.1.1-1
- N�jak� comment "�������������خ������"
