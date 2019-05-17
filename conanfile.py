import os
from conans import ConanFile, CMake, tools

class XboxInternalsConan(ConanFile):
    name = "XboxInternals"
    version = "0.1.0"
    license = "GPL-3.0-only"
    url = "https://github.com/SteffenL/conan-xboxinternals"
    description = "Xbox Internals library from Velocity"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    exports_sources = "CMakeLists.txt"
    generators = "cmake"

    source_dir = "Velocity"

    def source(self):
        git = tools.Git(folder=self.source_dir)
        git.clone("https://github.com/SteffenL/Velocity.git", "develop-custom")

    def build(self):
        with tools.chdir(self.source_dir):
            cmake = CMake(self)
            cmake.configure()
            cmake.build()

    def package(self):
        self.copy("COPYING", dst="licenses", src=self.source_dir)
        self.copy("*.h", dst="include", src=os.path.join(self.source_dir, "XboxInternals"))
        if self.settings.compiler == "Visual Studio":
            self.copy("*.h", dst="include/dirent", src=os.path.join(self.source_dir, "XboxInternals/thirdparty/msvc/dirent"))

        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so*", dst="lib", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["XboxInternals"]

        if not self.options.shared:
            self.cpp_info.defines += ["XBOXINTERNALS_STATIC"]

    def requirements(self):
        self.requires("Botan/[>=2.8]@langnes/testing")
