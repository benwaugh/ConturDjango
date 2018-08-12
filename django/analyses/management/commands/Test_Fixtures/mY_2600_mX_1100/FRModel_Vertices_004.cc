// -*- C++ -*-
//
// FRModel_Vertices_004.cc is a part of Herwig - A multi-purpose Monte Carlo event generator
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

  class FRModelV_V_114: public FFVVertex {
 public:
  FRModelV_V_114() {
    
    colourStructure(ColourStructure::DELTA);
    addToList(-2,2,23);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    double cw = model_->cw();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*((((cw*ee)*ii)/(2.0*sw))-(((ee*ii)*sw)/(6.0*cw)))));
    right(((((-ii)*1.0)*1.0)*((((-2.0*ee)*ii)*sw)/(3.0*cw))));
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
  FRModelV_V_114 & operator=(const FRModelV_V_114 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_114,Helicity::FFVVertex>
describeHerwigFRModelV_V_114("Herwig::FRModelV_V_114",
				       "FRModel.so");
// void FRModelV_V_114::getParams(Energy2 ) {
// }

class FRModelV_V_115: public FFVVertex {
 public:
  FRModelV_V_115() {
    
    colourStructure(ColourStructure::DELTA);
    addToList(-4,4,23);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    double cw = model_->cw();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*((((cw*ee)*ii)/(2.0*sw))-(((ee*ii)*sw)/(6.0*cw)))));
    right(((((-ii)*1.0)*1.0)*((((-2.0*ee)*ii)*sw)/(3.0*cw))));
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
  FRModelV_V_115 & operator=(const FRModelV_V_115 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_115,Helicity::FFVVertex>
describeHerwigFRModelV_V_115("Herwig::FRModelV_V_115",
				       "FRModel.so");
// void FRModelV_V_115::getParams(Energy2 ) {
// }

class FRModelV_V_116: public FFVVertex {
 public:
  FRModelV_V_116() {
    
    colourStructure(ColourStructure::DELTA);
    addToList(-6,6,23);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    double cw = model_->cw();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*((((cw*ee)*ii)/(2.0*sw))-(((ee*ii)*sw)/(6.0*cw)))));
    right(((((-ii)*1.0)*1.0)*((((-2.0*ee)*ii)*sw)/(3.0*cw))));
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
  FRModelV_V_116 & operator=(const FRModelV_V_116 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_116,Helicity::FFVVertex>
describeHerwigFRModelV_V_116("Herwig::FRModelV_V_116",
				       "FRModel.so");
// void FRModelV_V_116::getParams(Energy2 ) {
// }

class FRModelV_V_117: public FFVVertex {
 public:
  FRModelV_V_117() {
    
    colourStructure(ColourStructure::DELTA);
    addToList(-1,1,23);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    double cw = model_->cw();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*(((-((cw*ee)*ii))/(2.0*sw))-(((ee*ii)*sw)/(6.0*cw)))));
    right(((((-ii)*1.0)*1.0)*(((ee*ii)*sw)/(3.0*cw))));
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
  FRModelV_V_117 & operator=(const FRModelV_V_117 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_117,Helicity::FFVVertex>
describeHerwigFRModelV_V_117("Herwig::FRModelV_V_117",
				       "FRModel.so");
// void FRModelV_V_117::getParams(Energy2 ) {
// }

class FRModelV_V_118: public FFVVertex {
 public:
  FRModelV_V_118() {
    
    colourStructure(ColourStructure::DELTA);
    addToList(-3,3,23);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    double cw = model_->cw();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*(((-((cw*ee)*ii))/(2.0*sw))-(((ee*ii)*sw)/(6.0*cw)))));
    right(((((-ii)*1.0)*1.0)*(((ee*ii)*sw)/(3.0*cw))));
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
  FRModelV_V_118 & operator=(const FRModelV_V_118 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_118,Helicity::FFVVertex>
describeHerwigFRModelV_V_118("Herwig::FRModelV_V_118",
				       "FRModel.so");
// void FRModelV_V_118::getParams(Energy2 ) {
// }

class FRModelV_V_119: public FFVVertex {
 public:
  FRModelV_V_119() {
    
    colourStructure(ColourStructure::DELTA);
    addToList(-5,5,23);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    double cw = model_->cw();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*(((-((cw*ee)*ii))/(2.0*sw))-(((ee*ii)*sw)/(6.0*cw)))));
    right(((((-ii)*1.0)*1.0)*(((ee*ii)*sw)/(3.0*cw))));
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
  FRModelV_V_119 & operator=(const FRModelV_V_119 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_119,Helicity::FFVVertex>
describeHerwigFRModelV_V_119("Herwig::FRModelV_V_119",
				       "FRModel.so");
// void FRModelV_V_119::getParams(Energy2 ) {
// }

class FRModelV_V_120: public FFVVertex {
 public:
  FRModelV_V_120() {
    
    colourStructure(ColourStructure::SINGLET);
    addToList(-12,12,23);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double cw = model_->cw();
    double sw = model_->sw();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*((((cw*ee)*ii)/(2.0*sw))+(((ee*ii)*sw)/(2.0*cw)))));
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
  FRModelV_V_120 & operator=(const FRModelV_V_120 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_120,Helicity::FFVVertex>
describeHerwigFRModelV_V_120("Herwig::FRModelV_V_120",
				       "FRModel.so");
// void FRModelV_V_120::getParams(Energy2 ) {
// }

class FRModelV_V_121: public FFVVertex {
 public:
  FRModelV_V_121() {
    
    colourStructure(ColourStructure::SINGLET);
    addToList(-14,14,23);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double cw = model_->cw();
    double sw = model_->sw();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*((((cw*ee)*ii)/(2.0*sw))+(((ee*ii)*sw)/(2.0*cw)))));
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
  FRModelV_V_121 & operator=(const FRModelV_V_121 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_121,Helicity::FFVVertex>
describeHerwigFRModelV_V_121("Herwig::FRModelV_V_121",
				       "FRModel.so");
// void FRModelV_V_121::getParams(Energy2 ) {
// }

class FRModelV_V_122: public FFVVertex {
 public:
  FRModelV_V_122() {
    
    colourStructure(ColourStructure::SINGLET);
    addToList(-16,16,23);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double cw = model_->cw();
    double sw = model_->sw();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*1.0)*((((cw*ee)*ii)/(2.0*sw))+(((ee*ii)*sw)/(2.0*cw)))));
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
  FRModelV_V_122 & operator=(const FRModelV_V_122 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_122,Helicity::FFVVertex>
describeHerwigFRModelV_V_122("Herwig::FRModelV_V_122",
				       "FRModel.so");
// void FRModelV_V_122::getParams(Energy2 ) {
// }

class FRModelV_V_123: public FFVVertex {
 public:
  FRModelV_V_123() {
    
    colourStructure(ColourStructure::SINGLET);
    addToList(-11,11,23);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    double cw = model_->cw();
    
    //    getParams(q2);
    norm(1.0);
    left((((((-ii)*1.0)*1.0)*((-((cw*ee)*ii))/(2.0*sw)))+((((-ii)*1.0)*1.0)*(((ee*ii)*sw)/(2.0*cw)))));
    right(((((-ii)*1.0)*2.0)*(((ee*ii)*sw)/(2.0*cw))));
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
  FRModelV_V_123 & operator=(const FRModelV_V_123 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_123,Helicity::FFVVertex>
describeHerwigFRModelV_V_123("Herwig::FRModelV_V_123",
				       "FRModel.so");
// void FRModelV_V_123::getParams(Energy2 ) {
// }

class FRModelV_V_124: public FFVVertex {
 public:
  FRModelV_V_124() {
    
    colourStructure(ColourStructure::SINGLET);
    addToList(-13,13,23);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    double cw = model_->cw();
    
    //    getParams(q2);
    norm(1.0);
    left((((((-ii)*1.0)*1.0)*((-((cw*ee)*ii))/(2.0*sw)))+((((-ii)*1.0)*1.0)*(((ee*ii)*sw)/(2.0*cw)))));
    right(((((-ii)*1.0)*2.0)*(((ee*ii)*sw)/(2.0*cw))));
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
  FRModelV_V_124 & operator=(const FRModelV_V_124 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_124,Helicity::FFVVertex>
describeHerwigFRModelV_V_124("Herwig::FRModelV_V_124",
				       "FRModel.so");
// void FRModelV_V_124::getParams(Energy2 ) {
// }

class FRModelV_V_125: public FFVVertex {
 public:
  FRModelV_V_125() {
    
    colourStructure(ColourStructure::SINGLET);
    addToList(-15,15,23);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double ee = model_->ee();
    double sw = model_->sw();
    double cw = model_->cw();
    
    //    getParams(q2);
    norm(1.0);
    left((((((-ii)*1.0)*1.0)*((-((cw*ee)*ii))/(2.0*sw)))+((((-ii)*1.0)*1.0)*(((ee*ii)*sw)/(2.0*cw)))));
    right(((((-ii)*1.0)*2.0)*(((ee*ii)*sw)/(2.0*cw))));
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
  FRModelV_V_125 & operator=(const FRModelV_V_125 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_125,Helicity::FFVVertex>
describeHerwigFRModelV_V_125("Herwig::FRModelV_V_125",
				       "FRModel.so");
// void FRModelV_V_125::getParams(Energy2 ) {
// }

class FRModelV_V_126: public FFVVertex {
 public:
  FRModelV_V_126() {
    
    colourStructure(ColourStructure::SINGLET);
    addToList(52,52,9000006);
  }
  void setCoupling(Energy2 ,tcPDPtr p1,tcPDPtr,tcPDPtr) {
    double gYXm = model_->gYXm();
    
    //    getParams(q2);
    norm(1.0);
    left(((((-ii)*1.0)*-1.0)*((2.0*ii)*gYXm)));
    right(((((-ii)*1.0)*1.0)*((2.0*ii)*gYXm)));
    if(p1->id()!=52) {Complex ltemp=left(), rtemp=right(); left(-rtemp); right(-ltemp);}
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
  FRModelV_V_126 & operator=(const FRModelV_V_126 &);
  //    Complex leftval, rightval, normval;
  tcHwFRModelPtr model_;
};
DescribeClass<FRModelV_V_126,Helicity::FFVVertex>
describeHerwigFRModelV_V_126("Herwig::FRModelV_V_126",
				       "FRModel.so");
// void FRModelV_V_126::getParams(Energy2 ) {
// }

}
