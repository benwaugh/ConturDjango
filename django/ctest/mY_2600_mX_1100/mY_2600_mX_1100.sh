source /unix/cedar/software/sl6/Herwig-Tip/setupEnv.sh; cd /home/npart/bitbucket/conturtest/ctest/mY_2600_mX_1100; source /home/npart/bitbucket/conturtest/setupContur.sh; Herwig run --seed=26001100 --tag=mY_2600_mX_1100 --jobs=2 --numevents=15000 LHC.run;