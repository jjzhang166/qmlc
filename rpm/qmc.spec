Name:       qmc      
Version:    5.3.0
Release:    1%{?dist}
Summary:    QML Compiler
License:    LGPLv2.1 with exception

Source0:    %{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  qt5-qtdeclarative-import-qtquick2plugin

%description
The Qml Compiler can be used to convert Qml source code files into
precompiled Qml files. The precompiled Qml files are faster to load
and do not expose the source code. Normally, the Qt either compiles
the Qml files in the startup or interprets the Qml files runtime.

%package core
Summary:        Core library for qmc
Group:          System/Libraries
Requires:       %{name} >= %{version}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description core
Core library for qmc


%package core-devel
Summary:        Development files for the qmc core library
Group:          System/Libraries
Requires:       %{name}-core = %{version}-%{release}

%description core-devel
Development files for the qmc core library


%package loader
Summary:        Loader for compiled files
Group:          System/Libraries
Requires:       %{name} >= %{version}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description loader
Loader for compiled files


%package loader-devel
Summary:        Development files for the qmc loader library
Group:          System/Libraries
Requires:       %{name}-loader = %{version}-%{release}

%description loader-devel
Development files for the qmc loader library


%package tests
Summary:        Tests for qmc compiler/loader
Group:          System/Libraries
Requires:       %{name}-core = %{version}-%{release}
Requires:       %{name}-loader = %{version}-%{release}

%description tests
Tests for qmc compiler/loader


%package examples
Summary:        Examples for qmc compiler/loader
Group:          System/Libraries
Requires:       %{name}-core = %{version}-%{release}
Requires:       %{name}-loader = %{version}-%{release}

%description examples
Examples for qmc compiler/loader


%prep
%setup -q

%build
qtchooser -run-tool=qmake -qt=5 PREFIX="%{_prefix}" LIBDIR="%{_libdir}" BINDIR="%{_bindir}" INCLUDEDIR="%{_includedir}"
make %{?jobs:-j%jobs}

%install
%make_install

%post core -p /sbin/ldconfig
%postun core -p /sbin/ldconfig

%post loader -p /sbin/ldconfig
%postun loader -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/qmc
%{_bindir}/qmc-rcc.sh

%files core
%{_libdir}/libqmccompiler.so.*

%files core-devel
%{_libdir}/libqmccompiler.so
%{_libdir}/pkgconfig/qmccompiler.pc
%{_includedir}/qmccompiler
%{_datadir}/qt5/mkspecs/features/qmlc.pri

%files loader
%{_libdir}/libqmcloader.so.*
%{_bindir}/qmcloader

%files loader-devel
%{_libdir}/libqmcloader.so
%{_libdir}/pkgconfig/qmcloader.pc
%{_includedir}/qmcloader
%{_bindir}/qmcdump

%files tests
%{_bindir}/compiletest
%{_libdir}/qt5/tests/qmlc/manual/multipleitems/multipleitems
%{_libdir}/qt5/tests/qmlc/manual/multipleitems/multipleitems_loader
%{_libdir}/qt5/tests/qmlc/manual/multipleitems/app.qmc
%{_libdir}/qt5/tests/qmlc/manual/multipleitems/qml/QmlJSItems.qmc
%{_libdir}/qt5/tests/qmlc/manual/multipleitems/qml/content/QmlSubItem.qmc
%{_libdir}/qt5/tests/qmlc/manual/multipleitems/qml/content/testscript1.jsc
%{_libdir}/qt5/tests/qmlc/manual/multipleitems/Charts/libchartsplugin.so
%{_libdir}/qt5/tests/qmlc/manual/multipleitems/Charts/QmlInPlugin.qmc
%{_libdir}/qt5/tests/qmlc/manual/multipleitems/Charts/QmlInPlugin.qml
%{_libdir}/qt5/tests/qmlc/manual/multipleitems/Charts/qmldir
%{_libdir}/qt5/tests/qmlc/manual/multipleitems/Charts/qmldir_loader

%files examples

%changelog
* Tue Aug 12 2014 Matias Muhonen <> 5.3.0
- Bump version
* Mon Aug 11 2014 Matias Muhonen <> 0.0.1
- Initial version
