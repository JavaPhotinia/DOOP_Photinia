import os, sys, shutil, subprocess, time
# BENCHMARKS = ['mall-admin','mall-search','mall-portal', 'vhr','Vblog','FEBS-auth','My-Blog','SpringBlade','ruoyi','pybbs','newbee','WebGoat8', 'jeecg','MCMS']
# BENCHMARKS = ['WebGoat8', 'jeecg','MCMS']
BENCHMARKS = ['MCMS', 'SpringBlade']
# BENCHMARKS = ['shopizer']
# BENCHMARKS = ['My-Blog','favorites-web','WebGoat8','FEBSShiro']
# BENCHMARKS = ['FEBSShiro','ForestBlog','SpringBlog','pybbs','mall-admin','mall-search','mall-portal','My-Blog','jeesite','halo','jeecg','vhr','Vblog','SpringBlade','MCMS','WebGoat','ruoyi','favorites-web','FEBS-auth','FEBS-system']
BASICOPTIONS = ['-Xmx128g',]

APPPATH = {
    'FEBSShiro': '/root/0610newtest/src/FEBSShiro/',
    'ForestBlog': '/root/0610newtest/src/ForestBlog/',
    'SpringBlog': '/root/0610newtest/src/SpringBlog/',
    'pybbs': '/root/0610newtest/src/pybbs/', 
    'mall-admin': '/root/0610newtest/src/malladmin/',
    'mall-demo': '/root/0610newtest/src/malldemo/', 
    'mall-search': '/root/0610newtest/src/mallsearch/', 
    'mall-portal': '/root/0610newtest/src/mallportal/', 
    'My-Blog': '/root/0610newtest/src/MyBolg/', 
    'jeesite': '/root/0610newtest/src/jeesite/', 
    'shopizer': '/root/0610newtest/src/shopizer/', 
    'halo': '/root/0610newtest/src/halo/', 
    'jeecg': '/root/0610newtest/src/jeecg/', 
    'vhr': '/root/0610newtest/src/vhr/', 
    'Vblog': '/root/0610newtest/src/Vblog/', 
    'SpringBlade': '/root/0610newtest/src/SpringBlade/', 
    'MCMS': '/root/0610newtest/src/MCMS/', 
    'WebGoat8': '/root/0610newtest/src/WebGoat8/', 
    'ruoyi':'/root/0610newtest/src/ruoyi/',
    'favorites-web':'/root/0610newtest/src/favoritesweb/',
    'FEBS-auth':'/root/0610newtest/src/febs-auth/',
    'FEBS-system':'/root/0610newtest/src/febs-system/',
    'eladmin':'/root/0610newtest/src/eladmin/',
    'newbee':'/root/0610newtest/src/newbee-mall/',
    'opsli':'/root/0610newtest/src/opsli/'
}

LIBPATH = {
    'FEBSShiro': '/root/0610newtest/libs/FEBS-Shiro/lib/',
    'ForestBlog': '/root/0610newtest/libs/ForestBlog/lib/',
    'SpringBlog': '/root/0610newtest/libs/SpringBlog/lib/',
    'pybbs': '/root/0610newtest/libs/pybbs/lib/', 
    'mall-admin': '/root/0610newtest/libs/mall-admin/lib/', 
    'mall-search': '/root/0610newtest/libs/mall-search/lib/', 
    'mall-portal': '/root/0610newtest/libs/mall-protal/lib/', 
    'My-Blog': '/root/0610newtest/libs/My-Blog/lib/', 
    'jeesite': '/root/0610newtest/libs/jeesite/lib/', 
    'shopizer': '/root/0610newtest/libs/shopizer/lib-provided2/', 
    'halo': '/root/0610newtest/libs/halo/lib/', 
    'jeecg': '/root/0610newtest/libs/jeecg/lib-jeecg/', 
    'vhr': '/root/0610newtest/libs/vhr/lib/', 
    'Vblog': '/root/0610newtest/libs/Vblog/lib/', 
    'SpringBlade': '/root/0610newtest/libs/SpringBlade/lib/', 
    'MCMS': '/root/0610newtest/libs/MCMS/lib-MCMS/', 
    'WebGoat8': '/root/0610newtest/libs/WebGoat8/lib/',
    'ruoyi':'/root/0610newtest/libs/ruoyi/lib/',
    'favorites-web':'/root/0610newtest/libs/favoritesweb/lib/',
    'FEBS-auth':'/root/0610newtest/libs/febs-auth/lib/',
    'FEBS-system':'/root/0610newtest/libs/febs-system/lib/',
    'eladmin':'/root/0610newtest/libs/eladmin/lib/',
    'newbee':'/root/0610newtest/libs/newbee-mall/lib/',
    'opsli':'/root/0610newtest/libs/opsli/lib/'
}

def runPointsToAnalysis(args):
    runCommmand = args
    subprocess.run(runCommmand.split(' '), timeout=14400)

def getDoopCommand(analysis, bm, open_program):
    options = []
    options += ['-a', analysis]
    options += ['--id', "photinia"+bm]
    options += ['-i', APPPATH[bm]]
    options += ['-l', LIBPATH[bm]]
    options += ['--open-programs', open_program]
    options += ['--platform', 'java_8']
    options += ['--souffle-jobs', '60']
    options += ['--max-memory', '128g']
    options += ['-t', '3600']
    cmd = ' '.join(options)
    return cmd

def runAnalysis(analysis, bm, open_program):
    print('now running ' + analysis + ' and ' + open_program + ' for ' + bm)
    cmd = './doop ' + getDoopCommand(analysis, bm, open_program) 
    print(cmd)
    runPointsToAnalysis(cmd)

if __name__ == '__main__':
    benchmarks = BENCHMARKS
    analysis = 'context-insensitive'
    open_program = 'jasmine'
    for bm in benchmarks:
        runAnalysis(analysis, bm, open_program)
        time.sleep(120)
