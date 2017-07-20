from litex.gen import *
from litex.soc.interconnect.csr import *

class SDClocker(Module, AutoCSR):
    def __init__(self):
        self.divider = CSRStorage(32, reset=1)
        half = Signal(32)

        self.clk = Signal()
        counter = Signal(32)

        self.comb += [
            half.eq(self.divider.storage[1:]),
            If(half == 0, # Do not divide, use sys_clk
                self.clk.eq(ClockSignal("sys")),
            ).Else(
                self.clk.eq(counter >= half),
            )
        ]

        self.sync += [
            If((counter + 1) < self.divider.storage,
                counter.eq(counter + 1),
            ).Else(
                counter.eq(0),
            )
        ]

def tb(dut):
    for i in range(100):
        yield
    yield dut.divider.storage.eq(32)
    for i in range(1000):
        yield

if __name__ == '__main__':
    dut = SDClocker()
    run_simulation(dut, tb(dut), vcd_name='clocker.vcd')
