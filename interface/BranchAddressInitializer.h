#ifndef BRANCHADDRESSINITIALIZER_H
#define BRANCHADDRESSINITIALIZER_H

#include "tthAnalysis/HiggsToTauTau/interface/TypeTraits.h" // Traits<>

#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h" // cmsException()

#include <TTree.h> // TTree

#include <type_traits> // std::enable_if<,>, std::is_arithmetic<>
#include <string> // std::string
#include <algorithm> // std::sort(), std::set_union(), std::fill_n()

struct BranchAddressInitializer
{
public:
  BranchAddressInitializer(TTree * tree = nullptr,
                           int lenVar = -1,
                           const std::string & branchName_n = "")
    : tree_(tree)
    , lenVar_(lenVar)
    , branchName_n_(branchName_n)
    , ignoreErrors_(false)
    , inputBranchNamesFound_(false)
  {
    if(! tree_)
    {
      throw cmsException(this) << "No TTree provided!";
    }
  }

  void
  ignoreErrors(bool flag)
  {
    ignoreErrors_ = flag;
  }

  template<typename T,
           typename = std::enable_if<std::is_arithmetic<T>::value>>
  void
  setBranch(T & value,
            const std::string & branchName)
  {
    tree_ -> Branch(branchName.data(), &value, Form("%s/%s", branchName.data(), Traits<T>::TYPE_NAME));
  }

  template<typename T,
           typename = std::enable_if<std::is_arithmetic<T>::value>>
  void
  setBranch(T * & address,
            const std::string & branchName)
  {
    if(lenVar_ > 0)
    {
      address = new T[lenVar_];
    }
    tree_ -> Branch(branchName.data(), address, Form(
      "%s%s/%s", branchName.data(), Form("[%s]", branchName_n_.data()), Traits<T>::TYPE_NAME)
    );
  }

  template<typename T,
           typename U = T,
           typename = typename std::enable_if<std::is_arithmetic<T>::value>>
  void
  setBranchAddress(T & value,
                   const std::string & branchName,
                   U default_value = 0)
  {
    value = static_cast<T>(default_value);
    if(! branchName.empty() && ! (ignoreErrors_ && ! hasBranchName(branchName)))
    {
      tree_ -> SetBranchAddress(branchName.data(), &value);
    }
  }

  template<typename T,
           typename U = T,
           typename = std::enable_if<std::is_arithmetic<T>::value && std::is_arithmetic<U>::value>>
  void
  setBranchAddress(T * & address,
                   const std::string & branchName,
                   U default_value = 0)
  {
    if(lenVar_ > 0)
    {
      address = new T[lenVar_];
      std::fill_n(address, lenVar_, static_cast<T>(default_value));
    }
    if(! branchName.empty() && ! (ignoreErrors_ && ! hasBranchName(branchName)))
    {
      tree_ -> SetBranchAddress(branchName.data(), address);
    }
  }

  BranchAddressInitializer &
  setLenVar(int lenVar)
  {
    lenVar_ = lenVar;
    return *this;
  }

protected:
  bool
  hasBranchName(const std::string & branchName)
  {
    if(branchName.empty())
    {
      throw cmsException(this, __func__, __LINE__) << "Cannot search for an empty branch name";
    }
    if(! inputBranchNamesFound_)
    {
      const TObjArray * const tree_branches = tree_->GetListOfBranches();
      const int tree_numBranches = tree_branches->GetEntries();
      for(int idxBranch = 0; idxBranch < tree_numBranches; ++idxBranch)
      {
        const TBranch * const tree_branch = dynamic_cast<const TBranch * const>(tree_branches->At(idxBranch));
        assert(tree_branch);
        const std::string tree_branchName = tree_branch->GetName();
        if(std::find(inputBranchNames_.cbegin(), inputBranchNames_.cend(), tree_branchName) != inputBranchNames_.cend())
        {
          std::cout << "Found duplicate branch names in input TTree: " << tree_branchName << '\n';
          continue;
        }
        inputBranchNames_.push_back(tree_branchName);
      }
      inputBranchNamesFound_ = true;
    }
    return std::find(inputBranchNames_.cbegin(), inputBranchNames_.cend(), branchName) != inputBranchNames_.cend();
  }

  TTree * tree_;
  int lenVar_;
  std::string branchName_n_;
  bool ignoreErrors_;
  bool inputBranchNamesFound_;
  std::vector<std::string> inputBranchNames_;
};

#endif // BRANCHADDRESSINITIALIZER_H
