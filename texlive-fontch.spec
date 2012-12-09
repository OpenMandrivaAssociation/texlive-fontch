# revision 17859
# category Package
# catalog-ctan /macros/plain/contrib/fontch
# catalog-date 2010-04-13 09:02:45 +0200
# catalog-license lppl
# catalog-version 2.2
Name:		texlive-fontch
Version:	2.2
Release:	2
Summary:	Changing fonts, sizes and encodings in Plain TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/fontch
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontch.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontch.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.2-2
+ Revision: 752012
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.2-1
+ Revision: 718480
- texlive-fontch
- texlive-fontch
- texlive-fontch
- texlive-fontch

