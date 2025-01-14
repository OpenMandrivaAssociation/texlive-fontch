Name:		texlive-fontch
Version:	17859
Release:	2
Summary:	Changing fonts, sizes and encodings in Plain TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/plain/contrib/fontch
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontch.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontch.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The fontch macros allow the user to change font size and family
anywhere in a plain TeX document. Sizes of 8, 10, 12, 14, 20
and 24 points are available. A sans serif family (\sf) is
defined in addition to the families already defined in plain
TeX. Optional support for Latin Modern T1 and TS1 fonts is
given. There are macros for non-latin1 letters and for most TS1
symbols. Math mode always uses CM fonts. A command for
producing doubled-spaced documents is also provided. The
present version of the package is designed to deal with the
latest release of the Latin Modern fonts version 1.106.
Unfortunately, it can no longer support earlier versions of the
fonts, so an obsolete version of the package is retained for
users who don't yet have access to the latest version of the
fonts.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/plain/fontch/DSmac.tex
%{_texmfdistdir}/tex/plain/fontch/TS1mac.tex
%{_texmfdistdir}/tex/plain/fontch/bsymbols.tex
%{_texmfdistdir}/tex/plain/fontch/fontch.tex
%{_texmfdistdir}/tex/plain/fontch/fontch_doc.tex
%doc %{_texmfdistdir}/doc/plain/fontch/README
%doc %{_texmfdistdir}/doc/plain/fontch/fontch.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
