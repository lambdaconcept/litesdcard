#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from litex.soc.tools.remote import RemoteClient
from litescope.software.driver.analyzer import LiteScopeAnalyzerDriver

wb = RemoteClient(csr_csv="example_designs/build/csr.csv")
# wb = RemoteClient(csr_csv="build/csr.csv")
wb.open()

# # #

analyzer = LiteScopeAnalyzerDriver(wb.regs, "analyzer", debug=True, config_csv="example_designs/build/analyzer.csv")
# analyzer = LiteScopeAnalyzerDriver(wb.regs, "analyzer", debug=True, config_csv="build/analyzer.csv")
# analyzer.configure_trigger()
# analyzer.configure_trigger(cond={"sdctrl_crc16checker_sink_last": 1, "sdctrl_crc16checker_sink_payload_data": 0x00})
# analyzer.configure_trigger(cond={"sdphy_cmdr_enable": 1})
# analyzer.configure_trigger(cond={"sdctrl_sink_sink_valid": 1, "sdctrl_sink_sink_payload_ctrl": 0x01})
analyzer.configure_trigger(cond={"sdphy_cmdr_sdphycmdrfb_source_valid": 1})
# analyzer.configure_trigger(cond={"sdphy_datar_sink_sink_valid": 1})
analyzer.configure_subsampler(1)
analyzer.run(offset=300, length=2048) # 10000
while not analyzer.done():
    pass
analyzer.upload()
analyzer.save("test/vcd/litescope.vcd")

# # #

wb.close()
