Name:		scim-input-pad
Summary:	An onscreen input pad to input some symbols
Version:	0.1.1
Release:	%mkrel 6
Group:		System/Internationalization
License:	GPLv2+
URL:		http://sourceforge.net/projects/scim/
Source0:	http://prdownloads.sourceforge.net/scim/%{name}-%{version}.tar.bz2
Patch0:		scim-input-pad-0.1.1-linkage.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:	scim-client = %{scim_api}
BuildRequires:	scim-devel >= 1.4.7
Obsoletes:	%{_lib}scim-input-pad0

%description
An onscreen input pad to input some symbols.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# remove unnecessary files
rm -f %{buildroot}/%{_libdir}/*.{a,la,so}
rm -f %{buildroot}/%{scim_plugins_dir}/*/*.{a,la}

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
%{_libdir}/*.so.*
%{scim_plugins_dir}/Helper/*.so
