%global tl_name fontch
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.2
Release:	%{tl_revision}.1
Summary:	Changing fonts, sizes and encodings in Plain TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/plain/contrib/fontch
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fontch.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fontch.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The fontch macros allow the user to change font size and family anywhere
in a plain TeX document. Sizes of 8, 10, 12, 14, 20 and 24 points are
available. A sans serif family (\sf) is defined in addition to the
families already defined in plain TeX. Optional support for Latin Modern
T1 and TS1 fonts is given. There are macros for non-latin1 letters and
for most TS1 symbols. Math mode always uses CM fonts. A command for
producing doubled-spaced documents is also provided. The present version
of the package is designed to deal with the latest release of the Latin
Modern fonts version 1.106. Unfortunately, it can no longer support
earlier versions of the fonts, so an obsolete version of the package is
retained for users who don't yet have access to the latest version of
the fonts.

