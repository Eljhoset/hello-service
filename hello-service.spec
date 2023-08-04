Name:           hello-service
Version:        1.0
Release:        1%{?dist}
Summary:        Sample project in C++
License:        MIT
URL:            https://github.com/eljhoset/hello-service
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  hello-lib
Requires:       hello-lib

%description
This is a sample project in C++.

%prep
%setup -n %{name}-%{version} -c

%build
g++ %{optflags} -o greeting_program src/main.cpp -lgreet_lib

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 755 greeting_program %{buildroot}/%{_bindir}

%files
%{_bindir}/greeting_program

%changelog
* Mon Aug 01 2023 Daniel <jd-jd-@hotmail.com> - 1.0-1
- Initial version.