Name:		texlive-logpap
Version:	0.6
Release:	1
Summary:	Generate logarithmic graph paper with LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/logpap
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/logpap.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/logpap.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/logpap.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The logpap package provides four macros for drawing
logarithmic-logarithmic, logarithmic-linear, linear-logarithmic
and (because it was easy to implement) linear-linear graph
paper with LaTeX.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
