Name:		texlive-logpap
Version:	15878
Release:	2
Summary:	Generate logarithmic graph paper with LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/logpap
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/logpap.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/logpap.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/logpap.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
