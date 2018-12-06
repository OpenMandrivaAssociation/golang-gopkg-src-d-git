%bcond_with check
%global api             4
%global goipath         gopkg.in/src-d/go-git.v4
%global forgeurl        https://github.com/src-d/go-git
Version:                %{api}.2.1

%global common_description %{expand:
go-git is a highly extensible git implementation library written in pure Go.

It can be used to manipulate git repositories at low level (plumbing) or high
level (porcelain), through an idiomatic Go API. It also supports several type of
storage, such as in-memory filesystems, or custom implementations thanks to the
Storer interface.

It's being actively develop since 2015 and is being use extensively by source-d
and Keybase, and by many other libraries and tools.}

%gometa

Name:    golang-gopkg-src-d-git
Release: 2%{?dist}
Summary: A highly extensible Git implementation in pure Go
License: ASL 2.0
URL:     %{gourl}
Source0: %{gosource}
BuildRequires: golang(github.com/emirpasic/gods/trees/binaryheap)
BuildRequires: golang(github.com/jbenet/go-context/io)
BuildRequires: golang(github.com/kevinburke/ssh_config)
BuildRequires: golang(github.com/mitchellh/go-homedir)
BuildRequires: golang(github.com/sergi/go-diff/diffmatchpatch)
BuildRequires: golang(github.com/src-d/gcfg)
BuildRequires: golang(gopkg.in/src-d/go-billy.v4)
BuildRequires: golang(gopkg.in/src-d/go-billy.v4/osfs)
BuildRequires: golang(gopkg.in/src-d/go-billy.v4/util)
# there's a circular dependency between go-git-fixtures and go-git
%if %{with check}
BuildRequires: golang(github.com/google/go-cmp/cmp)
BuildRequires: golang(gopkg.in/src-d/go-git-fixtures.v3)
%endif

%description
%{common_description}

%package %{api}-devel
Summary:    %{summary}
BuildArch:  noarch

%description %{api}-devel
%{common_description}
 
This package contains the source code needed for building packages that import
the %{goipath} Go namespace.

%prep
%gosetup -q

%install
%goinstall

%if %{with check}
%check
%gochecks
%endif

%files %{api}-devel -f devel.file-list
%license LICENSE
%doc _examples CODE_OF_CONDUCT.md COMPATIBILITY.md CONTRIBUTING.md DCO MAINTAINERS README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 30 2018 Dominik Mierzejewski <dominik@greysector.net> - 4.2.1-1
- First package for Fedora
