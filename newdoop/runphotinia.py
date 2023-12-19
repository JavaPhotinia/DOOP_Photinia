import os, sys, shutil, subprocess, time
BENCHMARKS = ['FEBSShiro','ForestBlog','SpringBlog','pybbs','mall-admin','mall-search','mall-portal','My-Blog','jeesite','shopizer','halo','jeecg','vhr','Vblog','SpringBlade','MCMS','WebGoat8','ruoyi','favorites-web','FEBS-auth','FEBS-system','eladmin','newbee','opsli']
# BENCHMARKS = ['WebGoat8', 'jeecg','MCMS']
# BENCHMARKS = ['MCMS', 'SpringBlade']
# BENCHMARKS = ['shopizer']
# BENCHMARKS = ['My-Blog','favorites-web','WebGoat8','FEBSShiro']
# BENCHMARKS = ['FEBSShiro','ForestBlog','SpringBlog','pybbs','mall-admin','mall-search','mall-portal','My-Blog','jeesite','halo','jeecg','vhr','Vblog','SpringBlade','MCMS','WebGoat','ruoyi','favorites-web','FEBS-auth','FEBS-system']
BASICOPTIONS = ['-Xmx128g',]

APPPATH = {
    'FEBSShiro': '/root/Benchmarks/src/FEBSShiro/',
    'ForestBlog': '/root/Benchmarks/src/ForestBlog/',
    'SpringBlog': '/root/Benchmarks/src/SpringBlog/',
    'pybbs': '/root/Benchmarks/src/pybbs/', 
    'mall-admin': '/root/Benchmarks/src/malladmin/',
    'mall-demo': '/root/Benchmarks/src/malldemo/', 
    'mall-search': '/root/Benchmarks/src/mallsearch/', 
    'mall-portal': '/root/Benchmarks/src/mallportal/', 
    'My-Blog': '/root/Benchmarks/src/MyBolg/', 
    'jeesite': '/root/Benchmarks/src/jeesite/', 
    'shopizer': '/root/Benchmarks/src/shopizer/', 
    'halo': '/root/Benchmarks/src/halo/', 
    'jeecg': '/root/Benchmarks/src/jeecg/', 
    'vhr': '/root/Benchmarks/src/vhr/', 
    'Vblog': '/root/Benchmarks/src/Vblog/', 
    'SpringBlade': '/root/Benchmarks/src/SpringBlade/', 
    'MCMS': '/root/Benchmarks/src/MCMS/', 
    'WebGoat8': '/root/Benchmarks/src/WebGoat8/', 
    'ruoyi':'/root/Benchmarks/src/ruoyi/',
    'favorites-web':'/root/Benchmarks/src/favoritesweb/',
    'FEBS-auth':'/root/Benchmarks/src/febs-auth/',
    'FEBS-system':'/root/Benchmarks/src/febs-system/',
    'eladmin':'/root/Benchmarks/src/eladmin/',
    'newbee':'/root/Benchmarks/src/newbee-mall/',
    'opsli':'/root/Benchmarks/src/opsli/'
}

LIBPATH = {
    'FEBSShiro': '/root/Benchmarks/libs/FEBS-Shiro/lib/',
    'ForestBlog': '/root/Benchmarks/libs/ForestBlog/lib/',
    'SpringBlog': '/root/Benchmarks/libs/SpringBlog/lib/',
    'pybbs': '/root/Benchmarks/libs/pybbs/lib/', 
    'mall-admin': '/root/Benchmarks/libs/mall-admin/lib/', 
    'mall-search': '/root/Benchmarks/libs/mall-search/lib/', 
    'mall-portal': '/root/Benchmarks/libs/mall-protal/lib/', 
    'My-Blog': '/root/Benchmarks/libs/My-Blog/lib/', 
    'jeesite': '/root/Benchmarks/libs/jeesite/lib/', 
    'shopizer': '/root/Benchmarks/libs/shopizer/lib-provided2/', 
    'halo': '/root/Benchmarks/libs/halo/lib/', 
    'jeecg': '/root/Benchmarks/libs/jeecg/lib-jeecg/', 
    'vhr': '/root/Benchmarks/libs/vhr/lib/', 
    'Vblog': '/root/Benchmarks/libs/Vblog/lib/', 
    'SpringBlade': '/root/Benchmarks/libs/SpringBlade/lib/', 
    'MCMS': '/root/Benchmarks/libs/MCMS/lib-MCMS/', 
    'WebGoat8': '/root/Benchmarks/libs/WebGoat8/lib/',
    'ruoyi':'/root/Benchmarks/libs/ruoyi/lib/',
    'favorites-web':'/root/Benchmarks/libs/favoritesweb/lib/',
    'FEBS-auth':'/root/Benchmarks/libs/febs-auth/lib/',
    'FEBS-system':'/root/Benchmarks/libs/febs-system/lib/',
    'eladmin':'/root/Benchmarks/libs/eladmin/lib/',
    'newbee':'/root/Benchmarks/libs/newbee-mall/lib/',
    'opsli':'/root/Benchmarks/libs/opsli/lib/'
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
