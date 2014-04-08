%define		pkg	js-beautify
Summary:	JS/CSS/HTML Beautifier
Name:		nodejs-%{pkg}
Version:	1.4.2
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	http://registry.npmjs.org/js-beautify/-/%{pkg}-%{version}.tgz
# Source0-md5:	f5bf6e20d882a6b98cf80584f0366a7b
URL:		https://github.com/einars/js-beautify
BuildRequires:	rpmbuild(macros) >= 1.634
BuildRequires:	sed >= 4.0
Requires:	nodejs
Requires:	nodejs-config-chain
Requires:	nodejs-mkdirp
Requires:	nodejs-nopt
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This little beautifier will reformat and reindent bookmarklets, ugly
JavaScript, unpack scripts packed by Dean Edward's popular packer, as
well as deobfuscate scripts processed by javascriptobfuscator.com.

%prep
%setup -qc
mv package/* .
cd js
%{__sed} -i -e '1s,^#!.*node,#!/usr/bin/node,' bin/* lib/cli.js
chmod a+rx bin/*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{nodejs_libdir}/%{pkg}/js,%{_bindir}}
cp -p package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cd js
cp -a index.js lib config bin $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}/js
ln -s %{nodejs_libdir}/%{pkg}/js/bin/css-beautify.js $RPM_BUILD_ROOT%{_bindir}
ln -s %{nodejs_libdir}/%{pkg}/js/bin/js-beautify.js $RPM_BUILD_ROOT%{_bindir}
ln -s %{nodejs_libdir}/%{pkg}/js/bin/html-beautify.js $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CONTRIBUTING.md LICENSE
%attr(755,root,root) %{_bindir}/css-beautify.js
%attr(755,root,root) %{_bindir}/html-beautify.js
%attr(755,root,root) %{_bindir}/js-beautify.js
%dir %{nodejs_libdir}/%{pkg}
%{nodejs_libdir}/%{pkg}/package.json
%dir %{nodejs_libdir}/%{pkg}/js
%{nodejs_libdir}/%{pkg}/js/index.js
%{nodejs_libdir}/%{pkg}/js/config
%{nodejs_libdir}/%{pkg}/js/lib
%dir %{nodejs_libdir}/%{pkg}/js/bin
%attr(755,root,root) %{nodejs_libdir}/%{pkg}/js/bin/*
