source /unix/cedar/software/sl6/Herwig-Tip/setupEnv.sh; cd /home/npart/bitbucket/conturtest/ctest/mY_1600_mX_600; source /home/npart/bitbucket/conturtest/setupContur.sh; Herwig run --seed=1600600 --tag=mY_1600_mX_600 --jobs=2 --numevents=15000 LHC.run;