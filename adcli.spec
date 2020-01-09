Name:		adcli
Version:	0.8.1
Release:	1%{?dist}
Summary:	Active Directory enrollment
License:	LGPLv2+
URL:		http://cgit.freedesktop.org/realmd/adcli
Source0:	http://www.freedesktop.org/software/realmd/releases/adcli-%{version}.tar.gz

BuildRequires:	intltool pkgconfig
BuildRequires:	gettext-devel
BuildRequires:	krb5-devel
BuildRequires:	openldap-devel
BuildRequires:	libxslt
BuildRequires:	xmlto

Requires:	cyrus-sasl-gssapi

# adcli no longer has a library of development files
# the adcli tool itself is to be used by callers
Obsoletes:	adcli-devel < 0.5

%description
adcli is a library and tool for joining an Active Directory domain using
standard LDAP and Kerberos calls.

%define _hardened_build 1

%prep
%setup -q

%build
%configure --disable-static --disable-silent-rules
make %{?_smp_mflags}

%check
make check

%install
make install DESTDIR=%{buildroot}
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean

%files
%{_sbindir}/adcli
%doc AUTHORS COPYING ChangeLog NEWS README
%doc %{_datadir}/doc/adcli
%doc %{_mandir}/*/*

%changelog
* Wed Jan 20 2016 Sumit Bose <sbose@redhat.com> - 0.8.1-1
- Update to upstream release 0.8.1
- Add missing - in adcli man page  [#1296971]

* Thu Dec 17 2015 Sumit Bose <sbose@redhat.com> - 0.8.0-1
- Update to upstream release 0.8.0
- Support Host Keytab renewal [#1290731]

* Thu Jan 30 2014 Stef Walter <stefw@redhat.com> - 0.7.5-4
- Fix incorrect ownership of manual page directory [#1057563]

* Tue Jan 28 2014 Daniel Mach <dmach@redhat.com> - 0.7.5-3
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.7.5-2
- Mass rebuild 2013-12-27

* Fri Sep 13 2013 Stef Walter <stefw@redhat.com> - 0.7.5-1
- Update to upstream point release 0.7.5
- Workaround for discovery via IPv6 address [#1004442]
- Correctly put IPv6 addresses in temporary krb5.conf

* Mon Sep 09 2013 Stef Walter <stefw@redhat.com> - 0.7.4-1
- Update to upstream point release 0.7.4
- Correctly handle truncating long host names [#1001667]
- Try to contact all available addresses for discovery [#1004442]
- Build fixes [#1004823]

* Wed Aug 07 2013 Stef Walter <stefw@redhat.com> - 0.7.3-1
- Update to upstream point release 0.7.3
- Don't try to set encryption types on Windows 2003

* Mon Jul 22 2013 Stef Walter <stefw@redhat.com> - 0.7.2-1
- Update to upstream point release 0.7.2
- Part of fix for bug [#967008]

* Tue Jun 11 2013 Stef Walter <stefw@redhat.com> - 0.7.1-3
- Run 'make check' when building the package

* Mon May 13 2013 Stef Walter <stefw@redhat.com> - 0.7.1-2
- Bump version to get around botched update

* Mon May 13 2013 Stef Walter <stefw@redhat.com> - 0.7.1-1
- Update to upstream 0.7.1 release
- Fix problems with salt discovery [#961399]

* Mon May 06 2013 Stef Walter <stefw@redhat.com> - 0.7-1
- Work around broken krb5 with empty passwords [#960001]
- Fix memory corruption issue [#959999]
- Update to 0.7, fixing various bugs

* Mon Apr 29 2013 Stef Walter <stefw@redhat.com> - 0.6-1
- Update to 0.6, fixing various bugs

* Wed Apr 10 2013 Stef walter <stefw@redhat.com> - 0.5-2
- Add appropriate Obsoletes line for libadcli removal

* Wed Apr 10 2013 Stef Walter <stefw@redhat.com> - 0.5-1
- Update to upstream 0.5 version
- No more libadcli, and thus no adcli-devel
- Many new adcli commands
- Documentation

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 12 2012 Stef Walter <stefw@redhat.com> - 0.4-1
- Update for 0.4 version, fixing various bugs

* Sat Oct 20 2012 Stef Walter <stefw@redhat.com> - 0.3-1
- Update for 0.3 version

* Tue Sep 4 2012 Stef Walter <stefw@redhat.com> - 0.2-1
- Update for 0.2 version

* Wed Aug 15 2012 Stef Walter <stefw@redhat.com> - 0.1-1
- Initial 0.1 package
