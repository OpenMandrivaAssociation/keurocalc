Summary: 	Keurocalc 
Name:   	keurocalc
Version: 	1.0.2
Release: 	%mkrel 1
Url:		http://opensource.bureau-cornavin.com/keurocalc/index.html
Source0: 	http://opensource.bureau-cornavin.com/keurocalc/%name-%{version}.tgz
Patch2:         keurocalc-fix-desktopfile.patch
License:  	GPL
Group: 		Graphical desktop/KDE
BuildRoot: 	%_tmppath/%name-%version-%release-root
BuildRequires:  kdelibs4-devel 

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
%patch2 -p0

%build
%cmake_kde4
%make

%install
rm -fr %buildroot
cd build
%makeinstall_std
cd -

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
%_kde_datadir/applications/kde4/%name.desktop
%_kde_appsdir/%name
%_kde_iconsdir/hicolor/*/*/*

%files -n curconvd
%defattr(-,root,root)
%doc curconvd/API.txt
%_kde_bindir/curconvd
%_kde_appsdir/curconvd
