%define name	jlzma
%define version	4.23.1
%define release	%mkrel 1

Name:		%{name}
Summary:	Java port of the LZMA SDK 4.23
Version:	%{version}
Release:	%{release} 
Source0:	http://downloads.sourceforge.net/project/p7zip/java_lzma/4.23.01/java_lzma_4.23.1.tar.bz2
Patch0:		jlzma-4.23.1-fix-jar.patch
Patch1:		jlzma-4.23.1-javadoc-task.patch
URL:		http://p7zip.sourceforge.net/

Group:		Development/Java
License:        LGPLv2 or CPL

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ant
BuildRequires:	ant-nodeps
BuildRequires:	java-rpmbuild
Requires:	java

BuildArch:	noarch

%description
JAVA port of LZMA Encoder and Decoder from LZMA C# SDK 4.23.

%files
%defattr(-,root,root,-)
%doc readme.txt history.txt lzma#.txt LGPL.txt CPL.html
%_javadir/*.jar

#--------------------------------------------------------------------

%package	javadoc
Summary:	Javadoc for jlzma
Group:		Development/Java

%description javadoc
Javadoc for jlzma.


%files javadoc
%defattr(-,root,root,-)
%_javadocdir/*

#--------------------------------------------------------------------

%prep
%setup -q -n java_lzma_4.23.1
%patch0 -p0
%patch1 -p0

%build
export CLASSPATH="." 
%ant dist javadoc

%install
rm -rf $RPM_BUILD_ROOT

%__install -dm 755 $RPM_BUILD_ROOT%_javadir
%__install -m 644 dist/JLzma.jar $RPM_BUILD_ROOT%_javadir/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%_javadir/%{name}.jar

# javadoc
%__install -dm 755 $RPM_BUILD_ROOT%_javadocdir/%{name}-%{version}
pushd javadoc
cp -pr * $RPM_BUILD_ROOT%_javadocdir/%{name}-%{version}
popd
ln -s %{name}-%{version} $RPM_BUILD_ROOT%_javadocdir/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

