
Summary: 	Keurocalc 
Name:   	keurocalc
Version: 	0.9.7
Release: 	%mkrel 1 
Url:		http://opensource.bureau-cornavin.com/keurocalc/index.html
Source0: 	http://opensource.bureau-cornavin.com/keurocalc/%name-%{version}.tar.bz2

License:  	GPL
Group: 		Graphical desktop/KDE
BuildRequires:	arts 
BuildRequires:  kdelibs-devel 

Obsoletes:	kde3-keurocalc
Provides:	kde3-keurocalc
Patch1:		keurocalc-autoconf-2.6.patch

%description
KEuroCalc is a currency converter and calculator centered on the Euro. It can
convert from and to many currencies, either with a fixed conversion rate or a
variable conversion rate. It directly downloads the latest variable rates
through the Internet.

%prep

%setup -q -nkeurocalc
%patch1 -p1 -b .autoconf

%build
make -f admin/Makefile.common


CFLAGS="%optflags" CXXFLAGS="%optflags" \
        ./configure --prefix=%_prefix \
	            --disable-rpath \
		    --with-qt-dir=%{_prefix}/lib/qt3 \
		    --disable-rpath \
		    --disable-debug \
%if "%{_lib}" != "lib"
    --enable-libsuffix="%(A=%{_lib}; echo ${A/lib/})" \
%endif		
	            --enable-final

%make

%install
export QTDIR=%_libdir/qt3
export KDEDIR=%_prefix

export LD_LIBRARY_PATH=$QTDIR/lib:$KDEDIR/lib:$LD_LIBRARY_PATH
export PATH=$QTDIR/bin:$KDEDIR/bin:$PATH

make install prefix=%buildroot/%_prefix

install -d %buildroot/%_menudir

kdedesktop2mdkmenu.pl keurocalc Applications/Finances %buildroot/%_datadir/applnk/Applications/keurocalc.desktop %buildroot/%_menudir/keurocalc

# David - 0.03-2mdk - Provide menu's icons for all WM/DM
perl -ppi -e "s|icon=\"keurocalc.png\"|icon=\"finances_section.png\"|" %buildroot/%_menudir/keurocalc

%find_lang %{name} 

%clean
rm -fr %buildroot

%post
/sbin/ldconfig
%{update_menus}
%if %mdkversion > 200600
%update_icon_cache hicolor
%endif
 
%postun
/sbin/ldconfig
%{clean_menus} 
%if %mdkversion > 200600
%clean_icon_cache hicolor
%endif


%files -f %name.lang
%defattr(-,root,root)
%_bindir/%name
#
%_menudir/%name 
%_datadir/applnk/Applications/%name.desktop


%dir %_datadir/apps/keurocalc/
%_datadir/apps/keurocalc/splash.png

%_datadir/apps/keurocalc/currencies.xml

%dir %_docdir/HTML/pt/keurocalc
%_docdir/HTML/pt/keurocalc/common
%_docdir/HTML/pt/keurocalc/index.cache.bz2
%_docdir/HTML/pt/keurocalc/index.docbook

%_iconsdir/hicolor/16x16/apps/keurocalc.png
%_iconsdir/hicolor/32x32/apps/keurocalc.png
%_iconsdir/hicolor/48x48/apps/keurocalc.png


%dir %_docdir/HTML/en/keurocalc/
%doc %_docdir/HTML/en/keurocalc/common
%doc %_docdir/HTML/en/keurocalc/*.bz2
%doc %_docdir/HTML/en/keurocalc/*.docbook
%doc %_docdir/HTML/en/keurocalc/*.png

%dir %_docdir/HTML/da/keurocalc/
%doc %_docdir/HTML/da/keurocalc/common
%doc %_docdir/HTML/da/keurocalc/*.bz2
%doc %_docdir/HTML/da/keurocalc/*.docbook


%dir %_docdir/HTML/fr/keurocalc/
%doc %_docdir/HTML/fr/keurocalc/common
%doc %_docdir/HTML/fr/keurocalc/*.bz2
%doc %_docdir/HTML/fr/keurocalc/*.docbook
%doc %_docdir/HTML/fr/keurocalc/*.png

%dir %_docdir/HTML/sv/keurocalc/
%doc %_docdir/HTML/sv/keurocalc/common
%doc %_docdir/HTML/sv/keurocalc/*.bz2
%doc %_docdir/HTML/sv/keurocalc/*.docbook
%doc %_docdir/HTML/sv/keurocalc/*.png

%dir %_docdir/HTML/et/keurocalc/
%doc %_docdir/HTML/et/keurocalc/common
%doc %_docdir/HTML/et/keurocalc/*.bz2
%doc %_docdir/HTML/et/keurocalc/*.docbook

%dir %_docdir/HTML/es/keurocalc/
%doc %_docdir/HTML/es/keurocalc/common
%doc %_docdir/HTML/es/keurocalc/index.cache.bz2
%doc %_docdir/HTML/es/keurocalc/index.docbook

%dir %_docdir/HTML/it/keurocalc/
%doc %_docdir/HTML/it/keurocalc/common
%doc %_docdir/HTML/it/keurocalc/index.cache.bz2
%doc %_docdir/HTML/it/keurocalc/index.docbook
%doc %_docdir/HTML/it/keurocalc/*.png

%dir %_docdir/HTML/nb/keurocalc/
%doc %_docdir/HTML/nb/keurocalc/common
%doc %_docdir/HTML/nb/keurocalc/index.cache.bz2
%doc %_docdir/HTML/nb/keurocalc/index.docbook
%doc %_docdir/HTML/nb/keurocalc/*.png

%dir %_docdir/HTML/nl/keurocalc/
%doc %_docdir/HTML/nl/keurocalc/common
%doc %_docdir/HTML/nl/keurocalc/*.bz2
%doc %_docdir/HTML/nl/keurocalc/*.docbook



