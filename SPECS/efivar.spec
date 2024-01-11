Name:           efivar
Version:        37
Release:        4%{?dist}
Summary:        Tools to manage UEFI variables
License:        LGPL-2.1
URL:            https://github.com/rhboot/efivar
Requires:       %{name}-libs = %{version}-%{release}
ExclusiveArch:  %{ix86} x86_64 aarch64 %{arm}

BuildRequires:  popt-devel git glibc-static libabigail
# please don't fix this to reflect github's incomprehensible url that goes
# to a different tarball.
Source0:        https://github.com/rhboot/efivar/archive/efivar-%{version}.tar.bz2
Patch0001: 0001-util.h-add-unlikely-and-likely-macros.patch
Patch0002: 0002-dp.h-make-format_guid-handle-misaligned-guid-pointer.patch
Patch0003: 0003-linux-pci-root-remove-an-unused-assignment.patch
Patch0004: 0004-Fix-all-the-places-Werror-address-of-packed-member-c.patch
Patch0005: 0005-Get-rid-of-the-arrows-in-our-debug-messages.patch
Patch0006: 0006-Define-strdupa-if-it-is-not-defined.patch
Patch0007: 0007-Android-inital-porting-of-libefivar.patch
Patch0008: 0008-Remove-an-unused-function.patch
Patch0009: 0009-Fix-another-error-of-Werror-address-of-packed-member.patch
Patch0010: 0010-ucs2.h-remove-unused-variable.patch
Patch0011: 0011-ucs2.h-fix-logic-that-checks-for-UCS-2-string-termin.patch
Patch0012: 0012-dp-message-fix-efidp_ipv4_addr-fields-assignment.patch
Patch0013: 0013-Always-refer-to-MBR-and-GPT-fixed-values-as-magic-no.patch
Patch0014: 0014-Add-more-hexdump-logging-functions.patch
Patch0015: 0015-Add-efi_error_pop-and-pop-some-errors-sometimes.patch
Patch0016: 0016-Always-log-to-a-memfd-regardless-of-loglevel.patch
Patch0017: 0017-Always-initialize-any-variable-we-use-with-sscanf-s-.patch
Patch0018: 0018-Add-efi_get_libefivar_version-and-efi_get_libefiboot.patch
Patch0019: 0019-Fix-dbglog_seek-to-update-the-offset.patch
Patch0020: 0020-Update-efivar-37-.abixml-for-new-libabigail-version.patch
Patch0021: 0021-Fix-up-efi_guid_cmp-s-alignment-problem-a-different-.patch
Patch0022: 0022-Fix-dbglog_write-to-always-return-the-status-of-writ.patch
Patch0023: 0023-Do-a-better-job-of-making-sure-DLIBEFIVAR_VERSION-ha.patch
Patch0024: 0024-efi_stash_loglevel_-efi_set_loglevel.patch
Patch0025: 0025-guids-add-grub-guid-for-grubenv.patch
Patch0026: 0026-gcc.specs-add-grecord-gcc-switches.patch
Patch0027: 0027-Makefile-don-t-echo-our-deps-submake-invocation.patch
Patch0028: 0028-Make-Add-some-more-stuff-to-the-toplevel-clean.patch
Patch0029: 0029-Make-scan-build-rules-slightly-more-intuitive.patch
Patch0030: 0030-Local-header-whitespace-cleanup.patch
Patch0031: 0031-Exported-header-whitespace-cleanup.patch
Patch0032: 0032-Main-code-whitespace-cleanup.patch
Patch0033: 0033-efivar-rework-usage.patch
Patch0034: 0034-Try-to-deal-with-some-signof-char-signof-uint8_t-mad.patch
Patch0035: 0035-ucs2-document-things-a-little-better.patch
Patch0036: 0036-util.h-implement-add-mul-sub-for-more-integer-types.patch
Patch0037: 0037-Implement-efivar-export-foo.var.patch
Patch0038: 0038-Add-some-test-cases-for-efivar-export-import.patch
Patch0039: 0039-Fix-a-case-clang-analyzer-found-where-we-may-try-to-.patch
Patch0040: 0040-Make-sure-makeguids-helper-is-compiled-for-the-host-.patch
Patch0041: 0041-Makefile-sort-wildcard-output-for-reproducibility.patch
Patch0042: 0042-guids.txt-correct-sentinal-typo.patch
Patch0043: 0043-update-manpage-for-efivar-such-that-it-reflects-the-.patch
Patch0044: 0044-Fix-some-32-bit-size_t-format-specifier-errors.patch
Patch0045: 0045-Make-the-top-level-makefile-not-parallelize.patch
Patch0046: 0046-guids-add-auto_created_boot_option.patch
Patch0047: 0047-Move-our-infrastructure-makefiles-out-of-the-topdir.patch
Patch0048: 0048-Make-CC_FOR_BUILD-and-CCLD_FOR_BUILD-override-HOSTCC.patch
Patch0049: 0049-Rework-some-makefile-bits-to-make-overriding-some-op.patch
Patch0050: 0050-Make-add-Wno-missing-field-initializers.patch
Patch0051: 0051-debug-don-t-write-newlines-to-memfd.patch
Patch0052: 0052-sysfs-parsing-add-some-more-debugging-output.patch
Patch0053: 0053-gitignore-ignore-.strace.patch
Patch0054: 0054-Improve-consistency-of-debug-prints.patch
Patch0055: 0055-Fix-the-error-path-in-set_disk_and_part_name.patch
Patch0056: 0056-Try-even-harder-to-find-disk-device-symlinks-in-sysf.patch
Patch0057: 0057-Handle-sys-devices-virtual-nvme-fabrics-nvme-subsyst.patch
Patch0058: 0058-sysfs-parsers-make-all-the-sys-block-link-parsers-wo.patch
Patch0059: 0059-Put-some-EFI-device-paths-into-the-debug-log.patch
Patch0060: 0060-Update-abixml.patch
Patch0061: 0061-Update-abixml-files-and-work-around-some-inconsequen.patch
Patch0062: 0062-Don-t-use-march-native-on-ia64.patch
Patch0063: 0063-Work-around-autoconf-existing-in-the-world.patch
Patch0064: 0064-Fix-efivar-w-and-efivar-a.patch
Patch0065: 0065-Fix-variable-sz-uninitialized-error.patch

%description
efivar provides a simple command line interface to the UEFI variable facility.

%package libs
Summary: Library to manage UEFI variables

%description libs
Library to allow for the simple manipulation of UEFI variables.

%package devel
Summary: Development headers for libefivar
Requires: %{name}-libs = %{version}-%{release}

%description devel
development headers required to use libefivar.

%prep
%setup -q -n %{name}-%{version}
git init
git config user.email "%{name}-owner@fedoraproject.org"
git config user.name "Fedora Ninjas"
git add .
git commit -a -q -m "%{version} baseline."
git am %{patches} </dev/null
git config --unset user.email
git config --unset user.name

%build
make libdir=%{_libdir} bindir=%{_bindir} CFLAGS="$RPM_OPT_FLAGS -flto" LDFLAGS="$RPM_LD_FLAGS -flto"

%install
%makeinstall

%check
%ifarch x86_64
#make abicheck
%endif

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc README.md
%{_bindir}/efivar
%exclude %{_bindir}/efivar-static
%{_mandir}/man1/*

%files devel
%{_mandir}/man3/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files libs
%{_libdir}/*.so.*

%changelog
* Tue Jul 14 2020 Javier Martinez Canillas <javierm@redhat.com> - 37-4
- Fix efivar "-w" and "-a" options that broke due the rebase
  Related: rhbz#1755645

* Tue Jul 14 2020 Javier Martinez Canillas <javierm@redhat.com> - 37-3
- Fix uninitialized variable found by covscan
  Related: rhbz#1755645

* Mon Jul 13 2020 Javier Martinez Canillas <javierm@redhat.com> - 37-2
- Change License field to LGPL-2.1 to prevent rpminspect test to fail
  Related: rhbz#1755645

* Thu Jul 02 2020 Javier Martinez Canillas <javierm@redhat.com> - 37-1
- Update to efivar 37 and some changes to support NVMe over FC
  Resolves: rhbz#1755645

* Tue Oct 02 2018 Peter Jones <pjones@redhat.com> - 36-1
- Update to efivar 36 (and some change)
  Resolves: rhbz#1635019
- Add NVDIMM support
- Re-written linux interface parser to handle how devices are
  partitioned better, and for cleaner code, with one file per device
  type.
- lots of verbosity updates
- better CI
- analysis with clang's analyzer as well as coverity
- Better handling of immutable bits in sysfs
- LIBEFIVAR_OPS=help
- lots of code cleanups.
- Add emmc device support
- Add SAS port expander support
- Support for ACPI root nodes that are less common
  (i.e. ACPI Generic Container and Embedded Controller PNP nodes)
- Make abbreviated device paths if we can't parse a device's info
- Don't require NVME to have an EUI

* Mon Apr 09 2018 Peter Jones <pjones@redhat.com> - 35-1
- Update to efivar 35
- fixes for older compilers
- efi_get_variable_exists()
- Lots of stuff to make CI work.
- use usleep() to avoid hitting the kernel rate limiter on efivarfs
- better EFI_GUID macro
- add efi_guid_fwupdate (0abba7dc-e516-4167-bbf5-4d9d1c739416)

* Tue Feb 27 2018 Peter Jones <pjones@redhat.com> - 34-1
- Update to efivar 34, and include a patch to avoid upstream rate limiting.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Peter Robinson <pbrobinson@fedoraproject.org> 33-2
- Enable ARMv7, minor spec cleanups

* Tue Jan 23 2018 Peter Jones <pjones@redhat.com> - 33-1
- Add NVDIMM support
- Bump version to 33

* Tue Sep 12 2017 Peter Jones <pjones@redhat.com> - 32-2
- Make efi_guid_ux_capsule actually get exported right.

* Tue Sep 12 2017 Peter Jones <pjones@redhat.com> - 32-1
- efivar 32
- lots of coverity fixes; mostly leaked memory and fds and the like
- fix sysfs pci path formats
- handle device paths for dns, nfit, bluetooth, wifi, emmc, btle.
- improved abi checking on releases
- Fix failures on EDIT_WRITE in edit_variable() when the variable doesn't exist
- Add efi_guid_ux_capsule_guid to our guids
- Now with %%check

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 06 2017 Peter Jones <pjones@redhat.com> - 31-1
- Update to efivar 31
- Work around NVMe EUI sysfs change
- Provide some oldish version strings we should have kept.
- lots of overflow checking on our pointer math in dp parsing
- fix major/minor device number handling in the linux code
- Do better formatting checks for MBR partitions
- Fixes for gcc 7

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 30-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 17 2016 Peter Jones <pjones@redhat.com> - 30-4
- Handle NVMe device attributes paths moving around in sysfs.

* Wed Sep 28 2016 Peter Jones <pjones@redhat.com> - 30-3
- Maybe even provide the *right* old linker deps.

* Tue Sep 27 2016 Peter Jones <pjones@redhat.com> - 30-2
- Try not to screw up SONAME stuff quite so badly.

* Tue Sep 27 2016 Peter Jones <pjones@redhat.com> - 30-1
- Fix efidp_*() functions with __pure__ that break with some optimizations
- Fix NVMe EUI parsing.

* Tue Sep 27 2016 Peter Jones <pjones@redhat.com> - 29-1
- Use -pie not -PIE in our linker config
- Fix some overflow checks for gcc < 5.x
- Make variable class probes other than the first one actually work
- Move -flto to CFLAGS
- Pack all of the efi device path headers
- Fix redundant decl of efi_guid_zero()

* Wed Aug 17 2016 Peter Jones <pjones@redhat.com> - 28-1
- Make our sonames always lib$FOO.1 , not lib$FOO.$VERSION .

* Tue Aug 16 2016 Peter Jones <pjones@redhat.com> - 27-1
- Bug fix for 086eeb17 in efivar 26.

* Wed Aug 10 2016 Peter Jones <pjones@redhat.com> - 26-1
- Update to efivar-26 .

* Thu Jun 30 2016 Peter Jones <pjones@redhat.com> - 0.24-1
- Update to 0.24

* Mon Feb 15 2016 Peter Jones <pjones@redhat.com> - 0.23-1
- Update to 0.23

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 02 2015 Peter Jones <pjones@redhat.com> - 0.21-2
- Bump the release here so f22->f23->f24 updates work.

* Mon Jul 13 2015 Peter Jones <pjones@redhat.com> - 0.21-1
- Rename "make test" so packagers don't think it's a good idea to run it
  during builds.
- Error check sizes in vars_get_variable()
- Fix some file size comparisons
- make SONAME reflect the correct values.
- Fix some uses of "const"
- Compile with -O2 by default
- Fix some strict-aliasing violations
- Fix some of the .pc files and how we do linking to work better.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 02 2015 Peter Jones <pjones@redhat.com> - 0.20-1
- Update to 0.20
- Make sure tester is build with the right link order for libraries.
- Adjust linker order for pkg-config
- Work around LocateDevicePath() not grokking PcieRoot() devices properly.
- Rectify some missing changelog entries

* Thu May 28 2015 Peter Jones <pjones@redhat.com> - 0.19-1
- Update to 0.19
- add API from efibootmgr so fwupdate and other tools can use it.

* Wed Oct 15 2014 Peter Jones <pjones@redhat.com> - 0.15-1
- Update to 0.15
- Make 32-bit builds set variables' DataSize correctly.

* Wed Oct 08 2014 Peter Jones <pjones@redhat.com> - 0.14-1
- Update to 0.14
- add efi_id_guid_to_guid() and efi_guid_to_id_guid(), which support {ID GUID}
  as a concept.
- Add some vendor specific guids to our guid list.
- Call "empty" "zero" now, as many other places do.  References to
  efi_guid_is_empty() and efi_guid_empty still exist for ABI compatibility.
- add "efivar -L" to the man page.

* Tue Oct 07 2014 Peter Jones <pjones@redhat.com> - 0.13-1
- Update to 0.13:
- add efi_symbol_to_guid()
- efi_name_to_guid() will now fall back on efi_symbol_to_guid() as a last
  resort
- "efivar -L" to list all the guids we know about
- better namespacing on libefivar.so (rename well_known_* -> efi_well_known_*)

* Thu Sep 25 2014 Peter Jones <pjones@redhat.com> - 0.12-1
- Update to 0.12

* Wed Aug 20 2014 Peter Jones <pjones@redhat.com> - 0.11-1
- Update to 0.11

* Fri May 02 2014 Peter Jones <pjones@redhat.com> - 0.10-1
- Update package to 0.10.
- Fixes a build error due to different cflags in the builders vs updstream
  makefile.

* Fri May 02 2014 Peter Jones <pjones@redhat.com> - 0.9-0.1
- Update package to 0.9.

* Tue Apr 01 2014 Peter Jones <pjones@redhat.com> - 0.8-0.1
- Update package to 0.8 as well.

* Fri Oct 25 2013 Peter Jones <pjones@redhat.com> - 0.7-1
- Update package to 0.7
- adds --append support to the binary.

* Fri Sep 06 2013 Peter Jones <pjones@redhat.com> - 0.6-1
- Update package to 0.6
- fixes to documentation from lersek
- more validation of uefi guids
- use .xz for archives

* Thu Sep 05 2013 Peter Jones <pjones@redhat.com> - 0.5-0.1
- Update to 0.5

* Mon Jun 17 2013 Peter Jones <pjones@redhat.com> - 0.4-0.2
- Fix ldconfig invocation

* Mon Jun 17 2013 Peter Jones <pjones@redhat.com> - 0.4-0.1
- Initial spec file
