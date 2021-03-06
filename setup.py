"""
setup.py for pyhard2

Usage:
    python setup.py install
"""

import os
from glob import glob
from distutils.core import setup

import pyhard2


documentation = []
for ext in "rst py svg gv png xls".split():
    documentation.extend(glob(os.path.join("documentation", "*.%s" % ext)))

setup(name=u"pyhard2",
      version=pyhard2.__version__.split()[0],
      description=u"Free device-driver development kit (DDK)",
      author=u"Mathias Laurin",
      author_email="Mathias_Laurin@users.sf.net",
      url="http://pyhard2.sf.net",
      license="The MIT License (MIT)",
      packages=["pyhard2",
                "pyhard2.rsc",
                "pyhard2.ctrlr",
                "pyhard2.driver",
                "pyhard2.driver.daq",
                "pyhard2.driver.ieee",
               ],
      package_data={"pyhard2": ["rsc/resources.qrc",
                                "rsc/ui/*.ui",
                                "rsc/img/*.svg",
                                "rsc/icons/Tango/*.svg",
                                "../circat.yml",
                               ]},
      data_files=[("", ["LICENSE.TXT", "README.TXT"]),
                  ("", documentation)
                 ],
      requires=["pyserial",
                "pyyaml",
                "scipy",
               ],
      classifiers=os.linesep.join(
          s for s in """
          Development Status :: 3 - Alpha
          License :: OSI Approved :: The MIT License (MIT)
          Intended Audience :: Developers
          Intended Audience :: Science/Research
          Programming Language :: Python :: 2.7
          Environment :: X11 Applications :: Qt
          Topic :: Software Development :: Libraries :: Python Modules
          Topic :: System :: Hardware :: Hardware Drivers
          Topic :: System :: Monitoring
          """),
      platforms = "any",
      zip_safe=False,
     )
