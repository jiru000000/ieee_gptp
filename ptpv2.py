#!/usr/bin/env python
# encoding: utf-8

from gptp.layers import PTPv2
from gptp.utils import MatchedList
from scapy.utils import rdpcap

pcap = rdpcap("ptpv2_syn_twostep_ipv4.pcap")

for p in pcap:
    if p.haslayer('PTPv2'):
        p.show()



matched_list = MatchedList([c for c in pcap if c.haslayer('PTPv2')])

(sync, fup) = matched_list.sync[0]
sync.show()
