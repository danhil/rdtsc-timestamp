#! /usr/bin/env python
# encoding: utf-8

VERSION='0.0.0'
APPNAME='dynamic-cast'

top = '.'
out = 'build'

def options(opt):
    opt.load('compiler_cxx')
    opt.load('gas')

def configure(conf):
    conf.load('compiler_cxx')
    conf.load('gas')
    conf.env.CXXFLAGS = ['-std=c++14', '-O3']

def build(bld):
    bld.objects(features='cxx asm',
        source = ['asm/rdtsc.s'],
        target = 'rdtsc')
    bld.program(source=['main.cpp'], use = ['rdtsc'], target='rdtsc_test')
