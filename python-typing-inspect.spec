Name:		python-typing-inspect
Version:	0.9.0
Release:	2
Summary:	Runtime inspection utilities for typing module
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/typing-inspect/
Source0:	typing_inspect-0.9.0.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(mypy-extensions)
BuildRequires:	python%{pyver}dist(typing-extensions)
BuildArch:	noarch
%description
Runtime inspection utilities for typing module.

%files
%{py_sitedir}/*
