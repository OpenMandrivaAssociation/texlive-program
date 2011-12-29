# revision 20022
# category Package
# catalog-ctan /macros/latex/contrib/program
# catalog-date 2010-10-07 12:36:42 +0200
# catalog-license gpl3
# catalog-version 3.3.12
Name:		texlive-program
Version:	3.3.12
Release:	1
Summary:	Typesetting programs and algorithms
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/program
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/program.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/program.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The main offering is a program environment; a programbox
environment is available for fragments that must not break with
the pages.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/program/program.sty
%doc %{_texmfdistdir}/doc/latex/program/README
%doc %{_texmfdistdir}/doc/latex/program/gpl-3.0.txt
%doc %{_texmfdistdir}/doc/latex/program/plink.tex
%doc %{_texmfdistdir}/doc/latex/program/program-demo.tex
%doc %{_texmfdistdir}/doc/latex/program/program-doc.pdf
%doc %{_texmfdistdir}/doc/latex/program/program-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
