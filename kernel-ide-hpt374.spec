#
# Conditional build:
%bcond_without	dist_kernel	# without kernel from distribution
#
Summary:	Kernel HPT374 4-channel UDMA/ATA133 Controller
Summary(pl.UTF-8):   Sterownik dla Linuksa do HPT374 - 4-kanałowych kontrolerów UDMA/ATA133
Name:		kernel-ide-hpt374
Version:	2.11
%define	rel	0.1
Release:	%{rel}@%{_kernel_ver_str}
License:	???
Group:		Base/Kernel
Source0:	http://www.highpoint-tech.com/BIOS%20%2B%20Driver/hpt374/Linux/hpt374-opensource-v2.11.tgz
# Source0-md5:	3780db3bf03b2d0c6f14ffd997cca59a
%{?with_dist_kernel:BuildRequires:	kernel-source}
BuildRequires:	rpmbuild(macros) >= 1.118
%{?with_dist_kernel:%requires_releq_kernel_up}
Requires(post,postun):	/sbin/depmod
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kernel HPT374 4-channel UDMA/ATA133 Controller.

%description -l pl.UTF-8
Sterownik dla Linuksa do HPT374 - 4-kanałowych kontrolerów
UDMA/ATA133.

%package -n kernel-smp-ide-hpt374
Summary:	Kernel SMP HPT374 4-channel UDMA/ATA133 Controller
Summary(pl.UTF-8):   Sterownik dla Linuksa SMP do HPT374 - 4-kanałowych kontrolerów UDMA/ATA133
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
%{?with_dist_kernel:%requires_releq_kernel_up}
Requires(post,postun):	/sbin/depmod

%description -n kernel-smp-ide-hpt374
Kernel SMP HPT374 4-channel UDMA/ATA133 Controller.

%description -n kernel-smp-ide-hpt374 -l pl.UTF-8
Sterownik dla Linuksa SMP do HPT374 - 4-kanałowych kontrolerów
UDMA/ATA133.

%prep
%setup -q -c 

%build
mkdir build
for cfg in smp up; do
        if [ ! -r "%{_kernelsrcdir}/config-$cfg" ]; then
	    exit 1
	fi
	rm -rf tmp
	mkdir tmp
	cd tmp
	cp -r %{_kernelsrcdir}/scripts .
	install -d {arch,drivers}
	cp -r %{_kernelsrcdir}/arch/i386 arch/
	ln -sf %{_kernelsrcdir}/drivers/scsi drivers/scsi
	install -d include/config
	touch include/config/MARKER
        ln -sf %{_kernelsrcdir}/config-$cfg .config
        ln -sf %{_kernelsrcdir}/Makefile
	cp -r %{_kernelsrcdir}/include/asm-i386 include/asm-i386
	ln -sf asm-i386 include/asm
	ln -sf %{_kernelsrcdir}/include/asm-generic include/asm-generic
	ln -sf %{_kernelsrcdir}/include/linux include/linux
	ln -sf %{_kernelsrcdir}/include/scsi include/scsi
	cd ..
        %{__make} KERNELDIR=`pwd`/tmp
        mv -f *.ko build/hpt374-$cfg.ko
    done


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}{,smp}/kernel/drivers/ide/raid

install build/hpt374-up.ko $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}/kernel/drivers/ide/raid/hpt374.ko
install build/hpt374-smp.ko $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}smp/kernel/drivers/ide/raid/hpt374.ko

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
/lib/modules/%{_kernel_ver}/kernel/drivers/ide/raid/hpt374.ko*

%files -n kernel-smp-ide-hpt374
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}smp/kernel/drivers/ide/raid/hpt374.ko*
