# Generated from mime-types-1.16.gem by gem2rpm -*- rpm-spec -*-
%global gem_name mime-types


Summary: Return the MIME Content-Type for a given filename
Name: rubygem-%{gem_name}
Version: 3.1
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/mime-types/ruby-mime-types/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(rubygems)
Requires: ruby(release)
Requires: rubygem(mime-types-data) >= 3.2015
Requires: rubygem(mime-types-data) < 4
BuildRequires: rubygems-devel
BuildRequires: ruby(release)
BuildRequires: rubygem(minitest) < 5
BuildRequires: ruby >= 2.0
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
MIME::Types for Ruby manages a MIME Content-Type database that will return the
Content-Type for a given filename.

MIME::Types was originally based on and synchronized with MIME::Types for
Perl by Mark Overmeer, copyright 2001 - 2009. As of version 1.15, the data
format for the MIME::Type list has changed and the synchronization will no
longer happen.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
This package contains documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
testrb -Ilib test/*
popd

%files
%dir %{gem_instdir}
%{gem_instdir}/Manifest.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/Code-of-Conduct.rdoc
%doc %{gem_instdir}/Contributing.rdoc
%doc %{gem_instdir}/History.rdoc
%doc %{gem_instdir}/Licence.rdoc
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Fri Sep 16 2016 Rich Megginson <rmeggins@redhat.com> - 3.1-1
- update to 3.1

* Thu Feb 28 2013 Vít Ondruch <vondruch@redhat.com> - 1.19-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 26 2012 Vít Ondruch <vondruch@redhat.com> - 1.19-1
- Update to mime-types 1.19.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 31 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.16-7
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 08 2011 Mo Morsi <mmorsi@redhat.com> - 1.16-5
- Replace BR(check) with BR

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 30 2009 Matthew Kent <mkent@magoazul.com> - 1.16-3
- Remove needless rcov task in Rakefile causing issue (#544964).

* Sun Dec 27 2009 Matthew Kent <mkent@magoazul.com> - 1.16-2
- Fix license (#544964).
- Add note about rcov warning in test phase (#544964).

* Sun Dec 06 2009 Matthew Kent <mkent@magoazul.com> - 1.16-1
- Initial package
