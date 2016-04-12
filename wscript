import string

top = '.'
out = 'build'
APPNAME = 'falltergeist'
VERSION = '0.3.0'

def options(opt):
    opt.load('compiler_cxx')

def configure(cfg):
    cfg.check_waf_version(mini='1.8.20')
    cfg.load('compiler_cxx')
    cfg.parse_flags('-std=c++11 -g -Wall', 'DEBUG')
    cfg.parse_flags('-std=c++11 -O2 -s, -Wall', 'RELEASE')
    cfg.env.INCLUDES_GLM = ['/usr/include/glm/glm.h']
    cfg.check_cfg(package='sdl2', args='--libs --cflags', uselib_store='SDL2')
    cfg.check_cfg(package='SDL2_image', args='--libs --cflags', uselib_store='SDL2_IMAGE')
    cfg.check_cfg(package='SDL2_mixer', args='--libs --cflags', uselib_store='SDL2_MIXER')
    cfg.check_cfg(package='zlib', args='--libs --cflags', uselib_store='ZLIB')
    cfg.check_cfg(package='glew', args='--libs --cflags', uselib_store='GLEW')
    cfg.check(features='cxx cxxprogram', header_name=['glm/glm.hpp'], uselib_store='GLM', mandatory=True)
    cfg.check(features='cxx cxxprogram', lib=['GL'], uselib_store='OPENGL', mandatory=True)
    cfg.env.SYSTEM_DEPS = ['SDL2', 'SDL2_IMAGE', 'SDL2_MIXER', 'ZLIB', 'GLEW', 'OPENGL']
    cfg.env.BUILD_TYPE = ['DEBUG']
    
def build(bld):
    wscripts = [x.parent.abspath() for x in bld.path.ant_glob('*/**/wscript')]
    bld.recurse(wscripts)
