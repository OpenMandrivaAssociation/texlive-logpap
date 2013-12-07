# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/logpap
# catalog-date 2006-12-08 22:20:56 +0100
# catalog-license lppl
# catalog-version 0.6
Name:		texlive-logpap
Version:	0.6
Release:	6
Summary:	Generate logarithmic graph paper with LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/logpap
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/logpap.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/logpap.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/logpap.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The logpap package provides four macros for drawing
logarithmic-logarithmic, logarithmic-linear, linear-logarithmic
and (because it was easy to implement) linear-linear graph
paper with LaTeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/logpap/logpap.sty
%doc %{_texmfdistdir}/doc/latex/logpap/README
%doc %{_texmfdistdir}/doc/latex/logpap/example.pdf
%doc %{_texmfdistdir}/doc/latex/logpap/example.tex
#- source
%doc %{_texmfdistdir}/source/latex/logpap/logpap.dtx
%doc %{_texmfdistdir}/source/latex/logpap/logpap.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.6-2
+ Revision: 753447
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.6-1
+ Revision: 718879
- texlive-logpap
- texlive-logpap
- texlive-logpap
- texlive-logpap

