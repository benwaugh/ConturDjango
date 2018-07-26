// -*- C++ -*-
//
// FRModel_Vertices_002.cc is a part of Herwig - A multi-purpose Monte Carlo event generator
// Copyright (C) 2002-2007 The Herwig Collaboration
//
// Herwig is licenced under version 2 of the GPL, see COPYING for details.
// Please respect the MCnet academic guidelines, see GUIDELINES for details.

#include "FRModel.h"
#include "ThePEG/Helicity/Vertex/Vector/FFVVertex.h"

#include "ThePEG/Utilities/DescribeClass.h"
#include "ThePEG/Persistency/PersistentOStream.h"
#include "ThePEG/Persistency/PersistentIStream.h"

namespace Herwig 
{
  using namespace ThePEG;
  using namespace ThePEG::Helicity;
  using ThePEG::Constants::pi;

  class FRModelV_V_89: public FFVVertex {
 public:
  FRModelV_V_89() {
    
    colourStructure(ColourStructure::SINGLET);
    addToList(-15,15,22);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*(-(ee*ii))));
    right(((((-ii)*1.0)*1.0)*(-(ee*ii))));
    if(p1->id()!=-15) {Complex ltemp=left(), rtemp=right(); left(-rtemp); right(-ltemp);}
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
  FRModelV_V_89 & operator=(const FRModelV_V_89 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_89,Helicity::FFVVertex>
describeHerwigFRModelV_V_89("Herwig::FRModelV_V_89",
				       "FRModel.so");
// void FRModelV_V_89::getParams(Energy2 ) {
// }

class FRModelV_V_90: public FFVVertex {
 public:
  FRModelV_V_90() {
    
    colourStructure(ColourStructure::DELTA);
    addToList(-2,2,22);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*(((2.0*ee)*ii)/3.0)));
    right(((((-ii)*1.0)*1.0)*(((2.0*ee)*ii)/3.0)));
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
    
        orderInCoupling(CouplingType::DMS,0);
    orderInCoupling(CouplingType::QED,1);
    orderInCoupling(CouplingType::QCD,0);

    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_90 & operator=(const FRModelV_V_90 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_90,Helicity::FFVVertex>
describeHerwigFRModelV_V_90("Herwig::FRModelV_V_90",
				       "FRModel.so");
// void FRModelV_V_90::getParams(Energy2 ) {
// }

class FRModelV_V_91: public FFVVertex {
 public:
  FRModelV_V_91() {
    
    colourStructure(ColourStructure::DELTA);
    addToList(-4,4,22);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*(((2.0*ee)*ii)/3.0)));
    right(((((-ii)*1.0)*1.0)*(((2.0*ee)*ii)/3.0)));
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
    
        orderInCoupling(CouplingType::DMS,0);
    orderInCoupling(CouplingType::QED,1);
    orderInCoupling(CouplingType::QCD,0);

    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_91 & operator=(const FRModelV_V_91 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_91,Helicity::FFVVertex>
describeHerwigFRModelV_V_91("Herwig::FRModelV_V_91",
				       "FRModel.so");
// void FRModelV_V_91::getParams(Energy2 ) {
// }

class FRModelV_V_92: public FFVVertex {
 public:
  FRModelV_V_92() {
    
    colourStructure(ColourStructure::DELTA);
    addToList(-6,6,22);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*(((2.0*ee)*ii)/3.0)));
    right(((((-ii)*1.0)*1.0)*(((2.0*ee)*ii)/3.0)));
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
    
        orderInCoupling(CouplingType::DMS,0);
    orderInCoupling(CouplingType::QED,1);
    orderInCoupling(CouplingType::QCD,0);

    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_92 & operator=(const FRModelV_V_92 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_92,Helicity::FFVVertex>
describeHerwigFRModelV_V_92("Herwig::FRModelV_V_92",
				       "FRModel.so");
// void FRModelV_V_92::getParams(Energy2 ) {
// }

class FRModelV_V_93: public FFVVertex {
 public:
  FRModelV_V_93() {
    
    colourStructure(ColourStructure::DELTA);
    addToList(-1,1,22);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*((-(ee*ii))/3.0)));
    right(((((-ii)*1.0)*1.0)*((-(ee*ii))/3.0)));
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
    
        orderInCoupling(CouplingType::DMS,0);
    orderInCoupling(CouplingType::QED,1);
    orderInCoupling(CouplingType::QCD,0);

    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_93 & operator=(const FRModelV_V_93 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_93,Helicity::FFVVertex>
describeHerwigFRModelV_V_93("Herwig::FRModelV_V_93",
				       "FRModel.so");
// void FRModelV_V_93::getParams(Energy2 ) {
// }

class FRModelV_V_94: public FFVVertex {
 public:
  FRModelV_V_94() {
    
    colourStructure(ColourStructure::DELTA);
    addToList(-3,3,22);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*((-(ee*ii))/3.0)));
    right(((((-ii)*1.0)*1.0)*((-(ee*ii))/3.0)));
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
    
        orderInCoupling(CouplingType::DMS,0);
    orderInCoupling(CouplingType::QED,1);
    orderInCoupling(CouplingType::QCD,0);

    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_94 & operator=(const FRModelV_V_94 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_94,Helicity::FFVVertex>
describeHerwigFRModelV_V_94("Herwig::FRModelV_V_94",
				       "FRModel.so");
// void FRModelV_V_94::getParams(Energy2 ) {
// }

class FRModelV_V_95: public FFVVertex {
 public:
  FRModelV_V_95() {
    
    colourStructure(ColourStructure::DELTA);
    addToList(-5,5,22);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*((-(ee*ii))/3.0)));
    right(((((-ii)*1.0)*1.0)*((-(ee*ii))/3.0)));
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
    
        orderInCoupling(CouplingType::DMS,0);
    orderInCoupling(CouplingType::QED,1);
    orderInCoupling(CouplingType::QCD,0);

    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_95 & operator=(const FRModelV_V_95 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_95,Helicity::FFVVertex>
describeHerwigFRModelV_V_95("Herwig::FRModelV_V_95",
				       "FRModel.so");
// void FRModelV_V_95::getParams(Energy2 ) {
// }

class FRModelV_V_96: public FFVVertex {
 public:
  FRModelV_V_96() {
    
    colourStructure(ColourStructure::SU3TFUND);
    addToList(-2,2,21);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double G = model_->G();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*(ii*G)));
    right(((((-ii)*1.0)*1.0)*(ii*G)));
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
    
        orderInCoupling(CouplingType::DMS,0);
    orderInCoupling(CouplingType::QED,0);
    orderInCoupling(CouplingType::QCD,1);

    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_96 & operator=(const FRModelV_V_96 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_96,Helicity::FFVVertex>
describeHerwigFRModelV_V_96("Herwig::FRModelV_V_96",
				       "FRModel.so");
// void FRModelV_V_96::getParams(Energy2 ) {
// }

class FRModelV_V_97: public FFVVertex {
 public:
  FRModelV_V_97() {
    
    colourStructure(ColourStructure::SU3TFUND);
    addToList(-4,4,21);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double G = model_->G();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*(ii*G)));
    right(((((-ii)*1.0)*1.0)*(ii*G)));
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
    
        orderInCoupling(CouplingType::DMS,0);
    orderInCoupling(CouplingType::QED,0);
    orderInCoupling(CouplingType::QCD,1);

    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_97 & operator=(const FRModelV_V_97 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_97,Helicity::FFVVertex>
describeHerwigFRModelV_V_97("Herwig::FRModelV_V_97",
				       "FRModel.so");
// void FRModelV_V_97::getParams(Energy2 ) {
// }

class FRModelV_V_98: public FFVVertex {
 public:
  FRModelV_V_98() {
    
    colourStructure(ColourStructure::SU3TFUND);
    addToList(-6,6,21);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double G = model_->G();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*(ii*G)));
    right(((((-ii)*1.0)*1.0)*(ii*G)));
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
    
        orderInCoupling(CouplingType::DMS,0);
    orderInCoupling(CouplingType::QED,0);
    orderInCoupling(CouplingType::QCD,1);

    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_98 & operator=(const FRModelV_V_98 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_98,Helicity::FFVVertex>
describeHerwigFRModelV_V_98("Herwig::FRModelV_V_98",
				       "FRModel.so");
// void FRModelV_V_98::getParams(Energy2 ) {
// }

class FRModelV_V_99: public FFVVertex {
 public:
  FRModelV_V_99() {
    
    colourStructure(ColourStructure::SU3TFUND);
    addToList(-1,1,21);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double G = model_->G();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*(ii*G)));
    right(((((-ii)*1.0)*1.0)*(ii*G)));
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
    
        orderInCoupling(CouplingType::DMS,0);
    orderInCoupling(CouplingType::QED,0);
    orderInCoupling(CouplingType::QCD,1);

    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_99 & operator=(const FRModelV_V_99 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_99,Helicity::FFVVertex>
describeHerwigFRModelV_V_99("Herwig::FRModelV_V_99",
				       "FRModel.so");
// void FRModelV_V_99::getParams(Energy2 ) {
// }

class FRModelV_V_100: public FFVVertex {
 public:
  FRModelV_V_100() {
    
    colourStructure(ColourStructure::SU3TFUND);
    addToList(-3,3,21);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double G = model_->G();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*(ii*G)));
    right(((((-ii)*1.0)*1.0)*(ii*G)));
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
    
        orderInCoupling(CouplingType::DMS,0);
    orderInCoupling(CouplingType::QED,0);
    orderInCoupling(CouplingType::QCD,1);

    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_100 & operator=(const FRModelV_V_100 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_100,Helicity::FFVVertex>
describeHerwigFRModelV_V_100("Herwig::FRModelV_V_100",
				       "FRModel.so");
// void FRModelV_V_100::getParams(Energy2 ) {
// }

class FRModelV_V_101: public FFVVertex {
 public:
  FRModelV_V_101() {
    
    colourStructure(ColourStructure::SU3TFUND);
    addToList(-5,5,21);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double G = model_->G();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*(ii*G)));
    right(((((-ii)*1.0)*1.0)*(ii*G)));
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
    
        orderInCoupling(CouplingType::DMS,0);
    orderInCoupling(CouplingType::QED,0);
    orderInCoupling(CouplingType::QCD,1);

    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_101 & operator=(const FRModelV_V_101 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_101,Helicity::FFVVertex>
describeHerwigFRModelV_V_101("Herwig::FRModelV_V_101",
				       "FRModel.so");
// void FRModelV_V_101::getParams(Energy2 ) {
// }

class FRModelV_V_102: public FFVVertex {
 public:
  FRModelV_V_102() {
    
    colourStructure(ColourStructure::DELTA);
    addToList(-1,2,-24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*((ee*ii)/(sw*sqrt(2.0)))));
    right(0.0);
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
    
        orderInCoupling(CouplingType::DMS,0);
    orderInCoupling(CouplingType::QED,1);
    orderInCoupling(CouplingType::QCD,0);

    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_102 & operator=(const FRModelV_V_102 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_102,Helicity::FFVVertex>
describeHerwigFRModelV_V_102("Herwig::FRModelV_V_102",
				       "FRModel.so");
// void FRModelV_V_102::getParams(Energy2 ) {
// }

class FRModelV_V_103: public FFVVertex {
 public:
  FRModelV_V_103() {
    
    colourStructure(ColourStructure::DELTA);
    addToList(-3,4,-24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*((ee*ii)/(sw*sqrt(2.0)))));
    right(0.0);
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
    
        orderInCoupling(CouplingType::DMS,0);
    orderInCoupling(CouplingType::QED,1);
    orderInCoupling(CouplingType::QCD,0);

    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_103 & operator=(const FRModelV_V_103 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_103,Helicity::FFVVertex>
describeHerwigFRModelV_V_103("Herwig::FRModelV_V_103",
				       "FRModel.so");
// void FRModelV_V_103::getParams(Energy2 ) {
// }

class FRModelV_V_104: public FFVVertex {
 public:
  FRModelV_V_104() {
    
    colourStructure(ColourStructure::DELTA);
    addToList(-5,6,-24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*((ee*ii)/(sw*sqrt(2.0)))));
    right(0.0);
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
    
        orderInCoupling(CouplingType::DMS,0);
    orderInCoupling(CouplingType::QED,1);
    orderInCoupling(CouplingType::QCD,0);

    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_104 & operator=(const FRModelV_V_104 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_104,Helicity::FFVVertex>
describeHerwigFRModelV_V_104("Herwig::FRModelV_V_104",
				       "FRModel.so");
// void FRModelV_V_104::getParams(Energy2 ) {
// }

class FRModelV_V_105: public FFVVertex {
 public:
  FRModelV_V_105() {
    
    colourStructure(ColourStructure::DELTA);
    addToList(-2,1,24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*((ee*ii)/(sw*sqrt(2.0)))));
    right(0.0);
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
    
        orderInCoupling(CouplingType::DMS,0);
    orderInCoupling(CouplingType::QED,1);
    orderInCoupling(CouplingType::QCD,0);

    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_105 & operator=(const FRModelV_V_105 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_105,Helicity::FFVVertex>
describeHerwigFRModelV_V_105("Herwig::FRModelV_V_105",
				       "FRModel.so");
// void FRModelV_V_105::getParams(Energy2 ) {
// }

class FRModelV_V_106: public FFVVertex {
 public:
  FRModelV_V_106() {
    
    colourStructure(ColourStructure::DELTA);
    addToList(-4,3,24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*((ee*ii)/(sw*sqrt(2.0)))));
    right(0.0);
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
    
        orderInCoupling(CouplingType::DMS,0);
    orderInCoupling(CouplingType::QED,1);
    orderInCoupling(CouplingType::QCD,0);

    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_106 & operator=(const FRModelV_V_106 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_106,Helicity::FFVVertex>
describeHerwigFRModelV_V_106("Herwig::FRModelV_V_106",
				       "FRModel.so");
// void FRModelV_V_106::getParams(Energy2 ) {
// }

class FRModelV_V_107: public FFVVertex {
 public:
  FRModelV_V_107() {
    
    colourStructure(ColourStructure::DELTA);
    addToList(-6,5,24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*((ee*ii)/(sw*sqrt(2.0)))));
    right(0.0);
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
    
        orderInCoupling(CouplingType::DMS,0);
    orderInCoupling(CouplingType::QED,1);
    orderInCoupling(CouplingType::QCD,0);

    FFVVertex::doinit();
  }
  //    void getParams(Energy2);
 private:
  FRModelV_V_107 & operator=(const FRModelV_V_107 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_107,Helicity::FFVVertex>
describeHerwigFRModelV_V_107("Herwig::FRModelV_V_107",
				       "FRModel.so");
// void FRModelV_V_107::getParams(Energy2 ) {
// }

class FRModelV_V_108: public FFVVertex {
 public:
  FRModelV_V_108() {
    
    colourStructure(ColourStructure::SINGLET);
    addToList(-11,12,-24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*((ee*ii)/(sw*sqrt(2.0)))));
    right(0.0);
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
  FRModelV_V_108 & operator=(const FRModelV_V_108 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_108,Helicity::FFVVertex>
describeHerwigFRModelV_V_108("Herwig::FRModelV_V_108",
				       "FRModel.so");
// void FRModelV_V_108::getParams(Energy2 ) {
// }

class FRModelV_V_109: public FFVVertex {
 public:
  FRModelV_V_109() {
    
    colourStructure(ColourStructure::SINGLET);
    addToList(-13,14,-24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*((ee*ii)/(sw*sqrt(2.0)))));
    right(0.0);
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
  FRModelV_V_109 & operator=(const FRModelV_V_109 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_109,Helicity::FFVVertex>
describeHerwigFRModelV_V_109("Herwig::FRModelV_V_109",
				       "FRModel.so");
// void FRModelV_V_109::getParams(Energy2 ) {
// }

class FRModelV_V_110: public FFVVertex {
 public:
  FRModelV_V_110() {
    
    colourStructure(ColourStructure::SINGLET);
    addToList(-15,16,-24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*((ee*ii)/(sw*sqrt(2.0)))));
    right(0.0);
    if(p1->id()!=-15) {Complex ltemp=left(), rtemp=right(); left(-rtemp); right(-ltemp);}
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
  FRModelV_V_110 & operator=(const FRModelV_V_110 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_110,Helicity::FFVVertex>
describeHerwigFRModelV_V_110("Herwig::FRModelV_V_110",
				       "FRModel.so");
// void FRModelV_V_110::getParams(Energy2 ) {
// }

class FRModelV_V_111: public FFVVertex {
 public:
  FRModelV_V_111() {
    
    colourStructure(ColourStructure::SINGLET);
    addToList(-12,11,24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*((ee*ii)/(sw*sqrt(2.0)))));
    right(0.0);
    if(p1->id()!=-12) {Complex ltemp=left(), rtemp=right(); left(-rtemp); right(-ltemp);}
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
  FRModelV_V_111 & operator=(const FRModelV_V_111 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_111,Helicity::FFVVertex>
describeHerwigFRModelV_V_111("Herwig::FRModelV_V_111",
				       "FRModel.so");
// void FRModelV_V_111::getParams(Energy2 ) {
// }

class FRModelV_V_112: public FFVVertex {
 public:
  FRModelV_V_112() {
    
    colourStructure(ColourStructure::SINGLET);
    addToList(-14,13,24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*((ee*ii)/(sw*sqrt(2.0)))));
    right(0.0);
    if(p1->id()!=-14) {Complex ltemp=left(), rtemp=right(); left(-rtemp); right(-ltemp);}
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
  FRModelV_V_112 & operator=(const FRModelV_V_112 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_112,Helicity::FFVVertex>
describeHerwigFRModelV_V_112("Herwig::FRModelV_V_112",
				       "FRModel.so");
// void FRModelV_V_112::getParams(Energy2 ) {
// }

class FRModelV_V_113: public FFVVertex {
 public:
  FRModelV_V_113() {
    
    colourStructure(ColourStructure::SINGLET);
    addToList(-16,15,24);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*((ee*ii)/(sw*sqrt(2.0)))));
    right(0.0);
    if(p1->id()!=-16) {Complex ltemp=left(), rtemp=right(); left(-rtemp); right(-ltemp);}
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
  FRModelV_V_113 & operator=(const FRModelV_V_113 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_113,Helicity::FFVVertex>
describeHerwigFRModelV_V_113("Herwig::FRModelV_V_113",
				       "FRModel.so");
// void FRModelV_V_113::getParams(Energy2 ) {
// }

}
