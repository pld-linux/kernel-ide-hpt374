#
# Conditional build:
# _without_dist_kernel	- without kernel from distribution
#
Summary:	Kernel HPT374 4-channel UDMA/ATA133 Controller
Summary(pl):	Sterownik HPT374 dla Linuksa
Name:		kernel-ide-hpt374
Version:	2.10
%define	rel	0.1
Release:	%{rel}@%{_kernel_ver_str}
License:	???
Group:		Base/Kernel
Source0:	http://www.highpoint-tech.com/hpt374-opensource-v2.10.tgz
# Source0-md5:	da75a1f2bd1b8657bcc7b95862a2c4d6
%{!?_without_dist_kernel:BuildRequires:	kernel-source}
BuildRequires:	rpmbuild(macros) >= 1.118
%{!?_without_dist_kernel:%requires_releq_kernel_up}
Requires(post,postun):	/sbin/depmod
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kernel HPT374 4-channel UDMA/ATA133 Controller

%description -l pl
Sterownik HPT374 dla Linuksa

%package -n kernel-smp-ide-hpt374
Summary:	Kernel SMP HPT374 4-channel UDMA/ATA133 Controller
Summary(pl):	Sterownik HPT374 dla Linuksa SMP
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
%{!?_without_dist_kernel:%requires_releq_kernel_up}
Requires(post,postun):	/sbin/depmod

%description -n kernel-smp-ide-hpt374
Kernel SMP HPT374 4-channel UDMA/ATA133 Controller

%description -n kernel-smp-ide-hpt374 -l pl
Sterownik HPT374 dla Linuksa SMP

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
