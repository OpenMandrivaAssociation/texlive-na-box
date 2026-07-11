%global tl_name na-box
%global tl_revision 45130

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Arabic-aware version of pas-cours package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/na-box
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/na-box.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/na-box.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a modified version of the pas-cours package made compatible with
XeLaTeX/polyglossia to write arabic documents with fancy boxed theorem-
alike environments.

