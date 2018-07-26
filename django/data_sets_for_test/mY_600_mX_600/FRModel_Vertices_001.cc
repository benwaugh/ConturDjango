// -*- C++ -*-
//
// FRModel_Vertices_001.cc is a part of Herwig - A multi-purpose Monte Carlo event generator
// Copyright (C) 2002-2007 The Herwig Collaboration
//
// Herwig is licenced under version 2 of the GPL, see COPYING for details.
// Please respect the MCnet academic guidelines, see GUIDELINES for details.

#include "FRModel.h"
#include "ThePEG/Helicity/Vertex/Scalar/SSSVertex.h"
#include "ThePEG/Helicity/Vertex/Scalar/SSSSVertex.h"
#include "ThePEG/Helicity/Vertex/Vector/FFVVertex.h"
#include "ThePEG/Helicity/Vertex/Vector/VVVVVertex.h"
#include "ThePEG/Helicity/Vertex/Vector/VVVVertex.h"
#include "ThePEG/Helicity/Vertex/Scalar/VVSSVertex.h"
#include "ThePEG/Helicity/Vertex/Scalar/VVSVertex.h"
#include "ThePEG/Helicity/Vertex/Scalar/FFSVertex.h"

#include "ThePEG/Utilities/DescribeClass.h"
#include "ThePEG/Persistency/PersistentOStream.h"
#include "ThePEG/Persistency/PersistentIStream.h"

namespace Herwig 
{
  using namespace ThePEG;
  using namespace ThePEG::Helicity;
  using ThePEG::Constants::pi;

  class FRModelV_V_6: public SSSSVertex {
 public:
  FRModelV_V_6() {
    
    colourStructure(ColourStructure::SINGLET);
    addToList(25,25,25,25);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr,tcPDPtr) {
    double lam = model_->lam();
    
    //    getParams(q2);
    norm((((-ii)*1.0)*((-6.0*ii)*lam)));
    
    
    
  }
  void persistentOutput(PersistentOStream & os) const { os << model_; }
  void persistentInput(PersistentIStream & is, int) { is >> model_; }
  //  static void Init();
 protected:
  IBPtr clone() const { return new_ptr(*this); }
  IBPtr fullclone() const { return new_ptr(*this); }
  void doinit() {
    model_ = dynamic_ptr_cast<tcHwFRModelPtr>
	     (generator()->standardModel());
    assert(model_);
    //    getParams(q2);
    
        orderInCoupling(CouplingType::DMS,0);
    orderInCoupling(CouplingType::QED,2);
    orderInCoupling(CouplingType::QCD,0);

    SSSSVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_6 & operator=(const FRModelV_V_6 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_6,Helicity::SSSSVertex>
describeHerwigFRModelV_V_6("Herwig::FRModelV_V_6",
				       "FRModel.so");
// void FRModelV_V_6::getParams(Energy2 ) {
// }

class FRModelV_V_9: public SSSVertex {
 public:
  FRModelV_V_9() {
    
    colourStructure(ColourStructure::SINGLET);
    addToList(25,25,25);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double vev = model_->vev();
    double lam = model_->lam();
    
    //    getParams(q2);
    norm(Complex(((((-ii)*1.0)*(((-6.0*ii)*lam)*vev))) * GeV / UnitRemoval::E));
    
    
    
  }
  void persistentOutput(PersistentOStream & os) const { os << model_; }
  void persistentInput(PersistentIStream & is, int) { is >> model_; }
  //  static void Init();
 protected:
  IBPtr clone() const { return new_ptr(*this); }
  IBPtr fullclone() const { return new_ptr(*this); }
  void doinit() {
    model_ = dynamic_ptr_cast<tcHwFRModelPtr>
	     (generator()->standardModel());
    assert(model_);
    //    getParams(q2);
    
        orderInCoupling(CouplingType::DMS,0);
    orderInCoupling(CouplingType::QED,1);
    orderInCoupling(CouplingType::QCD,0);

    SSSVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_9 & operator=(const FRModelV_V_9 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_9,Helicity::SSSVertex>
describeHerwigFRModelV_V_9("Herwig::FRModelV_V_9",
				       "FRModel.so");
// void FRModelV_V_9::getParams(Energy2 ) {
// }

class FRModelV_V_36: public VVVVertex {
 public:
  FRModelV_V_36() {
    
    colourStructure(ColourStructure::SU3F);
    addToList(21,21,21);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double G = model_->G();
    
    //    getParams(q2);
    norm(((ii*((-ii)*1.0))*(-G)));
    
    
    
  }
  void persistentOutput(PersistentOStream & os) const { os << model_; }
  void persistentInput(PersistentIStream & is, int) { is >> model_; }
  //  static void Init();
 protected:
  IBPtr clone() const { return new_ptr(*this); }
  IBPtr fullclone() const { return new_ptr(*this); }
  void doinit() {
    model_ = dynamic_ptr_cast<tcHwFRModelPtr>
	     (generator()->standardModel());
    assert(model_);
    //    getParams(q2);
    
        orderInCoupling(CouplingType::DMS,0);
    orderInCoupling(CouplingType::QED,0);
    orderInCoupling(CouplingType::QCD,1);

    VVVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_36 & operator=(const FRModelV_V_36 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_36,Helicity::VVVVertex>
describeHerwigFRModelV_V_36("Herwig::FRModelV_V_36",
				       "FRModel.so");
// void FRModelV_V_36::getParams(Energy2 ) {
// }

class FRModelV_V_37: public VVVVVertex {
 public:
  FRModelV_V_37() {
    
    colourStructure(ColourStructure::SU3FF);
    addToList(21,21,21,21);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr,tcPDPtr) {
    double G = model_->G();
    
    //    getParams(q2);
    norm(((-1.0*(ii*1.0))*(ii*sqr(G))));
    
    
    setType(1);
setOrder(0,1,2,3);
  }
  void persistentOutput(PersistentOStream & os) const { os << model_; }
  void persistentInput(PersistentIStream & is, int) { is >> model_; }
  //  static void Init();
 protected:
  IBPtr clone() const { return new_ptr(*this); }
  IBPtr fullclone() const { return new_ptr(*this); }
  void doinit() {
    model_ = dynamic_ptr_cast<tcHwFRModelPtr>
	     (generator()->standardModel());
    assert(model_);
    //    getParams(q2);
    
        orderInCoupling(CouplingType::DMS,0);
    orderInCoupling(CouplingType::QED,0);
    orderInCoupling(CouplingType::QCD,2);

    VVVVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_37 & operator=(const FRModelV_V_37 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_37,Helicity::VVVVVertex>
describeHerwigFRModelV_V_37("Herwig::FRModelV_V_37",
				       "FRModel.so");
// void FRModelV_V_37::getParams(Energy2 ) {
// }

class FRModelV_V_40: public FFSVertex {
 public:
  FRModelV_V_40() {
    
    colourStructure(ColourStructure::DELTA);
    addToList(-5,5,25);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double yb = model_->yb();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*(-((ii*yb)/sqrt(2.0)))));
    right(((((-ii)*1.0)*1.0)*(-((ii*yb)/sqrt(2.0)))));
    
  }
  void persistentOutput(PersistentOStream & os) const { os << model_; }
  void persistentInput(PersistentIStream & is, int) { is >> model_; }
  //  static void Init();
 protected:
  IBPtr clone() const { return new_ptr(*this); }
  IBPtr fullclone() const { return new_ptr(*this); }
  void doinit() {
    model_ = dynamic_ptr_cast<tcHwFRModelPtr>
	     (generator()->standardModel());
    assert(model_);
    //    getParams(q2);
    
        orderInCoupling(CouplingType::DMS,0);
    orderInCoupling(CouplingType::QED,1);
    orderInCoupling(CouplingType::QCD,0);

    FFSVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_40 & operator=(const FRModelV_V_40 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_40,Helicity::FFSVertex>
describeHerwigFRModelV_V_40("Herwig::FRModelV_V_40",
				       "FRModel.so");
// void FRModelV_V_40::getParams(Energy2 ) {
// }

class FRModelV_V_43: public FFSVertex {
 public:
  FRModelV_V_43() {
    
    colourStructure(ColourStructure::SINGLET);
    addToList(-15,15,25);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double ytau = model_->ytau();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*(-((ii*ytau)/sqrt(2.0)))));
    right(((((-ii)*1.0)*1.0)*(-((ii*ytau)/sqrt(2.0)))));
    
  }
  void persistentOutput(PersistentOStream & os) const { os << model_; }
  void persistentInput(PersistentIStream & is, int) { is >> model_; }
  //  static void Init();
 protected:
  IBPtr clone() const { return new_ptr(*this); }
  IBPtr fullclone() const { return new_ptr(*this); }
  void doinit() {
    model_ = dynamic_ptr_cast<tcHwFRModelPtr>
	     (generator()->standardModel());
    assert(model_);
    //    getParams(q2);
    
        orderInCoupling(CouplingType::DMS,0);
    orderInCoupling(CouplingType::QED,1);
    orderInCoupling(CouplingType::QCD,0);

    FFSVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_43 & operator=(const FRModelV_V_43 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_43,Helicity::FFSVertex>
describeHerwigFRModelV_V_43("Herwig::FRModelV_V_43",
				       "FRModel.so");
// void FRModelV_V_43::getParams(Energy2 ) {
// }

class FRModelV_V_46: public FFSVertex {
 public:
  FRModelV_V_46() {
    
    colourStructure(ColourStructure::DELTA);
    addToList(-6,6,25);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double yt = model_->yt();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*(-((ii*yt)/sqrt(2.0)))));
    right(((((-ii)*1.0)*1.0)*(-((ii*yt)/sqrt(2.0)))));
    
  }
  void persistentOutput(PersistentOStream & os) const { os << model_; }
  void persistentInput(PersistentIStream & is, int) { is >> model_; }
  //  static void Init();
 protected:
  IBPtr clone() const { return new_ptr(*this); }
  IBPtr fullclone() const { return new_ptr(*this); }
  void doinit() {
    model_ = dynamic_ptr_cast<tcHwFRModelPtr>
	     (generator()->standardModel());
    assert(model_);
    //    getParams(q2);
    
        orderInCoupling(CouplingType::DMS,0);
    orderInCoupling(CouplingType::QED,1);
    orderInCoupling(CouplingType::QCD,0);

    FFSVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_46 & operator=(const FRModelV_V_46 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_46,Helicity::FFSVertex>
describeHerwigFRModelV_V_46("Herwig::FRModelV_V_46",
				       "FRModel.so");
// void FRModelV_V_46::getParams(Energy2 ) {
// }

class FRModelV_V_52: public VVVVertex {
 public:
  FRModelV_V_52() {
    
    colourStructure(ColourStructure::SINGLET);
    addToList(22,-24,24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr p2,tcPDPtr p3) {
    double ee = model_->ee();
    
    //    getParams(q2);
    norm(((ii*1.0)*(ee*ii)));
    
    
    if((p1->id()==-24&&p2->id()==22&&p3->id()==24)||(p1->id()==22&&p2->id()==24&&p3->id()==-24)||(p1->id()==24&&p2->id()==-24&&p3->id()==22)) {norm(-norm());}
  }
  void persistentOutput(PersistentOStream & os) const { os << model_; }
  void persistentInput(PersistentIStream & is, int) { is >> model_; }
  //  static void Init();
 protected:
  IBPtr clone() const { return new_ptr(*this); }
  IBPtr fullclone() const { return new_ptr(*this); }
  void doinit() {
    model_ = dynamic_ptr_cast<tcHwFRModelPtr>
	     (generator()->standardModel());
    assert(model_);
    //    getParams(q2);
    
        orderInCoupling(CouplingType::DMS,0);
    orderInCoupling(CouplingType::QED,1);
    orderInCoupling(CouplingType::QCD,0);

    VVVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_52 & operator=(const FRModelV_V_52 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_52,Helicity::VVVVertex>
describeHerwigFRModelV_V_52("Herwig::FRModelV_V_52",
				       "FRModel.so");
// void FRModelV_V_52::getParams(Energy2 ) {
// }

class FRModelV_V_60: public VVSSVertex {
 public:
  FRModelV_V_60() {
    
    colourStructure(ColourStructure::SINGLET);
    addToList(-24,24,25,25);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    
    //    getParams(q2);
    norm(((((-ii)*1.0)*((sqr(ee)*ii)/(2.0*sqr(sw))))*1.0));
    
    
    
  }
  void persistentOutput(PersistentOStream & os) const { os << model_; }
  void persistentInput(PersistentIStream & is, int) { is >> model_; }
  //  static void Init();
 protected:
  IBPtr clone() const { return new_ptr(*this); }
  IBPtr fullclone() const { return new_ptr(*this); }
  void doinit() {
    model_ = dynamic_ptr_cast<tcHwFRModelPtr>
	     (generator()->standardModel());
    assert(model_);
    //    getParams(q2);
    
        orderInCoupling(CouplingType::DMS,0);
    orderInCoupling(CouplingType::QED,2);
    orderInCoupling(CouplingType::QCD,0);

    VVSSVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_60 & operator=(const FRModelV_V_60 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_60,Helicity::VVSSVertex>
describeHerwigFRModelV_V_60("Herwig::FRModelV_V_60",
				       "FRModel.so");
// void FRModelV_V_60::getParams(Energy2 ) {
// }

class FRModelV_V_61: public VVSVertex {
 public:
  FRModelV_V_61() {
    
    colourStructure(ColourStructure::SINGLET);
    addToList(-24,24,25);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double vev = model_->vev();
    double sw = model_->sw();
    
    //    getParams(q2);
    norm(Complex((((((-ii)*1.0)*(((sqr(ee)*ii)*vev)/(2.0*sqr(sw))))*1.0)) * GeV / UnitRemoval::E));
    
    
    
  }
  void persistentOutput(PersistentOStream & os) const { os << model_; }
  void persistentInput(PersistentIStream & is, int) { is >> model_; }
  //  static void Init();
 protected:
  IBPtr clone() const { return new_ptr(*this); }
  IBPtr fullclone() const { return new_ptr(*this); }
  void doinit() {
    model_ = dynamic_ptr_cast<tcHwFRModelPtr>
	     (generator()->standardModel());
    assert(model_);
    //    getParams(q2);
    
        orderInCoupling(CouplingType::DMS,0);
    orderInCoupling(CouplingType::QED,1);
    orderInCoupling(CouplingType::QCD,0);

    VVSVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_61 & operator=(const FRModelV_V_61 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_61,Helicity::VVSVertex>
describeHerwigFRModelV_V_61("Herwig::FRModelV_V_61",
				       "FRModel.so");
// void FRModelV_V_61::getParams(Energy2 ) {
// }

class FRModelV_V_62: public VVVVVertex {
 public:
  FRModelV_V_62() {
    
    colourStructure(ColourStructure::SINGLET);
    addToList(22,22,-24,24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr p2,tcPDPtr p3,tcPDPtr p4) {
    double ee = model_->ee();
    
    //    getParams(q2);
    norm((0.5*((-2.0*(ii*1.0))*(sqr(ee)*ii))));
    
    
    bool done[4]={false,false,false,false};
    tcPDPtr part[4]={p1,p2,p3,p4};
    unsigned int iorder[4]={0,0,0,0};
    for(unsigned int ix=0;ix<4;++ix) {
       if(!done[0] && part[ix]->id()==22) {done[0]=true; iorder[0] = ix; continue;}
       if(!done[1] && part[ix]->id()==22) {done[1]=true; iorder[1] = ix; continue;}
       if(!done[2] && part[ix]->id()==-24) {done[2]=true; iorder[2] = ix; continue;}
       if(!done[3] && part[ix]->id()==24) {done[3]=true; iorder[3] = ix; continue;}
    }
    setType(2);
    setOrder(iorder[0],iorder[1],iorder[2],iorder[3]);
  }
  void persistentOutput(PersistentOStream & os) const { os << model_; }
  void persistentInput(PersistentIStream & is, int) { is >> model_; }
  //  static void Init();
 protected:
  IBPtr clone() const { return new_ptr(*this); }
  IBPtr fullclone() const { return new_ptr(*this); }
  void doinit() {
    model_ = dynamic_ptr_cast<tcHwFRModelPtr>
	     (generator()->standardModel());
    assert(model_);
    //    getParams(q2);
    
        orderInCoupling(CouplingType::DMS,0);
    orderInCoupling(CouplingType::QED,2);
    orderInCoupling(CouplingType::QCD,0);

    VVVVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_62 & operator=(const FRModelV_V_62 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_62,Helicity::VVVVVertex>
describeHerwigFRModelV_V_62("Herwig::FRModelV_V_62",
				       "FRModel.so");
// void FRModelV_V_62::getParams(Energy2 ) {
// }

class FRModelV_V_63: public VVVVertex {
 public:
  FRModelV_V_63() {
    
    colourStructure(ColourStructure::SINGLET);
    addToList(-24,24,23);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr p2,tcPDPtr p3) {
    double ee = model_->ee();
    double cw = model_->cw();
    double sw = model_->sw();
    
    //    getParams(q2);
    norm(((ii*1.0)*(((cw*ee)*ii)/sw)));
    
    
    if((p1->id()==24&&p2->id()==-24&&p3->id()==23)||(p1->id()==-24&&p2->id()==23&&p3->id()==24)||(p1->id()==23&&p2->id()==24&&p3->id()==-24)) {norm(-norm());}
  }
  void persistentOutput(PersistentOStream & os) const { os << model_; }
  void persistentInput(PersistentIStream & is, int) { is >> model_; }
  //  static void Init();
 protected:
  IBPtr clone() const { return new_ptr(*this); }
  IBPtr fullclone() const { return new_ptr(*this); }
  void doinit() {
    model_ = dynamic_ptr_cast<tcHwFRModelPtr>
	     (generator()->standardModel());
    assert(model_);
    //    getParams(q2);
    
        orderInCoupling(CouplingType::DMS,0);
    orderInCoupling(CouplingType::QED,1);
    orderInCoupling(CouplingType::QCD,0);

    VVVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_63 & operator=(const FRModelV_V_63 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_63,Helicity::VVVVertex>
describeHerwigFRModelV_V_63("Herwig::FRModelV_V_63",
				       "FRModel.so");
// void FRModelV_V_63::getParams(Energy2 ) {
// }

class FRModelV_V_64: public VVVVVertex {
 public:
  FRModelV_V_64() {
    
    colourStructure(ColourStructure::SINGLET);
    addToList(-24,-24,24,24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr p2,tcPDPtr p3,tcPDPtr p4) {
    double ee = model_->ee();
    double sw = model_->sw();
    
    //    getParams(q2);
    norm((0.5*((-2.0*(ii*1.0))*(-((sqr(ee)*ii)/sqr(sw))))));
    
    
    bool done[4]={false,false,false,false};
    tcPDPtr part[4]={p1,p2,p3,p4};
    unsigned int iorder[4]={0,0,0,0};
    for(unsigned int ix=0;ix<4;++ix) {
       if(!done[0] && part[ix]->id()==-24) {done[0]=true; iorder[0] = ix; continue;}
       if(!done[1] && part[ix]->id()==-24) {done[1]=true; iorder[1] = ix; continue;}
       if(!done[2] && part[ix]->id()==24) {done[2]=true; iorder[2] = ix; continue;}
       if(!done[3] && part[ix]->id()==24) {done[3]=true; iorder[3] = ix; continue;}
    }
    setType(2);
    setOrder(iorder[0],iorder[1],iorder[2],iorder[3]);
  }
  void persistentOutput(PersistentOStream & os) const { os << model_; }
  void persistentInput(PersistentIStream & is, int) { is >> model_; }
  //  static void Init();
 protected:
  IBPtr clone() const { return new_ptr(*this); }
  IBPtr fullclone() const { return new_ptr(*this); }
  void doinit() {
    model_ = dynamic_ptr_cast<tcHwFRModelPtr>
	     (generator()->standardModel());
    assert(model_);
    //    getParams(q2);
    
        orderInCoupling(CouplingType::DMS,0);
    orderInCoupling(CouplingType::QED,2);
    orderInCoupling(CouplingType::QCD,0);

    VVVVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_64 & operator=(const FRModelV_V_64 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_64,Helicity::VVVVVertex>
describeHerwigFRModelV_V_64("Herwig::FRModelV_V_64",
				       "FRModel.so");
// void FRModelV_V_64::getParams(Energy2 ) {
// }

class FRModelV_V_65: public FFVVertex {
 public:
  FRModelV_V_65() {
    
    colourStructure(ColourStructure::DELTA);
    addToList(-1,1,9000006);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double gYq = model_->gYq();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*(ii*gYq)));
    right(((((-ii)*1.0)*1.0)*(ii*gYq)));
    if(p1->id()!=-1) {Complex ltemp=left(), rtemp=right(); left(-rtemp); right(-ltemp);}
  }
  void persistentOutput(PersistentOStream & os) const { os << model_; }
  void persistentInput(PersistentIStream & is, int) { is >> model_; }
  //  static void Init();
 protected:
  IBPtr clone() const { return new_ptr(*this); }
  IBPtr fullclone() const { return new_ptr(*this); }
  void doinit() {
    model_ = dynamic_ptr_cast<tcHwFRModelPtr>
	     (generator()->standardModel());
    assert(model_);
    //    getParams(q2);
    
        orderInCoupling(CouplingType::DMS,1);
    orderInCoupling(CouplingType::QED,0);
    orderInCoupling(CouplingType::QCD,0);

    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_65 & operator=(const FRModelV_V_65 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_65,Helicity::FFVVertex>
describeHerwigFRModelV_V_65("Herwig::FRModelV_V_65",
				       "FRModel.so");
// void FRModelV_V_65::getParams(Energy2 ) {
// }

class FRModelV_V_66: public FFVVertex {
 public:
  FRModelV_V_66() {
    
    colourStructure(ColourStructure::DELTA);
    addToList(-3,3,9000006);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double gYq = model_->gYq();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*(ii*gYq)));
    right(((((-ii)*1.0)*1.0)*(ii*gYq)));
    if(p1->id()!=-3) {Complex ltemp=left(), rtemp=right(); left(-rtemp); right(-ltemp);}
  }
  void persistentOutput(PersistentOStream & os) const { os << model_; }
  void persistentInput(PersistentIStream & is, int) { is >> model_; }
  //  static void Init();
 protected:
  IBPtr clone() const { return new_ptr(*this); }
  IBPtr fullclone() const { return new_ptr(*this); }
  void doinit() {
    model_ = dynamic_ptr_cast<tcHwFRModelPtr>
	     (generator()->standardModel());
    assert(model_);
    //    getParams(q2);
    
        orderInCoupling(CouplingType::DMS,1);
    orderInCoupling(CouplingType::QED,0);
    orderInCoupling(CouplingType::QCD,0);

    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_66 & operator=(const FRModelV_V_66 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_66,Helicity::FFVVertex>
describeHerwigFRModelV_V_66("Herwig::FRModelV_V_66",
				       "FRModel.so");
// void FRModelV_V_66::getParams(Energy2 ) {
// }

class FRModelV_V_67: public FFVVertex {
 public:
  FRModelV_V_67() {
    
    colourStructure(ColourStructure::DELTA);
    addToList(-5,5,9000006);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double gYq = model_->gYq();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*(ii*gYq)));
    right(((((-ii)*1.0)*1.0)*(ii*gYq)));
    if(p1->id()!=-5) {Complex ltemp=left(), rtemp=right(); left(-rtemp); right(-ltemp);}
  }
  void persistentOutput(PersistentOStream & os) const { os << model_; }
  void persistentInput(PersistentIStream & is, int) { is >> model_; }
  //  static void Init();
 protected:
  IBPtr clone() const { return new_ptr(*this); }
  IBPtr fullclone() const { return new_ptr(*this); }
  void doinit() {
    model_ = dynamic_ptr_cast<tcHwFRModelPtr>
	     (generator()->standardModel());
    assert(model_);
    //    getParams(q2);
    
        orderInCoupling(CouplingType::DMS,1);
    orderInCoupling(CouplingType::QED,0);
    orderInCoupling(CouplingType::QCD,0);

    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_67 & operator=(const FRModelV_V_67 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_67,Helicity::FFVVertex>
describeHerwigFRModelV_V_67("Herwig::FRModelV_V_67",
				       "FRModel.so");
// void FRModelV_V_67::getParams(Energy2 ) {
// }

class FRModelV_V_68: public FFVVertex {
 public:
  FRModelV_V_68() {
    
    colourStructure(ColourStructure::DELTA);
    addToList(-2,2,9000006);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double gYq = model_->gYq();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*(ii*gYq)));
    right(((((-ii)*1.0)*1.0)*(ii*gYq)));
    if(p1->id()!=-2) {Complex ltemp=left(), rtemp=right(); left(-rtemp); right(-ltemp);}
  }
  void persistentOutput(PersistentOStream & os) const { os << model_; }
  void persistentInput(PersistentIStream & is, int) { is >> model_; }
  //  static void Init();
 protected:
  IBPtr clone() const { return new_ptr(*this); }
  IBPtr fullclone() const { return new_ptr(*this); }
  void doinit() {
    model_ = dynamic_ptr_cast<tcHwFRModelPtr>
	     (generator()->standardModel());
    assert(model_);
    //    getParams(q2);
    
        orderInCoupling(CouplingType::DMS,1);
    orderInCoupling(CouplingType::QED,0);
    orderInCoupling(CouplingType::QCD,0);

    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_68 & operator=(const FRModelV_V_68 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_68,Helicity::FFVVertex>
describeHerwigFRModelV_V_68("Herwig::FRModelV_V_68",
				       "FRModel.so");
// void FRModelV_V_68::getParams(Energy2 ) {
// }

class FRModelV_V_69: public FFVVertex {
 public:
  FRModelV_V_69() {
    
    colourStructure(ColourStructure::DELTA);
    addToList(-4,4,9000006);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double gYq = model_->gYq();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*(ii*gYq)));
    right(((((-ii)*1.0)*1.0)*(ii*gYq)));
    if(p1->id()!=-4) {Complex ltemp=left(), rtemp=right(); left(-rtemp); right(-ltemp);}
  }
  void persistentOutput(PersistentOStream & os) const { os << model_; }
  void persistentInput(PersistentIStream & is, int) { is >> model_; }
  //  static void Init();
 protected:
  IBPtr clone() const { return new_ptr(*this); }
  IBPtr fullclone() const { return new_ptr(*this); }
  void doinit() {
    model_ = dynamic_ptr_cast<tcHwFRModelPtr>
	     (generator()->standardModel());
    assert(model_);
    //    getParams(q2);
    
        orderInCoupling(CouplingType::DMS,1);
    orderInCoupling(CouplingType::QED,0);
    orderInCoupling(CouplingType::QCD,0);

    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_69 & operator=(const FRModelV_V_69 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_69,Helicity::FFVVertex>
describeHerwigFRModelV_V_69("Herwig::FRModelV_V_69",
				       "FRModel.so");
// void FRModelV_V_69::getParams(Energy2 ) {
// }

class FRModelV_V_70: public FFVVertex {
 public:
  FRModelV_V_70() {
    
    colourStructure(ColourStructure::DELTA);
    addToList(-6,6,9000006);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double gYq = model_->gYq();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*(ii*gYq)));
    right(((((-ii)*1.0)*1.0)*(ii*gYq)));
    if(p1->id()!=-6) {Complex ltemp=left(), rtemp=right(); left(-rtemp); right(-ltemp);}
  }
  void persistentOutput(PersistentOStream & os) const { os << model_; }
  void persistentInput(PersistentIStream & is, int) { is >> model_; }
  //  static void Init();
 protected:
  IBPtr clone() const { return new_ptr(*this); }
  IBPtr fullclone() const { return new_ptr(*this); }
  void doinit() {
    model_ = dynamic_ptr_cast<tcHwFRModelPtr>
	     (generator()->standardModel());
    assert(model_);
    //    getParams(q2);
    
        orderInCoupling(CouplingType::DMS,1);
    orderInCoupling(CouplingType::QED,0);
    orderInCoupling(CouplingType::QCD,0);

    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_70 & operator=(const FRModelV_V_70 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_70,Helicity::FFVVertex>
describeHerwigFRModelV_V_70("Herwig::FRModelV_V_70",
				       "FRModel.so");
// void FRModelV_V_70::getParams(Energy2 ) {
// }

class FRModelV_V_81: public VVVVVertex {
 public:
  FRModelV_V_81() {
    
    colourStructure(ColourStructure::SINGLET);
    addToList(22,-24,24,23);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr p2,tcPDPtr p3,tcPDPtr p4) {
    double ee = model_->ee();
    double cw = model_->cw();
    double sw = model_->sw();
    
    //    getParams(q2);
    norm((0.5*((ii*1.0)*((((-2.0*cw)*sqr(ee))*ii)/sw))));
    
    
    bool done[4]={false,false,false,false};
    tcPDPtr part[4]={p1,p2,p3,p4};
    unsigned int iorder[4]={0,0,0,0};
    for(unsigned int ix=0;ix<4;++ix) {
       if(!done[0] && part[ix]->id()==22) {done[0]=true; iorder[0] = ix; continue;}
       if(!done[1] && part[ix]->id()==-24) {done[1]=true; iorder[3] = ix; continue;}
       if(!done[2] && part[ix]->id()==24) {done[2]=true; iorder[1] = ix; continue;}
       if(!done[3] && part[ix]->id()==23) {done[3]=true; iorder[2] = ix; continue;}
    }
    setType(2);
    setOrder(iorder[0],iorder[1],iorder[2],iorder[3]);
  }
  void persistentOutput(PersistentOStream & os) const { os << model_; }
  void persistentInput(PersistentIStream & is, int) { is >> model_; }
  //  static void Init();
 protected:
  IBPtr clone() const { return new_ptr(*this); }
  IBPtr fullclone() const { return new_ptr(*this); }
  void doinit() {
    model_ = dynamic_ptr_cast<tcHwFRModelPtr>
	     (generator()->standardModel());
    assert(model_);
    //    getParams(q2);
    
        orderInCoupling(CouplingType::DMS,0);
    orderInCoupling(CouplingType::QED,2);
    orderInCoupling(CouplingType::QCD,0);

    VVVVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_81 & operator=(const FRModelV_V_81 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_81,Helicity::VVVVVertex>
describeHerwigFRModelV_V_81("Herwig::FRModelV_V_81",
				       "FRModel.so");
// void FRModelV_V_81::getParams(Energy2 ) {
// }

class FRModelV_V_84: public VVSSVertex {
 public:
  FRModelV_V_84() {
    
    colourStructure(ColourStructure::SINGLET);
    addToList(23,23,25,25);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double cw = model_->cw();
    double sw = model_->sw();
    
    //    getParams(q2);
    norm(((((-ii)*1.0)*(((sqr(ee)*ii)+(((sqr(cw)*sqr(ee))*ii)/(2.0*sqr(sw))))+(((sqr(ee)*ii)*sqr(sw))/(2.0*sqr(cw)))))*1.0));
    
    
    
  }
  void persistentOutput(PersistentOStream & os) const { os << model_; }
  void persistentInput(PersistentIStream & is, int) { is >> model_; }
  //  static void Init();
 protected:
  IBPtr clone() const { return new_ptr(*this); }
  IBPtr fullclone() const { return new_ptr(*this); }
  void doinit() {
    model_ = dynamic_ptr_cast<tcHwFRModelPtr>
	     (generator()->standardModel());
    assert(model_);
    //    getParams(q2);
    
        orderInCoupling(CouplingType::DMS,0);
    orderInCoupling(CouplingType::QED,2);
    orderInCoupling(CouplingType::QCD,0);

    VVSSVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_84 & operator=(const FRModelV_V_84 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_84,Helicity::VVSSVertex>
describeHerwigFRModelV_V_84("Herwig::FRModelV_V_84",
				       "FRModel.so");
// void FRModelV_V_84::getParams(Energy2 ) {
// }

class FRModelV_V_85: public VVSVertex {
 public:
  FRModelV_V_85() {
    
    colourStructure(ColourStructure::SINGLET);
    addToList(23,23,25);
  }
  void setCoupling(Energy2 ,tcPDPtr,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double vev = model_->vev();
    double cw = model_->cw();
    double sw = model_->sw();
    
    //    getParams(q2);
    norm(Complex((((((-ii)*1.0)*((((sqr(ee)*ii)*vev)+((((sqr(cw)*sqr(ee))*ii)*vev)/(2.0*sqr(sw))))+((((sqr(ee)*ii)*sqr(sw))*vev)/(2.0*sqr(cw)))))*1.0)) * GeV / UnitRemoval::E));
    
    
    
  }
  void persistentOutput(PersistentOStream & os) const { os << model_; }
  void persistentInput(PersistentIStream & is, int) { is >> model_; }
  //  static void Init();
 protected:
  IBPtr clone() const { return new_ptr(*this); }
  IBPtr fullclone() const { return new_ptr(*this); }
  void doinit() {
    model_ = dynamic_ptr_cast<tcHwFRModelPtr>
	     (generator()->standardModel());
    assert(model_);
    //    getParams(q2);
    
        orderInCoupling(CouplingType::DMS,0);
    orderInCoupling(CouplingType::QED,1);
    orderInCoupling(CouplingType::QCD,0);

    VVSVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_85 & operator=(const FRModelV_V_85 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_85,Helicity::VVSVertex>
describeHerwigFRModelV_V_85("Herwig::FRModelV_V_85",
				       "FRModel.so");
// void FRModelV_V_85::getParams(Energy2 ) {
// }

class FRModelV_V_86: public VVVVVertex {
 public:
  FRModelV_V_86() {
    
    colourStructure(ColourStructure::SINGLET);
    addToList(-24,24,23,23);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr p2,tcPDPtr p3,tcPDPtr p4) {
    double ee = model_->ee();
    double cw = model_->cw();
    double sw = model_->sw();
    
    //    getParams(q2);
    norm((0.5*((-2.0*(ii*1.0))*(((sqr(cw)*sqr(ee))*ii)/sqr(sw)))));
    
    
    bool done[4]={false,false,false,false};
    tcPDPtr part[4]={p1,p2,p3,p4};
    unsigned int iorder[4]={0,0,0,0};
    for(unsigned int ix=0;ix<4;++ix) {
       if(!done[0] && part[ix]->id()==-24) {done[0]=true; iorder[0] = ix; continue;}
       if(!done[1] && part[ix]->id()==24) {done[1]=true; iorder[1] = ix; continue;}
       if(!done[2] && part[ix]->id()==23) {done[2]=true; iorder[2] = ix; continue;}
       if(!done[3] && part[ix]->id()==23) {done[3]=true; iorder[3] = ix; continue;}
    }
    setType(2);
    setOrder(iorder[0],iorder[1],iorder[2],iorder[3]);
  }
  void persistentOutput(PersistentOStream & os) const { os << model_; }
  void persistentInput(PersistentIStream & is, int) { is >> model_; }
  //  static void Init();
 protected:
  IBPtr clone() const { return new_ptr(*this); }
  IBPtr fullclone() const { return new_ptr(*this); }
  void doinit() {
    model_ = dynamic_ptr_cast<tcHwFRModelPtr>
	     (generator()->standardModel());
    assert(model_);
    //    getParams(q2);
    
        orderInCoupling(CouplingType::DMS,0);
    orderInCoupling(CouplingType::QED,2);
    orderInCoupling(CouplingType::QCD,0);

    VVVVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_86 & operator=(const FRModelV_V_86 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_86,Helicity::VVVVVertex>
describeHerwigFRModelV_V_86("Herwig::FRModelV_V_86",
				       "FRModel.so");
// void FRModelV_V_86::getParams(Energy2 ) {
// }

class FRModelV_V_87: public FFVVertex {
 public:
  FRModelV_V_87() {
    
    colourStructure(ColourStructure::SINGLET);
    addToList(-11,11,22);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*(-(ee*ii))));
    right(((((-ii)*1.0)*1.0)*(-(ee*ii))));
    if(p1->id()!=-11) {Complex ltemp=left(), rtemp=right(); left(-rtemp); right(-ltemp);}
  }
  void persistentOutput(PersistentOStream & os) const { os << model_; }
  void persistentInput(PersistentIStream & is, int) { is >> model_; }
  //  static void Init();
 protected:
  IBPtr clone() const { return new_ptr(*this); }
  IBPtr fullclone() const { return new_ptr(*this); }
  void doinit() {
    model_ = dynamic_ptr_cast<tcHwFRModelPtr>
	     (generator()->standardModel());
    assert(model_);
    //    getParams(q2);
    
        orderInCoupling(CouplingType::DMS,0);
    orderInCoupling(CouplingType::QED,1);
    orderInCoupling(CouplingType::QCD,0);

    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_87 & operator=(const FRModelV_V_87 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_87,Helicity::FFVVertex>
describeHerwigFRModelV_V_87("Herwig::FRModelV_V_87",
				       "FRModel.so");
// void FRModelV_V_87::getParams(Energy2 ) {
// }

class FRModelV_V_88: public FFVVertex {
 public:
  FRModelV_V_88() {
    
    colourStructure(ColourStructure::SINGLET);
    addToList(-13,13,22);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*(-(ee*ii))));
    right(((((-ii)*1.0)*1.0)*(-(ee*ii))));
    if(p1->id()!=-13) {Complex ltemp=left(), rtemp=right(); left(-rtemp); right(-ltemp);}
  }
  void persistentOutput(PersistentOStream & os) const { os << model_; }
  void persistentInput(PersistentIStream & is, int) { is >> model_; }
  //  static void Init();
 protected:
  IBPtr clone() const { return new_ptr(*this); }
  IBPtr fullclone() const { return new_ptr(*this); }
  void doinit() {
    model_ = dynamic_ptr_cast<tcHwFRModelPtr>
	     (generator()->standardModel());
    assert(model_);
    //    getParams(q2);
    
        orderInCoupling(CouplingType::DMS,0);
    orderInCoupling(CouplingType::QED,1);
    orderInCoupling(CouplingType::QCD,0);

    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_88 & operator=(const FRModelV_V_88 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_88,Helicity::FFVVertex>
describeHerwigFRModelV_V_88("Herwig::FRModelV_V_88",
				       "FRModel.so");
// void FRModelV_V_88::getParams(Energy2 ) {
// }

}
