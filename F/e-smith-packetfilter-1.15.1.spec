Summary: e-smith server and gateway - packetfilter add-on
%define name e-smith-packetfilter
Name: %{name}
%define version 1.15.1
%define release 12
Version: %{version}
Release: %{release}
License: GPL
Vendor: Mitel Networks Corporation
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch0: e-smith-packetfilter-1.15.1-02.mitel_patch
Patch1: e-smith-packetfilter-1.15.1-04.mitel_patch
Patch2: e-smith-packetfilter-1.15.1-05.mitel_patch
Patch3: e-smith-packetfilter-1.15.1-06.mitel_patch
Patch4: e-smith-packetfilter-1.15.1-07.mitel_patch
Patch5: e-smith-packetfilter-1.15.1-08.mitel_patch
Patch6: e-smith-packetfilter-1.15.1-09.mitel_patch
Patch7: e-smith-packetfilter-1.15.1-10.mitel_patch
Patch8: e-smith-packetfilter-1.15.1-11.mitel_patch
Packager: e-smith developers <bugs@e-smith.com>
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires: e-smith-base >= 4.15.0-32
Requires: ulogd
Requires: daemontools
Requires: iptables
BuildRequires: e-smith-devtools
AutoReqProv: no

%description
e-smith server and gateway software - packetfilter add-on

%changelog
* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 1.15.1-12
- Bump release number only

* Wed Sep 21 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.1-11]
- Remove force/masq/status fragment, and fix "masq adjust" so
  that it is harmless if firewall is disabled. This leaves unsolved
  the problem of whether to toggle disabled->enabled during upgrades.
  [SF: 1261356]

* Wed Sep  7 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.1-10]
- Fix location of force/status fragment for masq service. [SF: 1261356]

* Tue Aug 30 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.1-09]
- Add force/status fragment for masq service, to force enabled.
  This ensures that firewall is running after a system upgrade,
  to avoid various panel failure modes. Solution to be reviewed
  for alternatives later. [SF: 1261356]

* Fri Aug 26 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.1-08]
- Remove filtering of outbound ICMP - it's blocking legitimate ICMP
  redirects. [MN00093544]

* Tue Aug  2 2005 Shad Lords <slords@email.com>
- [1.15.1-07]
- Add default $masq{Stealth} db entry

* Tue Aug  2 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.15.1-06]
- Rejct IDENT with a TCP reset [SF: 1240659]
- Add support for UDPPort (c.f. TCPPort) property to allow
  filtered UDP [SF: 1241398]
- Add support for DenyHosts property (see 1.15.0-02 for AllowHosts)
  [SF: 1241398]

* Mon Jul 18 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.1-05]
- Tidy up path reference to networks db. [SF: 1216546]

* Tue Jun  7 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.1-04]
- Fix ulogd logging to stdout not being captured by multilog.

* Mon May  2 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.1-03]
- Add requires headers for ulogd and daemontools.

* Sun May  1 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.1-02]
- Switch to logging via ulogd and multilog.

* Sun May  1 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.1-01]
- Roll new development stream - 1.15.1

* Wed Mar 30 2005 Charlie Brady <charlieb@e-smith.com>
- [1.15.0-15]
- Set $OUTERNET to equal $LocalIP in masq script in serveronly mode,
  so that masq script (if enabled) does not block allowed public access.
- Remove various 45Allow* fragments as TCPPort properties of services
  will allow access if public access is enabled.

* Fri Nov 12 2004 Tony Clayton <apc@e-smith.com>
- [1.15.0-14]
- More cleanup for iptables-trace [tonyc]

* Fri Nov 12 2004 Tony Clayton <apc@e-smith.com>
- [1.15.0-13]
- update to latest iptables-trace [tonyc] : 
-  add logging for default chain policy fallback
-  fix stop() bug causing _any_ rules with --log-prefix to be removed

* Fri Apr 30 2004 Michael Soulier <msoulier@e-smith.com>
- [1.15.0-12]
- Made TOS settings configurable, with just ssh set by default.
  [msoulier dpar-28993]

* Wed Feb 25 2004 Michael Soulier <msoulier@e-smith.com>
- [1.15.0-11]
- Tightened rules for remote vpn subnets. [msoulier dpar-21836]

* Wed Jan 28 2004 Michael Soulier <msoulier@e-smith.com>
- [1.15.0-10]
- Fixed iptables-trace "stop" removing rules from the denylog chain.
  [msoulier 10955]

* Wed Jan 28 2004 Michael Soulier <msoulier@e-smith.com>
- [1.15.0-09]
- Added a toggle of the trace option during adjust, so adjusts work with trace
  enabled. [msoulier 8117]

* Mon Dec  1 2003 Michael Soulier <msoulier@e-smith.com>
- [1.15.0-08]
- Changed multicast DROP target to denylog, so it toggles. [msoulier 9450]

* Mon Dec  1 2003 Michael Soulier <msoulier@e-smith.com>
- [1.15.0-07]
- Changed the toggle property name to DenylogTarget. [msoulier 9450]

* Mon Dec  1 2003 Michael Soulier <msoulier@e-smith.com>
- [1.15.0-06]
- Added firewall-wide toggle for denylog DROP/REJECT. [msoulier 9450]

* Sat Nov 29 2003 Charlie Brady <charlieb@e-smith.com>
- [1.15.0-05]
- Ensure that masq script expands without error in serveronly mode.
  [charlieb 10162]

* Sat Oct  4 2003 Michael Soulier <msoulier@e-smith.com>
- [1.15.0-04]
- Fixed error in masq fragment with stealth enabled. [msoulier 10165]

* Thu Sep 25 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.15.0-03]
- Add masq to 0.0.0.0/0 for public, unrestricted [gordonr 10050]

* Tue Sep 23 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.15.0-02]
- New fragment 90InboundTCP10filter_tcp, a further step towards
  auto-generation of rules, removing the 45Allow* fragments:

  For all services which have a TCPPort property defined:
    If the service is 'enabled' and the service is 'public', 
	generate iptables rules as follows:
	If an AllowHosts property is defined, allow only those hosts
	Otherwise allow all hosts 

  AllowHosts is comma separated, and can contain IPs, IP/mask and CIDR

  This will generate duplicate rules until the 45Allow* fragments
  are removed, which can happen once the TCPPort property is defined
  for a service.

  QUERY: Should this be TCPPort (singular) or TCPPorts (plural)?
  TODO: Create db defaults fragments to deprecate the 45Allow* fragments
  TODO: Possibly add DenyHosts processing [gordonr 10050]

* Tue Sep 23 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.15.0-01]
- Changing version to development stream number - 1.15.0
- Dev stream [gordonr 10050]

* Thu Jun 26 2003 Charlie Brady <charlieb@e-smith.com>
- [1.14.0-01]
- Changing version to stable stream number - 1.14.0

* Tue Jun 17 2003 Tony Clayton <apc@e-smith.com>
- [1.13.0-27]
- Again [tonyc 8578]

* Tue Jun 17 2003 Tony Clayton <apc@e-smith.com>
- [1.13.0-26]
- Add lo->lo ACCEPT rule back to 90local_chk00Start fragment [tonyc 8578]

* Mon Jun 16 2003 Tony Clayton <apc@e-smith.com>
- [1.13.0-25]
- Split 90AllowLocal masq fragment into 90local_chk* [tonyc 8578]

* Mon Jun  2 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.0-24]
- Explicitely blocking multicast not from a local network.
  [msoulier 6031]

* Thu May  1 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.0-23]
- Added chain creation during adjust. What a thought. [msoulier 7695]

* Thu May  1 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.0-22]
- Added support for a PPPconn chain to track rules to permit PPTP connections.
  [msoulier 7695]

* Fri Apr 25 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.0-21]
- Refactored the 90adjustUDP template into multiple fragments. [msoulier 8505]

* Fri Apr 25 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.0-20]
- Refactored the 90adjustTCP template into multiple fragments. [msoulier 8505]

* Tue Apr 22 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.0-19]
- Accepting all traffic from the loopback interface. [msoulier 8299]

* Mon Apr 21 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.0-18]
- Removed acceptance of anything not from the external interface. The local
  networks list should be sufficient. [msoulier 8299]

* Mon Apr 21 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.0-17]
- Added handling of local_chk chain in adjustment. [msoulier 8299]

* Mon Apr 14 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.0-16]
- Flag pptp masq as on by default [gordonr 6694]

* Tue Apr  8 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.0-15]
- Added iptables-trace in /etc/rc.d/init.d. [msoulier 7613]

* Tue Apr  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.0-14]
- Added denylog: prefix to denied packet logs [gordonr 6852]

* Tue Mar 25 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.0-13]
- Portforwarding still had problems, fixed here. [msoulier 7284]

* Tue Mar 25 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.0-12]
- Added ForwardedTCP and ForwardedUDP, as well as supporting code to
  permit certain ports to be opened for forwarded traffic inbound. Required
  for portforwarding. [msoulier 7284]

* Fri Mar  7 2003 Charlie Brady <charlieb@e-smith.com>
- [1.13.0-11]
- Add "use esmith::util" to 01localNetworks fragment. Needed if
  esmith::templates form of processTemplate is used. [charlieb 5650]

* Fri Feb 21 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.0-10]
- Remove quotes around 'Name' - not required [gordonr 7343]

* Fri Feb 21 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.0-09]
- Make use of ExternalInterface definition in 00Definitions [gordonr 7343]
- Update dependency on e-smithbase [gordonr 7343]
 
* Mon Feb  3 2003 Mark Knox <markk@e-smith.com>
- [1.13.0-08]
- Open port 443 when either web server is enabled [markk 6428]

* Fri Jan 24 2003 Charlie Brady <charlieb@e-smith.com>
- [1.13.0-07]
- Fix one last broken here document. [charlieb 6651]

* Thu Jan 23 2003 Charlie Brady <charlieb@e-smith.com>
- [1.13.0-06]
- Fix a few typos in previous round of masq fragment changes. [charlieb]

* Thu Jan 23 2003 Charlie Brady <charlieb@e-smith.com>
- [1.13.0-05]
- formatting changes in masq/00Functions template fragment [charlieb]
- Use connection tracking on both INPUT and FORWARD tables [charlieb 6651]
- Allow any local traffic on INPUT and FORWARD chains. Local traffic
  is currently defined as all traffic which didn't come in via the
  external interface. That definition can easily change, as there is
  a special chain for accepting local traffic. [charlieb 6709]
- Remove explicit allow of multicast traffic, as it is a subset of "local"
  traffic [charlieb 6031, 6709]
- Move ICMP type checking into "adjust" part of masq script [charlieb 6709]

* Sat Jan 18 2003 Michael Soulier <msoulier@e-smith.com>
- [1.13.0-04]
- Permitting multicast traffic to and from the internal interface.
  [msoulier 6031]

* Wed Jan 15 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.0-03]
- Put back non-redundant DROP lines, but add a comment as to why
  they are there [gordonr 6580]

* Wed Jan 15 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.13.0-02]
- Remove redundant DROP lines from denylog chain [gordonr 6580]

* Thu Jan  9 2003 Mark Knox <markk@e-smith.com>
- [1.13.0-01]
- Forced version update by co2rpm to 1.13.0

* Mon Dec 16 2002 Charlie Brady <charlieb@e-smith.com>
- [1.12.0-01]
- Roll to stable version to 1.12.0

* Fri Nov 29 2002 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-07]
- Added a get_safe_id function, to factor out firewall rule scanning code, and
  prevent chain name clashes in the extreme case. [msoulier 5696]

* Thu Nov 28 2002 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-06]
- Removed specific tcp_in and udp_in chains in favour of the InboundTCP_$$ and
  InboundUDP__$$ chains. They are far, far easier to manage, especially for
  the portforwarding blade. [msoulier 5696]

* Wed Nov 20 2002 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-05]
- Make sure that --numeric is used with any --list command, to avoid
  reverse lookup delays. [charlieb 5644]

* Wed Nov 13 2002 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-04]
- Peel off ICMP for checking after packets for ESTABLISHED and RELATED
  connections are allowed. This allows outbound ping to work. [charlieb 5423]

* Mon Nov 11 2002 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-03]
- Apply UDP filtering only on traffic entering via external
  interface. [charlieb 5644]

* Mon Nov 11 2002 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-02]
- Add UDP input filter setup and adjust rules.
  Re-arrange 00Functions a bit so that perl block is
  shorter and the rest is in-line [charlieb 5644]
- Move adjustEnd to 92, to allow 91 hole for any adjustments
  needing to be done after input filter rules are adjusted
  (e.g. port forwarding).

* Mon Nov 11 2002 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-01]
- rolling development stream to 1.11.0

* Sat Oct 19 2002 Charlie Brady <charlieb@e-smith.com>
- [1.10.0-08]
- Send default packets on the FORWARD filter to denylog, rather than
  DROP. [charlieb 5246]
- Revert 2) from 1.10.0-05 checkin. 5.5 ipchains forwarding rules do not allow
  IP masqueraded packets. [charlieb 5246]

* Fri Oct 18 2002 Charlie Brady <charlieb@e-smith.com>
- [1.10.0-07]
- Commit new file 42CheckTCPInput which was missed in last checkin.
  [charlieb 5246]

* Fri Oct 18 2002 Charlie Brady <charlieb@e-smith.com>
- [1.10.0-06]
- Create a new intermediate TCP input chain, and create a new temporary
  TCP input chain whenever we run "masq adjust". This ensures that
  new TCP input checking rules occur at the same place during input
  checking as existing rules, and also means that rules previously created
  by now-removed packages disappear. [charlieb 4501, 5246]

* Thu Oct 17 2002 Charlie Brady <charlieb@e-smith.com>
- [1.10.0-05]
- Fix to the previous change 1) to restore some commented out rules,
  and 2) to fix those rules so that they match the 5.5 ipchains
  version. [charlieb 5246]

* Thu Oct 17 2002 Charlie Brady <charlieb@e-smith.com>
- [1.10.0-04]
- Changes so that local networks can be added/deleted and "masq adjust"
  will correctly re-adjust the filters. [charlieb 5246]

* Tue Oct 15 2002 Charlie Brady <charlieb@e-smith.com>
- [1.10.0-03]
- Change 00Functions so that "tcp_in" function can create chains as required
  during "masq adjust", so that new modules can add rules and still avoid
  "masq restart".  [charlieb 4501]

* Tue Oct 15 2002 Mark Knox <markk@e-smith.com>
- [1.10.0-02]
- Re-add echo-reply support (doesn't work with conntrack) [markk 5213]

* Sat Oct 12 2002 Charlie Brady <charlieb@e-smith.com>
- [1.10.0-01]
- Roll to maintained version number to 1.10.0
- Remove "perl createlinks" from %build section, since we no longer
  have a createlinks file.

* Fri Oct 11 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.9.15-07]
- Check the correct configDB entry for public POP [gordonr 5181]

* Tue Oct  8 2002 Mark Knox <markk@e-smith.com>
- [1.9.15-06]
- Use denylog target for dropped ICMP packets [markk 5095]
- Remove explicit echo-reply support (we use conntrack now) [markk 5095]

* Mon Oct  7 2002 Mark Knox <markk@e-smith.com>
- [1.9.15-05]
- Drop ICMP echo-requests on ext i/f when in private s/g mode or if Stealth
  property is set. General cleanup of ICMP rules. [markk 5095]

* Wed Sep 11 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.9.15-04]
- Added extra slosh in tcp_in as one gets gobbled by template evaluation
  and we need one in the final output. Reformatted the lines and moved
  proto/port together on first line of pair for readability [gordonr 4792]

* Thu Sep  5 2002 Charlie Brady <charlieb@e-smith.com>
- [1.9.15-03]
- Fix tcp_in function - it doesn't work too well without the jump to the
  newly defined rule. Change DROP to denylog in the placeholder rule,
  even though it is short-lived. [charlieb 4792]

* Mon Sep  2 2002 Charlie Brady <charlieb@e-smith.com>
- [1.9.15-02]
- Remove createlinks script and network-{create,delete} event directories -
  the required change was made in e-smith-base, and this shouldn't have
  been checked in. [charlieb 4501]

* Wed Aug 28 2002 Charlie Brady <charlieb@e-smith.com>
- [1.9.15-01]
- Rolling minor version number to work around wrinkle in co2rpm [charlieb 3700]

* Wed Aug 28 2002 Charlie Brady <charlieb@e-smith.com>
- [1.9.14-04]
- Remove 45AllowAUTH masq fragment - moved to e-smith-oidentd package.
  [charlieb 4435]

* Tue Aug 27 2002 Charlie Brady <charlieb@e-smith.com>
- [1.9.14-03]
- Fix iptables syntax in AdjustTOS fragment [charlieb 1268]

* Mon Aug 26 2002 Charlie Brady <charlieb@e-smith.com>
- [1.9.14-02]
- Fix AllowICMPfromLAN template error [charlieb 1268]

* Thu Aug 22 2002 Charlie Brady <charlieb@e-smith.com>
- [1.9.14-01]
- Use full iptables path in status fragment - allows "service masq status" to
  work. [charlieb 1268]
- Fix local networks list [charlieb 1268]

* Tue Aug 20 2002 Charlie Brady <charlieb@e-smith.com>
- [1.9.13-01]
- Fix syntax in 30adjustTOS fragment. Move definitions to start of masq
  script where they can be used in functions. [charlieb 4501]

* Mon Aug 19 2002 Charlie Brady <charlieb@e-smith.com>
- [1.9.12-01]
- Add 90adjustDenyLog fragment missed in last commit. [charlieb 4501]

* Mon Aug 19 2002 Charlie Brady <charlieb@e-smith.com>
- [1.9.11-01]
- Further re-arrangement to facilitate non-disruptive update of filtering
  rules. [charlieb 4501]

* Fri Aug 16 2002 Charlie Brady <charlieb@e-smith.com>
- [1.9.10-01]
- Remove 98adjust, and split it into 49adjustStart, 50adjustTCP and 51adjustEnd
  fragments. Migrate network stack tuning stuff to sysctl.conf templates.
  Add TOS adjustment stuff. [charlieb 4501]

* Thu Aug 15 2002 Charlie Brady <charlieb@e-smith.com>
- [1.9.9-01]
- Change masq template fragments to allow non-disruptive modification.
  Add "masq adjust" verb. [charlieb 4501]

* Thu Aug  8 2002 Charlie Brady <charlieb@e-smith.com>
- [1.9.8-01]
- Remove deprecated split in masq template fragment, and add FIXME comment
  to code which looks to be wrong. [charlieb 1268]

* Wed Jul 31 2002 Charlie Brady <charlieb@e-smith.com>
- [1.9.7-01]
- Use iptables state tracking to allow return traffic. Remove special
  rules set up to allow the return traffic. [charlieb 4499]

* Tue Jul 23 2002 Charlie Brady <charlieb@e-smith.com>
- [1.9.6-01]
- Allow local and masqueraded traffic on forward chain. Fix syntax for denylog
  chain. [charlieb 1268]

* Thu Jul 18 2002 Charlie Brady <charlieb@e-smith.com>
- [1.9.5-01]
- Avoid a perl warning from use of ${httpd-e-smith}{status} - 
  change to ${'httpd-e-smith'}{status}. [charlieb 1268]

* Wed Jul 17 2002 Charlie Brady <charlieb@e-smith.com>
- [1.9.4-01]
- Change syntax from ipchains (2.2 kernel) to iptables (2.4 kernel).
  [charlieb 1268]
- Add "status" option to list tables.
- Miscellaneous syntax cleanups.

* Tue Jul  2 2002 Charlie Brady <charlieb@e-smith.com>
- [1.9.3-01]
- Add "modprobe ipchains" to allow firewall to work with 2.4 kernel
  [charlieb 4223]

* Fri Jun 21 2002 Mark Knox <markk@e-smith.com>
- [1.9.2-01]
- Allow ICMP from all "local" networks, not just physical LAN [markk 3698]

* Fri Jun 21 2002 Mark Knox <markk@e-smith.com>
- [1.9.1-01]
- Allow ICMP on internal interface [markk 3698]

* Wed Jun  5 2002 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-01]
- Changing version to maintained stream number to 1.9.0

* Fri May 31 2002 Charlie Brady <charlieb@e-smith.com>
- [1.8.0-01]
- Changing version to maintained stream number to 1.8.0

* Thu May 23 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.7.3-01]
- RPM rebuild forced by cvsroot2rpm

* Fri May 10 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.2-01]
- Remove 45AllowSMTP - moved to e-smith-mailfront. [charlieb 3419]

* Fri May 10 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.1-01]
- No change. Test build of CVS conversion.

* Fri May 10 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.0-01]
- rollRPM: Rolled version number to 1.7.0-01. Includes patches up to 1.6.0-02.

* Wed Dec 19 2001 Charlie Brady <charlieb@e-smith.com>
- [1.6.0-02]
- Restore run time lookup of ExternalIP by /etc/rc.d/init.d/masq.
- Make sure that OUTERNET is set to a valid IP address, even if
  ExternalIP is not set in config db, to avoid syntax errors in
  ipchains command in masq script.

* Tue Dec 11 2001 Jason Miller <jay@e-smith.com>
- [1.6.0-01]
- rollRPM: Rolled version number to 1.6.0-01. Includes patches up to 1.5.0-05.

* Thu Dec 06 2001 Charlie Brady <charlieb@e-smith.com>
- [1.5.0-05]
- Add support for ippp0 as the external interface - if sync ISDN is used.

* Wed Nov 21 2001 Adrian Chung <adrianc@e-smith.com>
- [1.5.0-04]
- Add $OUT = "" to 01localNetworks so that '1' isn't output
  into template when 01localNetworks generates no output.

* Wed Nov 21 2001 Adrian Chung <adrianc@e-smith.com>
- [1.5.0-03]
- Splitting @locals and $primaryLocalNet generation out of
  40AllowLocals into 01localNetworks.
- transproxy fragment from e-smith-proxy needs these variables in
  35transproxy.

* Tue Nov 06 2001 Charlie Brady <charlieb@e-smith.com>
- [1.5.0-02]
- Fix variable naming error in setting up @locals array.
- Remove forwarding rules from stopmasq section - and remove the 'stop'
  alias for this case - there is a separate stop section of the script.
- Add bidirectional forwarding rules for each local network to our network.
  This both enables the forwarded traffic, and also prevents masquerading
  of the local traffic.

* Mon Nov 5 2001 Charlie Brady <charlieb@e-smith.com>
- [1.5.0-01]
- Rolled version number to 1.5.0-01. Includes patches upto 1.4.0-02.

* Mon Oct 29 2001 Charlie Brady <charlieb@e-smith.com>
- [1.4.0-02]
- Allow packet forwarding from localnet to localnet in serveronly mode -
  this is necessary for PPTP VPN termination.

* Thu Aug 23 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.4.0-01]
- Rolled version number to 1.4.0-01. Includes patches upto 1.3.0-08.

* Fri Aug 17 2001 gordonr
- [1.3.0-08]
- Autorebuild by rebuildRPM

* Mon Aug 13 2001 Adrian Chung <adrianc@e-smith.com>
- [1.3.0-07]
- Apply the patch. :)

* Fri Aug 10 2001 Adrian Chung <adrianc@e-smith.com>
- [1.3.0-06]
- Multicast range is 224.0.0.0 to 239.255.255.255 which
  is 224.0.0.0/4 not 224.0.0.0/3.
  224.0.0.0/3 covers 255.255.255.255 which denies DHCP traffic

* Mon Apr 21 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.3.0-05]
- Putback Charlie's change to add Stealth property to masq service, defaulting
  to "no". If set to "yes", external ICMP echo packets are ignored.

* Sat Apr 07 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.3.0-04]
- Forward port patches from 1.2.0-01 to 1.2.0-06

* Sun Mar 25 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.2.0-06]
- Two new properties of masq service - PermitHighUDP and PermitHighTCP.
  Both default to "yes", but provide an easy way to block unprivileged
  TCP/UDP or both.

* Fri Mar 23 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.2.0-05]
- Default auth/smtp/http[s] to public for backwards compatability

* Fri Mar 23 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.2.0-04]
- masq service now has an optional property Logging, defaulting to "none"
- Only log denied packets if Logging is other than "none" - this stops
  logging of the SMB chatter on cable and other shared networks
- Ignore SMB and RIP packets unless Logging is "all"

* Thu Mar 22 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.2.0-03]
- Check access property for httpd-e-smith/smtpd/identd

* Wed Mar  7 2001 Adrian Chung <adrianc@e-smith.com>
- [1.3.0-03]
- set rp_filter to 0 for 'all' interface as well.

* Wed Mar  7 2001 Adrian Chung <adrianc@e-smith.com>
- [1.3.0-02]
- set rp_filter to 0 for 'default' interface, explicitly set
  it to 1 for eth0, eth1.
- ipsec-restart will set eth1 to '0'.

* Wed Mar  7 2001 Adrian Chung <adrianc@e-smith.com>
- [1.3.0-01]
- branching to development stream.

* Thu Feb  8 2001 Adrian Chung <adrianc@e-smith.com>
- [1.2.0-02]
- Rolling release number for GPG signing.

* Thu Jan 25 2001 Peter Samuel <peters@e-smith.com>
- [1.2.0-01]
- Rolled version number to 1.2.0-01. Includes patches upto 1.1.0-16.

* Thu Jan 25 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-16]
- removed 35DenyUnrouteable fragment, since it affects
  us, and anyone else using a provider who masquerades
  connections.

* Wed Jan 24 2001 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-15]
- Remove AllowFTP fragment - moved to e-smith-proftpd.

* Thu Jan 18 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-14]
- adjusted 45AllowFTP to follow value of FTP accessLimits instead
  of service status.

* Mon Dec 18 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-13]
- Added use esmith::db

* Mon Dec 18 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-12]
- Backed out -11 patch - not required
- Reordered fragments

* Mon Dec 18 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-11]
- Added source/destination to icmp rules

* Fri Dec 15 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-10]
- Added protocol option to icmp fragments
- Removed masqstart/masqstop
- Allowed icmp echo-request and echo-reply

* Fri Dec 15 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-9]
- Rearranged fragments
- Split some rules into new chains
- Added extra ICMP rules

* Fri Dec 15 2000 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-8]
- Move AllowSSH template fragment to e-smith-openssh.
- Fix uninitialised value problem in  15Definitions.

* Tue Dec 12 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-7]
- Normalised AUTH template and fixed HTTP[S] templates

* Tue Dec 12 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-6]
- Used hard-quote form of HERE documents to avoid $ expansions

* Tue Dec 12 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-5]
- Normalised structure of 45Allow* fragments
- Moved 45AllowIONonPriv to 46AllowIONonPriv

* Tue Dec 12 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-4]
- Fixed service name in templates - imapd -> imap
- Changed mode -> access

* Tue Dec 12 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-3]
- Rewrote 15definitions and 45* fragments which checked services entries

* Tue Dec 05 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-2]
- Determine ExternalIP at run time
- Modified templates to check services entries
- Added COPYING file and GPL Copyright

* Tue Dec 05 2000 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-1]
- Rolled version and tarball including patches to 0.1-4
- Used e-smith-devtools

* Thu Nov 30 2000 Gordon Rowell <gordonr@e-smith.com>
- [0.1-4]
- Changes to match change to pppoe service

* Wed Nov 29 2000 Gordon Rowell <gordonr@e-smith.com>
- Handle ppp0 as external interface for PPPoE setups

* Tue Nov 21 2000 Charlie Brady <charlieb@e-smith.com>
- Remove extraneous } in 15definitions

* Sun Nov 19 2000 Charlie Brady <charlieb@e-smith.com>
- initial release

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
mkdir -p $RPM_BUILD_ROOT/var/log/iptables
mkdir -p $RPM_BUILD_ROOT/service
ln -s /var/service/ulogd $RPM_BUILD_ROOT/service/ulogd
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
    --dir /var/service/ulogd 'attr(1755,root,root)' \
    --file /var/service/ulogd/run 'attr(0755,root,root)' \
    --dir /var/service/ulogd/log 'attr(0755,root,root)' \
    --file /var/service/ulogd/log/run 'attr(0755,root,root)' \
    --dir /var/log/iptables 'attr(0755,smelog,smelog)' \
 > e-smith-%{version}-filelist
echo "%doc COPYING"          >> e-smith-%{version}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f e-smith-%{version}-filelist
%defattr(-,root,root)
