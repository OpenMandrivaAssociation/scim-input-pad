%define version	0.1.1
%define release	%mkrel 5

%define scim_version	1.4.0

%define libname_orig lib%{name}
%define libname %mklibname %{name} 0

Name:		scim-input-pad
Summary:	An onscreen input pad to input some symbols
Version:		%{version}
Release:		%{release}
Group:		System/Internationalization
License:		GPL
URL:			http://sourceforge.net/projects/scim/
Source0:		http://prdownloads.sourceforge.net/scim/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:			%{libname} = %{version}
Requires:			scim >= %{scim_version}
BuildRequires:		scim-devel >= %{scim_version}

%description
An onscreen input pad to input some symbols.


%package -n	%{libname}
Summary:	Scim-input-pad library
Group:		System/Internationalization
Provides:		%{libname_orig} = %{version}-%{release}

%description -n %{libname}
Scim-input-pad library.


%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# remove unnecessary files
rm -f %{buildroot}/%{_libdir}/*.{a,la,so}
rm -f %{buildroot}/%{_libdir}/scim-*/*/*.{a,la}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif


%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING README
%{_bindir}/scim-*
%{_datadir}/scim/icons/*
%{_datadir}/scim/input-pad/*

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/*.so.*
%{_libdir}/scim-1.0/1.4.0/Helper/*.so
%{_libdir}/scim-1.0/1.4.0/Helper/*.a
%{_libdir}/scim-1.0/1.4.0/Helper/*.la


