import os
import shutil
from conans import ConanFile, CMake, tools
from conans.errors import ConanException
from subprocess import call

class InnoSetupConan(ConanFile):
    name = "InnoSetup"
    version = "6.1.2"
    license = "..."
    license_url = "..."
    url = "..."
    homepage = "..."
    description = "..."
    author = "Karl Wallner <karl.wallner@gmx.de>"
    generators = "txt"
    settings = {"os": ["Windows"], "arch": ["x86_64"]}
    no_copy_source = True
    _iss_pack= "%s-%s.exe" % (name.lower(), version)
    _iss_url = "https://mlaan2.home.xs4all.nl/ispack/%s" % (_iss_pack)
    _iss_unpack= "%s-%s.zip" % (name.lower(), version)
   
    def source(self):
        tools.download("https://constexpr.org/innoextract/files/innoextract-1.9-windows.zip", self._iss_unpack)
        tools.download(self._iss_url, self._iss_pack)
        tools.unzip(self._iss_unpack)

    def build(self):
        call([os.path.join(self.source_folder, "innoextract.exe"), "-e", os.path.join(self.source_folder, self._iss_pack)])
        shutil.rmtree("tmp")
        
    def package(self):
        self.copy(pattern="*", src= "%s/app" % self.build_folder)
                    
    def package_info(self):
        self.env_info.PATH.insert(0, self.package_folder)
