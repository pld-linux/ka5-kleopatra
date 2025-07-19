#
# Conditional build:
%define		kdeappsver	22.04.2
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		kleopatra
Summary:	Certificate manager and GUI for OpenPGP and CMS cryptography
Name:		ka5-%{kaname}
Version:	22.04.2
Release:	0.1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	974b3a8e2c9de193760072c68686fae1
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5Positioning-devel >= 5.11.1
BuildRequires:	Qt5PrintSupport-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5WebChannel-devel >= 5.11.1
BuildRequires:	Qt5WebEngine-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	gpgmepp-devel >= 1.8.0
BuildRequires:	ka5-akonadi-contacts-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-mime-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-search-devel >= %{kdeappsver}
BuildRequires:	ka5-kcalutils-devel >= %{kdeappsver}
BuildRequires:	ka5-kidentitymanagement-devel >= %{kdeappsver}
BuildRequires:	ka5-kldap-devel >= %{kdeappsver}
BuildRequires:	ka5-kmailtransport-devel >= %{kdeappsver}
BuildRequires:	ka5-kmime-devel >= %{kdeappsver}
BuildRequires:	ka5-kontactinterface-devel >= %{kdeappsver}
BuildRequires:	ka5-kpimtextedit-devel >= %{kdeappsver}
BuildRequires:	ka5-ktnef-devel >= %{kdeappsver}
BuildRequires:	ka5-libgravatar-devel >= %{kdeappsver}
BuildRequires:	ka5-libkdepim-devel >= %{kdeappsver}
BuildRequires:	ka5-libkleo-devel >= %{kdeappsver}
BuildRequires:	ka5-libksieve-devel >= %{kdeappsver}
BuildRequires:	ka5-mailcommon-devel >= %{kdeappsver}
BuildRequires:	ka5-messagelib-devel >= %{kdeappsver}
BuildRequires:	ka5-messagelib-devel >= %{kdeappsver}
BuildRequires:	ka5-pimcommon-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kbookmarks-devel >= %{kframever}
BuildRequires:	kf5-kcalendarcore-devel >= %{kframever}
BuildRequires:	kf5-kcmutils-devel >= %{kframever}
BuildRequires:	kf5-kcodecs-devel >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcontacts-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-kguiaddons-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kiconthemes-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-kitemviews-devel >= %{kframever}
BuildRequires:	kf5-kjobwidgets-devel >= %{kframever}
BuildRequires:	kf5-knotifications-devel >= %{kframever}
BuildRequires:	kf5-knotifyconfig-devel >= %{kframever}
BuildRequires:	kf5-kparts-devel >= %{kframever}
BuildRequires:	kf5-kservice-devel >= %{kframever}
BuildRequires:	kf5-ktextwidgets-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kwindowsystem-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	kf5-sonnet-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kleopatra is a certificate manager and GUI for OpenPGP
and CMS cryptography.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%{_desktopdir}/kleopatra_import.desktop
%{_desktopdir}/org.kde.kleopatra.desktop
%attr(755,root,root) %{_bindir}/kleopatra
%attr(755,root,root) %{_bindir}/kwatchgnupg
%{_datadir}/qlogging-categories5/kleopatra.categories
%{_datadir}/qlogging-categories5/kleopatra.renamecategories
%dir %{_iconsdir}/hicolor/256x256
%dir %{_iconsdir}/hicolor/256x256/apps
%{_iconsdir}/hicolor/*/apps/kleopatra.png
%attr(755,root,root) %{_libdir}/libkleopatraclientcore.so.1.3.*
%ghost %{_libdir}/libkleopatraclientcore.so.1
%ghost %{_libdir}/libkleopatraclientcore.so
%attr(755,root,root) %{_libdir}/libkleopatraclientgui.so.1.3.*
%ghost %{_libdir}/libkleopatraclientgui.so.1
%ghost %{_libdir}/libkleopatraclientgui.so
%{_datadir}/kservices5/kleopatra_*.desktop
%dir %{_libdir}/qt5/plugins/pim/kcms/kleopatra
%attr(755,root,root) %{_libdir}/qt5/plugins/pim/kcms/kleopatra/kleopatra_config_gnupgsystem.so
%{_datadir}/kconf_update/
%{_datadir}/kleopatra/
%{_datadir}/kwatchgnupg/
%{_datadir}/kio/servicemenus/kleopatra_decryptverifyfiles.desktop
%{_datadir}/kio/servicemenus/kleopatra_decryptverifyfolders.desktop
%{_datadir}/kio/servicemenus/kleopatra_signencryptfiles.desktop
%{_datadir}/kio/servicemenus/kleopatra_signencryptfolders.desktop
%{_datadir}/mime/packages/application-vnd-kde-kleopatra.xml
#%doc %lang(en) %{_htmldir}/en/kleopatra/
#%doc %lang(en) %{_htmldir}/en/kwatchgnupg/
#%{_desktopdir}/org.kde.kleopatra.appdata.xml
