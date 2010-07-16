Summary: 	Keurocalc 
Name:   	keurocalc
Version: 	1.0.3
Release: 	%mkrel 1
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
