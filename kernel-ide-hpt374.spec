#
# Conditional build:
%bcond_without	dist_kernel	# without kernel from distribution
#
Summary:	Kernel HPT374 4-channel UDMA/ATA133 Controller
Summary(pl):	Sterownik dla Linuksa do HPT374 - 4-kana這wych kontroler闚 UDMA/ATA133
Name:		kernel-ide-hpt374
Version:	2.10
%define	rel	0.1
Release:	%{rel}@%{_kernel_ver_str}
License:	???
Group:		Base/Kernel
Source0:	http://www.highpoint-tech.com/hpt374-opensource-v2.10.tgz
# Source0-md5:	917268ff537a20a7f04093b680fb30b2
%{?with_dist_kernel:BuildRequires:	kernel-source}
BuildRequires:	rpmbuild(macros) >= 1.118
%{?with_dist_kernel:%requires_releq_kernel_up}
Requires(post,postun):	/sbin/depmod
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kernel HPT374 4-channel UDMA/ATA133 Controller.

%description -l pl
Sterownik dla Linuksa do HPT374 - 4-kana這wych kontroler闚
UDMA/ATA133.

%package -n kernel-smp-ide-hpt374
Summary:	Kernel SMP HPT374 4-channel UDMA/ATA133 Controller
Summary(pl):	Sterownik dla Linuksa SMP do HPT374 - 4-kana這wych kontroler闚 UDMA/ATA133
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
%{?with_dist_kernel:%requires_releq_kernel_up}
Requires(post,postun):	/sbin/depmod

%description -n kernel-smp-ide-hpt374
Kernel SMP HPT374 4-channel UDMA/ATA133 Controller.

%description -n kernel-smp-ide-hpt374 -l pl
Sterownik dla Linuksa SMP do HPT374 - 4-kana這wych kontroler闚
UDMA/ATA133.

%prep
%setup -q -c 

%build
%{__make} SMP="1"
mv hpt374.o hpt374.smp
%{__make} clean
%{__make} SMP=""

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}{,smp}/kernel/drivers/ide/raid

install hpt374.o $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}/kernel/drivers/ide/raid
install hpt374.smp $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}smp/kernel/drivers/ide/raid/hpt374.o

%clean
rm -rf $RPM_BUILD_ROOT

%post
%depmod %{_kernel_ver}

%postun
%depmod %{_kernel_ver}

%post	-n kernel-smp-ide-hpt374
%depmod %{_kernel_ver}smp

%postun	-n kernel-smp-ide-hpt374
%depmod %{_kernel_ver}smp

%files
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/kernel/drivers/ide/raid/hpt374.o*

%files -n kernel-smp-ide-hpt374
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}smp/kernel/drivers/ide/raid/hpt374.o*
