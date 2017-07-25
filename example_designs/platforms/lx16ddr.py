from litex.build.generic_platform import *
from litex.build.xilinx import XilinxPlatform
from litex.build.xilinx.programmer import XC3SProg


_io = [
    ("user_led", 0, Pins("T9"), IOStandard("LVCMOS33"), Drive(24), Misc("SLEW=QUIETIO")),
    ("user_led", 1, Pins("R9"), IOStandard("LVCMOS33"), Drive(24), Misc("SLEW=QUIETIO")),

    ("clk50", 0, Pins("A10"), IOStandard("LVCMOS33")),

    ("serial", 0,
        Subsignal("tx", Pins("C13"), IOStandard("LVCMOS33"), Misc("SLEW=SLOW")),
        Subsignal("rx", Pins("A14"), IOStandard("LVCMOS33"), Misc("PULLUP"))
    ),
    ("serial", 1,
        Subsignal("tx", Pins("A13"), IOStandard("LVCMOS33"), Misc("SLEW=SLOW")),
        Subsignal("rx", Pins("B14"), IOStandard("LVCMOS33"), Misc("PULLUP"))
    ),

    ("spiflash", 0,
        Subsignal("cs_n", Pins("T3")),
        Subsignal("clk", Pins("R11")),
        Subsignal("mosi", Pins("T10")),
        Subsignal("miso", Pins("P10"), Misc("PULLUP")),
        IOStandard("LVCMOS33"), Misc("SLEW=FAST")
    ),

    ("ddram", 0,
     Subsignal("a", Pins("K5 K6 D1 L4 G5 H4 H3 D3 B2 A2 G6 E3 F3 F6 F5"), IOStandard("SSTL15")),
     Subsignal("ba", Pins("C3 C2 B1"), IOStandard("SSTL15")),
     Subsignal("ras_n", Pins("J6"), IOStandard("SSTL15")),
     Subsignal("cas_n", Pins("H5"), IOStandard("SSTL15")),
     Subsignal("we_n", Pins("C1"), IOStandard("SSTL15")),
     Subsignal("dm", Pins("J4 K3"), IOStandard("SSTL15")),
     Subsignal("dq", Pins("K2 K1 J3 J1 F2 F1 G3 G1 L3 L1 M2 M1 P2 P1 R2 R1"), IOStandard("SSTL15"), Misc("IN_TERM=UNTUNED_SPLIT_50")),
     Subsignal("dqs_p", Pins("H2 N3"), IOStandard("DIFF_SSTL15")),
     Subsignal("dqs_n", Pins("H1 N1"), IOStandard("DIFF_SSTL15")),
     Subsignal("clk_p", Pins("E2"), IOStandard("DIFF_SSTL15")),
     Subsignal("clk_n", Pins("E1"), IOStandard("DIFF_SSTL15")),
     Subsignal("cke", Pins("F4"), IOStandard("SSTL15")),
     Subsignal("odt", Pins("L5"), IOStandard("SSTL15")),
     Subsignal("reset_n", Pins("E4"), IOStandard("SSTL15")),
     Misc("SLEW=FAST"),
    ),

    ("sdcard", 0,
        Subsignal("data", Pins("K15 K14 M15 K11"), Misc("PULLUP")),
        Subsignal("cmd", Pins("L16"), Misc("PULLUP")),
        Subsignal("clk", Pins("J11"), Misc("PULLUP")),
        Subsignal("cd", Pins("N14")),
        Subsignal("sel", Pins("H13")),
        Subsignal("clk_fb", Pins("J14")),
        IOStandard("LVCMOS18"), Misc("SLEW=FAST"),
    ),

    ("sdcard", 1, #
        Subsignal("data", Pins("K16 J13 M16 K12"), Misc("PULLUP")),
        Subsignal("cmd", Pins("L14"), Misc("PULLUP")),
        Subsignal("clk", Pins("J12"), Misc("PULLUP")),
        Subsignal("cd", Pins("N16")),
        Subsignal("sel", Pins("H14")),
        Subsignal("clk_fb", Pins("J16")),
        IOStandard("LVCMOS18"), Misc("SLEW=FAST"),
    ),

]

_connectors = [
    ("A", "E12 B15 C15 D14 E15 F15 G11 F14 G16 H15 G12 H13 J14 J11 K14 K15 L16 K11 M15 N14 M13 L12 P15 R15 R14 T13 T12"),
    ("B", "E13 B16 C16 D16 E16 F16 F12 F13 G14 H16 H11 H14 J16 J12 J13 K16 L14 K12 M16 N16 M14 L13 P16 R16 T15 T14 R12"),
    ("C", "A14 C13 B12 C11 B10 C9 B8 C7 B6 B5 E10 E11 F9 C8 E7 F7 D6 M7 N8 P9 T5 T6 N9 L8 L10 P12 R9"),
    ("D", "B14 A13 A12 A11 A9 A8 A7 A6 A5 A4 C10 F10 D9 D8 E6 C6 N6 P6 L7 T4 R5 T7 M9 M10 P11 M11 T9")
]


class Platform(XilinxPlatform):
    default_clk_name = "clk50"
    default_clk_period = 20.00

    def __init__(self):
        XilinxPlatform.__init__(self, "xc6slx16-ftg256-2", _io, _connectors)

    def create_programmer(self):
        return XC3SProg("lx16ddr", "bscan_spi_lx9_papilio.bit")
