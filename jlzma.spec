Name:		jlzma
Summary:	Java port of the LZMA SDK 4.23
Version:	4.23.1
Release:	%mkrel 1
Source0:	http://downloads.sourceforge.net/project/p7zip/java_lzma/4.23.01/java_lzma_4.23.1.tar.bz2
Patch0:		jlzma-4.23.1-fix-jar.patch
Patch1:		jlzma-4.23.1-javadoc-task.patch
URL:		http://p7zip.sourceforge.net/

Group:		Development/Java
License:	LGPLv2.1 or CPL

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ant
BuildRequires:	ant-nodeps
BuildRequires:	java-rpmbuild
Requires:	java

BuildArch:	noarch

%description
JAVA port of LZMA Encoder and Decoder from LZMA C# SDK 4.23.

%package	javadoc
Summary:	Javadoc for jlzma
Group:		Development/Java

%description	javadoc
Javadoc for jlzma.

%prep
%setup -q -n java_lzma_%{version}
%patch0 -p0
%patch1 -p0

%build
export CLASSPATH="." 
%ant dist javadoc

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javadir}
install -m644 dist/JLzma.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}
cp -r javadoc $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc readme.txt history.txt lzma#.txt LGPL.txt CPL.html
%{_javadir}/*.jar

%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/*
