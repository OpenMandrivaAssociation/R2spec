Name:           R2spec
Version:        4.1.0
Release:        2
Summary:        Python script to generate R spec file

Group:          Development/Other
License:        GPLv3+
URL:            https://fedorahosted.org/r2spec/
Source0:        https://fedorahosted.org/releases/r/2/r2spec/R2spec-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel
Requires:       R python-jinja2 wget
Provides:       R2rpm = 1.0.0
Patch0:		R2spec-4.1.0-mandriva.patch

%description
R2spec is a small python tool that generates spec file for R libraries.
It can work from a URL or a tarball.
R2spec provides R2rpm which generates rpm for R libraries using the 
R2spec API.

%prep
%setup -q
%patch0 -p1

%build
%{__python} setup.py build

%install
%{__python} setup.py install --root=%{buildroot}
install r2spec/specfile.tpl %{buildroot}/%{py_puresitedir}/r2spec/
chmod -x %{buildroot}/%{py_puresitedir}/r2spec/specfile.tpl

## Only work localy, needs internet
#%check
#%{__python} tests.py

%files
#-f installed_files2
%doc README LICENSE CHANGELOG
%{py_puresitedir}/*
%config(noreplace) %{_sysconfdir}/%{name}/repos.cfg
%{_bindir}/%{name}
%{_bindir}/R2rpm
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/R2rpm.1*
