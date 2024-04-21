import time
from labjack import ljm


class LabJackFixture:
    def __init__(self):
        self.handle = ljm.openS("T4", "ANY", "ANY")
        if self.handle is None:
            raise ConnectionError("LabJack T4 connection fail")

        ljm.eWriteName(self.handle, "DIO0_STATE", 0)
        ljm.eWriteName(self.handle, "DIO1_STATE", 1)

    def toggle_output_pin(self):
        ljm.eWriteName(self.handle, "DIO0_STATE", 1)
        time.sleep(1)
        ljm.eWriteName(self.handle, "DIO0_STATE", 0)

    def read_input_pin_state(self):
        return ljm.eReadName(self.handle, "DIO1_STATE")

    def close(self):
        ljm.close(self.handle)


def test_labjack_fixture():
    labjack = LabJackFixture()
    labjack.toggle_output_pin()
    input_state = labjack.read_input_pin_state()
    assert input_state == 0
    labjack.close()

# In order to test this with hardware in the loop in CI/CD:
# Set up CI/CD and connect LabJack T4, correct environment and configuration.
# Install all necessary dependency, drivers, and software in order to communicate with LabJack T4.
# Set up loggers and notifications.
# Data clean up - clean all data from LabJack T4.
