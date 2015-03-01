# -*- coding: utf-8 -*-
"""Graphical user interface to Pfeiffer Maxigauge pressure controller."""

import sys

from PyQt5 import QtWidgets

from pyhard2.gui.controller import Config, Controller
from pyhard2.gui.widgets import ScientificSpinBox
from pyhard2.gui.delegates import FormatTextDelegate
from pyhard2.gui.programs import SetpointRampProgram
import pyhard2.driver as drv
from pyhard2.driver.pfeiffer import Maxigauge
import pyhard2.driver.virtual as virtual


def createController():
    """Initialize controller."""
    config = Config("pfeiffer", "Multigauge")
    if not config.nodes:
        config.nodes = list(range(6))
    if not config.nodes:
        config.nodes = list(range(1, 7))
        config.names = ["G%i" % node for node in config.nodes]
    if config.virtual:
        driver = virtual.VirtualInstrument()
        iface = Controller.virtualInstrumentController(config, driver)
        iface.programs.default_factory = SetpointRampProgram
    else:
        driver = Maxigauge(drv.Serial(config.port))
        iface = Controller(config, driver)
        iface.editorPrototype.default_factory = ScientificSpinBox
        iface.addCommand(driver.gauge.pressure, "pressure")
    iface.driverWidget.driverView.setItemDelegateForColumn(
        0, FormatTextDelegate("%.2e"))
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
