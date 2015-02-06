Summary: 	Keurocalc 
Name:   	keurocalc
Version: 	1.1.0
Release: 	2
Url:		http://opensource.bureau-cornavin.com/keurocalc/index.html
Source0: 	http://opensource.bureau-cornavin.com/keurocalc/sources/%name-%version.tgz
License:  	GPL
Group: 		Graphical desktop/KDE
BuildRoot: 	%_tmppath/%name-%version-%release-root
BuildRequires:  kdelibs4-devel
BuildRequires:	desktop-file-utils

%description
KEuroCalc is a currency converter and calculator centered on the Euro. It can
convert from and to many currencies, either with a fixed conversion rate or a
variable conversion rate. It directly downloads the latest variable rates
through the Internet.

%package -n curconvd
Summary:	A daemon that acts as a currency conversion service over D-Bus
Group:		Graphical desktop/KDE
Requires:	%name = %version

%description -n curconvd
curconvd is a daemon that acts as a currency conversion service over D-Bus.

%prep
%setup -q

%build
%cmake_kde4
%make

%install
rm -fr %buildroot
%makeinstall_std -C build

desktop-file-install --dir=%buildroot%_kde_applicationsdir \
	--add-category='Finance' \
	%buildroot%_kde_applicationsdir/%name.desktop

%find_lang %{name} --with-html

%clean
rm -fr %buildroot

%if %mdkversion < 200900
%post
%{update_menus}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun 
%{clean_menus} 
%clean_icon_cache hicolor
%endif

%files -f %name.lang
%defattr(-,root,root)
%doc ChangeLog README TODO
%_kde_bindir/%name
%_kde_applicationsdir/%name.desktop
%_kde_appsdir/%name
%_kde_iconsdir/hicolor/*/*/*

%files -n curconvd
%defattr(-,root,root)
%doc curconvd/API.txt
%_kde_bindir/curconvd
%_kde_appsdir/curconvd


%changelog
* Sun Jan 09 2011 Funda Wang <fwang@mandriva.org> 1.1.0-1mdv2011.0
+ Revision: 630790
- update to new version 1.1.0

* Fri Jul 16 2010 Funda Wang <fwang@mandriva.org> 1.0.3-1mdv2011.0
+ Revision: 554384
- new version 1.0.3

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 1.0.2-2mdv2010.1
+ Revision: 438094
- rebuild

* Sat Jan 10 2009 Funda Wang <fwang@mandriva.org> 1.0.2-1mdv2009.1
+ Revision: 327819
- New version 1.0.2

* Fri Jul 04 2008 Pixel <pixel@mandriva.com> 1.0.0-2mdv2009.0
+ Revision: 231504
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri May 16 2008 Funda Wang <fwang@mandriva.org> 1.0.0-1mdv2009.0
+ Revision: 208211
- New version 1.0.0

* Tue Jan 29 2008 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 0.9.7-2mdv2008.1
+ Revision: 160001
- Fix automake patch
- [BUGFIX] Fix menu file (Bug #36748)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Nov 13 2006 Laurent Montel <lmontel@mandriva.com> 0.9.7-1mdv2007.0
+ Revision: 83567
- 0.9.7
- Import keurocalc

* Wed Jul 12 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.9.6-3mdv2007.0
- Rebuild for new menu and extension
- Use Macros for icons

* Thu May 11 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.9.6-2mdk
- Rebuild to generate categories

* Fri Apr 21 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.9.6-1mdk
- New release 0.9.6

* Sat Mar 25 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.9.5-1mdk
- New release 0.9.5

* Thu Jan 19 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.9.4-3mdk
- Fix Build for x86_64

* Mon Dec 26 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.9.4-2mdk
- Remove redundant Buildrequires

* Tue Jul 26 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.9.4-1mdk
- New release 0.9.4
- Drop Patch 0 ( unneeded )
- Fix Source 0

* Tue Jul 05 2005 Lenny Cartier <lenny@mandriva.com> 0.9.3-1mdk
- 0.9.3

* Fri Jun 03 2005 Laurent MONTEL <lmontel@mandriva.com> 0.9.2-1mdk
- 0.9.2

* Sat Jun 05 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.9.1-2mdk
- Rebuild

* Tue May 18 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.9.1-1mdk
- 0.9.1

* Wed May 05 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.9.0-1mdk
- 0.9

* Wed Apr 07 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.8.2-1mdk
- 0.8.2

* Tue Feb 24 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.8.1-2mdk
- Fix

* Mon Feb 23 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.8.1-1mdk
- 0.8.1

* Tue Feb 10 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.8.0-2mdk
- Fix description and url (fix from Eric Bischoff <e.bischoff@noos.fr>)

* Mon Feb 09 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.8.0-1mdk
- 0.8.0

* Fri Dec 12 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 0.7.2-1mdk
- 0.7.2

* Wed Dec 10 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 0.7.1-1mdk
- 0.7.1

