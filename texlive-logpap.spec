%global tl_name logpap
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.6
Release:	%{tl_revision}.1
Summary:	Generate logarithmic graph paper with LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/logpap
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/logpap.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/logpap.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/logpap.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The logpap package provides four macros for drawing logarithmic-
logarithmic, logarithmic-linear, linear-logarithmic and (because it was
easy to implement) linear-linear graph paper with LaTeX.

