import os
import shutil
from conans import ConanFile, CMake, tools
from conans.errors import ConanException

class InnoSetupConan(ConanFile):
    name = "InnoSetup"
    version = "5.6.1"
    license = "..."
    license_url = "..."
    url = "..."
    homepage = "..."
    description = "..."
    author = "Karl Wallner <karl.wallner@gmx.de>"
    generators = "txt"
    settings = {"os": ["Windows"], "arch": ["x86_64"]}
    no_copy_source = True
    
    def source(self):
        # Download unrar (https://www.rarlab.com)
        unrarw_pack = "unrarw32.exe"
        unrarw_url = "https://www.rarlab.com/rar/%s" % unrarw_pack
        tools.download(unrarw_url, unrarw_pack)
        self.run("%s /s" % unrarw_pack)
        os.remove(unrarw_pack)
        os.remove("license.txt")
        
        # Download innounp (http://innounp.sourceforge.net/)
        innounp_pack= "innounp047.rar"
        innounp_url= "https://sourceforge.net/projects/innounp/files/innounp/innounp%200.47/innounp047.rar/download"
        tools.download(innounp_url, innounp_pack)
        self.run("UnRAR.exe x %s" % innounp_pack)
        os.remove("innounp.htm")
        os.remove(innounp_pack)
        
        # Download InnoSetup (https://kinddragon.github.io/vld/)
        iss_pack= "%s-%s-unicode.exe" % (self.name.lower(), self.version)
        iss_url = "https://mlaan2.home.xs4all.nl/ispack/%s" % (iss_pack)
        tools.download(iss_url, iss_pack)
        self.run("innounp.exe -x %s" % iss_pack)
        os.remove(iss_pack)
        os.remove("install_script.iss")
        shutil.rmtree("{tmp}")
        
        # Clean up
        os.remove("UnRAR.exe")   
        os.remove("innounp.exe")
       
        # Rename
        os.rename("{app}", "InnoSetup")

    def package(self):
        #self.copy("FindVLD.cmake", ".", "")
        self.copy(pattern="*", src= "%s/InnoSetup" % self.source_folder)
        
        #win_arch = "Win32" if self.settings.arch == "x86" else "Win64"
        #xXX_arch = "x86" if self.settings.arch == "x86" else "x64"
        # 
        #shutil.move(os.path.join(self.package_folder, "lib", win_arch, "vld.lib"), os.path.join(self.package_folder, "lib", "vld.lib"))
        #shutil.move(os.path.join(self.package_folder, "bin", win_arch, "dbghelp.dll"), os.path.join(self.package_folder, "bin", "dbghelp.dll"))
        #shutil.move(os.path.join(self.package_folder, "bin", win_arch, "Microsoft.DTfW.DHL.manifest"), os.path.join(self.package_folder, "bin", "Microsoft.DTfW.DHL.manifest"))
        #shutil.move(os.path.join(self.package_folder, "bin", win_arch, "vld_%s.dll" % xXX_arch), os.path.join(self.package_folder, "bin", "vld_%s.dll" % xXX_arch))
        #shutil.move(os.path.join(self.package_folder, "bin", win_arch, "vld_%s.pdb" % xXX_arch), os.path.join(self.package_folder, "bin", "vld_%s.pdb" % xXX_arch))

        #shutil.rmtree(os.path.join(self.package_folder, "bin", "Win64"))
        #shutil.rmtree(os.path.join(self.package_folder, "lib", "Win64"))
        #shutil.rmtree(os.path.join(self.package_folder, "bin", "Win32"))
        #shutil.rmtree(os.path.join(self.package_folder, "lib", "Win32"))
        pass
            
    def package_info(self):
        self.env_info.PATH.insert(0, self.package_folder)
