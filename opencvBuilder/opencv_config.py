import os

import opencvBuilderUtils

class configParameters:
    FALSE = 0;
    TRUE = 1;
    INHERIT = 2;

# Default configuration
ccmake = {
        # 3rd party builds
        'BUILD_JASPER' : False,
        'BUILD_JPEG' : False,		# Supported
        'BUILD_OPENEXR' : False,
        'BUILD_PNG' : False,
        'BUILD_SHARED_LIBS' : configParameters.INHERIT, # Inherited from Scons settings
        'BUILD_TBB' : False,
        'BUILD_TIFF' : False,
        'BUILD_ZLIB' : False,		# Supported
        'BZIP2_LIBRARIES' : '/lib64/libbz2.so',
        'BUILD_WITH_DEBUG_INFO' : False, # Supported	

        # Enable stuff
        'ENABLE_AVX' : False,
        'ENABLE_COVERAGE' : False,
        'ENABLE_FAST_MATH' : False,
        'ENABLE_OMIT_POINTER_FRAME' : False,     # Supported
        'ENABLE_PRECOMPILED_HEADER' : False,
        'ENABLE_PROFILING' : False,
        'ENABLE_SOLUTION_FOLDERS' : False,
        'ENABLE_SSE' : False,	# Supported
        'ENABLE_SSE2' : False,	# Supported
        'ENABLE_SSE3' : False,	# Supported
        'ENABLE_SSE41' : False,
        'ENABLE_SSE42' : False,
        'ENABLE_SSSE3' : False,

        # With stuff
        'WITH_1394-V1' : False,
        'WITH_1394-V2' : False,
	'WITH_ANDROID' : False,
        'WITH_CARBON' : False,
        'WITH_CLP' : False,
        'WITH_CMU1394' : False,
	'WITH_COCOA' : False,		# Supported
        'WITH_CUBLAS' : False,
        'WITH_CUDA' : False,
        'WITH_CUFFT' : False,
        'WITH_DSHOW' : False,
        'WITH_EIGEN' : False,
        'WITH_FFMPEG' : False,		# Supported
        'WITH_GIGEAPI' : False,		# Supported
        'WITH_GSTREAMER' : False,	# Supported
        'WITH_GSTREAMER_0_10' : False,	# Supported
        'WITH_GTK' : False,		# Supported
        'WITH_GTK_2_X' : False,
	'WITH_IOS' : False,
        'WITH_INTELPERC' : False,
        'WITH_IPP' : False,
        'WITH_IPP_A' : False,
        'WITH_JASPER' : False,
        'WITH_JPEG' : False,		# Supported
        'WITH_LIBV4L' : False,		# Supported
        'WITH_MIL' : False,
        'WITH_MSMF' : False,
        'WITH_NVCUVID' : False,
        'WITH_OPENCL' : False,
        'WITH_OPENCLAMDBLAS' : False,
        'WITH_OPENCV_CLAMDFFT' : False,
        'WITH_OPENEXR' : False,
        'WITH_OPENGL' : False,
        'WITH_OPENMP' : configParameters.INHERIT,
        'WITH_OPENNI' : False,
        'WITH_PNG' : False,
        'WITH_PVAPI' : False,
	'WITH_QT' : False,
        'WITH_QTKIT' : False,		# Supported
        'WITH_TBB' : False,
        'WITH_TIFF' : False,
        'WITH_TYZX' : False,
        'WITH_UNICAP' : False,
        'WITH_V4L' : False,		# Supported
        'WITH_VFW' : False,
        'WITH_VTK' : False,
        'WITH_WIN32UI' : False,
        'WITH_WEBP' : False,
        'WITH_XIMEA' : False,		# Supported
        'WITH_XINE' : False		# Supported
}

class configFileGenerator(object):
    @staticmethod
    def notDefined(value):
        return None

    @staticmethod
    def defUndef(value, string):
        if(value):
            return '#define {string}\n'.format(string = string)
        else:
            return '/* #undef {string} */\n'.format(string = string)

    @staticmethod
    def withJpeg(value):
        return configFileGenerator.defUndef(value, 'HAVE_JPEG')

    @staticmethod
    def withXimea(value):
        return configFileGenerator.defUndef(value, 'HAVE_XIMEA')

    @staticmethod
    def withXine(value):
        return configFileGenerator.defUndef(value, 'HAVE_XINE')
   
    @staticmethod
    def withDc1394V2(value):
        return configFileGenerator.defUndef(value, 'HAVE_DC1394_2')
    
    @staticmethod
    def withDc1394(value):
        return configFileGenerator.defUndef(value, 'HAVE_DC1394')

    @staticmethod
    def withFfmpeg(value):
        defines = configFileGenerator.defUndef(value, 'HAVE_FFMPEG')
        defines = defines + configFileGenerator.defUndef(value, 'HAVE_FFMPEG_SWSCALE')
        defines = defines + configFileGenerator.defUndef(value, 'HAVE_GENTOO_FFMPEG')
        return defines
    @staticmethod
    def withLibv4l(value):
        defines = configFileGenerator.defUndef(value, 'HAVE_LIBV4L')
        defines = defines + configFileGenerator.defUndef(value, 'HAVE_CAMV4L')
        defines = defines + configFileGenerator.defUndef(value, 'HAVE_CAMV4L2')
        return defines
    @staticmethod
    def withV4L(value):
        defines = configFileGenerator.withLibv4l(value)
#        defines = defines + configFileGenerator.defUndef(value, 'HAVE_VIDEOIO')
        return defines
    @staticmethod
    def withGtkGeneral(value):
        return configFileGenerator.defUndef(value, 'HAVE_GTHREAD')
    @staticmethod
    def withGtk(value):
        defines = configFileGenerator.withGtkGeneral(value)
        defines = defines + configFileGenerator.defUndef(value, 'HAVE_GTK')
        defines = defines + configFileGenerator.defUndef(value, 'HAVE_GTK3')
        return defines
    @staticmethod
    def withGtk2(value):
        defines = configFileGenerator.withGtkGeneral(value)
        defines = defines + configFileGenerator.defUndef(value, 'HAVE_GTK_2_X')
        return defines
    @staticmethod
    def withQtkit(value):
        return configFileGenerator.defUndef(value, 'HAVE_QTKIT')
    @staticmethod
    def withCocoa(value):
        return configFileGenerator.defUndef(value, 'HAVE_COCOA')
    @staticmethod
    def withGstreamer(value):
        return configFileGenerator.defUndef(value, 'HAVE_GSTREAMER')

# Config file functions
ccmakeToCvconfig = {
        # 3rd party builds
        'BUILD_JASPER' : configFileGenerator.notDefined,
        'BUILD_JPEG' : configFileGenerator.notDefined,
        'BUILD_OPENEXR' : configFileGenerator.notDefined,
        'BUILD_PNG' : configFileGenerator.notDefined,
        'BUILD_SHARED_LIBS' : configFileGenerator.notDefined,
        'BUILD_TBB' : configFileGenerator.notDefined,
        'BUILD_TIFF' : configFileGenerator.notDefined,
        'BUILD_ZLIB' : configFileGenerator.notDefined,
        'BZIP2_LIBRARIES' : configFileGenerator.notDefined,
        'BUILD_WITH_DEBUG_INFO' : configFileGenerator.notDefined,

        # Enable stuff
        'ENABLE_AVX' : configFileGenerator.notDefined,
        'ENABLE_COVERAGE' : configFileGenerator.notDefined,
        'ENABLE_FAST_MATH' : configFileGenerator.notDefined,
        'ENABLE_OMIT_POINTER_FRAME' : configFileGenerator.notDefined,
        'ENABLE_PRECOMPILED_HEADER' : configFileGenerator.notDefined,
        'ENABLE_PROFILING' : configFileGenerator.notDefined,
        'ENABLE_SOLUTION_FOLDERS' : configFileGenerator.notDefined,
        'ENABLE_SSE' : configFileGenerator.notDefined,
        'ENABLE_SSE2' : configFileGenerator.notDefined,
        'ENABLE_SSE3' : configFileGenerator.notDefined,
        'ENABLE_SSE41' : configFileGenerator.notDefined,
        'ENABLE_SSE42' : configFileGenerator.notDefined,
        'ENABLE_SSSE3' : configFileGenerator.notDefined,

        # With stuff
        'WITH_1394-V1' : configFileGenerator.withDc1394,
        'WITH_1394-V2' : configFileGenerator.withDc1394V2,
	'WITH_ANDROID' : configFileGenerator.notDefined,
        'WITH_CARBON' : configFileGenerator.notDefined,
        'WITH_CLP' : configFileGenerator.notDefined,
        'WITH_CMU1394' : configFileGenerator.notDefined,
	'WITH_COCOA' : configFileGenerator.withCocoa,
        'WITH_CUBLAS' : configFileGenerator.notDefined,
        'WITH_CUDA' : configFileGenerator.notDefined,
        'WITH_CUFFT' : configFileGenerator.notDefined,
        'WITH_DSHOW' : configFileGenerator.notDefined,
        'WITH_EIGEN' : configFileGenerator.notDefined,
        'WITH_FFMPEG' : configFileGenerator.withFfmpeg,
        'WITH_GIGEAPI' : configFileGenerator.notDefined,
        'WITH_GSTREAMER' : configFileGenerator.withGstreamer,
        'WITH_GSTREAMER_0_10' : configFileGenerator.notDefined,
        'WITH_GTK' : configFileGenerator.withGtk,
        'WITH_GTK_2_X' : configFileGenerator.withGtk2,
	'WITH_IOS' : configFileGenerator.notDefined,
        'WITH_INTELPERC' : configFileGenerator.notDefined,
        'WITH_IPP' : configFileGenerator.notDefined,
        'WITH_IPP_A' : configFileGenerator.notDefined,
        'WITH_JASPER' : configFileGenerator.notDefined,
        'WITH_JPEG' : configFileGenerator.withJpeg,
        'WITH_LIBV4L' : configFileGenerator.withLibv4l,
        'WITH_MIL' : configFileGenerator.notDefined,
        'WITH_MSMF' : configFileGenerator.notDefined,
        'WITH_NVCUVID' : configFileGenerator.notDefined,
        'WITH_OPENCL' : configFileGenerator.notDefined,
        'WITH_OPENCLAMDBLAS' : configFileGenerator.notDefined,
        'WITH_OPENCV_CLAMDFFT' : configFileGenerator.notDefined,
        'WITH_OPENEXR' : configFileGenerator.notDefined,
        'WITH_OPENGL' : configFileGenerator.notDefined,
        'WITH_OPENMP' : configFileGenerator.notDefined,
        'WITH_OPENNI' : configFileGenerator.notDefined,
        'WITH_PNG' : configFileGenerator.notDefined,
        'WITH_PVAPI' : configFileGenerator.notDefined,
	'WITH_QT' : configFileGenerator.notDefined,
        'WITH_QTKIT' : configFileGenerator.withQtkit,
        'WITH_TBB' : configFileGenerator.notDefined,
        'WITH_TIFF' : configFileGenerator.notDefined,
        'WITH_TYZX' : configFileGenerator.notDefined,
        'WITH_UNICAP' : configFileGenerator.notDefined,
        'WITH_V4L' : configFileGenerator.withV4L,
        'WITH_VFW' : configFileGenerator.notDefined,
        'WITH_VTK' :  configFileGenerator.notDefined,
        'WITH_WIN32UI' : configFileGenerator.notDefined,
        'WITH_WEBP' : configFileGenerator.notDefined,
        'WITH_XIMEA' : configFileGenerator.withXimea,
        'WITH_XINE' : configFileGenerator.withXine
}

class modulesToFilterFunctions(object):
    @staticmethod
    def optionToSources(option, sources,source):
        if not ccmake[option]:
            sources = modulesToFilterFunctions.removeFromList(sources, source)
        return sources
    @staticmethod
    def removeFromList(sources, valueToRemove):
        try:
            for source in sources:
                if(os.path.basename(source.rstr()) == os.path.basename(valueToRemove)):
                    sources.remove(source)
        except:
	    pass
        return sources
    @staticmethod
    def nothingSpecial(env, sources, modulePath):
        return sources,None,None
    @staticmethod
    def highgui(env, sources, modulePath):
        additionalIncludes = list()
        additionalLibs = list()
        sources = modulesToFilterFunctions.optionToSources('WITH_XIMEA', sources, '{module}/src/cap_ximea.cpp'.format(module = modulePath))
        # TODO: Add ximea 32-bit lib if needed 
        additionalLibs.append('m3apiX64')
	sources = modulesToFilterFunctions.optionToSources('WITH_XINE', sources, '{module}/src/cap_xine.cpp'.format(module = modulePath))
	sources = modulesToFilterFunctions.optionToSources('WITH_1394-V1', sources, '{module}/src/cap_dc1394.cpp'.format(module = modulePath))
	sources = modulesToFilterFunctions.optionToSources('WITH_1394-V2', sources, '{module}/src/cap_dc1394_v2.cpp'.format(module = modulePath))
        sources = modulesToFilterFunctions.optionToSources('WITH_GIGEAPI', sources, '{module}/src/cap_giganetix.cpp'.format(module = modulePath))
        sources = modulesToFilterFunctions.optionToSources('WITH_VFW', sources, '{module}/src/cap_vfw.cpp'.format(module = modulePath))
        if not ccmake['WITH_GSTREAMER'] and not ccmake['WITH_GSTREAMER_0_10']:
            sources = modulesToFilterFunctions.optionToSources('WITH_GSTREAMER', sources, '{module}/src/cap_gstreamer.cpp'.format(module = modulePath))
        else:
            if ccmake['WITH_GSTREAMER']:
                additionalIncludes.extend(findGstreamer())
            else:
                additionalIncludes.extend(findGstreamer010())
	    for includePath in opencvBuilderAdditionalIncludePaths:
            	additionalIncludes.append('{path}/glib-2.0'.format(path=includePath))
            	additionalIncludes.append('{path}/glib-2.0/include'.format(path=includePath))

        # Handle GTK
        if ccmake['WITH_GTK']:
            additionalIncludes.extend(findGtk3())
        if ccmake['WITH_GTK_2_X']:
            additionalIncludes.extend(findGtk2())

        if not ccmake['WITH_GTK'] and not ccmake['WITH_GTK_2_X']:
            sources = modulesToFilterFunctions.removeFromList(sources, '{module}/src/window_gtk.cpp'.format(module = modulePath))

        sources = modulesToFilterFunctions.optionToSources('WITH_CARBON', sources, '{module}/src/window_carbon.cpp'.format(module = modulePath))
        sources = modulesToFilterFunctions.optionToSources('WITH_WIN32UI', sources, '{module}/src/window_w32.cpp'.format(module = modulePath))
	sources = modulesToFilterFunctions.optionToSources('WITH_COCOA', sources, '{module}/src/window_cocoa.mm'.format(module = modulePath))
        sources = modulesToFilterFunctions.optionToSources('WITH_QT', sources, '{module}/src/window_QT.cpp'.format(module = modulePath))
        sources = modulesToFilterFunctions.optionToSources('WITH_UNICAP', sources, '{module}/src/cap_unicap.cpp'.format(module = modulePath))
        sources = modulesToFilterFunctions.optionToSources('WITH_QT', sources, '{module}/src/cap_qt.cpp'.format(module = modulePath))
        sources = modulesToFilterFunctions.optionToSources('WITH_QTKIT', sources, '{module}/src/cap_qtkit.mm'.format(module = modulePath))
	sources = modulesToFilterFunctions.optionToSources('WITH_LIBV4L', sources, '{module}/src/cap_libv4l.cpp'.format(module = modulePath))
        sources = modulesToFilterFunctions.optionToSources('WITH_V4L', sources, '{module}/src/cap_v4l.cpp'.format(module = modulePath))
        sources = modulesToFilterFunctions.optionToSources('WITH_TYZX', sources, '{module}/src/cap_tyzx.cpp'.format(module = modulePath))
        sources = modulesToFilterFunctions.optionToSources('WITH_MIL', sources, '{module}/src/cap_mil.cpp'.format(module = modulePath))
	sources = modulesToFilterFunctions.optionToSources('WITH_IOS', sources, '{module}/src/cap_ios_abstract_camera.mm'.format(module = modulePath))
	sources = modulesToFilterFunctions.optionToSources('WITH_IOS', sources, '{module}/src/cap_ios_photo_camera.mm'.format(module = modulePath))
	sources = modulesToFilterFunctions.optionToSources('WITH_IOS', sources, '{module}/src/cap_ios_video_camera.mm'.format(module = modulePath))
	sources = modulesToFilterFunctions.optionToSources('WITH_QTKIT', sources, '{module}/src/cap_avfoundation.mm'.format(module = modulePath))
        # In order to support the following: add reference to their respective libs
        sources = modulesToFilterFunctions.optionToSources('WITH_ANDROID', sources, '{module}/src/cap_android.cpp'.format(module = modulePath))
        sources = modulesToFilterFunctions.optionToSources('WITH_CMU1394', sources, '{module}/src/cap_cmu.cpp'.format(module = modulePath))
        sources = modulesToFilterFunctions.optionToSources('WITH_DSHOW', sources, '{module}/src/cap_dshow.cpp'.format(module = modulePath))
        sources = modulesToFilterFunctions.optionToSources('WITH_FFMPEG', sources, '{module}/src/cap_ffmpeg.cpp'.format(module = modulePath))
        sources = modulesToFilterFunctions.optionToSources('WITH_FFMPEG', sources, '{module}/src/cap_ffmpeg_api.cpp'.format(module = modulePath))
        sources = modulesToFilterFunctions.optionToSources('WITH_FFMPEG', sources, '{module}/src/cap_ffmpeg.cpp'.format(module = modulePath))
        sources = modulesToFilterFunctions.optionToSources('WITH_FFMPEG', sources, '{module}/src/cap_ffmpeg_impl.cpp'.format(module = modulePath))
        sources = modulesToFilterFunctions.optionToSources('WITH_INTELPERC', sources, '{module}/src/cap_intelperc.cpp'.format(module = modulePath))
        sources = modulesToFilterFunctions.optionToSources('WITH_MSMF', sources, '{module}/src/cap_msmf.cpp'.format(module = modulePath))
        sources = modulesToFilterFunctions.optionToSources('WITH_OPENNI', sources, '{module}/src/cap_openni.cpp'.format(module = modulePath))
        sources = modulesToFilterFunctions.optionToSources('WITH_PVAPI', sources, '{module}/src/cap_pvapi.cpp'.format(module = modulePath))
        return sources,additionalIncludes,additionalLibs
    @staticmethod
    def videoio(env, sources, modulePath):
        additionalIncludes = list()
        additionalLibs = list()
        sources = modulesToFilterFunctions.optionToSources('WITH_XIMEA', sources, '{module}/src/cap_ximea.cpp'.format(module = modulePath))
        # TODO: Add ximea 32-bit lib if needed 
        additionalLibs.append('m3apiX64')
	sources = modulesToFilterFunctions.optionToSources('WITH_XINE', sources, '{module}/src/cap_xine.cpp'.format(module = modulePath))
	sources = modulesToFilterFunctions.optionToSources('WITH_1394-V1', sources, '{module}/src/cap_dc1394.cpp'.format(module = modulePath))
	sources = modulesToFilterFunctions.optionToSources('WITH_1394-V2', sources, '{module}/src/cap_dc1394_v2.cpp'.format(module = modulePath))
        sources = modulesToFilterFunctions.optionToSources('WITH_GIGEAPI', sources, '{module}/src/cap_giganetix.cpp'.format(module = modulePath))
        sources = modulesToFilterFunctions.optionToSources('WITH_VFW', sources, '{module}/src/cap_vfw.cpp'.format(module = modulePath))
            
        sources = modulesToFilterFunctions.optionToSources('WITH_UNICAP', sources, '{module}/src/cap_unicap.cpp'.format(module = modulePath))
        sources = modulesToFilterFunctions.optionToSources('WITH_QT', sources, '{module}/src/cap_qt.cpp'.format(module = modulePath))
        sources = modulesToFilterFunctions.optionToSources('WITH_QTKIT', sources, '{module}/src/cap_qtkit.mm'.format(module = modulePath))
	sources = modulesToFilterFunctions.optionToSources('WITH_LIBV4L', sources, '{module}/src/cap_libv4l.cpp'.format(module = modulePath))
        sources = modulesToFilterFunctions.optionToSources('WITH_V4L', sources, '{module}/src/cap_v4l.cpp'.format(module = modulePath))
        sources = modulesToFilterFunctions.optionToSources('WITH_TYZX', sources, '{module}/src/cap_tyzx.cpp'.format(module = modulePath))
        sources = modulesToFilterFunctions.optionToSources('WITH_MIL', sources, '{module}/src/cap_mil.cpp'.format(module = modulePath))
	sources = modulesToFilterFunctions.optionToSources('WITH_IOS', sources, '{module}/src/cap_ios_abstract_camera.mm'.format(module = modulePath))
	sources = modulesToFilterFunctions.optionToSources('WITH_IOS', sources, '{module}/src/cap_ios_photo_camera.mm'.format(module = modulePath))
	sources = modulesToFilterFunctions.optionToSources('WITH_IOS', sources, '{module}/src/cap_ios_video_camera.mm'.format(module = modulePath))
	sources = modulesToFilterFunctions.optionToSources('WITH_QTKIT', sources, '{module}/src/cap_avfoundation.mm'.format(module = modulePath))
        # In order to support the following: add reference to their respective libs
        sources = modulesToFilterFunctions.optionToSources('WITH_ANDROID', sources, '{module}/src/cap_android.cpp'.format(module = modulePath))
        sources = modulesToFilterFunctions.optionToSources('WITH_CMU1394', sources, '{module}/src/cap_cmu.cpp'.format(module = modulePath))
        sources = modulesToFilterFunctions.optionToSources('WITH_DSHOW', sources, '{module}/src/cap_dshow.cpp'.format(module = modulePath))
        sources = modulesToFilterFunctions.optionToSources('WITH_FFMPEG', sources, '{module}/src/cap_ffmpeg_api.cpp'.format(module = modulePath))
        sources = modulesToFilterFunctions.optionToSources('WITH_FFMPEG', sources, '{module}/src/cap_ffmpeg.cpp'.format(module = modulePath))
        sources = modulesToFilterFunctions.optionToSources('WITH_FFMPEG', sources, '{module}/src/cap_ffmpeg_impl.cpp'.format(module = modulePath))
        sources = modulesToFilterFunctions.optionToSources('WITH_INTELPERC', sources, '{module}/src/cap_intelperc.cpp'.format(module = modulePath))
        sources = modulesToFilterFunctions.optionToSources('WITH_MSMF', sources, '{module}/src/cap_msmf.cpp'.format(module = modulePath))
        sources = modulesToFilterFunctions.optionToSources('WITH_OPENNI', sources, '{module}/src/cap_openni.cpp'.format(module = modulePath))
        sources = modulesToFilterFunctions.optionToSources('WITH_PVAPI', sources, '{module}/src/cap_pvapi.cpp'.format(module = modulePath))
        if not ccmake['WITH_GSTREAMER'] and not ccmake['WITH_GSTREAMER_0_10']:
            sources = modulesToFilterFunctions.optionToSources('WITH_GSTREAMER', sources, '{module}/src/cap_gstreamer.cpp'.format(module = modulePath))
        else:
            if ccmake['WITH_GSTREAMER']:
                additionalIncludes.extend(findGstreamer())
            else:
                additionalIncludes.extend(findGstreamer010())
	    for includePath in opencvBuilderAdditionalIncludePaths:
            	additionalIncludes.append('{path}/glib-2.0'.format(path=includePath))
            	additionalIncludes.append('{path}/glib-2.0/include'.format(path=includePath))
        return sources,additionalIncludes,additionalLibs

    @staticmethod
    def nonfree(env, sources, modulePath):
        additionalIncludes = list()
        additionalLibs = list()
        additionalIncludes.append('../../3rdparty/include/opencl/1.2')
        return sources,additionalIncludes,additionalLibs
    @staticmethod
    def features2d(env, sources, modulePath):
        additionalIncludes = list()
        additionalLibs = list()
        sources.extend(opencvBuilderUtils.getFilesInFolder(env,'{module}/src/akaze'.format(module = modulePath), '*.c'))
        sources.extend(opencvBuilderUtils.getFilesInFolder(env,'{module}/src/kaze'.format(module = modulePath), '*.c'))
        return sources,additionalIncludes,additionalLibs
    @staticmethod
    def imgcodecs(env, sources, modulePath):
        additionalIncludes = list()
        additionalLibs = list()
	sources = modulesToFilterFunctions.optionToSources('WITH_IOS', sources, '{module}/src/ios_conversions.mm'.format(module = modulePath))
        if ccmake['BUILD_JPEG']:
            additionalIncludes.append('{modulePath}/../../3rdparty/libjpeg'.format(modulePath = modulePath))
        return sources,additionalIncludes,additionalLibs

def findGstreamer():
    paths = []
    for includePath in opencvBuilderAdditionalIncludePaths:
	paths.append('{path}/gstreamer-1.0'.format(path=includePath))
    return paths

def findGstreamer010():
    paths = []
    for includePath in opencvBuilderAdditionalIncludePaths:
	paths.append('{path}/gstreamer-0.10'.format(path=includePath))
    return paths

def findGtkGeneral():
    paths = []
    for includePath in opencvBuilderAdditionalIncludePaths:
	paths.append('{path}/cairo'.format(path=includePath))
	paths.append('{path}/pango-1.0'.format(path=includePath))
	paths.append('{path}/gdk-pixbuf-2.0'.format(path=includePath))
	paths.append('{path}/atk-1.0'.format(path=includePath))
        paths.append('{path}/glib-2.0'.format(path=includePath))
        paths.append('{path}/glib-2.0/include'.format(path=includePath))
    return paths

def findGtk2():
    paths = []
    for includePath in opencvBuilderAdditionalIncludePaths:
	paths.append('{path}/gtk-2.0'.format(path=includePath))
	paths.append('{path}/gtk-2.0/include'.format(path=includePath))
    paths.extend(findGtkGeneral())
    return paths

def findGtk3():
    paths = []
    for includePath in opencvBuilderAdditionalIncludePaths:
	paths.append('{path}/gtk-3.0'.format(path=includePath))
    paths.extend(findGtkGeneral())
    return paths

modulesToFilter = {
        'highgui' : modulesToFilterFunctions.highgui,
        'nonfree' : modulesToFilterFunctions.nonfree,
        'features2d'    : modulesToFilterFunctions.features2d,
        'imgcodecs' : modulesToFilterFunctions.imgcodecs,
        'videoio'   : modulesToFilterFunctions.videoio
}

class getAdditionalLibsFunctions(object):
    @staticmethod
    def core():
        libs = []
	frameworks=[]
        if ccmake['WITH_JPEG']:
            libs.extend([
                'libjpeg'
                ])
        if ccmake['BUILD_ZLIB']:
            libs.extend([
                'zlib'
                ])
        return libs, frameworks
    @staticmethod
    def highgui():
        libs = []
	frameworks = []
        frameworks.append('-pthread')
        if ccmake['WITH_GTK_2_X']:
            libs.extend([
		'gtk-x11-2.0',
		'gdk-x11-2.0',
                ])

        if ccmake['WITH_GTK']:
            libs.extend([
                'gtkmm-3.0',
                'gtk-3',
                'gdkmm-3.0',
                'gdk-3',
                ])
        if ccmake['WITH_GTK_2_X'] or ccmake['WITH_GTK']:
            libs.extend([
		'cairo',
		'gdk_pixbuf-2.0',
		'gobject-2.0',
		'glib-2.0'
                ])
        if ccmake['WITH_FFMPEG']:
            libs.extend([
		'avformat',
		'avcodec',
		'avutil',
		'swscale'
                ])
        if ccmake['WITH_LIBV4L'] or ccmake['WITH_V4L']:
            libs.extend([
		'v4l2',
		'v4l1',
                ])
	if ccmake['WITH_1394-V2'] or ccmake['WITH_1394-V1']:
            libs.extend([
		'dc1394',
                ])
	if ccmake['WITH_GSTREAMER']:
	    libs.extend([
		'gstreamer-1.0',
		'gstapp-1.0',
		'gstpbutils-1.0',
		'gstriff-1.0',
		'gobject-2.0',
		'glib-2.0'
                ])
	if ccmake['WITH_COCOA']:
	    frameworks.extend([
		'-framework', 'Cocoa'
		])
	if ccmake['WITH_QTKIT']:
	    frameworks.extend([
		'-framework', 'QTKit',
		'-framework', 'CoreVideo',
		])
        return libs,frameworks

getAdditionalLibs = {
        'core' : getAdditionalLibsFunctions.core,
        'highgui' : getAdditionalLibsFunctions.highgui,
}

def getDefinesAndCompileOptions():
    defines = ['__OPENCV_BUILD', 'OPENCV_NOSTL']
    options = ['-fPIC', '-static']
    if ccmake['ENABLE_SSE']:
        options.append('-msse')
    if ccmake['ENABLE_SSE2']:
        options.append('-msse2')
    if ccmake['ENABLE_SSE3']:
        options.append('-msse3')
    if not ccmake['BUILD_WITH_DEBUG_INFO']:
        defines.append('NDEBUG')
    if ccmake['ENABLE_OMIT_POINTER_FRAME']:
        options.append('-fomit-frame-pointer')
    if ccmake['WITH_GTK']:
        defines.append('GTK_MAJOR_VERSION=3')
    return defines,options

configFile = 'cvconfig.h'

class moduleToEmitterValuesFunctions:
    @staticmethod
    def getDefaultIncludePath(module, filename):
        defaultPath = 'opencv/modules/{module}/include/opencv2'.format(module = module)
        return ['{path}/{filename}'.format(path = defaultPath, filename = filename), '{path}/{module}/{filename}'.format(module = module, filename = filename, path = defaultPath)]
    @staticmethod
    def defaultAction(moduleName):
        sourceList = moduleToEmitterValuesFunctions.getDefaultIncludePath(moduleName, '{module}.hpp'.format(module = moduleName))
        targetList = ['opencv_{module}'.format(module = moduleName)]
        return sourceList,targetList

moduleToEmitterValues = {
    'default' : moduleToEmitterValuesFunctions.defaultAction
}

class moduleToAdditionalHeadersFunctions:
    @staticmethod
    def getDefaultIncludePath(module, filename = ''):
        defaultPath = 'opencv/modules/{module}/include/opencv2/{module}'.format(module = module)
        return '{path}/{filename}'.format(path = defaultPath, filename = filename)
    @staticmethod
    def defaultAdditionalHeaderFunctions(moduleName, env):
        defaultPath = moduleToAdditionalHeadersFunctions.getDefaultIncludePath(moduleName)
        return opencvBuilderUtils.getFilesInFolder(env,defaultPath,opencvBuilderUtils.headerExtensions)
    @staticmethod
    def core(moduleName, env):
        # Collect the default headers
        defaultHeaders = moduleToAdditionalHeadersFunctions.defaultAdditionalHeaderFunctions(moduleName, env)

        # Add opencl ones
        defaultPath = moduleToAdditionalHeadersFunctions.getDefaultIncludePath(moduleName)
        openclFolderHeaders = (opencvBuilderUtils.getFilesInFolder(env, '{defaultPath}/opencl'.format(defaultPath = defaultPath), opencvBuilderUtils.headerExtensions))
        env.Install('{includeDir}/opencv2/{module}/opencl'.format(module = moduleName, includeDir = env['OPENCVBUILDER_INCLUDE_DIR']), openclFolderHeaders)
        openclRuntimeHeaders = (opencvBuilderUtils.getFilesInFolder(env, '{defaultPath}/opencl/runtime'.format(defaultPath = defaultPath), opencvBuilderUtils.headerExtensions))
        env.Install('{includeDir}/opencv2/{module}/opencl/runtime'.format(module = moduleName, includeDir = env['OPENCVBUILDER_INCLUDE_DIR']), openclRuntimeHeaders)
        return defaultHeaders

moduleToAdditionalHeaders = {
        'default' : moduleToAdditionalHeadersFunctions.defaultAdditionalHeaderFunctions,
        'core' : moduleToAdditionalHeadersFunctions.core
}
