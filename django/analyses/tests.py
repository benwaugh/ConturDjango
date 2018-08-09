# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import models

from django.test import TestCase
from django.core.exceptions import ValidationError
import pickle
import os
from django.core.files import File
from PIL import Image, ImageDraw


class Test_Models(TestCase):

    # Tests for Pools
    def create_Pool(self,name="Test_Pool"):
        self.pool = models.AnalysisPool.objects.create(pool=name)
        return self.pool

    def test_pool_creation(self):
        instance = self.create_Pool()
        self.assertTrue(isinstance(instance, models.AnalysisPool))
        self.assertEqual(instance.__str__(), instance.pool)

    # Tests for Analysis Model
    def create_Analyses(self,pool, anaid="only a test", lumi=10):
        return models.Analysis.objects.create(anaid=anaid, lumi=lumi, pool=pool)

    def test_Analyses_creation(self):
        pool = self.create_Pool("Test_Pool")
        Ana_instance = self.create_Analyses(pool)
        # Check that instance is created correctly
        self.assertTrue(isinstance(Ana_instance,models.Analysis))
        # Check that instance has correct contents
        self.assertEqual(Ana_instance .__str__(), Ana_instance.anaid)

    def test_Analysis_creation_fail(self):
        with self.assertRaises(ValueError):
            self.create_Analyses("Pool String Instead of Pool Object")

    # Tests for Blacklist Model
    def create_Blacklist(self,anaid,pattern="test"):
        return models.Blacklist.objects.create(anaid=anaid,pattern=pattern)

    def test_Blacklist_creation(self):
        pool = self.create_Pool("Test_Pool")
        anaid = self.create_Analyses(pool)
        self.Blacklist_instance = self.create_Blacklist(anaid)
        # Check that instance is created correctly
        self.assertTrue(isinstance(self.Blacklist_instance, models.Blacklist))
        # Check that instance has correct contents
        self.assertEqual(self.Blacklist_instance.__str__(),
                         str(self.Blacklist_instance.anaid) + " " + str(self.Blacklist_instance.pattern))

    def test_Blacklist_creation_fails(self):
        with self.assertRaises(ValueError):
            self.Blacklist_instance = self.create_Blacklist("Analysis string Instead of Analysis Object")


    # Tests for Normalisation
    def create_Normalisation(self,anaid,pattern="test",norm=1.1,scalemc=1):
        return models.Normalization.objects.create(anaid=anaid,pattern=pattern,norm=norm,scalemc=scalemc)

    def test_Normalisation_creation(self):
        pool = self.create_Pool("Test_Pool")
        anaid = self.create_Analyses(pool)
        self.Normalisation_instance = self.create_Normalisation(anaid)
        # Check that instance is created correctly
        self.assertTrue(isinstance(self.Normalisation_instance, models.Normalization))
        # Check that instance has correct contents
        self.assertEqual(self.Normalisation_instance.__str__(),
                         str(self.Normalisation_instance.anaid) + " " + str(self.Normalisation_instance.pattern))

    def test_Normalisation_creation_fails1(self):
        with self.assertRaises(ValueError):
            self.Normalisation_instance = self.create_Normalisation("Analysis string Instead of Analysis Object")

    def test_Normalisation_creation_fails2(self):
        with self.assertRaises(ValueError):
            pool = self.create_Pool("Test_Pool")
            anaid = self.create_Analyses(pool)
            self.Normalisation_instance = self.create_Normalisation(anaid,norm="string")

    def test_Normalisation_creation_fails3(self):
        with self.assertRaises(ValueError):
            pool = self.create_Pool("Test_Pool")
            anaid = self.create_Analyses(pool)
            self.Normalisation_instance = self.create_Normalisation(anaid,scalemc="string")

    # Tests for subpool
    def create_Subpool(self,anaid,pattern="test",subanaid=1):
        return models.Subpool.objects.create(anaid=anaid,pattern=pattern,subanaid=subanaid)

    def test_Subpool_creation(self):
        pool = self.create_Pool("Test_Pool")
        anaid = self.create_Analyses(pool)
        self.Subpool_instance = self.create_Subpool(anaid)
        # Check that instance is created correctly
        self.assertTrue(isinstance(self.Subpool_instance, models.Subpool))
        # Check that instance has correct contents
        self.assertEqual(self.Subpool_instance.__str__(),
                         str(self.Subpool_instance.anaid) + " " + str(self.Subpool_instance.pattern))

    def test_Subpool_creation_fails(self):
        with self.assertRaises(ValueError):
            self.Subpool_instance = self.create_Subpool("Analysis string Instead of Analysis Object")

    # Tests for Whitelist Model
    def create_Whitelist(self,anaid,pattern="test"):
        return models.Whitelist.objects.create(anaid=anaid,pattern=pattern)

    def test_Whitelist_creation(self):
        pool = self.create_Pool("Test_Pool")
        anaid = self.create_Analyses(pool)
        self.Whitelist_instance = self.create_Whitelist(anaid)
        # Check that instance is created correctly
        self.assertTrue(isinstance(self.Whitelist_instance, models.Whitelist))
        # Check that instance has correct contents
        self.assertEqual(self.Whitelist_instance.__str__(),
                         str(self.Whitelist_instance.anaid) + " " + str(self.Whitelist_instance.pattern))

    def test_Whitelist_creation_fails(self):
        with self.assertRaises(ValueError):
            self.Whitelist_instance = self.create_Whitelist("Analysis string Instead of Analysis Object")


    # Tests for BSM_Model Model
    def create_BSM(self, date,name="Test_BSM",ufolink="TestLink",author="Test_Author"):
        self.bsm = models.BSM_Model.objects.create(name=name,UFO_Link=ufolink,author=author,date_downloaded=date)
        return self.bsm

    def test_bsm_creation(self):
        instance = self.create_BSM("1995-08-08")
        self.assertTrue(isinstance(instance, models.BSM_Model))
        self.assertEqual(instance.__str__(), instance.name)

    def test_BSM_creation_fails(self):
        with self.assertRaises(ValidationError):
            instance = self.create_BSM("Not a date")

    # Tests for ana_list Model
    def create_ana_list(self,ana_name="name",author="author"):
        self.ana_list = models.ana_list.objects.create(ana_name=ana_name, author=author)
        return self.ana_list

    def test_ana_list_creation(self):
        instance = self.create_ana_list()
        self.assertTrue(isinstance(instance, models.ana_list))
        self.assertEqual(instance.__str__(), instance.ana_name)

    # Tests for used_analyses Model
    def create_used_analyses(self,ana_list,bsm_model):
        self.used_ana = models.used_analyses.objects.create(ana_name=ana_list,modelname=bsm_model)
        return self.used_ana

    def test_used_analyses_creation(self):
        bsm = self.create_BSM("1995-08-08")
        ana_list = self.create_ana_list()
        instance = self.create_used_analyses(ana_list,bsm)
        self.assertTrue(isinstance(instance, models.used_analyses))
        self.assertEqual(instance.__str__(), instance.ana_name)

    def test_used_analyses_creation_fails1(self):
        bsm = self.create_BSM("1995-08-08")
        with self.assertRaises(ValueError):
            self.create_used_analyses("Not ana instance",bsm)

    def test_used_analyses_creation_fails2(self):
        ana_list = self.create_ana_list()
        with self.assertRaises(ValueError):
            self.create_used_analyses(ana_list,"Not bsm instance")

    # Tests for ana_file Model
    def create_ana_file(self,ana_list,anaid):
        self.ana_file = models.ana_file.objects.create(linked_ana=ana_list,anaid=anaid)
        return self.ana_file

    def test_ana_file_creation(self):
        pool = self.create_Pool("Test_Pool")
        Ana_instance = self.create_Analyses(pool)
        ana_list = self.create_ana_list()
        instance = self.create_ana_file(ana_list,Ana_instance)
        self.assertTrue(isinstance(instance, models.ana_file))
        self.assertEqual(instance.__str__(), str(instance.linked_ana) + "-" + str(instance.anaid))

    def test_ana_file_creation_fails1(self):
        pool = self.create_Pool("Test_Pool")
        Ana_instance = self.create_Analyses(pool)
        with self.assertRaises(ValueError):
            self.create_ana_file("Not ana list instance",Ana_instance)

    def test_ana_file_creation_fails2(self):
        ana_list = self.create_ana_list()
        with self.assertRaises(ValueError):
            self.create_ana_file(ana_list,"Not ana instance")

    # Tests for Runcard model
    def create_Runcard(self,modelname,author="author",runcard_name="runcard_name",param_card="params"):
        return models.runcard.objects.create(author=author,runcard_name=runcard_name,param_card=param_card,
                                             modelname=modelname)

    def test_Runcard_creation(self):
        model = self.create_BSM("1995-08-08")
        self.Runcard_instance = self.create_Runcard(model)
        # Check that instance is created correctly
        self.assertTrue(isinstance(self.Runcard_instance, models.runcard))
        # Check that instance has correct contents
        self.assertEqual(self.Runcard_instance.__str__(),self.Runcard_instance.runcard_name)

    def test_Runcard_creation_fails1(self):
        with self.assertRaises(ValueError):
            self.Runcard_instance = self.create_Runcard("string Instead of BSM Object")

    # Tests for Results header model
    def create_Results_header(self,runcard,author="author",name="name",mc_ver="0",contur_ver="0"):
        return models.results_header.objects.create(runcard=runcard,author=author,name=name,mc_ver=mc_ver,
                                                    contur_ver=contur_ver)

    def test_Results_header_creation(self):
        model = self.create_BSM("1995-08-08")
        runcard = self.create_Runcard(model)
        self.rh_instance = self.create_Results_header(runcard)
        # Check that instance is created correctly
        self.assertTrue(isinstance(self.rh_instance, models.results_header))
        # Check that instance has correct contents
        self.assertEqual(self.rh_instance.__str__(), self.rh_instance.name)

    def test_Results_header_creation_fails1(self):
        with self.assertRaises(ValueError):
            self.rh_instance = self.create_Results_header("string Instead of Runcard Object")


    # Tests for Results header model
    def create_Results_position(self, parent,name="name_1002010"):
        return models.results_position.objects.create(name=name, parent=parent)

    def test_Results_position_creation(self):
        model = self.create_BSM("1995-08-08")
        runcard = self.create_Runcard(model)
        results_header = self.create_Results_header(runcard)
        self.rp_instance = self.create_Results_position(results_header)
        # Check that instance is created correctly
        self.assertTrue(isinstance(self.rp_instance, models.results_position))
        # Check that instance has correct contents
        self.assertEqual(self.rp_instance.__str__(), self.rp_instance.name)

    def test_Results_position_creation_fails1(self):
        with self.assertRaises(ValueError):
            self.rp_instance = self.create_Results_position("string Instead of Results Header Object")

    def test_non_unique_position_names(self):
        try:
            model = self.create_BSM("1995-08-08")
            runcard = self.create_Runcard(model)

            results_header = self.create_Results_header(runcard)
            self.rp_instance = self.create_Results_position(results_header)

            self.rp_instance = self.create_Results_position(results_header)
        except:
            self.fail("Does not allow repeated position names [This is required]")

    # Tests for Results_analyses model
    def create_Results_analyses(self, parent,name="name",xyd="xyd",Path="Path",Title="Title",Type="Type",
                                XLabel="XLabel",YLabel="YLabel",ScaledBy=1,PolyMarker="PM",
                                ErrorBars="EB",LineColor="LC",yodamerge_scale="YS",mean=1,area=1):
        return models.results_analyses.objects.create(name=name, parent=parent,xyd=xyd,Path=Path,Title=Title,
                                                      Type=Type,XLabel=XLabel,YLabel=YLabel,ScaledBy=ScaledBy,
                                                      PolyMarker=PolyMarker,ErrorBars=ErrorBars,LineColor=LineColor,
                                                      yodamerge_scale=yodamerge_scale,mean=mean,area=area)
    def test_Results_analyses_creation(self):
        model = self.create_BSM("1995-08-08")
        runcard = self.create_Runcard(model)
        results_header = self.create_Results_header(runcard)
        rp = self.create_Results_position(results_header)
        self.ra_instance = self.create_Results_analyses(rp)

        # Check that instance is created correctly
        self.assertTrue(isinstance(self.ra_instance, models.results_analyses))
        # Check that instance has correct contents
        self.assertEqual(self.ra_instance.__str__(), self.ra_instance.name)

    def create_Results_analyses_null(self, parent,name="name2",xyd=None,Path=None,Title=None,Type=None,
                                XLabel=None,YLabel=None,ScaledBy=None,PolyMarker=None,
                                ErrorBars=None,LineColor=None,yodamerge_scale=None,mean=None,area=None):
        return models.results_analyses.objects.create(name=name, parent=parent,xyd=xyd,Path=Path,Title=Title,
                                                      Type=Type,XLabel=XLabel,YLabel=YLabel,ScaledBy=ScaledBy,
                                                      PolyMarker=PolyMarker,ErrorBars=ErrorBars,LineColor=LineColor,
                                                      yodamerge_scale=yodamerge_scale,mean=mean,area=area)

    def test_Results_analyses_null_creation(self):
        model = self.create_BSM("1995-08-08")
        runcard = self.create_Runcard(model)
        results_header = self.create_Results_header(runcard)
        rp = self.create_Results_position(results_header)
        self.ra_instance = self.create_Results_analyses_null(rp)

        # Check that instance is created correctly
        self.assertTrue(isinstance(self.ra_instance, models.results_analyses))
        # Check that instance has correct contents
        self.assertEqual(self.ra_instance.__str__(), self.ra_instance.name)

    def test_Results_analyses_creation_fails1(self):
        with self.assertRaises(ValueError):
            self.rp_instance = self.create_Results_position("string Instead of results position Object")

    # Tests for Scatter3D model
    def create_scatter3D(self, parent, xval=1.0,xerr_n=1.0,xerr_p=1.0,yval=1.0,yerr_n=1.0,yerr_p=1.0,
                         zval=1.0,zerr_n=1.0,zerr_p=1.0):
        return models.scatter3_data.objects.create(parent=parent,xval=xval,xerr_n=xerr_n,xerr_p=xerr_p,yval=yval,
                                                   yerr_n=yerr_n,yerr_p=yerr_p,zval=zval,zerr_n=zerr_n,zerr_p=zerr_p)

    def test_Scatter3D_creation(self):
        model = self.create_BSM("1995-08-08")
        runcard = self.create_Runcard(model)
        results_header = self.create_Results_header(runcard)
        rp = self.create_Results_position(results_header)
        ra = self.create_Results_analyses(rp)
        self.s3d = self.create_scatter3D(ra)

        # Check that instance is created correctly
        self.assertTrue(isinstance(self.s3d, models.scatter3_data))

    # Tests for Scatter2D model
    def create_scatter2D(self, parent, xval=1.0,xerr_n=1.0,xerr_p=1.0,yval=1.0,yerr_n=1.0,yerr_p=1.0):
        return models.scatter2_data.objects.create(parent=parent,xval=xval,xerr_n=xerr_n,xerr_p=xerr_p,yval=yval,
                                                   yerr_n=yerr_n,yerr_p=yerr_p)

    def test_Scatter2D_creation(self):
        model = self.create_BSM("1995-08-08")
        runcard = self.create_Runcard(model)
        results_header = self.create_Results_header(runcard)
        rp = self.create_Results_position(results_header)
        ra = self.create_Results_analyses(rp)
        self.s2d = self.create_scatter2D(ra)

        # Check that instance is created correctly
        self.assertTrue(isinstance(self.s2d, models.scatter2_data))

    # Tests for Scatter1D model
    def create_scatter1D(self, parent, xval=1.0,xerr_n=1.0,xerr_p=1.0):
        return models.scatter1_data.objects.create(parent=parent,xval=xval,xerr_n=xerr_n,xerr_p=xerr_p)

    def test_Scatter1D_creation(self):
        model = self.create_BSM("1995-08-08")
        runcard = self.create_Runcard(model)
        results_header = self.create_Results_header(runcard)
        rp = self.create_Results_position(results_header)
        ra = self.create_Results_analyses(rp)
        self.s1d = self.create_scatter1D(ra)

        # Check that instance is created correctly
        self.assertTrue(isinstance(self.s1d, models.scatter1_data))

    # Tests for Histo1D model
    def create_Histo1D(self, parent, xlow=1.0,xhigh=1.0,sumw=1.0,sumw2=1.0,sumwx=1.0,sumwx2=1.0,numEntries=1):
        return models.histo1_data.objects.create(parent=parent,xlow=xlow,xhigh=xhigh,sumw=sumw,sumw2=sumw2,
                                                 sumwx=sumwx,sumwx2=sumwx2,numEntries=numEntries)

    def test_Histo1D_creation(self):
        model = self.create_BSM("1995-08-08")
        runcard = self.create_Runcard(model)
        results_header = self.create_Results_header(runcard)
        rp = self.create_Results_position(results_header)
        ra = self.create_Results_analyses(rp)
        self.h1d = self.create_Histo1D(ra)

        # Check that instance is created correctly
        self.assertTrue(isinstance(self.h1d, models.histo1_data))



    # Tests for Profile1D model
    def create_Profile1D(self, parent, xlow=1.0,xhigh=1.0,sumw=1.0,sumw2=1.0,sumwx=1.0,sumwx2=1.0,sumwy=1.0,
                       sumwy2=1.0,numEntries=1):
        return models.profile1_data.objects.create(parent=parent,xlow=xlow,xhigh=xhigh,sumw=sumw,sumw2=sumw2,
                                                 sumwx=sumwx,sumwx2=sumwx2,sumwy=sumwy,sumwy2=sumwy2,
                                                 numEntries=numEntries)

    def test_Profile1D_creation(self):
        model = self.create_BSM("1995-08-08")
        runcard = self.create_Runcard(model)
        results_header = self.create_Results_header(runcard)
        rp = self.create_Results_position(results_header)
        ra = self.create_Results_analyses(rp)
        self.p1d = self.create_Profile1D(ra)

        # Check that instance is created correctly
        self.assertTrue(isinstance(self.p1d, models.profile1_data))


    # Tests for Overflow/Underflow Profile model
    def create_oup(self, parent,row_type="rowtype",sumw=1.0,sumw2=1.0,sumwx=1.0,sumwx2=1.0,sumwy=1.0,
                       sumwy2=1.0,numEntries=1):
        return models.overflow_underflow_profile.objects.create(parent=parent,sumw=sumw,sumw2=sumw2,
                                                 sumwx=sumwx,sumwx2=sumwx2,sumwy=sumwy,sumwy2=sumwy2,
                                                 numEntries=numEntries,row_type=row_type)

    def test_oup_creation(self):
        model = self.create_BSM("1995-08-08")
        runcard = self.create_Runcard(model)
        results_header = self.create_Results_header(runcard)
        rp = self.create_Results_position(results_header)
        ra = self.create_Results_analyses(rp)
        self.oup = self.create_oup(ra)

        # Check that instance is created correctly
        self.assertTrue(isinstance(self.oup, models.overflow_underflow_profile))

    # Tests for Overflow/Underflow Profile model
    def create_ouh(self, parent,row_type="rowtype",sumw=1.0,sumw2=1.0,sumwx=1.0,sumwx2=1.0,numEntries=1):
        return models.overflow_underflow_histo.objects.create(parent=parent,sumw=sumw,sumw2=sumw2,
                                                 sumwx=sumwx,sumwx2=sumwx2,numEntries=numEntries,row_type=row_type)

    def test_ouh_creation(self):
        model = self.create_BSM("1995-08-08")
        runcard = self.create_Runcard(model)
        results_header = self.create_Results_header(runcard)
        rp = self.create_Results_position(results_header)
        ra = self.create_Results_analyses(rp)
        self.ouh = self.create_ouh(ra)

        # Check that instance is created correctly
        self.assertTrue(isinstance(self.ouh, models.overflow_underflow_histo))

    # Tests for counter model
    def create_counter(self, parent,sumw=1.0,sumw2=1.0,numEntries=1):
        return models.counter.objects.create(parent=parent,sumw=sumw,sumw2=sumw2,numEntries=numEntries)

    def test_counter_creation(self):
        model = self.create_BSM("1995-08-08")
        runcard = self.create_Runcard(model)
        results_header = self.create_Results_header(runcard)
        rp = self.create_Results_position(results_header)
        ra = self.create_Results_analyses(rp)
        self.counter = self.create_counter(ra)

        # Check that instance is created correctly
        self.assertTrue(isinstance(self.counter, models.counter))

    # Tests for Results header model
    def create_map_header(self, parent,name="name_1002010"):
        return models.map_header.objects.create(analyses=name, parent=parent)

    def test_map_header_creation(self):
        model = self.create_BSM("1995-08-08")
        runcard = self.create_Runcard(model)
        results_header = self.create_Results_header(runcard)
        self.mh_instance = self.create_map_header(results_header)
        # Check that instance is created correctly
        self.assertTrue(isinstance(self.mh_instance, models.map_header))
        # Check that instance has correct contents
        self.assertEqual(self.mh_instance.__str__(), self.mh_instance.analyses)


    # Tests for map pickle model
    def create_map_pickle(self, parent,pickle):
        return models.map_pickle.objects.create(parent=parent,pickle=pickle)

    def test_map_pickle_creation(self):
        model = self.create_BSM("1995-08-08")
        runcard = self.create_Runcard(model)
        results_header = self.create_Results_header(runcard)
        mh = self.create_map_header(results_header)

        data = dict()
        data['Test'] = 'This is for testing Pickle'

        pickle.dump(data,open( "Pickle_Test_Fixture.map", "wb" ))

        pickle_val = pickle.load( open( "Pickle_Test_Fixture.map", "rb" ) )
        os.remove("Pickle_Test_Fixture.map")

        self.mp_instance = self.create_map_pickle(mh,pickle_val)
        # Check that instance is created correctly
        self.assertTrue(isinstance(self.mp_instance, models.map_pickle))
        # Check that instance has correct contents
        self.assertEqual(self.mp_instance.__str__(), self.mp_instance._check_id_field)

    def test_map_pickle_creation_fails1(self):

        data = dict()
        data['Test'] = 'This is for testing Pickle'

        pickle.dump(data, open("Pickle_Test_Fixture.map", "wb"))

        pickle_val = pickle.load(open("Pickle_Test_Fixture.map", "rb"))
        os.remove("Pickle_Test_Fixture.map")

        with self.assertRaises(ValueError):
            self.mp_instance = self.create_map_pickle("Not map header", pickle_val)

    # Tests for dat_database model
    def create_dat_database(self, parent, date):
        return models.dat_database.objects.create(results_object=parent, uploaded=date)

    def test_dat_database_creation(self):
        model = self.create_BSM("1995-08-08")
        runcard = self.create_Runcard(model)
        results_header = self.create_Results_header(runcard)
        rp = self.create_Results_position(results_header)

        self.dd_instance = self.create_dat_database(rp, "1995-08-08")
        # Check that instance is created correctly
        self.assertTrue(isinstance(self.dd_instance, models.dat_database))
        # Check that instance has correct contents
        self.assertEqual(self.dd_instance.__str__(), self.dd_instance._check_id_field)

    def test_dat_database_creation_fails1(self):
        with self.assertRaises(ValueError):
            self.mp_instance = self.create_dat_database("Not map header", "1995-08-08")

    def test_dat_database_creation_fails2(self):
        model = self.create_BSM("1995-08-08")
        runcard = self.create_Runcard(model)
        results_header = self.create_Results_header(runcard)
        rp = self.create_Results_position(results_header)
        with self.assertRaises(ValidationError):
            self.mp_instance = self.create_dat_database(rp, "Not date format")

    # Tests for summary_text model
    def create_summary_text(self, parent, file):
        return models.summary_text.objects.create(parent=parent, summary_store=file)

    def test_summary_text_creation(self):
        model = self.create_BSM("1995-08-08")
        runcard = self.create_Runcard(model)
        results_header = self.create_Results_header(runcard)
        rp = self.create_Results_position(results_header)
        dd = self.create_dat_database(rp, "1995-08-08")

        with open('test_summary.txt', 'w') as f:
            f.write('Test Contents')

        file = File(open("test_summary.txt",'w+'))

        self.summary_instance = self.create_summary_text(dd,file)

        # Check that instance is created correctly
        self.assertTrue(isinstance(self.summary_instance, models.summary_text))
        # Check that instance has correct contents
        self.assertEqual(self.summary_instance.__str__(), self.summary_instance._check_id_field)

    # Tests for dat_files model
    def create_dat_files(self, parent, file,name="name"):
        return models.dat_files.objects.create(parent=parent, dat_store=file,name=name)

    def test_dat_files_creation(self):
        model = self.create_BSM("1995-08-08")
        runcard = self.create_Runcard(model)
        results_header = self.create_Results_header(runcard)
        rp = self.create_Results_position(results_header)
        dd = self.create_dat_database(rp, "1995-08-08")

        with open('test_summary.txt', 'w') as f:
            f.write('Test Contents')

        file = File(open("test_summary.txt",'w+'))

        self.dat_instance = self.create_dat_files(dd,file)

        # Check that instance is created correctly
        self.assertTrue(isinstance(self.dat_instance, models.dat_files))
        # Check that instance has correct contents
        self.assertEqual(self.dat_instance.__str__(), self.dat_instance._check_id_field)

    # Tests for histo_header model
    def create_histo_header(self, parent, date):
        return models.histo_header.objects.create(results_object=parent, uploaded=date)

    def test_histo_header_creation(self):
        model = self.create_BSM("1995-08-08")
        runcard = self.create_Runcard(model)
        results_header = self.create_Results_header(runcard)
        rp = self.create_Results_position(results_header)

        self.hh_instance = self.create_histo_header(rp, "1995-08-08")
        # Check that instance is created correctly
        self.assertTrue(isinstance(self.hh_instance, models.histo_header))
        # Check that instance has correct contents
        self.assertEqual(self.hh_instance.__str__(), self.hh_instance._check_id_field)

    def test_histo_header_creation_fails1(self):
        with self.assertRaises(ValueError):
            self.create_histo_header("Not position object", "1995-08-08")

    # Tests for histo_data model
    def create_histo_data(self, parent, file,position="name"):
        return models.histo_data.objects.create(parent=parent, dat_store=file,position=position)

    def test_histo_data_creation(self):
        model = self.create_BSM("1995-08-08")
        runcard = self.create_Runcard(model)
        results_header = self.create_Results_header(runcard)
        rp = self.create_Results_position(results_header)
        hh = self.create_histo_header(rp, "1995-08-08")

        with open('test_summary.txt', 'w') as f:
            f.write('Test Contents')

        file = File(open("test_summary.txt",'w+'))
        os.remove('test_summary.txt')
        self.hd_instance = self.create_histo_data(hh,file)

        # Check that instance is created correctly
        self.assertTrue(isinstance(self.hd_instance, models.histo_data))
        # Check that instance has correct contents
        self.assertEqual(self.hd_instance.__str__(), self.hd_instance._check_id_field)

    # Tests for histo_image model
    def create_histo_images(self, parent, image,position="name"):
        return models.histo_images.objects.create(parent=parent, image=image,position=position)

    def test_histo_image_creation(self):
        model = self.create_BSM("1995-08-08")
        runcard = self.create_Runcard(model)
        results_header = self.create_Results_header(runcard)
        rp = self.create_Results_position(results_header)
        hh = self.create_histo_header(rp, "1995-08-08")

        img = Image.new('RGB', (60, 30), color = 'red')
        img.save('image_test.png')

        file = File(open("image_test.png",mode="rb"))

        self.hi_instance = self.create_histo_images(hh,file)
        os.remove('image_test.png')
        # Check that instance is created correctly
        self.assertTrue(isinstance(self.hi_instance, models.histo_images))
        # Check that instance has correct contents
        self.assertEqual(self.hi_instance.__str__(), self.hi_instance._check_id_field)