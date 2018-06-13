from fabric.api import *
import os

env.hosts = ['chicagolx.webfactional.com']
env.user = 'chicagolx'
env.remotepath = '/home/chicagolx/webapps/clx_splash'
env.git_branch = 'master'
env.warn_only = True

def production():
  env.hosts = ['chicagolx.webfactional.com']
  env.user = 'chicagolx'
  env.remotepath = '/home/chicagolx/webapps/clx_splash'

def assets():
  local('npx gulp --production')

def devsetup():
  print "Installing composer, node and bower assets...\n"
  local('npm install')
  local('cd assets && bower install')
  local('npx gulp')

def deploy():
  update()
  # composer_install()

def update():
  with cd(env.remotepath):
    run('git pull origin {0}'.format(env.git_branch))

def composer_install():
  with cd(env.remotepath):
    run('~/bin/composer install')
