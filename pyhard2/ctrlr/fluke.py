"""Graphical user interface to Fluke Series 18x multimeters."""

import sys

from PyQt5 import QtWidgets

from pyhard2.gui.controller import Config, Controller
from pyhard2.gui.programs import SetpointRampProgram
import pyhard2.driver as drv
import pyhard2.driver.virtual as virtual
import pyhard2.driver.fluke as fluke


def createController():
    """Initialize controller."""
    config = Config("fluke", "18x")
    if not config.nodes:
        config.nodes, config.names = ([0], ["Fluke 18x"])
    if config.virtual:
        driver = virtual.VirtualInstrument()
        iface = Controller.virtualInstrumentController(config, driver)
        iface.programs.default_factory = SetpointRampProgram
    else:
        driver = fluke.Fluke18x(drv.Serial(config.port))
        iface = Controller(config, driver)
        iface.addCommand(driver.measure, "Measure")
        iface.addCommand(driver.unit, "Unit")
    iface.populate()
    return iface


def main(argv):
    """Start controller."""
    app = QtWidgets.QApplication(argv)
    app.lastWindowClosed.connect(app.quit)
    iface = createController()
    iface.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main(sys.argv)
