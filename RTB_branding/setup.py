import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.md")) as f:
    README = f.read()
with open(os.path.join(here, "CHANGES.txt")) as f:
    CHANGES = f.read()

requires = [
    "climmob",
]

tests_require = [
    "WebTest >= 1.3.1",  # py3 compat
    "pytest",
    "pytest-cov",
]

setup(
    name="RTB_branding",
    version="1.0",
    description="Branding",
    long_description=README + "\n\n" + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author="Alliance Bioversity-CIAT",
    author_email="c.f.quiros@cgiar.org",
    url="https://rtb.climmob.net",
    keywords="climmob plugin",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={"testing": tests_require,},
    install_requires=requires,
    entry_points={
        "climmob.plugins": ["RTB_branding = RTB_branding.plugin:RTBBranding",],
    },
)
