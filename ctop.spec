%define		vendor_version	0.7.7

Summary:	Top-like interface for container metrics
Name:		ctop
Version:	0.7.7
Release:	1
License:	MIT
Group:		Applications/System
Source0:	https://github.com/bcicen/ctop/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	9221f9bd69952392c47b8570d2ba25eb
Source1:	%{name}-vendor-%{vendor_version}.tar.xz
# Source1-md5:	66c94eb62c9a648fb69a2a95cbafa3c3
URL:		https://ctop.sh
BuildRequires:	golang >= 1.15
BuildRequires:	rpmbuild(macros) >= 2.009
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
ExclusiveArch:	%go_arches
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_debugsource_packages	0

%description
ctop provides a concise and condensed overview of real-time metrics
for multiple containers as well as a single container view for
inspecting a specific container.

ctop comes with built-in support for Docker and runC.

%prep
%setup -q -a1

%{__mv} ctop-%{vendor_version}/vendor .

%{__mkdir} .go-cache

%build
%__go build -v -mod=vendor -o target/%{name}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}

cp -p target/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT
%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/%{name}
