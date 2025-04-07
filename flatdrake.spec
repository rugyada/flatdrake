%global gb3_ver %(rpm -q --qf '%%{version}' gambas-devel)

Summary:	FlatDrake is a frontend for FlatPak
Name:		flatdrake
Version:	2.3.91
Release:	1
License:	GPLv3
Group:		Graphical desktop/KDE
URL:		https://mib.pianetalinux.org
#URL:		https://github.com/astrgl/flatdrake
Source0:	https://github.com/astrgl/flatdrake/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	gambas-devel
BuildRequires:	gambas-gb.dbus
BuildRequires:	gambas-gb.form
BuildRequires:	gambas-gb.form.stock
BuildRequires:	gambas-gb.gui
BuildRequires:  gambas-gb.qt6
BuildRequires:	gambas-gb.image
BuildRequires:	gambas-gui-backend
BuildRequires:	imagemagick

Requires:	flatpak
Requires:	(gambas-runtime >= %{gb3_major} with gambas-runtime < %{gb3_next_major})
Requires:	(gambas-gb.dbus >= %{gb3_major} with gambas-gb.dbus < %{gb3_next_major})
Requires:	(gambas-gb.form >= %{gb3_major} with gambas-gb.form < %{gb3_next_major})
Requires:	(gambas-gb.form.stock >= %{gb3_major} with gambas-gb.form.stock < %{gb3_next_major})
Requires:	(gambas-gb.gui >= %{gb3_major} with gambas-gb.gui < %{gb3_next_major})
Requires:	(gambas-gb.qt6 >= %{gb3_major} with gambas-gb.qt6 < %{gb3_next_major})
Requires:	(gambas-gb.image >= %{gb3_major} with gambas-gb.image < %{gb3_next_major})
Requires:	(gambas-gui-backend >= %{gb3_major} with gambas-gui-backend < %{gb3_next_major})
Requires:	(gambas-gb.form.dialog >= %{gb3_major} with gambas-gb.form.dialog < %{gb3_next_major})
Requires:	(gambas-gb.complex >= %{gb3_major} with gambas-gb.complex < %{gb3_next_major})
Requires:	lsb-release
Requires:	xrandr
Requires:	draketray

BuildArch: noarch

%description
FlatDrake is a frontend for FlatPak
Powerful like a terminal and simple like a GUI!

%files
%license FILE-EXTRA/license
%{_bindir}/%{name}.gambas
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/*/apps/%{name}.svg

#---------------------------------------------------------------------------

%prep
%autosetup -p1

%build
gbc3 -e -a -g -t -f public-module -f public-control -j%{?_smp_mflags}
gba3

# unversion binary
mv %{name}-%{version}.gambas %{name}.gambas

%install
# binary
install -Dm 0755 %{name}.gambas -t %{buildroot}/%{_bindir}/

# data files
install -Dm 0644 FILE-EXTRA/%{name}-* -t %{buildroot}/%{_datadir}/%{name}/
install -Dm 0644 LINUX.png OMA.png -t %{buildroot}/%{_datadir}/%{name}/

#.desktop
install -Dm 0755 FILE-EXTRA/%{name}.desktop -t %{buildroot}/%{_datadir}/applications

# icons
install -Dm 0644 ICONS-EXTRA/* -t %{buildroot}%{_datadir}/%{name}/
install -Dm 0644 %{name}.svg -t %{buildroot}%{_iconsdir}/hicolor/scalable/apps/
for d in 16 32 48 64 72 128 256 512
do
	install -dm 0755 %{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/
	convert -background none -scale ${d}x${d} %{name}.svg \
			%{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/%{name}.png
done
install -dm 0755 %{buildroot}%{_datadir}/pixmaps/
convert -scale 32x32 %{name}.svg %{buildroot}%{_datadir}/pixmaps/%{name}.xpm
