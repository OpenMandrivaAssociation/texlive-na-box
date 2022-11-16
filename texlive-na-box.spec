Name:		texlive-na-box
Version:	45130
Release:	1
Summary:	Arabic-aware version of pas-cours package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/na-box
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/na-box.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/na-box.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a modified version of the pas-cours package made
compatible with XeLaTeX/polyglossia to write arabic documents
with fancy boxed theorem-alike environments.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/xelatex/na-box
%doc %{_texmfdistdir}/doc/xelatex/na-box

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
